# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:53:29

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6382 | 0.5046 | 0.1426 | 78.9378 | 0.004 | 18.0 | 1426.2 | `8a31a2cb1c85` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6343 | 0.5235 | 0.1765 | 81.7317 | 0.004 | 17.0 | 1396.5 | `4241c9452e86` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6363 +- 0.0019 [worst 0.6382] | 0.6382 |
| gap_mean | 0.5141 +- 0.0095 [worst 0.5235] | 0.5235 |
| invalid_engagement_rate | 0.1595 +- 0.0169 [worst 0.1765] | 0.1765 |
| ammo_efficiency | 80.3347 +- 1.3969 [worst 78.9378] | 78.9378 |
| latency_p50 | 0.0038 +- 0.0001 [worst 0.0040] | 0.0040 |
| latency_p90 | 0.0157 +- 0.0088 [worst 0.0246] | 0.0246 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1411.3667 +- 14.8667 [worst 1396.5000] | 1396.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
