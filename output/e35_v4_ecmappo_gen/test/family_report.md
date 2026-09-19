# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:27:38

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.6666 | n/a | 0.2174 | 92.3347 | 0.008 | 29.1 | 2719.7 | `78541688f23c` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.6190 | n/a | 0.2122 | 96.8342 | 0.008 | 30.0 | 2901.9 | `a7f8d9a6836b` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6428 +- 0.0238 [worst 0.6666] | 0.6666 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2148 +- 0.0026 [worst 0.2174] | 0.2174 |
| ammo_efficiency | 94.5845 +- 2.2498 [worst 92.3347] | 92.3347 |
| latency_p50 | 0.0080 +- 0.0001 [worst 0.0080] | 0.0080 |
| latency_p90 | 0.0103 +- 0.0011 [worst 0.0114] | 0.0114 |
| shots_total | 29.5667 +- 0.4333 [worst 30.0000] | 30.0000 |
| destroyed_value | 2810.7833 +- 91.0833 [worst 2719.7000] | 2719.7000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
