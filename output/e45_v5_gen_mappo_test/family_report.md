# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **mappo** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:15:51

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.5374 | n/a | 0.3913 | 53.9073 | 0.015 | 69.0 | 3773.5 | `9cbb3ed42aa9` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4025 | n/a | 0.2800 | 64.8938 | 0.015 | 70.0 | 4550.7 | `d4a7c95f8a08` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4699 +- 0.0675 [worst 0.5374] | 0.5374 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3357 +- 0.0557 [worst 0.3913] | 0.3913 |
| ammo_efficiency | 59.4005 +- 5.4932 [worst 53.9073] | 53.9073 |
| latency_p50 | 0.0154 +- 0.0000 [worst 0.0155] | 0.0155 |
| latency_p90 | 0.0231 +- 0.0063 [worst 0.0294] | 0.0294 |
| shots_total | 69.5000 +- 0.5000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4162.1000 +- 388.6000 [worst 3773.5000] | 3773.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
