# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:54:07

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6354 | 0.4213 | 0.1500 | 79.5544 | 0.004 | 18.0 | 1437.3 | `19fa42473e31` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6285 | 0.2762 | 0.1074 | 78.9831 | 0.004 | 18.0 | 1418.6 | `ef764d6c9ebb` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6320 +- 0.0034 [worst 0.6354] | 0.6354 |
| gap_mean | 0.3487 +- 0.0725 [worst 0.4213] | 0.4213 |
| invalid_engagement_rate | 0.1287 +- 0.0213 [worst 0.1500] | 0.1500 |
| ammo_efficiency | 79.2688 +- 0.2856 [worst 78.9831] | 78.9831 |
| latency_p50 | 0.0037 +- 0.0001 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0191 +- 0.0016 [worst 0.0207] | 0.0207 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1427.9333 +- 9.3333 [worst 1418.6000] | 1418.6000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
