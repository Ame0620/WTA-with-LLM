"""e53 stage 0: lock the formal-round budget tier from smoke runs (r2 §5).

Rule (preregistered extrapolation): smoke (1,1,1) and (0,0,0) for 50
iters @128 eps on the SAME device as the formal arms (CPU - the e20
main table ran CPU at ~1.3 s/iter while MPS is ~6x slower on this
small model; device choice is declared in the budget json + report).

Decision quantity: worst-arm sec/iter x 24 arms x the e20 main-table
EC-MAPPO early-stop point (1750 iters) -> expected wall. Tier A kept
iff expected <= 60h; else A-1 (2000x128, patience 50), then A-2
(1500x128, patience 40). The full-budget upper bound (3000 iters, no
early stop) is recorded alongside for the audit trail. Early stopping
is the declared dependency (r2 §8), same as e20.
"""
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "logs", "ablation_v3r2_budget.json")
SMOKE = {"(1,1,1)": "output/e53_v3_ablation_r2/_smoke_111",
         "(0,0,0)": "output/e53_v3_ablation_r2/_smoke_000"}
TIERS = [  # (name, iters, epi, patience)
    ("A", 3000, 128, 60), ("A-1", 2000, 128, 50), ("A-2", 1500, 128, 40),
]
EXPECT_ITERS = 1750          # e20 main-table EC-MAPPO early-stop point
CEIL_H = 60.0
WINDOW_H = (20.0, 60.0)


def main():
    if os.path.exists(OUT):
        print("[lock] %s already present - refusing to overwrite" % OUT)
        return 0
    rows = {}
    worst = 0.0
    for tag, d in SMOKE.items():
        log = [json.loads(l) for l in open(os.path.join(ROOT, d,
                                                        "train_log.jsonl"))]
        spi = log[-1]["wall_sec"] / log[-1]["iter"]
        rows[tag] = {"sec_per_iter": round(spi, 4), "smoke_dir": d}
        worst = max(worst, spi)
    ladder = []
    pick = None
    for (name, it, epi, pat) in TIERS:
        exp_h = worst * EXPECT_ITERS * 24 / 3600.0
        ub_h = worst * it * 24 / 3600.0
        ladder.append({"tier": name, "iters": it, "episodes_per_iter": epi,
                       "patience": pat,
                       "expected_wall_h": round(exp_h, 2),
                       "upper_bound_wall_h": round(ub_h, 2)})
        if pick is None and exp_h <= CEIL_H:
            pick = (name, it, epi, pat, exp_h, ub_h)
    if pick is None:
        pick = (TIERS[-1][0], TIERS[-1][1], TIERS[-1][2], TIERS[-1][3],
                worst * EXPECT_ITERS * 24 / 3600.0,
                worst * TIERS[-1][1] * 24 / 3600.0)
        reason = ("even A-2 expected > %.0fh ceiling - taking A-2 and "
                  "escalating (r2 §5 ladder exhausted)" % CEIL_H)
    else:
        reason = ("expected wall %.1fh <= %.0fh ceiling (window %s, early-"
                  "stop dependency declared, e20 convergence point %d iters)"
                  % (pick[4], CEIL_H, WINDOW_H, EXPECT_ITERS))
    doc = {
        "locked_tier": pick[0],
        "config": {"iters": pick[1], "episodes_per_iter": pick[2],
                   "patience": pick[3], "eval_every": 25},
        "device": "cpu",
        "device_rationale": ("e20 main table ran CPU (~1.3 s/iter); auto->"
                             "MPS measured ~8 s/iter on this model (6x "
                             "slower) - 24-arm tier A infeasible on MPS; "
                             "all 24 arms + smokes run CPU (R4' uniform)"),
        "window_h": list(WINDOW_H),
        "smoke_measurements": rows,
        "worst_sec_per_iter": round(worst, 4),
        "expected_convergence_iters": EXPECT_ITERS,
        "ladder": ladder,
        "reason": reason,
        "locked_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    }
    with open(OUT, "w") as f:
        json.dump(doc, f, indent=2)
    print("[lock] tier %s (%dx%d, patience %d) - %s"
          % (pick[0], pick[1], pick[2], pick[3], reason))
    return 0


if __name__ == "__main__":
    sys.exit(main())
