# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **maddpg** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:17:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.7336 | 2.1262 | 0.4976 | 30.6135 | 0.572 | 70.0 | 2172.8 | `3c3e2b727433` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.6799 | 1.8385 | 0.4162 | 34.7635 | 0.553 | 70.0 | 2438.0 | `ee309064aa6b` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7068 +- 0.0269 [worst 0.7336] | 0.7336 |
| gap_mean | 1.9823 +- 0.1439 [worst 2.1262] | 2.1262 |
| invalid_engagement_rate | 0.4569 +- 0.0407 [worst 0.4976] | 0.4976 |
| ammo_efficiency | 32.6885 +- 2.0750 [worst 30.6135] | 30.6135 |
| latency_p50 | 0.5622 +- 0.0094 [worst 0.5716] | 0.5716 |
| latency_p90 | 0.6610 +- 0.0166 [worst 0.6776] | 0.6776 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 2305.4167 +- 132.6167 [worst 2172.8000] | 2172.8000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
