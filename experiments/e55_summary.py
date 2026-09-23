"""e55: r2 ablation summary (r2 spec §S7).

Reads e53 training outputs, e54 test evals (+ generalization), the
locked budget tier (logs/ablation_v3r2_budget.json) and the locked
recalibration pick (logs/recal_selection.json), then writes
logs/ablation_v3r2_summary.json with everything e51 produced, plus the
r2 additions:

  * per-arm reshaping metadata + lock-consistency assertion (R3)
  * mechanism-instrumentation table (r_shape_share / credit_adv_share
    per arm, window tail means - nonzero iff the module is on)
  * recalibration evidence table (e52 ten-arm val curves + selection
    chain digest) (R8/R10)
  * round-over-round comparison table c8/c1/c3/c5 vs the round-1
    summary (descriptive; tier/device differ - declared caveat)
  * acceptance checklist R1-R11 with machine-checkable entries.
"""
import json
from pathlib import Path
from statistics import mean, stdev

ROOT = Path(__file__).resolve().parents[1]
E53 = ROOT / "output" / "e53_v3_ablation_r2"
E54 = "output/e54_v3_ablation_{arm}_s{seed}_eval"
GEN = "output/e54_v3_ablation_{arm}_s{seed}_gen/{split}"
SUMMARY = ROOT / "logs" / "ablation_v3r2_summary.json"
R1_SUMMARY = ROOT / "logs" / "ablation_v3_summary.json"
BUDGET = ROOT / "logs" / "ablation_v3r2_budget.json"
SEL = ROOT / "logs" / "recal_selection.json"
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
HYPO = [
    ("h1_full_vs_b0", "c8", "c1"),
    ("h2_only_casp_vs_b0", "c2", "c1"),
    ("h3_only_eaps_vs_b0", "c3", "c1"),
    ("h4_eaps_casp_vs_b0", "c4", "c1"),
    ("h5_dcca_margin", "c8", "c5"),
    ("h6_eaps_margin", "c8", "c6"),
    ("h7_casp_margin", "c8", "c7"),
    ("h8_combo_vs_only_casp", "c8", "c4"),
    # r2 spec §7.4: the three single-module pairs (c2/c3/c5 vs c1) are
    # the formal criteria for requirement (2); c5<->c1 was missing.
    ("h9_only_dcca_vs_b0", "c5", "c1"),
]


def _msw(xs):
    if not xs:
        return None
    m = mean(xs)
    return {"mean": m, "std": stdev(xs) if len(xs) > 1 else 0.0,
            "min": min(xs), "max": max(xs), "n": len(xs)}


def load_arm_seed(dirname, s):
    rep = json.load(open(ROOT / E54.format(arm=dirname, seed=s) /
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
    sel = json.load(open(SEL))
    lock = sel["locked"]
    lock_t = (float(lock["phi_scale"]), float(lock["credit_alpha"]),
              float(lock["cf_beta"]))
    out = {"budget_tier": budget, "recal_lock": lock,
           "converge_threshold": CONVERGE,
           "paired_units_per_arm": 180, "arms": {}, "main": {},
           "cross_seed": {}, "stability": {}, "direction": {},
           "significance": {}, "mechanism": {}, "recal_evidence": {},
           "round_comparison": {}, "generalization": {},
           "acceptance": {}, "caveats": []}

    per_seed_metric = {}
    for cfg, (dirname, sw, label) in ARMS.items():
        out["arms"][cfg] = {"dir": dirname, "switches": list(sw),
                            "label": label, "seeds": {}}
        per_seed_metric[cfg] = {}
        for s in SEEDS:
            d = E53 / f"{dirname}_s{s}"
            ts = json.load(open(d / "train_summary.json"))
            # R3: every arm carries the LOCKED triple verbatim
            got_t = (float(ts["reshaping"]["phi_scale"]),
                     float(ts["reshaping"]["credit_alpha"]),
                     float(ts["reshaping"]["cf_beta"]))
            assert got_t == lock_t, \
                "arm %s_s%s reshaping %s != locked %s" % (dirname, s,
                                                          got_t, lock_t)
            log = [json.loads(l) for l in open(d / "train_log.jsonl")]
            last_val = log[-1]["val_leak_mean"]
            converged = any(r["val_leak_mean"] <= CONVERGE for r in log)
            it_at = next((r["iter"] for r in log
                          if r["val_leak_mean"] <= CONVERGE), None)
            rep, runs = load_arm_seed(dirname, s)
            mech = rep["instances"][0].get("policy_mechanics", {})
            out["arms"][cfg]["seeds"][str(s)] = {
                "converged": converged, "iters_to_converge": it_at,
                "last_val": last_val, "best_val": ts["best_val"],
                "wall_h": ts["total_wall_sec"] / 3600.0,
                "env_steps": ts["env_steps"],
                "stop_reason": ts["final_metrics"]["stop_reason"],
                "params": ts["params_count"],
                "ablation_meta": ts["ablation"],
                "reshaping_meta": ts["reshaping"],
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
                  "destroyed_value", "destroyed_value_rel",
                  "ammo_efficiency"):
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

    # ---- cross-seed std + stability ----
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

    # ---- direction consistency (3 votes per hypothesis) ----
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

    # ---- significance: paired Wilcoxon + seed-mean t ----
    from scipy.stats import ttest_rel, wilcoxon

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

    # ---- mechanism instrumentation (r2 §3.4) ---------------------------
    # tail-window means of r_shape_share / credit_adv_share: nonzero iff
    # the corresponding module is on in that arm
    for cfg, (dirname, sw, label) in ARMS.items():
        rows = {}
        for k in ("r_shape_share", "credit_adv_share"):
            vals = []
            for s in SEEDS:
                log = [json.loads(l) for l in
                       open(E53 / f"{dirname}_s{s}" / "train_log.jsonl")]
                vals.append(mean([r[k] for r in log[-8:]]))
            rows[k] = {"tail_mean": mean(vals), "per_seed": vals}
        out["mechanism"][cfg] = {
            "r_shape_share": rows["r_shape_share"],
            "credit_adv_share": rows["credit_adv_share"],
            "consistency": (
                (rows["r_shape_share"]["tail_mean"] > 0.0)
                == bool(ARMS[cfg][1][1])
                and (rows["credit_adv_share"]["tail_mean"] > 0.0)
                == bool(ARMS[cfg][1][0]))}

    # ---- recalibration evidence (R8/R10) --------------------------------
    out["recal_evidence"] = {
        "e52_arms": {n: {"best_val": a["best_val"],
                         "best_iter": a["best_iter"],
                         "params": a["params"],
                         "curve_pts": [[p["iter"], p["val"]]
                                       for p in a["val_curve"]]}
                     for n, a in sel.get("arms", {}).items()},
        "stage_eaps": sel.get("stages", {}).get("eaps"),
        "stage_dcca": sel.get("stages", {}).get("dcca"),
        "fuse": sel.get("stages", {}).get("fuse"),
        "P3_triggered": "P3" in (sel.get("stages", {}).get("fuse", {})
                                 or {}),
        "history": sel.get("history", []),
        "budget": json.load(open(ROOT / "logs" / "recal_budget.json")),
    }

    # ---- round-over-round comparison (descriptive; declared caveat) ----
    if R1_SUMMARY.exists():
        r1 = json.load(open(R1_SUMMARY))
        for cfg in ("c8", "c1", "c3", "c5", "c2"):
            r1m = r1["main"][cfg]["leak_rate"]["mean"]
            r2m = out["main"][cfg]["leak_rate"]["mean"]
            out["round_comparison"][cfg] = {
                "r1_leak": r1m, "r2_leak": r2m,
                "delta": r2m - r1m,
                "r1_dir_consistent":
                    r1["direction"].get(
                        {"c8": "h1_full_vs_b0", "c1": "h1_full_vs_b0",
                         "c3": "h3_only_eaps_vs_b0", "c5": "h5_dcca_margin",
                         "c2": "h2_only_casp_vs_b0"}[cfg],
                        {}).get("leak_rate", {}).get("consistent"),
                "r2_dir_consistent":
                    out["direction"].get(
                        {"c8": "h1_full_vs_b0", "c1": "h1_full_vs_b0",
                         "c3": "h3_only_eaps_vs_b0", "c5": "h5_dcca_margin",
                         "c2": "h2_only_casp_vs_b0"}[cfg],
                        {}).get("leak_rate", {}).get("consistent")}

    # ---- generalization (split means per arm, seeds pooled) ----
    for cfg, (dirname, sw, label) in ARMS.items():
        out["generalization"][cfg] = {}
        for split in ("train", "val", "test"):
            vals, dvals = [], []
            for s in SEEDS:
                rep = json.load(open(ROOT / GEN.format(
                    arm=dirname, seed=s, split=split) /
                    "family_report.json"))
                for inst in rep["instances"]:
                    tv = inst["meta"]["total_value"]
                    for r in inst["runs"]:
                        vals.append(r["leak_rate"])
                        dvals.append(r["destroyed_value"] / tv)
            out["generalization"][cfg][split] = {
                "leak_rate_mean": mean(vals),
                "destroyed_value_rel_mean": mean(dvals)}

    # ---- acceptance checklist (R1-R11) -----------------------------------
    out["acceptance"] = {
        "R1_default_bit_identity": {
            "e1_report": "output/_pre_ablation_ref/r2_recheck_report.md",
            "check": "see report E1 section"},
        "R2_isolation": {"e2_report":
                         "output/_pre_ablation_ref/r2_recheck_report.md"},
        "R3_explicit_params_every_arm": {
            "verified_here": True,
            "locked": list(lock_t)},
        "R4p_uniform_commands": {
            "differs_only_in": ["use-dcca/use-eaps/use-casp",
                                "phi-scale/credit-alpha/cf-beta"],
            "device": budget["device"],
            "tier": budget["locked_tier"]},
        "R5_test_untouched_in_tuning": {
            "e52_arms": sorted(sel.get("arms", {}).keys()),
            "splits_used": ["train", "val"]},
        "R6_single_module_pairs": {
            "pairs": ["h2 (c2-c1)", "h3 (c3-c1)", "h5 (c8-c5)"],
            "same_instance_same_cplex": True},
        "R7_defaults_frozen": {"audit":
                               "tests/test_ablation_switches.py E5"},
        "R8_selection_chain_auditable": {
            "chain": "logs/recal_selection.json history+stages"},
        "R9_budget_declared": {"budget":
                               "logs/ablation_v3r2_budget.json"},
        "R10_grid_frozen": {"preregistered": sel["preregistered"]},
        "R11_r1_ckpts_rejected": {"audit":
                                  "tests/test_ablation_switches.py E7"},
    }

    out["caveats"] = [
        "round-over-round absolute levels: r2 runs tier %s on %s, r1 ran "
        "tier D with --device=auto; comparisons are descriptive, paired "
        "conclusions rely on within-round pairs only (r2 §7)"
        % (budget["locked_tier"], budget["device"]),
        "direction votes use paired-unit means per training seed",
        "mechanism shares are window-tail means of the instrumentation "
        "columns, not exact gradient magnitudes",
    ]
    SUMMARY.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print("written:", SUMMARY)
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

    print("\n%-4s %14s %16s" %
          ("cfg", "r_shape_share", "credit_adv_share"))
    for cfg in ARMS:
        mm = out["mechanism"][cfg]
        print("%-4s %14.4f %16.4f" %
              (cfg, mm["r_shape_share"]["tail_mean"],
               mm["credit_adv_share"]["tail_mean"]))


if __name__ == "__main__":
    main()
