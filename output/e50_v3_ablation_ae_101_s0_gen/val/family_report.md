# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:49:48

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5624 | n/a | 0.1167 | 100.3400 | 0.004 | 18.0 | 1817.9 | `9c2481a37d7b` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6259 | n/a | 0.1574 | 95.0731 | 0.004 | 18.0 | 1720.3 | `2667b5948b7b` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6729 | n/a | 0.1537 | 85.6776 | 0.004 | 18.0 | 1557.0 | `06d6beea4ab1` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.7097 | n/a | 0.3241 | 73.3878 | 0.004 | 18.0 | 1336.4 | `9d9b15d07dbd` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6427 +- 0.0551 [worst 0.7097] | 0.7097 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1880 +- 0.0802 [worst 0.3241] | 0.3241 |
| ammo_efficiency | 88.6196 +- 10.2430 [worst 73.3878] | 73.3878 |
| latency_p50 | 0.0038 +- 0.0002 [worst 0.0042] | 0.0042 |
| latency_p90 | 0.0050 +- 0.0017 [worst 0.0080] | 0.0080 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1607.9000 +- 182.3491 [worst 1336.4333] | 1336.4333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
