"""e52 stage 0: lock the recalibration budget tier T from smoke runs.

Rule (r2 spec §4.1, preregistered): smoke (1,0,0) and (0,1,0) for 30
iters @128 eps each; the SLOWER arm's sec/iter extrapolated to the
tier-T default 800 iters must land the single-arm wall inside
[0.4h, 1.2h]; above -> iters 640 (one step down), below -> iters 1000
(one step up). Writes logs/recal_budget.json; refuses to overwrite.
"""
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "logs", "recal_budget.json")
SMOKE = {"(1,0,0)": "output/e52_recal/_smoke_100",
         "(0,1,0)": "output/e52_recal/_smoke_010"}
WINDOW = (0.4, 1.2)
DEVICE = "cpu"


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
        rows[tag] = {"sec_per_iter": round(spi, 4),
                     "smoke_dir": d}
        worst = max(worst, spi)
    wall800 = worst * 800 / 3600.0
    if wall800 > WINDOW[1]:
        pick, reason = 640, "extrapolated %.2fh above ceiling %.1fh" \
            % (wall800, WINDOW[1])
    elif wall800 < WINDOW[0]:
        pick, reason = 1000, ("extrapolated %.2fh below floor %.1fh -> "
                              "one step up to 1000 (device faster than "
                              "the MPS baseline the window was calibrated "
                              "on; declared)" % (wall800, WINDOW[0]))
    else:
        pick, reason = 800, "default 800 inside window"
    doc = {
        "tier": "T",
        "config": {"iters": pick, "episodes_per_iter": 128,
                   "patience": 30, "eval_every": 25},
        "device": DEVICE,
        "device_rationale": ("CPU matches the e53 formal round device "
                             "and the e20 main table (~1.3 s/iter); "
                             "auto->MPS measured ~8 s/iter (6x slower)"),
        "window_h": list(WINDOW),
        "smoke_measurements": rows,
        "slower_sec_per_iter": round(worst, 4),
        "extrapolated_arm_wall_h": {
            "800": round(worst * 800 / 3600.0, 3),
            "640": round(worst * 640 / 3600.0, 3),
            "1000": round(worst * 1000 / 3600.0, 3)},
        "picked_iters": pick,
        "reason": reason,
        "locked_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    }
    with open(OUT, "w") as f:
        json.dump(doc, f, indent=2)
    print("[lock] tier T iters=%d (%s); slower arm %.3f s/iter" %
          (pick, reason, worst))
    return 0


if __name__ == "__main__":
    sys.exit(main())
