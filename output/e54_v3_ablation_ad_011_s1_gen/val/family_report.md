# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:10:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5959 | n/a | 0.1313 | 104.3936 | 0.004 | 16.0 | 1678.8 | `ab6c382f5c91` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5921 | n/a | 0.1074 | 103.1947 | 0.004 | 18.0 | 1875.4 | `2c9262090be9` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6224 | n/a | 0.1094 | 104.7593 | 0.004 | 17.1 | 1797.2 | `c144a59fdc16` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6092 | n/a | 0.1111 | 99.1334 | 0.004 | 18.0 | 1799.4 | `19e1c3ed6b78` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6049 +- 0.0119 [worst 0.6224] | 0.6224 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1148 +- 0.0096 [worst 0.1313] | 0.1313 |
| ammo_efficiency | 102.8702 +- 2.2337 [worst 99.1334] | 99.1334 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0047 +- 0.0012 [worst 0.0068] | 0.0068 |
| shots_total | 17.2667 +- 0.8246 [worst 18.0000] | 18.0000 |
| destroyed_value | 1787.7167 +- 70.3423 [worst 1678.7667] | 1678.7667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
