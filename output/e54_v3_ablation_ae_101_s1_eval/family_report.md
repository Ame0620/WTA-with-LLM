# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:04:00

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6371 | 0.4761 | 0.2037 | 79.1550 | 0.004 | 18.0 | 1430.5 | `4a34a701b658` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5524 | 0.3144 | 0.1259 | 92.9200 | 0.004 | 18.0 | 1709.5 | `b996d74202f0` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5947 +- 0.0424 [worst 0.6371] | 0.6371 |
| gap_mean | 0.3952 +- 0.0809 [worst 0.4761] | 0.4761 |
| invalid_engagement_rate | 0.1648 +- 0.0389 [worst 0.2037] | 0.2037 |
| ammo_efficiency | 86.0375 +- 6.8825 [worst 79.1550] | 79.1550 |
| latency_p50 | 0.0038 +- 0.0001 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0054 +- 0.0014 [worst 0.0068] | 0.0068 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1570.0167 +- 139.5167 [worst 1430.5000] | 1430.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
