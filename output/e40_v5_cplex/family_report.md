# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **cplex** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 19:52:16

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4609 | 0.0000 | 0.1138 | 70.6936 | 0.605 | 70.0 | 4397.5 | `9e435aae9b69` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4164 | 0.0000 | 0.1148 | 68.2694 | 0.590 | 70.0 | 4444.7 | `21f65e97948e` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4386 +- 0.0222 [worst 0.4609] | 0.4609 |
| gap_mean | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| invalid_engagement_rate | 0.1143 +- 0.0005 [worst 0.1148] | 0.1148 |
| ammo_efficiency | 69.4815 +- 1.2121 [worst 68.2694] | 68.2694 |
| latency_p50 | 0.5974 +- 0.0078 [worst 0.6052] | 0.6052 |
| latency_p90 | 0.7081 +- 0.0012 [worst 0.7093] | 0.7093 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4421.1167 +- 23.6167 [worst 4397.5000] | 4397.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
