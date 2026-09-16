# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **greedy_nearest** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 16:32:19

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 1.0000 | 0.8118 | 0.0000 | n/a | 0.579 | 0.0 | 0.0 | `978e41ee12da` |
| `dn_3x50_K10_s02.txt` | 3819 | 1.0000 | 0.7871 | 0.0000 | n/a | 0.571 | 0.0 | 0.0 | `29faf747e90e` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 1.0000 +- 0.0000 [worst 1.0000] | 1.0000 |
| gap_mean | 0.7994 +- 0.0124 [worst 0.8118] | 0.8118 |
| invalid_engagement_rate | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| ammo_efficiency | n/a | n/a |
| latency_p50 | 0.5751 +- 0.0041 [worst 0.5792] | 0.5792 |
| latency_p90 | 0.6110 +- 0.0191 [worst 0.6301] | 0.6301 |
| shots_total | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| destroyed_value | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
