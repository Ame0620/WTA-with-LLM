# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **rh-cplex** | seeds: 30 (base 42) | solver timelimit 15s
- generated at: 2026-09-18 23:20:55

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4485 | 15.8324 | 0.1590 | 69.2558 | 15.458 | 70.0 | 4498.7 | `9ed200486f05` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4178 | 17.6544 | 0.1424 | 64.0364 | 15.404 | 70.0 | 4434.1 | `51c19d1d72bf` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4331 +- 0.0153 [worst 0.4485] | 0.4485 |
| gap_mean | 16.7434 +- 0.9110 [worst 17.6544] | 17.6544 |
| invalid_engagement_rate | 0.1507 +- 0.0083 [worst 0.1590] | 0.1590 |
| ammo_efficiency | 66.6461 +- 2.6097 [worst 64.0364] | 64.0364 |
| latency_p50 | 15.4312 +- 0.0272 [worst 15.4583] | 15.4583 |
| latency_p90 | 15.4908 +- 0.0284 [worst 15.5192] | 15.5192 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4466.3833 +- 32.3167 [worst 4434.0667] | 4434.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
