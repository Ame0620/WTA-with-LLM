# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **mappo** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:03:31

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 1.0000 | n/a | 0.0000 | n/a | 0.012 | 0.0 | 0.0 | `c9ed490996aa` |
| `dn_10x100_K10_s02.txt` | 7616 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `d1bf012320ab` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 1.0000 +- 0.0000 [worst 1.0000] | 1.0000 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| ammo_efficiency | n/a | n/a |
| latency_p50 | 0.0119 +- 0.0006 [worst 0.0125] | 0.0125 |
| latency_p90 | 0.0177 +- 0.0056 [worst 0.0233] | 0.0233 |
| shots_total | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| destroyed_value | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
