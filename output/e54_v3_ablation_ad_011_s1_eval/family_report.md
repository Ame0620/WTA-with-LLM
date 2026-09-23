# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:03:57

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6230 | 0.5088 | 0.1510 | 84.8360 | 0.004 | 17.0 | 1486.0 | `98a745852b7f` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5378 | 0.3539 | 0.0722 | 98.3646 | 0.004 | 18.0 | 1765.0 | `ce830e443d7d` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5804 +- 0.0426 [worst 0.6230] | 0.6230 |
| gap_mean | 0.4314 +- 0.0774 [worst 0.5088] | 0.5088 |
| invalid_engagement_rate | 0.1116 +- 0.0394 [worst 0.1510] | 0.1510 |
| ammo_efficiency | 91.6003 +- 6.7643 [worst 84.8360] | 84.8360 |
| latency_p50 | 0.0037 +- 0.0000 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0054 +- 0.0013 [worst 0.0067] | 0.0067 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1625.5000 +- 139.4667 [worst 1486.0333] | 1486.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
