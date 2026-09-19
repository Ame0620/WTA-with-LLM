# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **cplex** | seeds: 5 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 16:09:47

## Per-instance metrics (mean +- std over 5 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.3198 | 0.0000 | 0.1175 | 78.2264 | 0.633 | 80.0 | 5548.2 | `a1803ba84b56` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.2678 | 0.0000 | 0.0975 | 75.1652 | 0.623 | 80.0 | 5576.6 | `d5ac10fb2def` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.2938 +- 0.0260 [worst 0.3198] | 0.3198 |
| gap_mean | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| invalid_engagement_rate | 0.1075 +- 0.0100 [worst 0.1175] | 0.1175 |
| ammo_efficiency | 76.6958 +- 1.5306 [worst 75.1652] | 75.1652 |
| latency_p50 | 0.6283 +- 0.0049 [worst 0.6333] | 0.6333 |
| latency_p90 | 0.7992 +- 0.0490 [worst 0.8482] | 0.8482 |
| shots_total | 80.0000 +- 0.0000 [worst 80.0000] | 80.0000 |
| destroyed_value | 5562.4000 +- 14.2000 [worst 5548.2000] | 5548.2000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
