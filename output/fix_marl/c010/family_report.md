# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 13:41:44

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6535 | 0.4712 | 0.2074 | 75.8189 | 0.422 | 18.0 | 1365.9 | `2862d5b866e6` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5763 | 0.2846 | 0.0944 | 89.6586 | 0.420 | 18.0 | 1618.1 | `49be89df4cbc` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6149 +- 0.0386 [worst 0.6535] | 0.6535 |
| gap_mean | 0.3779 +- 0.0933 [worst 0.4712] | 0.4712 |
| invalid_engagement_rate | 0.1509 +- 0.0565 [worst 0.2074] | 0.2074 |
| ammo_efficiency | 82.7387 +- 6.9198 [worst 75.8189] | 75.8189 |
| latency_p50 | 0.4211 +- 0.0011 [worst 0.4222] | 0.4222 |
| latency_p90 | 0.4633 +- 0.0109 [worst 0.4741] | 0.4741 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1492.0167 +- 126.1167 [worst 1365.9000] | 1365.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
