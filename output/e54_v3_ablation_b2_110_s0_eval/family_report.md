# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:03:41

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6491 | 0.4791 | 0.2102 | 80.0243 | 0.003 | 17.3 | 1383.1 | `d86da7d40828` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5552 | 0.3379 | 0.1463 | 93.9597 | 0.003 | 18.0 | 1698.6 | `52f4de4febfa` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6022 +- 0.0469 [worst 0.6491] | 0.6491 |
| gap_mean | 0.4085 +- 0.0706 [worst 0.4791] | 0.4791 |
| invalid_engagement_rate | 0.1783 +- 0.0320 [worst 0.2102] | 0.2102 |
| ammo_efficiency | 86.9920 +- 6.9677 [worst 80.0243] | 80.0243 |
| latency_p50 | 0.0032 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0180 +- 0.0016 [worst 0.0196] | 0.0196 |
| shots_total | 17.6500 +- 0.3500 [worst 18.0000] | 18.0000 |
| destroyed_value | 1540.8500 +- 157.7167 [worst 1383.1333] | 1383.1333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
