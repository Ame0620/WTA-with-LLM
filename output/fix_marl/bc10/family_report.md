# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 14:00:21

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6729 | 0.5111 | 0.2574 | 70.5519 | 0.417 | 18.0 | 1289.4 | `81ce8d777c92` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6074 | 0.2954 | 0.1037 | 83.1546 | 0.394 | 18.0 | 1499.4 | `0ebe90651e1a` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6401 +- 0.0328 [worst 0.6729] | 0.6729 |
| gap_mean | 0.4033 +- 0.1078 [worst 0.5111] | 0.5111 |
| invalid_engagement_rate | 0.1806 +- 0.0769 [worst 0.2574] | 0.2574 |
| ammo_efficiency | 76.8533 +- 6.3014 [worst 70.5519] | 70.5519 |
| latency_p50 | 0.4054 +- 0.0113 [worst 0.4167] | 0.4167 |
| latency_p90 | 0.4379 +- 0.0083 [worst 0.4461] | 0.4461 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1394.4000 +- 105.0333 [worst 1289.3667] | 1289.3667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
