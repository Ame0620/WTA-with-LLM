# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-07 20:15:18

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6519 | 0.2878 | 0.1796 | 83.1983 | 0.390 | 18.0 | 1372.2 | `9f0e34d5aff8` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6084 | 0.2130 | 0.1611 | 77.9822 | 0.385 | 19.0 | 1495.5 | `63064dda4a7b` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6302 +- 0.0217 [worst 0.6519] | 0.6519 |
| gap_mean | 0.2504 +- 0.0374 [worst 0.2878] | 0.2878 |
| invalid_engagement_rate | 0.1703 +- 0.0093 [worst 0.1796] | 0.1796 |
| ammo_efficiency | 80.5902 +- 2.6080 [worst 77.9822] | 77.9822 |
| latency_p50 | 0.3874 +- 0.0023 [worst 0.3897] | 0.3897 |
| latency_p90 | 0.4163 +- 0.0092 [worst 0.4255] | 0.4255 |
| shots_total | 18.5167 +- 0.5167 [worst 19.0333] | 19.0333 |
| destroyed_value | 1433.8333 +- 61.6333 [worst 1372.2000] | 1372.2000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
