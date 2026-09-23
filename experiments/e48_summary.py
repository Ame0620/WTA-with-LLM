"""e48: v5 ablation summary & statistics (spec §8.1).

Run AFTER scripts/run_e47_batch.sh completed:
  /opt/anaconda3/envs/wta/bin/python experiments/e48_summary.py

Reads:
  - output/e46_v5_ablation/<arm>_s0/train_log.jsonl + train_summary.json
  - output/e47_v5_ablation_<arm>_s0_eval/family_report.json      (test, 30 seeds)
  - output/e47_v5_ablation_<arm>_s0_gen/<split>/family_report.json
Writes:
  - logs/ablation_v5_summary.json  (arms / pairwise / generalization,
    budget_tier preserved from S5)
Primary metric: leak_rate on test (60 paired units = 2 inst x 30 seeds).
"""
import json
import math
import os

import numpy as np
from scipy import stats

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E46 = os.path.join(HERE, "output", "e46_v5_ablation")
E47 = os.path.join(HERE, "output")
SUMMARY = os.path.join(HERE, "logs", "ablation_v5_summary.json")

ARMS = ["b0_000", "b1_100", "only_010", "only_001",
        "b2_110", "ae_101", "ad_011", "b3_111"]
VEC = {a: tuple(int(c) for c in a[-3:]) for a in ARMS}
CORE = [("b3_111", "b0_000", "三模块整体"),
        ("b3_111", "ad_011", "DCCA 条件贡献"),
        ("b3_111", "ae_101", "EAPS 条件贡献"),
        ("b3_111", "b2_110", "CASP 条件贡献")]


def load_json(p):
    with open(p) as f:
        return json.load(f)


def units(rep):
    """(inst, seed) -> run dict, aligned pairing units."""
    out = {}
    for inst in rep["instances"]:
        for run in inst["runs"]:
            out[(inst["instance"], run["seed"])] = run
    return out


def ci_t(d):
    d = np.asarray(d, float)
    n = len(d)
    m = d.mean()
    if n < 2 or d.std(ddof=1) == 0:
        return m, (m, m)
    h = stats.t.ppf(0.975, n - 1) * d.std(ddof=1) / math.sqrt(n)
    return m, (m - h, m + h)


def ci_boot(d, b=10000, seed=0):
    rng = np.random.default_rng(seed)
    d = np.asarray(d, float)
    idx = rng.integers(0, len(d), size=(b, len(d)))
    means = d[idx].mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def compare(ua, ub, metric="leak_rate"):
    """A vs B: diff = B - A on metric (positive => A better for leak)."""
    keys = sorted(set(ua) & set(ub))
    assert len(keys) == 60, f"expected 60 paired units, got {len(keys)}"
    da = np.array([ua[k][metric] for k in keys], float)
    db = np.array([ub[k][metric] for k in keys], float)
    d = db - da
    m, tci = ci_t(d)
    bci = ci_boot(d)
    if np.allclose(d, 0):
        w_stat, w_p = float("nan"), 1.0
        note = "zero differences (Wilcoxon undefined)"
    else:
        w = stats.wilcoxon(da, db, zero_method="wilcox")
        w_stat, w_p = float(w.statistic), float(w.pvalue)
        note = ""
    return {
        "metric": metric, "n_paired_units": len(keys),
        "mean_A": float(da.mean()), "mean_B": float(db.mean()),
        "mean_diff_B_minus_A": float(m),
        "ci95_t": [float(tci[0]), float(tci[1])],
        "ci95_bootstrap": [bci[0], bci[1]],
        "wilcoxon_stat": w_stat, "wilcoxon_p": float(w_p),
        "significant_alpha0.05": bool(w_p < 0.05),
        "per_unit_diffs": {f"{k[0]}|seed{k[1]}": float(x)
                           for k, x in zip(keys, d)},
        "note": note,
    }


def mech_from_trainlog(arm):
    rows = [json.loads(l) for l in
            open(os.path.join(E46, f"{arm}_s0", "train_log.jsonl"))]
    best_i = int(np.argmin([r["val_leak_mean"] for r in rows]))
    r = rows[best_i]
    # 收敛速度: first eval point reaching val_leak_mean < 0.6 (else None)
    conv = next((row["iter"] for row in rows
                 if row["val_leak_mean"] < 0.6), None)
    return {
        "best_iter": r["iter"], "best_val": r["val_leak_mean"],
        "credit_nonzero_ratio": r.get("credit_nonzero_ratio"),
        "adv_indiv_over_team_std": r.get("adv_indiv_over_team_std"),
        "reward_nonzero_ratio": r.get("reward_nonzero_ratio"),
        "reward_nonzero_ratio_base": r.get("reward_nonzero_ratio_base"),
        "r_shaped_mean": r.get("r_shaped_mean"),
        "iter_to_val_below_0.6": conv,
    }, rows


def main():
    summ = load_json(SUMMARY) if os.path.exists(SUMMARY) else {}
    arms, ev_units, fams = {}, {}, {}
    for a in ARMS:
        rep = load_json(os.path.join(
            E47, f"e47_v5_ablation_{a}_s0_eval", "family_report.json"))
        fam = rep["family"]
        ev_units[a] = units(rep)
        fams[a] = fam
        mech, rows = mech_from_trainlog(a)
        last = rows[-1]
        ts = load_json(os.path.join(E46, f"{a}_s0", "train_summary.json"))
        # destroyed value per shot (resource efficiency, family level)
        dv = fam["destroyed_value"]["mean"]
        sh = fam["shots_total"]["mean"]
        pm = fam.get("policy_mechanics", {})
        arms[a] = {
            "vec_(D,E,C)": VEC[a],
            "budget_wall_sec": ts.get("total_wall_sec"),
            "wall_per_iter_last": last.get("wall_per_iter"),
            "task": {
                "leak_rate_mean": fam["leak_rate"]["mean"],
                "leak_rate_std": fam["leak_rate"]["std"],
                "leak_rate_worst": fam["leak_rate"]["worst"],
            },
            "engagement": {
                "invalid_engagement_rate": fam[
                    "invalid_engagement_rate"]["mean"],
                "destroyed_value": dv,
                "shots_total": sh,
            },
            "resource": {
                "destroyed_value_per_shot":
                    dv / sh if sh else None,
            },
            "engineering": {
                "params_actor": last.get("params_actor"),
                "params_critic": last.get("params_critic"),
                "policy_latency_us_mean": pm.get("policy_latency_us_mean"),
                "eval_latency_p50_ms": fam["latency_p50"]["mean"],
            },
            "mechanism": {
                "dcca": {k: mech[k] for k in
                         ("credit_nonzero_ratio",
                          "adv_indiv_over_team_std")},
                "eaps": {k: mech[k] for k in
                         ("reward_nonzero_ratio",
                          "reward_nonzero_ratio_base", "r_shaped_mean",
                          "iter_to_val_below_0.6")},
                "casp": {
                    "repeat_targeting_per_run_mean": pm.get(
                        "repeat_targeting_per_run_mean"),
                    "best_val": mech["best_val"],
                    "best_iter": mech["best_iter"],
                },
            },
            "stability": None,  # 待阶段 2 多训练种子
        }
        print(f"{a}: leak={fam['leak_rate']['mean']:.4f} "
              f"inv_eng={fam['invalid_engagement_rate']['mean']:.4f} "
              f"dv/shot={arms[a]['resource']['destroyed_value_per_shot']:.1f}"
              if arms[a]["resource"]["destroyed_value_per_shot"]
              else f"{a}: leak={fam['leak_rate']['mean']:.4f}")

    pairwise = {}
    for A, B, label in CORE:
        pairwise[f"{A} vs {B}"] = {"question": label,
                                   "leak_rate": compare(ev_units[A],
                                                        ev_units[B])}
    # incremental path (descriptive)
    inc = [float(fams[a]["leak_rate"]["mean"]) for a in
           ("b0_000", "b1_100", "b2_110", "b3_111")]
    pairwise["incremental_path_b0-b1-b2-b3"] = {
        "question": "递增路径(描述性)", "leak_rate_means":
            {"b0_000": inc[0], "b1_100": inc[1], "b2_110": inc[2],
             "b3_111": inc[3]},
        "deltas": {"b1-b0": inc[1] - inc[0], "b2-b1": inc[2] - inc[1],
                   "b3-b2": inc[3] - inc[2]},
        "monotonic_decreasing": bool(inc[0] > inc[1] > inc[2] > inc[3])}
    # full-factorial descriptive (single seed!)
    def cell(d, e, c):
        return next(a for a in ARMS if VEC[a] == (d, e, c))
    fac = {"leak_rate_cells": {a: float(fams[a]["leak_rate"]["mean"])
                               for a in ARMS}}
    for name, idx in (("DCCA", 0), ("EAPS", 1), ("CASP", 2)):
        on = [fams[a]["leak_rate"]["mean"] for a in ARMS if VEC[a][idx] == 1]
        off = [fams[a]["leak_rate"]["mean"] for a in ARMS if VEC[a][idx] == 0]
        fac[f"main_effect_{name}"] = float(np.mean(on) - np.mean(off))
    pairwise["factorial_descriptive_single_seed"] = fac

    # generalization block
    gen = {}
    for a in ARMS:
        gen[a] = {}
        for sp in ("train", "val", "test"):
            p = os.path.join(E47, f"e47_v5_ablation_{a}_s0_gen", sp,
                             "family_report.json")
            if os.path.exists(p):
                g = load_json(p)["family"]
                gen[a][sp] = {"leak_rate_mean": g["leak_rate"]["mean"],
                              "leak_rate_std": g["leak_rate"]["std"],
                              "invalid_engagement_rate":
                                  g["invalid_engagement_rate"]["mean"]}
    summ.update({"arms": arms, "pairwise": pairwise,
                 "generalization": gen,
                 "caveats": [
                     "单训练种子(s0)轮次: 所有比较结论仅为「初步」,正式结论待阶段2多训练种子",
                     "预算档位 A-1(1000x48, patience 30): 与 v5 主表 12h 完整档采样预算不同,不可同表直接对比(R8)",
                     "配对单元 = 2 test 实例 x 30 MC seeds = 60; Wilcoxon 零差异情形记 p=1",
                     "三个留一差值不得相加当作总提升(模块交互, §9)",
                     "CASP 动态规模适应性: v5 家族内同规模(10x100),跨规模检验留待后续家族",
                 ]})
    with open(SUMMARY, "w") as f:
        json.dump(summ, f, indent=2, ensure_ascii=False)
    print("summary written:", SUMMARY)
    for k, v in pairwise.items():
        if "vs" in k:
            lr = v["leak_rate"]
            print(f"{k}: mean {lr['mean_A']:.4f} vs {lr['mean_B']:.4f}, "
                  f"diff(B-A)={lr['mean_diff_B_minus_A']:+.4f} "
                  f"CI_t=[{lr['ci95_t'][0]:+.4f},{lr['ci95_t'][1]:+.4f}] "
                  f"p={lr['wilcoxon_p']:.2e} "
                  f"sig={lr['significant_alpha0.05']}")


if __name__ == "__main__":
    main()
