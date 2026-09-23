# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:04:28

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6560 | 0.4821 | 0.2537 | 75.4504 | 0.003 | 18.0 | 1356.1 | `42524823dddd` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5495 | 0.2988 | 0.1148 | 95.0602 | 0.003 | 18.0 | 1720.5 | `13bc3d8b6ad8` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6027 +- 0.0532 [worst 0.6560] | 0.6560 |
| gap_mean | 0.3904 +- 0.0917 [worst 0.4821] | 0.4821 |
| invalid_engagement_rate | 0.1843 +- 0.0694 [worst 0.2537] | 0.2537 |
| ammo_efficiency | 85.2553 +- 9.8049 [worst 75.4504] | 75.4504 |
| latency_p50 | 0.0032 +- 0.0000 [worst 0.0033] | 0.0033 |
| latency_p90 | 0.0049 +- 0.0014 [worst 0.0063] | 0.0063 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1538.3333 +- 182.2000 [worst 1356.1333] | 1356.1333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
