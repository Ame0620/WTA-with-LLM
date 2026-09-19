# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ecmappo** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 06:55:01

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4138 | n/a | 0.2986 | 67.4727 | 0.012 | 70.0 | 4781.9 | `cf4a12c52cff` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.3782 | n/a | 0.3586 | 67.6062 | 0.012 | 70.0 | 4735.8 | `1ba7b1db389a` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.3960 +- 0.0178 [worst 0.4138] | 0.4138 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3286 +- 0.0300 [worst 0.3586] | 0.3586 |
| ammo_efficiency | 67.5395 +- 0.0667 [worst 67.4727] | 67.4727 |
| latency_p50 | 0.0121 +- 0.0003 [worst 0.0124] | 0.0124 |
| latency_p90 | 0.0168 +- 0.0044 [worst 0.0212] | 0.0212 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4758.8500 +- 23.0500 [worst 4735.8000] | 4735.8000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
