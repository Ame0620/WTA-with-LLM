# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:45:36

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4159 | 2.0341 | 0.3460 | 68.9228 | 0.694 | 69.2 | 4764.6 | `4a8a6d346c60` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4355 | 1.4797 | 0.4319 | 61.7837 | 0.698 | 70.0 | 4299.2 | `2f653aa195bf` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4257 +- 0.0098 [worst 0.4355] | 0.4355 |
| gap_mean | 1.7569 +- 0.2772 [worst 2.0341] | 2.0341 |
| invalid_engagement_rate | 0.3889 +- 0.0430 [worst 0.4319] | 0.4319 |
| ammo_efficiency | 65.3532 +- 3.5695 [worst 61.7837] | 61.7837 |
| latency_p50 | 0.6962 +- 0.0020 [worst 0.6982] | 0.6982 |
| latency_p90 | 0.8156 +- 0.0237 [worst 0.8393] | 0.8393 |
| shots_total | 69.5833 +- 0.4167 [worst 70.0000] | 70.0000 |
| destroyed_value | 4531.9167 +- 232.6833 [worst 4299.2333] | 4299.2333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
