# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ga** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 19:48:09

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4781 | 0.1543 | 0.1395 | 69.1153 | 0.616 | 70.0 | 4256.9 | `790d0392f2c3` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4366 | 0.1602 | 0.1290 | 66.0328 | 0.625 | 70.0 | 4291.2 | `e65141051bf8` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4573 +- 0.0208 [worst 0.4781] | 0.4781 |
| gap_mean | 0.1573 +- 0.0029 [worst 0.1602] | 0.1602 |
| invalid_engagement_rate | 0.1343 +- 0.0052 [worst 0.1395] | 0.1395 |
| ammo_efficiency | 67.5741 +- 1.5412 [worst 66.0328] | 66.0328 |
| latency_p50 | 0.6205 +- 0.0041 [worst 0.6246] | 0.6246 |
| latency_p90 | 0.6999 +- 0.0032 [worst 0.7030] | 0.7030 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4274.0500 +- 17.1833 [worst 4256.8667] | 4256.8667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
