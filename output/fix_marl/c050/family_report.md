# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 13:49:24

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6562 | 0.4985 | 0.2012 | 75.9076 | 0.441 | 17.9 | 1355.2 | `027d67c922f9` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5621 | 0.3044 | 0.0093 | 93.3397 | 0.422 | 18.0 | 1672.4 | `e2a266f5b788` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6092 +- 0.0471 [worst 0.6562] | 0.6562 |
| gap_mean | 0.4015 +- 0.0970 [worst 0.4985] | 0.4985 |
| invalid_engagement_rate | 0.1052 +- 0.0960 [worst 0.2012] | 0.2012 |
| ammo_efficiency | 84.6236 +- 8.7161 [worst 75.9076] | 75.9076 |
| latency_p50 | 0.4315 +- 0.0094 [worst 0.4409] | 0.4409 |
| latency_p90 | 0.4649 +- 0.0081 [worst 0.4730] | 0.4730 |
| shots_total | 17.9500 +- 0.0500 [worst 18.0000] | 18.0000 |
| destroyed_value | 1513.7833 +- 158.6167 [worst 1355.1667] | 1355.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
