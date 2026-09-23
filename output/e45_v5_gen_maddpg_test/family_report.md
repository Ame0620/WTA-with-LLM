# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **maddpg** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:31:51

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.5822 | n/a | 0.2571 | 48.8958 | 0.015 | 70.0 | 3408.2 | `e912c403afc8` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.5282 | n/a | 0.3014 | 49.7240 | 0.014 | 70.0 | 3593.3 | `8cbeec3da340` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5552 +- 0.0270 [worst 0.5822] | 0.5822 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2793 +- 0.0221 [worst 0.3014] | 0.3014 |
| ammo_efficiency | 49.3099 +- 0.4141 [worst 48.8958] | 48.8958 |
| latency_p50 | 0.0147 +- 0.0005 [worst 0.0152] | 0.0152 |
| latency_p90 | 0.0216 +- 0.0060 [worst 0.0276] | 0.0276 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 3500.7500 +- 92.5500 [worst 3408.2000] | 3408.2000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
