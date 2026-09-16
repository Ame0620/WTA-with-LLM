"""E15-A0: read-only diagnostics for the e14 MARL artefacts.

CLI (from the project root):

    python experiments/e15_diag.py --ckpt output/e14_marl_train/best.pt \
        --output output/e15_diag

Sections (all read-only; global-truth reads are allowed HERE only, as the
spec grants diagnostics access):
  1. lambda-hat quality   AgentMemory lambda estimates vs true in-flight
                          occupancy on the val split (Pearson / MAE /
                          error by target age); both scopes reported
                          (all in-flight vs others-only, the latter being
                          the quantity the recursion actually targets).
  2. e14 val-curve audit  parse e14 train_log.jsonl -> slope of the tail,
                          best-vs-stop distance, stop-vs-plateau verdict.
  3. ammo profile         mean pool curve + per-step launch histogram.
  4. shaping decomposition (bias (c) quantification): per-shot split of the
                          R_shaped signal into the launch-step marginal
                          potential kick (-Delta(w*pbar)) vs the settlement
                          step payoff; if the mean launch kick is of the
                          same magnitude as the mean kill credit (~0.02),
                          flag the Phi-flip alternative (A3-alt-1).
  5. conclusions          c_invalid tier advice + Phi-flip trigger verdict.
"""

import argparse
import json
import math
import os
import sys

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from dwta.dn_instance import DNInstance                     # noqa: E402
from dwta.dn_env import DNEnv                               # noqa: E402
from marl.policy import MarlPolicy                          # noqa: E402
from marl.reward import build_rewards                       # noqa: E402

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "dn-data-v3")
VAL_INSTS = ["dn_3x50_K10_s%02d.txt" % s for s in range(27, 31)]
TRAIN_INSTS = ["dn_3x50_K10_s%02d.txt" % s for s in range(3, 27)]

AGE_BUCKETS = [(0, 1), (2, 3), (4, 5), (6, 10)]


# ----------------------------------------------------------------------
# small stats helpers
# ----------------------------------------------------------------------

def _mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def _std(xs):
    if len(xs) < 2:
        return 0.0
    m = _mean(xs)
    return (sum((x - m) ** 2 for x in xs) / len(xs)) ** 0.5


def _quantiles(xs, qs=(0.1, 0.25, 0.5, 0.75, 0.9)):
    if not xs:
        return {q: float("nan") for q in qs}
    s = sorted(xs)
    out = {}
    for q in qs:
        idx = min(len(s) - 1, max(0, int(round(q * (len(s) - 1)))))
        out[q] = s[idx]
    return out


def _pearson(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan")
    mx, my = _mean(xs), _mean(ys)
    sx, sy = _std(xs), _std(ys)
    if sx <= 0 or sy <= 0:
        return float("nan")
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / n
    return cov / (sx * sy)


def _linfit_slope(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan")
    mx, my = _mean(xs), _mean(ys)
    denom = sum((x - mx) ** 2 for x in xs)
    if denom <= 0:
        return float("nan")
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / denom


# ----------------------------------------------------------------------
# section 1 + 3 driver: run the e14 policy on val, recording lambda rows
# and ammo profiles; section 4 reuses the same finished envs.
# ----------------------------------------------------------------------

class _DiagWrap(object):
    """Wrap MarlPolicy.act to snapshot lambda-hat vs true occupancy right
    after the internal memory update (pre-fire, matching decision time)."""

    def __init__(self, pol, sink):
        self.pol = pol
        self.sink = sink

    def act(self, env, t):
        actions, info = self.pol.act(env, t)
        try:
            self.sink.record_lam(env, t, self.pol._mems)
        except Exception as e:                     # diagnostics must not
            print("[e15-diag][warn] lam record failed: %s" % e)  # break runs
        return actions, info


class _Sink(object):
    def __init__(self):
        self.lam_rows = []          # (j, lam, truth_all, truth_others, age)
        self.pool_curves = []       # per-episode [pool_after per t]
        self.launch_hist = {}       # t -> launches at t
        self.envs = []              # finished envs for section 4
        self.recs = []

    def record_lam(self, env, t, mems):
        truth_all = {}
        truth_own = {i: {} for i in range(env.dn.m)}
        for ev in env.inflight:
            j = ev["j"]
            truth_all[j] = truth_all.get(j, 0) + 1
            truth_own[ev["i"]][j] = truth_own[ev["i"]].get(j, 0) + 1
        for i in range(env.dn.m):
            lam = mems[i].lam
            for j, v in lam.items():
                own = truth_own[i].get(j, 0)
                self.lam_rows.append((
                    j, float(v), truth_all.get(j, 0),
                    truth_all.get(j, 0) - own,
                    env.dn.age(j, t)))


def run_val_pass(ckpt, device):
    pol = MarlPolicy(model_path=ckpt, device=device, greedy=True, seed=0)
    sink = _Sink()
    wrap = _DiagWrap(pol, sink)
    leaks = []
    for name in VAL_INSTS:
        dn = DNInstance(os.path.join(DATA_DIR, name))
        for seed in range(42, 52):
            env = DNEnv(dn, seed)
            pol.reset_episode()
            rec = env.run(wrap)
            leaks.append(rec["leak_rate"])
            sink.pool_curves.append(rec["pool_curve"])
            for s in rec["steps"]:
                if s["decision_step"]:
                    sink.launch_hist[s["t"]] = \
                        sink.launch_hist.get(s["t"], 0) + s["shots"]
            sink.envs.append((env, dn, rec))
            sink.recs.append(rec)
    return sink, leaks


# ----------------------------------------------------------------------
# section 4: per-shot shaping decomposition
# ----------------------------------------------------------------------

def launch_marginals(env, dn):
    """Per-shot marginal potential kick at the firing step.

    At each t, in-flight shots (t_fire <= t < t_hit) are folded onto their
    targets in (t_fire, i) order -- the same settlement order the env uses;
    each shot's launch kick is the marginal -w_j/total * Delta(pbar_j) it
    caused when entering (recorded once, at t == t_fire).
    """
    total = float(dn.total_value())
    out = {}
    for t in range(dn.K + 1):
        fl = sorted((ev for ev in env.shots
                     if ev["t_fire"] <= t < ev["t_hit"]),
                    key=lambda e: (e["t_fire"], e["i"]))
        pbar = {}
        for ev in fl:
            j = ev["j"]
            pb = pbar.get(j, 0.0)
            pa = 1.0 - (1.0 - pb) * (1.0 - ev["p_shot"])
            if ev["t_fire"] == t:
                out[id(ev)] = -(dn.w[j] / total) * (pa - pb)
            pbar[j] = pa
    return out


def shape_decompose(sink, c_invalid):
    launch_pens, settle_rets, outcomes = [], [], []
    kill_credit_vals = []
    for env, dn, rec in sink.envs:
        marg = launch_marginals(env, dn)
        build_rewards(env, rec, dn, c_invalid)  # sanity: reward path runs
        total = float(dn.total_value())
        for ev in env.shots:
            oc = ev.get("outcome")
            ret = 0.0
            if oc == "kill":
                ret = dn.w[ev["j"]] / total
                kill_credit_vals.append(ret)
            elif oc == "invalid":
                ret = -c_invalid
            launch_pens.append(marg.get(id(ev), 0.0))
            settle_rets.append(ret)
            outcomes.append(oc)
    return launch_pens, settle_rets, outcomes, kill_credit_vals


# ----------------------------------------------------------------------
# section 2: e14 train_log audit
# ----------------------------------------------------------------------

def audit_train_log(path):
    rows = [json.loads(ln) for ln in open(path) if ln.strip()]
    iters = [r["iter"] for r in rows]
    vals = [r["val_leak_mean"] for r in rows]
    best_i = min(range(len(rows)), key=lambda i: vals[i])
    tail = rows[max(0, len(rows) // 2):]
    tail_slope = _linfit_slope([r["iter"] for r in tail],
                               [r["val_leak_mean"] for r in tail])
    # new-best within the last 5 eval points?
    recent_best = best_i >= len(rows) - 5
    last_iters = rows[-1]["iter"]
    stop_reason = "early_stop" if recent_best is False else "running/iters"
    # distance from best to stop, in eval points
    verdict = ("STILL-DESCENDING (truncated by patience)" if recent_best
               else "PLATEAU (patience stop justified on this curve)")
    return {
        "n_points": len(rows),
        "best": {"iter": rows[best_i]["iter"], "val": vals[best_i],
                 "idx": best_i},
        "last": {"iter": last_iters, "val": vals[-1]},
        "best_to_stop_eval_points": len(rows) - 1 - best_i,
        "tail_slope_per_iter": tail_slope,
        "verdict": verdict,
        "rows": rows,
    }


# ----------------------------------------------------------------------
# report writer
# ----------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description="e15-A0 read-only diagnostics")
    ap.add_argument("--ckpt", default=os.path.join(
        PROJECT_ROOT, "output", "e14_marl_train", "best.pt"))
    ap.add_argument("--train-log", default=os.path.join(
        PROJECT_ROOT, "output", "e14_marl_train", "train_log.jsonl"))
    ap.add_argument("--output", default=os.path.join(
        PROJECT_ROOT, "output", "e15_diag"))
    ap.add_argument("--device", default="auto",
                    choices=["auto", "mps", "cpu"])
    ap.add_argument("--c-invalid", type=float, default=0.01)
    args = ap.parse_args(argv)
    os.makedirs(args.output, exist_ok=True)

    L = []   # report lines
    L.append("# E15-A0 诊断报告（只读）")
    L.append("")
    L.append("- ckpt: `%s`" % os.path.relpath(args.ckpt, PROJECT_ROOT))
    L.append("- val 协议: s27-s30 × seeds 42-51（40 episodes，greedy argmax）")
    L.append("- c_invalid (e14 default): %g" % args.c_invalid)
    L.append("")

    # ---- section 1: lambda quality ------------------------------------
    sink, leaks = run_val_pass(args.ckpt, args.device)
    lam_est_all = [r[1] for r in sink.lam_rows]
    lam_tru_all = [r[2] for r in sink.lam_rows]
    lam_tru_oth = [r[3] for r in sink.lam_rows]
    ages = [r[4] for r in sink.lam_rows]
    pear_all = _pearson(lam_est_all, lam_tru_all)
    pear_oth = _pearson(lam_est_all, lam_tru_oth)
    mae_all = _mean([abs(e - t) for e, t in zip(lam_est_all, lam_tru_all)])
    mae_oth = _mean([abs(e - t) for e, t in zip(lam_est_all, lam_tru_oth)])
    nz = [i for i, t in enumerate(lam_tru_oth) if t > 0]

    L.append("## 1. λ̂ 质量（AgentMemory 递归 vs 真值在途占用）")
    L.append("")
    L.append("| 口径 | Pearson | MAE | 样本 |")
    L.append("|---|---:|---:|---:|")
    L.append("| λ̂ vs 全部在途(含自己) | %.4f | %.4f | %d |"
             % (pear_all, mae_all, len(lam_est_all)))
    L.append("| λ̂ vs 他人平台在途(目标语义) | %.4f | %.4f | %d |"
             % (pear_oth, mae_oth, len(lam_est_all)))
    if nz:
        mae_nz = _mean([abs(lam_est_all[i] - lam_tru_oth[i]) for i in nz])
        L.append("- 他人占用>0 的子集上 MAE = %.4f（%d/%d 样本，%.1f%%）"
                 % (mae_nz, len(nz), len(lam_est_all),
                    100.0 * len(nz) / len(lam_est_all)))
    L.append("")
    L.append("按目标 age 分桶（他人口径 MAE）：")
    L.append("")
    L.append("| age 桶 | 样本 | MAE | λ̂ 均值 | 真值均值 |")
    L.append("|---|---:|---:|---:|---:|")
    for lo, hi in AGE_BUCKETS:
        sel = [i for i in range(len(ages)) if lo <= ages[i] <= hi]
        if not sel:
            continue
        L.append("| %d-%d | %d | %.4f | %.4f | %.4f |"
                 % (lo, hi, len(sel),
                    _mean([abs(lam_est_all[i] - lam_tru_oth[i])
                           for i in sel]),
                    _mean([lam_est_all[i] for i in sel]),
                    _mean([lam_tru_oth[i] for i in sel])))
    L.append("")

    # ---- section 2: val curve audit -----------------------------------
    audit = audit_train_log(args.train_log)
    L.append("## 2. e14 val 曲线复盘（%d 个 eval 点）"
             % audit["n_points"])
    L.append("")
    L.append("- best val %.4f @ iter %d（第 %d 个 eval 点）"
             % (audit["best"]["val"], audit["best"]["iter"],
                audit["best"]["idx"] + 1))
    L.append("- 停止点 iter %d（val %.4f），距 best %d 个 eval 点"
             % (audit["last"]["iter"], audit["last"]["val"],
                audit["best_to_stop_eval_points"]))
    L.append("- 后半段线性斜率 %.3g / iter" % audit["tail_slope_per_iter"])
    L.append("- 判定：**%s**" % audit["verdict"])
    L.append("")

    # ---- section 3: ammo profile ---------------------------------------
    K = 10
    n_ep = len(sink.pool_curves)
    mean_pool = [_mean([pc[t] for pc in sink.pool_curves
                        if t < len(pc)]) for t in range(K + 1)]
    total_launches = [0.0] * (K - 1)
    for t, c in sink.launch_hist.items():
        if 0 <= t < K - 1:
            total_launches[t] = c / float(n_ep)
    launches_flat = []
    for t in range(K - 1):
        launches_flat += [total_launches[t]]   # per-episode mean per t
    ammo_end = _mean([r["ammo_end"] for r in sink.recs])
    shots_total = _mean([r["shots_total"] for r in sink.recs])
    invalid_rate = _mean([r["invalid_shots"] / max(1, r["shots_total"])
                          for r in sink.recs])

    L.append("## 3. 弹药形态（val × 40 episodes）")
    L.append("")
    L.append("- 平均 pool 曲线: " + " ".join("%.1f" % v for v in mean_pool))
    L.append("- 每步平均发射数: " + " ".join(
        "%.2f" % total_launches[t] for t in range(K - 1)))
    L.append("- 每集平均发射 %0.1f 发 / 弹药池 %d；期末剩余均值 %.1f"
             % (shots_total, sink.envs[0][0].pool0, ammo_end))
    L.append("- 无效交战率（invalid/shots）: %.4f；val 泄漏率 %.4f ± %.4f"
             % (invalid_rate, _mean(leaks), _std(leaks)))
    L.append("")

    # ---- section 4: shaping decomposition ------------------------------
    lp, sr, oc, kc = shape_decompose(sink, args.c_invalid)
    mean_lp = _mean(lp)
    q_lp = _quantiles(lp)
    mean_kc = _mean(kc) if kc else float("nan")
    n_invalid = sum(1 for o in oc if o == "invalid")
    n_miss = sum(1 for o in oc if o == "miss")
    n_kill = sum(1 for o in oc if o == "kill")
    # trigger: mean |launch kick| comparable to mean kill credit
    trigger = abs(mean_lp) >= 0.25 * max(mean_kc, 1e-9)

    L.append("## 4. 整形分解（偏置 (c) 量化，%d 发弹）" % len(lp))
    L.append("")
    L.append("- 结算结果分布：kill %d / miss %d / invalid %d"
             % (n_kill, n_miss, n_invalid))
    L.append("- 平均击杀信用 = %.4f（≈ w̄/total 理论值 79/3942≈0.020）"
             % mean_kc)
    L.append("- 发射步 Φ 负踢：mean %.4f | p25 %.4f | p50 %.4f | p75 %.4f"
             % (mean_lp, q_lp[0.25], q_lp[0.5], q_lp[0.75]))
    L.append("- 结算步回报（含 miss=0）：mean %.4f" % _mean(sr))
    L.append("- 判定：发射步负踢 %s 平均击杀信用的 25%%（%.5f）"
             % (">=" if trigger else "<", 0.25 * mean_kc))
    L.append("- **Φ 翻转备选（A3-备选①）触发：%s**"
             % ("是" if trigger else "否"))
    L.append("")

    # ---- section 5: conclusions ----------------------------------------
    ratio = args.c_invalid / max(mean_kc, 1e-9)
    L.append("## 5. 结论与建议")
    L.append("")
    L.append("1. λ̂：他人口径 Pearson %.3f / MAE %.3f —— %s"
             % (pear_oth, mae_oth,
                "估计基本可用但分辨率有限" if pear_oth > 0.3 else
                ("几乎无信息量（e14 囤弹下真值多 0，属预期）"
                 if _mean(lam_tru_oth) < 0.15 else "需改进")))
    L.append("2. e14 曲线：%s；预算放宽（A2）预期有效。"
             % audit["verdict"])
    L.append("3. c_invalid 档位：当前 %g 达平均击杀信用的 %.1f%%，与偏置(b)"
             "分析一致；维持 e16 四档扫描 0.005/0.01/0.03/0.05，"
             "重点观察 0.05 档是否压制发射数。" % (args.c_invalid,
                                                   100 * ratio))
    L.append("4. Φ 翻转备选：%s（触发条件：|mean 发射步负踢| ≥ 0.25×平均"
             "击杀信用）。" % ("已触发，建议 e16 选档后补 pos 对照"
                              if trigger else "未触发，保持 neg 默认"))
    L.append("")

    rep_path = os.path.join(args.output, "diag_report.md")
    with open(rep_path, "w") as f:
        f.write("\n".join(L) + "\n")
    # raw data dump for later phases
    with open(os.path.join(args.output, "diag_raw.json"), "w") as f:
        json.dump({
            "lam": {"pearson_all": pear_all, "pearson_others": pear_oth,
                    "mae_all": mae_all, "mae_others": mae_oth,
                    "n": len(lam_est_all)},
            "audit": {k: v for k, v in audit.items() if k != "rows"},
            "ammo": {"mean_pool": mean_pool,
                     "launches_per_step": total_launches,
                     "ammo_end": ammo_end, "shots_total": shots_total,
                     "invalid_rate": invalid_rate},
            "shape": {"mean_launch_pen": mean_lp,
                      "quantiles_launch_pen": {str(k): v
                                               for k, v in q_lp.items()},
                      "mean_kill_credit": mean_kc,
                      "outcome_counts": {"kill": n_kill, "miss": n_miss,
                                         "invalid": n_invalid},
                      "phi_flip_trigger": trigger},
            "val_leak": {"mean": _mean(leaks), "std": _std(leaks)},
        }, f, indent=2)
    print("diag report -> %s" % rep_path)
    print("phi-flip trigger: %s | mean launch pen %.5f | mean kill "
          "credit %.5f" % (trigger, mean_lp, mean_kc))
    return 0


if __name__ == "__main__":
    sys.exit(main())
