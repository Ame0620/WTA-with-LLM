# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 3 (base 7) | solver timelimit 30s
- generated at: 2026-09-22 18:47:36

## Per-instance metrics (mean +- std over 3 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5802 | n/a | 0.1296 | 100.3669 | 0.004 | 18.0 | 1743.7 | `dc6f9bc83c19` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5796 | n/a | 0.0556 | 106.5689 | 0.004 | 18.0 | 1933.0 | `eceeb9b76923` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6684 | n/a | 0.2037 | 96.2856 | 0.004 | 18.0 | 1578.3 | `af8df889aabc` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6570 | n/a | 0.2037 | 86.8961 | 0.004 | 18.0 | 1579.3 | `66d54a2f6d73` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6213 +- 0.0416 [worst 0.6684] | 0.6684 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1481 +- 0.0614 [worst 0.2037] | 0.2037 |
| ammo_efficiency | 97.5294 +- 7.1480 [worst 86.8961] | 86.8961 |
| latency_p50 | 0.0038 +- 0.0002 [worst 0.0041] | 0.0041 |
| latency_p90 | 0.0128 +- 0.0148 [worst 0.0384] | 0.0384 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1708.5833 +- 146.0003 [worst 1578.3333] | 1578.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
