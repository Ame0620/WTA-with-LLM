# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **qmix** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:11:31

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.7890 | n/a | 0.4214 | 26.8466 | 0.011 | 70.0 | 1720.8 | `6b90b44f42a8` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.7634 | n/a | 0.4300 | 26.6760 | 0.010 | 70.0 | 1801.8 | `41c20a0b1a23` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7762 +- 0.0128 [worst 0.7890] | 0.7890 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.4257 +- 0.0043 [worst 0.4300] | 0.4300 |
| ammo_efficiency | 26.7613 +- 0.0853 [worst 26.6760] | 26.6760 |
| latency_p50 | 0.0105 +- 0.0001 [worst 0.0106] | 0.0106 |
| latency_p90 | 0.0166 +- 0.0030 [worst 0.0195] | 0.0195 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 1761.3000 +- 40.5000 [worst 1720.8000] | 1720.8000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
