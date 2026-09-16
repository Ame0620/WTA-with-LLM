# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-07 18:59:16

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6170 | 0.4469 | 0.1973 | 79.5705 | 0.407 | 18.9 | 1509.9 | `a66d4cb7bd08` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.4921 | 0.2843 | 0.0850 | 95.0021 | 0.391 | 20.0 | 1939.5 | `b1632c2018ba` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5546 +- 0.0624 [worst 0.6170] | 0.6170 |
| gap_mean | 0.3656 +- 0.0813 [worst 0.4469] | 0.4469 |
| invalid_engagement_rate | 0.1411 +- 0.0561 [worst 0.1973] | 0.1973 |
| ammo_efficiency | 87.2863 +- 7.7158 [worst 79.5705] | 79.5705 |
| latency_p50 | 0.3991 +- 0.0080 [worst 0.4071] | 0.4071 |
| latency_p90 | 0.4248 +- 0.0127 [worst 0.4374] | 0.4374 |
| shots_total | 19.4667 +- 0.5333 [worst 20.0000] | 20.0000 |
| destroyed_value | 1724.7167 +- 214.8167 [worst 1509.9000] | 1509.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
