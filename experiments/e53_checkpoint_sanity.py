"""e53 s0 lightweight checkpoint (r2 §5, after the first seed pass).

Per arm (8 arms of s0): artifacts exist; the train log's first line is
the [ablation] switch line and the second the [reshaping] line, both
matching the arm config; train_summary + best.pt carry ablation AND
reshaping metadata equal to the LOCKED recalibration params (from
logs/recal_selection.json); all log fields finite; stop_reason valid;
curve milestones (first iter with val < 0.75, best_val@iter).

Direction sanity (halt on anomaly, single-seed wide thresholds):
  c8: best(b3_111)  <= best(b0_000) + 0.03
  c3: best(only_010) <= best(b0_000) + 0.02   (post-recal EAPS single)
  c5: best(b1_100)  <= best(b0_000) + 0.02   (post-recal DCCA single)
Writes logs/e53_s0_checkpoint.json. Exits 0 (PASS) / 1 (FAIL).
"""
import json
import math
import os
import sys

import torch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E53 = os.path.join(ROOT, "output", "e53_v3_ablation_r2")
SEL = json.load(open(os.path.join(ROOT, "logs", "recal_selection.json")))
LOCK = SEL["locked"]
WANT = (float(LOCK["phi_scale"]), float(LOCK["credit_alpha"]),
        float(LOCK["cf_beta"]))
ARMS = {
    "b0_000_s0": (0, 0, 0), "b3_111_s0": (1, 1, 1), "ad_011_s0": (0, 1, 1),
    "ae_101_s0": (1, 0, 1), "b2_110_s0": (1, 1, 0), "b1_100_s0": (1, 0, 0),
    "only_010_s0": (0, 1, 0), "only_001_s0": (0, 0, 1),
}


def finite(o):
    if isinstance(o, float):
        return math.isfinite(o)
    if isinstance(o, dict):
        return all(finite(v) for v in o.values())
    if isinstance(o, list):
        return all(finite(v) for v in o)
    return True


report = {"locked_params": WANT, "arms": {}, "sanity": {}, "fails": []}
for arm, sw in ARMS.items():
    d = os.path.join(E53, arm)
    try:
        ts = json.load(open(os.path.join(d, "train_summary.json")))
        rows = [json.loads(l) for l in open(os.path.join(d,
                                                         "train_log.jsonl"))]
        got = (ts["ablation"]["use_dcca"], ts["ablation"]["use_eaps"],
               ts["ablation"]["use_casp"])
        assert got == sw, "summary meta %s != %s" % (got, sw)
        gsh = (float(ts["reshaping"]["phi_scale"]),
               float(ts["reshaping"]["credit_alpha"]),
               float(ts["reshaping"]["cf_beta"]))
        assert gsh == WANT, "summary reshaping %s != locked %s" % (gsh, WANT)
        with open(os.path.join(ROOT, "logs", "e53_%s.log" % arm)) as f:
            head = [next(f) for _ in range(2)]
        assert head[0].startswith("[ablation]"), "first log line wrong"
        assert head[1].startswith("[reshaping]"), "second log line wrong"
        for ln, w in zip((head[0], head[1]),
                         ("use_dcca=%d use_eaps=%d use_casp=%d" % sw,
                          "phi_scale=%g credit_alpha=%g cf_beta=%g" % WANT)):
            assert w in ln, "log line %r lacks %r" % (ln, w)
        assert all(finite(r) for r in rows), "NaN in train_log"
        assert ts["final_metrics"]["stop_reason"] in ("iters_done",
                                                      "early_stop")
        # r2 §5: params window + zero illegal actions over the pass
        assert all(1e3 <= r["params_actor"] <= 1e5
                   and 1e3 <= r["params_critic"] <= 1e5 for r in rows), \
            "params window [1e3,1e5] violated"
        assert all(r["illegal_actions"] == 0 for r in rows), \
            "illegal actions > 0"
        ck = torch.load(os.path.join(d, "best.pt"), map_location="cpu",
                        weights_only=False)
        cg = (ck["ablation"]["use_dcca"], ck["ablation"]["use_eaps"],
              ck["ablation"]["use_casp"])
        assert cg == sw, "ckpt meta %s != %s" % (cg, sw)
        csh = (float(ck["reshaping"]["phi_scale"]),
               float(ck["reshaping"]["credit_alpha"]),
               float(ck["reshaping"]["cf_beta"]))
        assert csh == WANT, "ckpt reshaping %s != locked %s" % (csh, WANT)
        below = [r["iter"] for r in rows if r["val_leak_mean"] < 0.75]
        best_row = min(rows, key=lambda r: r["val_leak_mean"])
        report["arms"][arm] = {
            "first_val_below_075": below[0] if below else None,
            "best_val": best_row["val_leak_mean"],
            "best_iter": best_row["iter"],
            "iters_run": rows[-1]["iter"],
            "wall_h": round(rows[-1]["wall_sec"] / 3600.0, 3),
            "stop_reason": ts["final_metrics"]["stop_reason"],
            "mech_tail": {k: rows[-1][k] for k in rows[-1]
                          if k.startswith(("r_shape_share",
                                           "credit_adv_share"))}}
    except Exception as e:  # noqa: BLE001
        report["fails"].append("%s: %s" % (arm, e))

bv = {a: report["arms"][a]["best_val"] for a in ARMS
      if a in report["arms"]}
if len(bv) == 8:
    report["sanity"] = {
        "c8_vs_c1": {"delta": round(bv["b3_111_s0"] - bv["b0_000_s0"], 5),
                     "limit": 0.03,
                     "pass": bv["b3_111_s0"] <= bv["b0_000_s0"] + 0.03},
        "c3_vs_c1": {"delta": round(bv["only_010_s0"] - bv["b0_000_s0"], 5),
                     "limit": 0.02,
                     "pass": bv["only_010_s0"] <= bv["b0_000_s0"] + 0.02},
        "c5_vs_c1": {"delta": round(bv["b1_100_s0"] - bv["b0_000_s0"], 5),
                     "limit": 0.02,
                     "pass": bv["b1_100_s0"] <= bv["b0_000_s0"] + 0.02}}
    for k, v in report["sanity"].items():
        if not v["pass"]:
            report["fails"].append("direction sanity %s (delta %.5f > "
                                   "%.2f)" % (k, v["delta"], v["limit"]))

# ---- lightweight rollout invariant check (12 rollouts per arm) -----
# loads best.pt through the anti-cross-arm-guarded evaluator path and
# re-verifies shots_total <= 18 / ammo_end >= 0 on val instances.
import subprocess  # noqa: E402
import sys as _sys  # noqa: E402

os.environ["MARL_EXPECT_RESHAPING"] = "%.10g,%.10g,%.10g" % WANT
for arm in ARMS:
    tmp = os.path.join(ROOT, "output", "e53_v3_ablation_r2",
                       "_sanity_" + arm)
    r = subprocess.run(
        [_sys.executable, os.path.join(ROOT, "experiments",
                                       "dn_family_eval.py"),
         "--split", "val", "--policy", "ecmappo",
         "--model", os.path.join(E53, arm, "best.pt"),
         "--seeds", "3", "--seed-base", "7", "--no-ref",
         "--output", tmp],
        capture_output=True, text=True, timeout=1800)
    if r.returncode != 0:
        report["fails"].append("%s: sanity rollout failed: %s"
                               % (arm, r.stderr.strip()[-200:]))
        continue
    fr = json.load(open(os.path.join(tmp, "family_report.json")))
    worst_shots = max(rr["shots_total"] for i in fr["instances"]
                      for rr in i["runs"])
    min_ammo = min(rr["ammo_end"] for i in fr["instances"]
                   for rr in i["runs"])
    if not (worst_shots <= 18 and min_ammo >= 0):
        report["fails"].append("%s: rollout invariant (shots<=%d, "
                               "ammo_end>=%d)" % (arm, worst_shots,
                                                  min_ammo))
    report["arms"][arm].setdefault("rollout", {})["worst_shots"] = \
        worst_shots
    report["arms"][arm]["rollout"]["min_ammo_end"] = min_ammo

with open(os.path.join(ROOT, "logs", "e53_s0_checkpoint.json"), "w") as f:
    json.dump(report, f, indent=1, ensure_ascii=False)
print(json.dumps({"sanity": report.get("sanity", {}),
                  "fails": report["fails"]}, ensure_ascii=False, indent=1))
print("E53 S0 CHECKPOINT:", "PASS" if not report["fails"] else "FAIL")
sys.exit(0 if not report["fails"] else 1)
