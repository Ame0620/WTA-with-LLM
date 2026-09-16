# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 13:56:46

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6729 | 0.4887 | 0.2463 | 71.5695 | 0.414 | 18.0 | 1289.5 | `797cb1cf2910` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5668 | 0.2873 | 0.0759 | 90.1536 | 0.401 | 18.0 | 1654.2 | `73aeada74e61` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6199 +- 0.0530 [worst 0.6729] | 0.6729 |
| gap_mean | 0.3880 +- 0.1007 [worst 0.4887] | 0.4887 |
| invalid_engagement_rate | 0.1611 +- 0.0852 [worst 0.2463] | 0.2463 |
| ammo_efficiency | 80.8616 +- 9.2921 [worst 71.5695] | 71.5695 |
| latency_p50 | 0.4075 +- 0.0067 [worst 0.4142] | 0.4142 |
| latency_p90 | 0.4452 +- 0.0059 [worst 0.4511] | 0.4511 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1471.8500 +- 182.3500 [worst 1289.5000] | 1289.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
