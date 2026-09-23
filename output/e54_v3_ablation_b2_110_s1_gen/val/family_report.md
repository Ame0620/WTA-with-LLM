# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:11:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5554 | n/a | 0.1574 | 100.7513 | 0.003 | 18.0 | 1847.0 | `40b8b75e88cc` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5894 | n/a | 0.1241 | 104.4464 | 0.003 | 18.0 | 1887.9 | `08dd96e4297e` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6263 | n/a | 0.1196 | 109.4524 | 0.003 | 17.0 | 1778.6 | `3a93a0027de7` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6415 | n/a | 0.1593 | 96.1464 | 0.003 | 18.0 | 1650.5 | `47b8c24fdb17` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6032 +- 0.0335 [worst 0.6415] | 0.6415 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1401 +- 0.0183 [worst 0.1593] | 0.1593 |
| ammo_efficiency | 102.6991 +- 4.8834 [worst 96.1464] | 96.1464 |
| latency_p50 | 0.0031 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0040 +- 0.0012 [worst 0.0060] | 0.0060 |
| shots_total | 17.7500 +- 0.4330 [worst 18.0000] | 18.0000 |
| destroyed_value | 1791.0250 +- 90.0403 [worst 1650.5000] | 1650.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
