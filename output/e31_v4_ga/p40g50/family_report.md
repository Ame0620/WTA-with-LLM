# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **ga** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 17:42:32

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.7195 | 0.0104 | 0.1433 | 89.4265 | 0.589 | 30.0 | 2288.3 | `8a943acc71bb` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.6886 | 0.0144 | 0.0311 | 80.6911 | 0.524 | 30.0 | 2371.3 | `a238b20198d5` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7041 +- 0.0154 [worst 0.7195] | 0.7195 |
| gap_mean | 0.0124 +- 0.0020 [worst 0.0144] | 0.0144 |
| invalid_engagement_rate | 0.0872 +- 0.0561 [worst 0.1433] | 0.1433 |
| ammo_efficiency | 85.0588 +- 4.3677 [worst 80.6911] | 80.6911 |
| latency_p50 | 0.5564 +- 0.0323 [worst 0.5887] | 0.5887 |
| latency_p90 | 0.6886 +- 0.0027 [worst 0.6913] | 0.6913 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 2329.7667 +- 41.5000 [worst 2288.2667] | 2288.2667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
