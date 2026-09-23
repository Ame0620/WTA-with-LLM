# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:58:09

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6509 | 0.5233 | 0.1176 | 80.4400 | 0.004 | 17.0 | 1376.0 | `9172ee816432` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6650 | 0.5306 | 0.3000 | 79.8404 | 0.004 | 16.0 | 1279.3 | `0cf5c94a4c69` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6580 +- 0.0070 [worst 0.6650] | 0.6650 |
| gap_mean | 0.5269 +- 0.0037 [worst 0.5306] | 0.5306 |
| invalid_engagement_rate | 0.2088 +- 0.0912 [worst 0.3000] | 0.3000 |
| ammo_efficiency | 80.1402 +- 0.2998 [worst 79.8404] | 79.8404 |
| latency_p50 | 0.0037 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0056 +- 0.0014 [worst 0.0070] | 0.0070 |
| shots_total | 16.5000 +- 0.5000 [worst 17.0000] | 17.0000 |
| destroyed_value | 1327.6333 +- 48.3667 [worst 1279.2667] | 1279.2667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
