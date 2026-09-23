# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:03:46

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6897 | 0.5160 | 0.3111 | 77.5772 | 0.003 | 18.0 | 1223.4 | `e63c1951db20` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5712 | 0.3887 | 0.1481 | 90.5828 | 0.003 | 18.0 | 1637.6 | `58e19fd5a778` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6304 +- 0.0592 [worst 0.6897] | 0.6897 |
| gap_mean | 0.4523 +- 0.0636 [worst 0.5160] | 0.5160 |
| invalid_engagement_rate | 0.2296 +- 0.0815 [worst 0.3111] | 0.3111 |
| ammo_efficiency | 84.0800 +- 6.5028 [worst 77.5772] | 77.5772 |
| latency_p50 | 0.0032 +- 0.0001 [worst 0.0033] | 0.0033 |
| latency_p90 | 0.0047 +- 0.0014 [worst 0.0061] | 0.0061 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1430.4667 +- 207.1000 [worst 1223.3667] | 1223.3667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
