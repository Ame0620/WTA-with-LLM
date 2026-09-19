# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **cplex** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 17:38:54

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.7112 | 0.0000 | 0.1411 | 91.2844 | 0.661 | 30.0 | 2355.6 | `77558141f1d2` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.6796 | 0.0000 | 0.0344 | 82.0416 | 0.632 | 30.0 | 2440.1 | `d950bdb825e5` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6954 +- 0.0158 [worst 0.7112] | 0.7112 |
| gap_mean | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| invalid_engagement_rate | 0.0878 +- 0.0533 [worst 0.1411] | 0.1411 |
| ammo_efficiency | 86.6630 +- 4.6214 [worst 82.0416] | 82.0416 |
| latency_p50 | 0.6465 +- 0.0143 [worst 0.6608] | 0.6608 |
| latency_p90 | 0.7397 +- 0.0018 [worst 0.7414] | 0.7414 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 2397.8333 +- 42.2333 [worst 2355.6000] | 2355.6000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
