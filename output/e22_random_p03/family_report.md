# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **random** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 16:20:57

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.8595 | n/a | 0.1333 | 37.6755 | 0.000 | 18.0 | 553.7 | `c9cb59691eb3` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.8336 | n/a | 0.0130 | 34.5240 | 0.000 | 18.0 | 635.5 | `9962efef5b8c` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8466 +- 0.0130 [worst 0.8595] | 0.8595 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.0731 +- 0.0602 [worst 0.1333] | 0.1333 |
| ammo_efficiency | 36.0998 +- 1.5758 [worst 34.5240] | 34.5240 |
| latency_p50 | 0.0001 +- 0.0000 [worst 0.0001] | 0.0001 |
| latency_p90 | 0.0001 +- 0.0000 [worst 0.0002] | 0.0002 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 594.6333 +- 40.9000 [worst 553.7333] | 553.7333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
