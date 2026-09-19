# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **random** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 17:49:51

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.8405 | n/a | 0.0422 | 41.8799 | 0.000 | 30.0 | 1300.7 | `2b54be3eca31` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.8438 | n/a | 0.0267 | 38.7440 | 0.000 | 30.0 | 1189.5 | `98686a94e89c` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8422 +- 0.0016 [worst 0.8438] | 0.8438 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.0344 +- 0.0078 [worst 0.0422] | 0.0422 |
| ammo_efficiency | 40.3120 +- 1.5680 [worst 38.7440] | 38.7440 |
| latency_p50 | 0.0002 +- 0.0000 [worst 0.0002] | 0.0002 |
| latency_p90 | 0.0003 +- 0.0000 [worst 0.0003] | 0.0003 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 1245.0667 +- 55.6000 [worst 1189.4667] | 1189.4667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
