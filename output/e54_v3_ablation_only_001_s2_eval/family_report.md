# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:04:33

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6766 | 0.4833 | 0.2426 | 71.6160 | 0.004 | 18.0 | 1274.8 | `59ada046de91` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5604 | 0.3157 | 0.0870 | 92.2923 | 0.003 | 18.0 | 1678.9 | `dae0090f60f3` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6185 +- 0.0581 [worst 0.6766] | 0.6766 |
| gap_mean | 0.3995 +- 0.0838 [worst 0.4833] | 0.4833 |
| invalid_engagement_rate | 0.1648 +- 0.0778 [worst 0.2426] | 0.2426 |
| ammo_efficiency | 81.9542 +- 10.3381 [worst 71.6160] | 71.6160 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0059 +- 0.0022 [worst 0.0081] | 0.0081 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1476.8500 +- 202.0167 [worst 1274.8333] | 1274.8333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
