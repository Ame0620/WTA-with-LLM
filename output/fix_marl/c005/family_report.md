# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 13:37:59

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6312 | 0.4617 | 0.1778 | 80.3247 | 0.412 | 18.0 | 1453.6 | `9da4a980ea1a` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5674 | 0.2503 | 0.0759 | 87.6980 | 0.394 | 18.0 | 1651.9 | `dcf32c3f7d3e` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5993 +- 0.0319 [worst 0.6312] | 0.6312 |
| gap_mean | 0.3560 +- 0.1057 [worst 0.4617] | 0.4617 |
| invalid_engagement_rate | 0.1269 +- 0.0509 [worst 0.1778] | 0.1778 |
| ammo_efficiency | 84.0113 +- 3.6866 [worst 80.3247] | 80.3247 |
| latency_p50 | 0.4032 +- 0.0088 [worst 0.4119] | 0.4119 |
| latency_p90 | 0.4349 +- 0.0064 [worst 0.4413] | 0.4413 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1552.7833 +- 99.1500 [worst 1453.6333] | 1453.6333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
