# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 02:01:01

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6599 | 0.5189 | 0.2118 | 78.7647 | 0.004 | 17.0 | 1340.6 | `109b9e46f541` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6190 | 0.4747 | 0.1500 | 80.8606 | 0.004 | 18.0 | 1455.0 | `3d20dddf6404` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6395 +- 0.0205 [worst 0.6599] | 0.6599 |
| gap_mean | 0.4968 +- 0.0221 [worst 0.5189] | 0.5189 |
| invalid_engagement_rate | 0.1809 +- 0.0309 [worst 0.2118] | 0.2118 |
| ammo_efficiency | 79.8126 +- 1.0479 [worst 78.7647] | 78.7647 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0054 +- 0.0015 [worst 0.0069] | 0.0069 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1397.8000 +- 57.2333 [worst 1340.5667] | 1340.5667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
