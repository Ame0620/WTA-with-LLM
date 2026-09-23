# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:54:01

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5648 | n/a | 0.0667 | 100.6095 | 0.004 | 18.0 | 1807.9 | `3eac31b8e10a` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6239 | n/a | 0.1167 | 96.4275 | 0.004 | 18.0 | 1729.2 | `e95b4e20433e` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6413 | n/a | 0.1574 | 94.5395 | 0.004 | 18.0 | 1707.3 | `4d154c2615bc` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6781 | n/a | 0.2130 | 80.8922 | 0.004 | 18.0 | 1481.9 | `14ea5d3feb87` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6270 +- 0.0409 [worst 0.6781] | 0.6781 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1384 +- 0.0537 [worst 0.2130] | 0.2130 |
| ammo_efficiency | 93.1172 +- 7.3920 [worst 80.8922] | 80.8922 |
| latency_p50 | 0.0038 +- 0.0004 [worst 0.0044] | 0.0044 |
| latency_p90 | 0.0050 +- 0.0018 [worst 0.0082] | 0.0082 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1681.5917 +- 121.1967 [worst 1481.9333] | 1481.9333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
