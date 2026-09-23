# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:59:56

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.8117 | 0.1781 | 0.2204 | 43.7397 | 0.003 | 18.0 | 742.2 | `7eca0aaa5d39` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.7284 | 0.1437 | 0.0944 | 56.5876 | 0.003 | 18.0 | 1037.2 | `4027c0c7cb37` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7701 +- 0.0417 [worst 0.8117] | 0.8117 |
| gap_mean | 0.1609 +- 0.0172 [worst 0.1781] | 0.1781 |
| invalid_engagement_rate | 0.1574 +- 0.0630 [worst 0.2204] | 0.2204 |
| ammo_efficiency | 50.1636 +- 6.4239 [worst 43.7397] | 43.7397 |
| latency_p50 | 0.0032 +- 0.0002 [worst 0.0035] | 0.0035 |
| latency_p90 | 0.0324 +- 0.0291 [worst 0.0615] | 0.0615 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 889.7167 +- 147.5167 [worst 742.2000] | 742.2000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
