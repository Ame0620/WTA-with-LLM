# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 3 (base 7) | solver timelimit 30s
- generated at: 2026-09-22 18:47:41

## Per-instance metrics (mean +- std over 3 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5894 | n/a | 0.2037 | 93.8032 | 0.004 | 18.0 | 1705.7 | `df65fa8ea59c` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6240 | n/a | 0.0763 | 106.7848 | 0.003 | 17.3 | 1729.0 | `9f35f2ad94cb` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6684 | n/a | 0.2037 | 95.1067 | 0.008 | 18.0 | 1578.3 | `790f81ac174f` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6329 | n/a | 0.1296 | 91.1452 | 0.003 | 18.0 | 1690.3 | `da552f608807` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6287 +- 0.0281 [worst 0.6684] | 0.6684 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1533 +- 0.0538 [worst 0.2037] | 0.2037 |
| ammo_efficiency | 96.7100 +- 5.9893 [worst 91.1452] | 91.1452 |
| latency_p50 | 0.0044 +- 0.0020 [worst 0.0079] | 0.0079 |
| latency_p90 | 0.0119 +- 0.0100 [worst 0.0289] | 0.0289 |
| shots_total | 17.8333 +- 0.2887 [worst 18.0000] | 18.0000 |
| destroyed_value | 1675.8333 +- 57.9509 [worst 1578.3333] | 1578.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
