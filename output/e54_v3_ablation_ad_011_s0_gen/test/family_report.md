# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:06:06

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6402 | n/a | 0.1066 | 81.3322 | 0.004 | 17.1 | 1418.4 | `a7edb7e6343b` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5721 | n/a | 0.1426 | 90.0043 | 0.004 | 18.0 | 1634.0 | `33f66d7de7d2` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6062 +- 0.0340 [worst 0.6402] | 0.6402 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1246 +- 0.0180 [worst 0.1426] | 0.1426 |
| ammo_efficiency | 85.6682 +- 4.3360 [worst 81.3322] | 81.3322 |
| latency_p50 | 0.0037 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0054 +- 0.0014 [worst 0.0068] | 0.0068 |
| shots_total | 17.5667 +- 0.4333 [worst 18.0000] | 18.0000 |
| destroyed_value | 1526.2000 +- 107.8000 [worst 1418.4000] | 1418.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
