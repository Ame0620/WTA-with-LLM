# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **maddpg** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:18:31

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.7371 | n/a | 0.4943 | 30.5750 | 0.011 | 70.0 | 2144.4 | `220aeacaf133` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.6822 | n/a | 0.4129 | 34.7754 | 0.010 | 70.0 | 2420.1 | `cd8e1b36355e` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7097 +- 0.0274 [worst 0.7371] | 0.7371 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.4536 +- 0.0407 [worst 0.4943] | 0.4943 |
| ammo_efficiency | 32.6752 +- 2.1002 [worst 30.5750] | 30.5750 |
| latency_p50 | 0.0107 +- 0.0007 [worst 0.0114] | 0.0114 |
| latency_p90 | 0.0170 +- 0.0059 [worst 0.0229] | 0.0229 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 2282.2500 +- 137.8500 [worst 2144.4000] | 2144.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
