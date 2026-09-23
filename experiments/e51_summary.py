"""e51: v3 ablation summary (spec S6).

Reads e49 training outputs, e50 test evals (+ generalization) and the locked
budget tier, then writes logs/ablation_v3_summary.json with:

  * per-arm per-seed records (convergence @ 0.75, wall, early-stop, budget)
  * main table over 180 paired units per arm (2 test instances x 30 MC
    seeds x 3 training seeds): leak, hit-rate, invalid engagement,
    destroyed value (abs+rel), ammo efficiency, worst, params, latency
  * cross-seed std + stability table (std/mean per arm)
  * direction consistency: 8 module hypotheses x 2 primary metrics,
    one vote per training seed (3 votes each)
  * generalization table (train/val/test split means per arm)
  * cross-family descriptive comparison vs v5 (logs/ablation_v5_summary.json)
  * hard invariants: shots_total <= 18, ammo_end >= 0, zero illegal actions
"""
import json
from pathlib import Path
from statistics import mean, stdev

ROOT = Path(__file__).resolve().parents[1]
E49 = ROOT / "output" / "e49_v3_ablation"
E50 = "output/e50_v3_ablation_{arm}_s{seed}_eval"
GEN = "output/e50_v3_ablation_{arm}_s{seed}_gen/{split}"
SUMMARY = ROOT / "logs" / "ablation_v3_summary.json"
V5_SUMMARY = ROOT / "logs" / "ablation_v5_summary.json"
BUDGET = ROOT / "logs" / "ablation_v3_budget.json"
CONVERGE = 0.75
SEEDS = [0, 1, 2]

ARMS = {  # cfg-id -> (dirname, (dcca, eaps, casp), label)
    "c1": ("b0_000", (0, 0, 0), "b0 MAPPO^0"),
    "c2": ("only_001", (0, 0, 1), "only CASP"),
    "c3": ("only_010", (0, 1, 0), "only EAPS"),
    "c4": ("ad_011", (0, 1, 1), "EAPS+CASP"),
    "c5": ("b1_100", (1, 0, 0), "only DCCA"),
    "c6": ("ae_101", (1, 0, 1), "DCCA+CASP"),
    "c7": ("b2_110", (1, 1, 0), "DCCA+EAPS"),
    "c8": ("b3_111", (1, 1, 1), "full EC-MAPPO"),
}

# 8 module hypotheses: (name, arm_high, arm_low, metric direction)
#   primary metrics: leak_rate (lower better), destroyed_value_rel (higher better)
HYPO = [
    ("h1_full_vs_b0", "c8", "c1"),
    ("h2_only_casp_vs_b0", "c2", "c1"),
    ("h3_only_eaps_vs_b0", "c3", "c1"),
    ("h4_eaps_casp_vs_b0", "c4", "c1"),
    ("h5_dcca_margin", "c8", "c5"),
    ("h6_eaps_margin", "c8", "c6"),
    ("h7_casp_margin", "c8", "c7"),
    ("h8_combo_vs_only_casp", "c8", "c4"),
]


def _msw(xs):
    if not xs:
        return None
    m = mean(xs)
    return {"mean": m, "std": stdev(xs) if len(xs) > 1 else 0.0,
            "min": min(xs), "max": max(xs), "n": len(xs)}


def load_arm_seed(cfg, dirname, s):
    """Collect per-run flattened metrics for one (arm, training seed)."""
    rep = json.load(open(ROOT / E50.format(arm=dirname, seed=s) /
                         "family_report.json"))
    runs = []
    for inst in rep["instances"]:
        tv = inst["meta"]["total_value"]
        for r in inst["runs"]:
            assert r["shots_total"] <= 18, "ammo bound violated (shots>18)"
            assert r["ammo_end"] >= 0, "ammo_end < 0"
            runs.append({
                "leak_rate": r["leak_rate"],
                "hit_rate": (r["destroyed_count"] / r["shots_total"]
                             if r["shots_total"] else 0.0),
                "invalid_engagement_rate":
                    r["invalid_shots"] / r["shots_total"]
                    if r["shots_total"] else 0.0,
                "destroyed_value": r["destroyed_value"],
                "destroyed_value_rel": r["destroyed_value"] / tv,
                "ammo_efficiency": r["destroyed_value"] / r["shots_total"]
                if r["shots_total"] else 0.0,
            })
    return rep, runs


def main():
    budget = json.load(open(BUDGET))
    out = {"budget_tier": budget, "converge_threshold": CONVERGE,
           "paired_units_per_arm": 180, "arms": {}, "main": {},
           "cross_seed": {}, "stability": {}, "direction": {},
           "significance": {},
           "generalization": {}, "cross_family_v5_vs_v3": {}, "caveats": []}

    per_seed_metric = {}   # cfg -> seed -> {metric: [values over 180]}
    for cfg, (dirname, sw, label) in ARMS.items():
        out["arms"][cfg] = {"dir": dirname, "switches": list(sw),
                            "label": label, "seeds": {}}
        per_seed_metric[cfg] = {}
        for s in SEEDS:
            d = E49 / f"{dirname}_s{s}"
            ts = json.load(open(d / "train_summary.json"))
            log = [json.loads(l) for l in open(d / "train_log.jsonl")]
            last_val = log[-1]["val_leak_mean"]
            converged = any(r["val_leak_mean"] <= CONVERGE for r in log)
            it_at = next((r["iter"] for r in log
                          if r["val_leak_mean"] <= CONVERGE), None)
            rep, runs = load_arm_seed(cfg, dirname, s)
            mech = rep["instances"][0].get("policy_mechanics", {})
            out["arms"][cfg]["seeds"][str(s)] = {
                "converged": converged, "iters_to_converge": it_at,
                "last_val": last_val, "best_val": ts["best_val"],
                "wall_h": ts["total_wall_sec"] / 3600.0,
                "env_steps": ts["env_steps"],
                "stop_reason": ts["final_metrics"]["stop_reason"],
                "params": ts["params_count"],
                "ablation_meta": ts["ablation"],
                "result_hashes": [i["result_hash"][:16]
                                  for i in rep["instances"]],
            }
            per_seed_metric[cfg][s] = {
                k: [r[k] for r in runs] for k in runs[0]}
            per_seed_metric[cfg][s]["latency_us"] = \
                mech.get("policy_latency_us_mean")
            per_seed_metric[cfg][s]["repeat_targeting_per_run"] = \
                mech.get("repeat_targeting_per_run_mean")

    # ---- main table: pool all 180 paired units per arm ----
    for cfg in ARMS:
        pooled = {}
        for k in ("leak_rate", "hit_rate", "invalid_engagement_rate",
                  "destroyed_value", "destroyed_value_rel", "ammo_efficiency"):
            xs = []
            for s in SEEDS:
                xs += per_seed_metric[cfg][s][k]
            pooled[k] = _msw(xs)
        pooled["worst_leak"] = pooled["leak_rate"]["max"]
        pooled["params"] = out["arms"][cfg]["seeds"]["0"]["params"]
        pooled["latency_us"] = mean(
            [per_seed_metric[cfg][s]["latency_us"]
             for s in SEEDS
             if per_seed_metric[cfg][s]["latency_us"] is not None])
        out["main"][cfg] = pooled

    # ---- cross-seed std (arm-level seed means) + stability ----
    for cfg in ARMS:
        out["cross_seed"][cfg] = {}
        out["stability"][cfg] = {}
        for k in ("leak_rate", "hit_rate", "destroyed_value_rel",
                  "invalid_engagement_rate", "ammo_efficiency"):
            seed_means = [mean(per_seed_metric[cfg][s][k]) for s in SEEDS]
            sd = stdev(seed_means) if len(seed_means) > 1 else 0.0
            mu = mean(seed_means)
            out["cross_seed"][cfg][k] = {
                "seed_means": seed_means, "std": sd}
            out["stability"][cfg][k] = (abs(sd / mu) if mu else None)

    # ---- direction consistency: 3 votes (one per seed) per hypothesis ----
    for name, hi, lo in HYPO:
        out["direction"][name] = {
            "pair": f"{hi}({ARMS[hi][0]}) vs {lo}({ARMS[lo][0]})"}
        for met, better in (("leak_rate", "lower"),
                            ("destroyed_value_rel", "higher")):
            votes = []
            for s in SEEDS:
                a = mean(per_seed_metric[hi][s][met])
                b = mean(per_seed_metric[lo][s][met])
                votes.append((a < b) if better == "lower" else (a > b))
            out["direction"][name][met] = {
                "votes": votes, "consistent": all(votes),
                "votes_for": sum(votes)}

    # ---- significance: paired Wilcoxon over 180 paired units per hypothesis
    # plus paired t over the 3 seed-level means (descriptive, n=3) ----
    from scipy.stats import ttest_rel, wilcoxon

    out["significance"] = {}
    for name, hi, lo in HYPO:
        out["significance"][name] = {}
        for met in ("leak_rate", "destroyed_value_rel"):
            a, b = [], []
            for s in SEEDS:
                a += per_seed_metric[hi][s][met]
                b += per_seed_metric[lo][s][met]
            diff = [x - y for x, y in zip(a, b)]
            w = wilcoxon(a, b, zero_method="wilcox", mode="auto")
            sm_hi = [mean(per_seed_metric[hi][s][met]) for s in SEEDS]
            sm_lo = [mean(per_seed_metric[lo][s][met]) for s in SEEDS]
            t = ttest_rel(sm_hi, sm_lo)
            out["significance"][name][met] = {
                "mean_diff": mean(diff),
                "wilcoxon_p": float(w.pvalue),
                "seedmean_t_p": float(t.pvalue),
                "n_pairs": len(diff),
                "test": "Wilcoxon signed-rank, two-sided, 180 paired units "
                        "(2 instances x 30 MC seeds x 3 training seeds)"}

    # ---- generalization (split means per arm, seeds pooled) ----
    for cfg, (dirname, sw, label) in ARMS.items():
        out["generalization"][cfg] = {}
        for split in ("train", "val", "test"):
            vals, dvals = [], []
            for s in SEEDS:
                rep = json.load(open(ROOT / GEN.format(
                    arm=dirname, seed=s, split=split) / "family_report.json"))
                for inst in rep["instances"]:
                    tv = inst["meta"]["total_value"]
                    for r in inst["runs"]:
                        vals.append(r["leak_rate"])
                        dvals.append(r["destroyed_value"] / tv)
            out["generalization"][cfg][split] = {
                "leak_rate_mean": mean(vals),
                "destroyed_value_rel_mean": mean(dvals)}

    # ---- cross-family descriptive comparison (v5 single-seed vs v3 3-seed) --
    if V5_SUMMARY.exists():
        v5 = json.load(open(V5_SUMMARY))
        v5_map = {"c1": "b0_000", "c8": "b3_111", "c4": "ad_011",
                  "c6": "ae_101", "c7": "b2_110", "c5": "b1_100",
                  "c3": "only_010", "c2": "only_001"}
        for cfg, v5arm in v5_map.items():
            v5leak = v5["arms"][v5arm].get("task", {}).get("leak_rate_mean")
            out["cross_family_v5_vs_v3"][cfg] = {
                "v5_leak_single_seed": v5leak,
                "v3_leak_3seed": out["main"][cfg]["leak_rate"]["mean"],
                "note": "descriptive only: v5 = DN-WTA v5 dataset (n=100), "
                        "v3 = DN-WTA v3 dataset (n=50); budgets differ "
                        "(v5 tier A vs v3 tier D)"}

    out["caveats"] = [
        "v3 tier-D budget (500x64, patience 20) is smaller than the v5 "
        "tier-A budget; absolute levels are not comparable across families",
        "single training seed per arm in v5 vs 3 seeds in v3",
        "direction votes use paired-unit means per training seed",
    ]
    SUMMARY.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print("written:", SUMMARY)
    # console digest
    print("\n%-4s %-10s %10s %10s %10s %10s %8s" %
          ("cfg", "dir", "leak", "hit", "dval_rel", "invalid", "params"))
    for cfg in ARMS:
        m = out["main"][cfg]
        print("%-4s %-10s %10.4f %10.4f %10.4f %10.4f %8d" %
              (cfg, ARMS[cfg][0], m["leak_rate"]["mean"],
               m["hit_rate"]["mean"], m["destroyed_value_rel"]["mean"],
               m["invalid_engagement_rate"]["mean"], m["params"]))

    print("\n%-22s %10s %12s %12s" %
          ("hypothesis", "leak_diff", "wilcoxon_p", "seed_t_p"))
    for name, _, _ in HYPO:
        sg = out["significance"][name]["leak_rate"]
        print("%-22s %+10.4f %12.2e %12.3f" %
              (name, sg["mean_diff"], sg["wilcoxon_p"], sg["seedmean_t_p"]))


if __name__ == "__main__":
    main()
