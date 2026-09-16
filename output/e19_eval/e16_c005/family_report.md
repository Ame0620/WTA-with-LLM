# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-07 18:55:45

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.5920 | 0.4412 | 0.1684 | 84.0971 | 0.408 | 19.0 | 1608.3 | `6fe6f07d5a33` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5650 | 0.2503 | 0.0781 | 87.5767 | 0.387 | 18.1 | 1661.2 | `6bd9d913e6cc` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5785 +- 0.0135 [worst 0.5920] | 0.5920 |
| gap_mean | 0.3458 +- 0.0954 [worst 0.4412] | 0.4412 |
| invalid_engagement_rate | 0.1233 +- 0.0451 [worst 0.1684] | 0.1684 |
| ammo_efficiency | 85.8369 +- 1.7398 [worst 84.0971] | 84.0971 |
| latency_p50 | 0.3976 +- 0.0109 [worst 0.4084] | 0.4084 |
| latency_p90 | 0.4291 +- 0.0095 [worst 0.4386] | 0.4386 |
| shots_total | 18.5667 +- 0.4333 [worst 19.0000] | 19.0000 |
| destroyed_value | 1634.7500 +- 26.4500 [worst 1608.3000] | 1608.3000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
