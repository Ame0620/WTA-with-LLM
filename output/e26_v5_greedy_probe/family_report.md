# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **greedy** | seeds: 5 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 16:11:10

## Per-instance metrics (mean +- std over 5 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.7258 | 1.7117 | 0.6700 | 28.4542 | 0.803 | 80.0 | 2236.6 | `2aa9461575d6` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.6428 | 1.3017 | 0.6275 | 33.6419 | 0.786 | 80.0 | 2720.4 | `aeb47044892f` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6843 +- 0.0415 [worst 0.7258] | 0.7258 |
| gap_mean | 1.5067 +- 0.2050 [worst 1.7117] | 1.7117 |
| invalid_engagement_rate | 0.6488 +- 0.0212 [worst 0.6700] | 0.6700 |
| ammo_efficiency | 31.0481 +- 2.5938 [worst 28.4542] | 28.4542 |
| latency_p50 | 0.7941 +- 0.0085 [worst 0.8026] | 0.8026 |
| latency_p90 | 1.0627 +- 0.1746 [worst 1.2373] | 1.2373 |
| shots_total | 80.0000 +- 0.0000 [worst 80.0000] | 80.0000 |
| destroyed_value | 2478.5000 +- 241.9000 [worst 2236.6000] | 2236.6000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
