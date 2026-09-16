# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **greedy_nearest** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 16:44:08

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.8891 | 0.5703 | 0.3352 | 24.2588 | 0.435 | 18.0 | 437.1 | `0c6e8de3d220` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.8954 | 0.5702 | 0.3074 | 21.9628 | 0.410 | 18.0 | 399.6 | `aa919140199b` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8922 +- 0.0031 [worst 0.8954] | 0.8954 |
| gap_mean | 0.5703 +- 0.0001 [worst 0.5703] | 0.5703 |
| invalid_engagement_rate | 0.3213 +- 0.0139 [worst 0.3352] | 0.3352 |
| ammo_efficiency | 23.1108 +- 1.1480 [worst 21.9628] | 21.9628 |
| latency_p50 | 0.4226 +- 0.0124 [worst 0.4349] | 0.4349 |
| latency_p90 | 0.4978 +- 0.0205 [worst 0.5183] | 0.5183 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 418.3833 +- 18.7500 [worst 399.6333] | 399.6333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
