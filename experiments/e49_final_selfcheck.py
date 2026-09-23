"""e49 final self-check: all 24 arms (8 cfg x 3 seeds).

Exits 0 (PASS) / 1 (FAIL). Checks per arm:
  * train_summary.json / train_log.jsonl / best.pt exist
  * ablation metadata == expected switch triple
  * all numeric log fields finite (no NaN/inf)
  * checkpoint loads and its ablation field matches
  * stop_reason in {iters_done, early_stop}
Plus direction sanity: mean best_val of c8 arms < c1 arms across seeds.
"""
import json
import math
import sys

import torch

ROOT = "/Users/fgod/Desktop/FGOD/Projects/UAS/WTA-Dn-branch01"
EXP = {
    "b0_000": (0, 0, 0), "b3_111": (1, 1, 1), "ad_011": (0, 1, 1),
    "ae_101": (1, 0, 1), "b2_110": (1, 1, 0), "b1_100": (1, 0, 0),
    "only_010": (0, 1, 0), "only_001": (0, 0, 1),
}
SEEDS = [0, 1, 2]
fails = []


def finite(o):
    if isinstance(o, float):
        return math.isfinite(o)
    if isinstance(o, dict):
        return all(finite(v) for v in o.values())
    if isinstance(o, list):
        return all(finite(v) for v in o)
    return True


best = {"b0_000": [], "b3_111": []}
n = 0
for arm, sw in EXP.items():
    for s in SEEDS:
        d = f"{ROOT}/output/e49_v3_ablation/{arm}_s{s}"
        n += 1
        try:
            ts = json.load(open(d + "/train_summary.json"))
            rows = [json.loads(l) for l in open(d + "/train_log.jsonl")]
            got = (ts["ablation"]["use_dcca"], ts["ablation"]["use_eaps"],
                   ts["ablation"]["use_casp"])
            assert got == sw, f"meta {got} != {sw}"
            assert all(finite(r) for r in rows), "NaN in train_log"
            assert ts["final_metrics"]["stop_reason"] in (
                "iters_done", "early_stop"), "bad stop_reason"
            ck = torch.load(d + "/best.pt", map_location="cpu",
                            weights_only=False)
            cg = (ck["ablation"]["use_dcca"], ck["ablation"]["use_eaps"],
                  ck["ablation"]["use_casp"])
            assert cg == sw, f"ckpt meta {cg} != {sw}"
            assert ck["train_seed"] == s, "ckpt seed mismatch"
            if arm in best:
                best[arm].append(ts["best_val"])
        except Exception as e:  # noqa: BLE001
            fails.append(f"{arm}_s{s}: {e}")

print(f"checked {n} arms, failures: {len(fails)}")
for f in fails:
    print("  FAIL", f)
if "b0_000" in best and len(best["b0_000"]) == 3 and len(best["b3_111"]) == 3:
    m0 = sum(best["b0_000"]) / 3.0
    m3 = sum(best["b3_111"]) / 3.0
    direction = m3 < m0
    print(f"direction sanity: c8 mean best_val {m3:.4f} "
          f"< c1 {m0:.4f}: {direction}")
    if not direction:
        fails.append("direction sanity (c8 >= c1)")
print("E49 FINAL SELF-CHECK:", "PASS" if not fails else "FAIL")
sys.exit(0 if not fails else 1)
