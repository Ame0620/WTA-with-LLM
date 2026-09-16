# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-07 19:09:43

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6364 | 0.4621 | 0.2333 | 75.8027 | 0.398 | 19.0 | 1433.5 | `886be25fcf78` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5005 | 0.2870 | 0.0709 | 94.4722 | 0.387 | 19.7 | 1907.6 | `16259bd5fe17` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5684 +- 0.0679 [worst 0.6364] | 0.6364 |
| gap_mean | 0.3746 +- 0.0876 [worst 0.4621] | 0.4621 |
| invalid_engagement_rate | 0.1521 +- 0.0812 [worst 0.2333] | 0.2333 |
| ammo_efficiency | 85.1375 +- 9.3348 [worst 75.8027] | 75.8027 |
| latency_p50 | 0.3924 +- 0.0052 [worst 0.3976] | 0.3976 |
| latency_p90 | 0.4243 +- 0.0089 [worst 0.4333] | 0.4333 |
| shots_total | 19.3333 +- 0.3333 [worst 19.6667] | 19.6667 |
| destroyed_value | 1670.5500 +- 237.0500 [worst 1433.5000] | 1433.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
