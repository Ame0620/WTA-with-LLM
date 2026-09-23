# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **maddpg** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:30:13

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.5803 | 1.6650 | 0.2576 | 48.8756 | 0.679 | 70.0 | 3423.2 | `7a4dce43e7e3` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.5396 | 1.4304 | 0.3005 | 49.7740 | 0.662 | 70.0 | 3506.5 | `62571c77dda9` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5600 +- 0.0204 [worst 0.5803] | 0.5803 |
| gap_mean | 1.5477 +- 0.1173 [worst 1.6650] | 1.6650 |
| invalid_engagement_rate | 0.2790 +- 0.0214 [worst 0.3005] | 0.3005 |
| ammo_efficiency | 49.3248 +- 0.4492 [worst 48.8756] | 48.8756 |
| latency_p50 | 0.6704 +- 0.0087 [worst 0.6792] | 0.6792 |
| latency_p90 | 0.7479 +- 0.0150 [worst 0.7629] | 0.7629 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 3464.8333 +- 41.6667 [worst 3423.1667] | 3423.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
