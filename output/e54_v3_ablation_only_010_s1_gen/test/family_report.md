# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:12:02

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6497 | n/a | 0.2118 | 89.4102 | 0.003 | 17.0 | 1380.9 | `436f6f67eb50` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5469 | n/a | 0.1185 | 96.6597 | 0.003 | 18.0 | 1730.5 | `661bca6445fa` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5983 +- 0.0514 [worst 0.6497] | 0.6497 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1651 +- 0.0466 [worst 0.2118] | 0.2118 |
| ammo_efficiency | 93.0350 +- 3.6247 [worst 89.4102] | 89.4102 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0031] | 0.0031 |
| latency_p90 | 0.0047 +- 0.0012 [worst 0.0059] | 0.0059 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1555.7167 +- 174.8167 [worst 1380.9000] | 1380.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
