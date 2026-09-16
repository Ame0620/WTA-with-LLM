# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-07 19:13:13

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6350 | 0.4842 | 0.2439 | 74.8386 | 0.407 | 19.0 | 1438.7 | `059ff1798672` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6048 | 0.2947 | 0.1029 | 83.3391 | 0.385 | 18.1 | 1509.4 | `94d781e41b49` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6199 +- 0.0151 [worst 0.6350] | 0.6350 |
| gap_mean | 0.3895 +- 0.0947 [worst 0.4842] | 0.4842 |
| invalid_engagement_rate | 0.1734 +- 0.0705 [worst 0.2439] | 0.2439 |
| ammo_efficiency | 79.0888 +- 4.2502 [worst 74.8386] | 74.8386 |
| latency_p50 | 0.3960 +- 0.0105 [worst 0.4065] | 0.4065 |
| latency_p90 | 0.4266 +- 0.0092 [worst 0.4359] | 0.4359 |
| shots_total | 18.5333 +- 0.4667 [worst 19.0000] | 19.0000 |
| destroyed_value | 1474.0667 +- 35.3667 [worst 1438.7000] | 1438.7000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
