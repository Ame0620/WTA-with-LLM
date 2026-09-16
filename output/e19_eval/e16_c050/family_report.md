# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-07 19:06:14

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6562 | 0.4985 | 0.2012 | 75.9076 | 0.403 | 17.9 | 1355.2 | `027d67c922f9` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5373 | 0.3029 | 0.0364 | 91.5820 | 0.386 | 19.3 | 1767.2 | `72ae0cedd142` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5967 +- 0.0595 [worst 0.6562] | 0.6562 |
| gap_mean | 0.4007 +- 0.0978 [worst 0.4985] | 0.4985 |
| invalid_engagement_rate | 0.1188 +- 0.0824 [worst 0.2012] | 0.2012 |
| ammo_efficiency | 83.7448 +- 7.8372 [worst 75.9076] | 75.9076 |
| latency_p50 | 0.3941 +- 0.0085 [worst 0.4026] | 0.4026 |
| latency_p90 | 0.4269 +- 0.0096 [worst 0.4365] | 0.4365 |
| shots_total | 18.5833 +- 0.6833 [worst 19.2667] | 19.2667 |
| destroyed_value | 1561.1833 +- 206.0167 [worst 1355.1667] | 1355.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
