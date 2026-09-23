# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:55:42

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.6819 | n/a | 0.1093 | 71.8047 | 0.003 | 18.0 | 1321.4 | `5e6518c4343d` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6286 | n/a | 0.0481 | 94.5708 | 0.003 | 18.0 | 1707.6 | `7c0261d6a120` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.7567 | n/a | 0.2000 | 68.4665 | 0.003 | 18.0 | 1158.1 | `135d1cff3f3c` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.7357 | n/a | 0.1167 | 66.7625 | 0.003 | 18.0 | 1216.9 | `599657ce4d8b` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7007 +- 0.0498 [worst 0.7567] | 0.7567 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1185 +- 0.0540 [worst 0.2000] | 0.2000 |
| ammo_efficiency | 75.4011 +- 11.2152 [worst 66.7625] | 66.7625 |
| latency_p50 | 0.0032 +- 0.0001 [worst 0.0034] | 0.0034 |
| latency_p90 | 0.0042 +- 0.0012 [worst 0.0062] | 0.0062 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1351.0083 +- 214.0211 [worst 1158.1333] | 1158.1333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
