# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:54:44

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6565 | 0.5360 | 0.1627 | 78.9513 | 0.003 | 17.0 | 1354.1 | `2f44c0c5cf7b` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6452 | 0.5451 | 0.1187 | 83.5611 | 0.004 | 16.0 | 1355.1 | `b47aa02ccf97` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6508 +- 0.0057 [worst 0.6565] | 0.6565 |
| gap_mean | 0.5406 +- 0.0046 [worst 0.5451] | 0.5451 |
| invalid_engagement_rate | 0.1407 +- 0.0220 [worst 0.1627] | 0.1627 |
| ammo_efficiency | 81.2562 +- 2.3049 [worst 78.9513] | 78.9513 |
| latency_p50 | 0.0035 +- 0.0004 [worst 0.0039] | 0.0039 |
| latency_p90 | 0.0053 +- 0.0008 [worst 0.0061] | 0.0061 |
| shots_total | 16.5000 +- 0.5000 [worst 17.0000] | 17.0000 |
| destroyed_value | 1354.6333 +- 0.5000 [worst 1354.1333] | 1354.1333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
