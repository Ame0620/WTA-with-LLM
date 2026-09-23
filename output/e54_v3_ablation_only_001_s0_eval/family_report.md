# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:03:49

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6651 | 0.5248 | 0.2426 | 72.9167 | 0.004 | 18.0 | 1320.1 | `ba6a8f85bb6c` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5807 | 0.4521 | 0.1481 | 88.0048 | 0.004 | 18.0 | 1601.4 | `8edd83a6b627` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6229 +- 0.0422 [worst 0.6651] | 0.6651 |
| gap_mean | 0.4885 +- 0.0363 [worst 0.5248] | 0.5248 |
| invalid_engagement_rate | 0.1954 +- 0.0472 [worst 0.2426] | 0.2426 |
| ammo_efficiency | 80.4608 +- 7.5441 [worst 72.9167] | 72.9167 |
| latency_p50 | 0.0037 +- 0.0001 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0117 +- 0.0079 [worst 0.0196] | 0.0196 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1460.7500 +- 140.6500 [worst 1320.1000] | 1320.1000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
