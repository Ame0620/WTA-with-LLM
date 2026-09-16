# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 13:34:25

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6719 | 0.1955 | 0.1463 | 70.0917 | 0.415 | 18.0 | 1293.5 | `f0ed7ae054cb` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6397 | 0.2754 | 0.1759 | 73.9212 | 0.389 | 18.0 | 1376.1 | `ff1c40ebfd3d` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6558 +- 0.0161 [worst 0.6719] | 0.6719 |
| gap_mean | 0.2354 +- 0.0400 [worst 0.2754] | 0.2754 |
| invalid_engagement_rate | 0.1611 +- 0.0148 [worst 0.1759] | 0.1759 |
| ammo_efficiency | 72.0065 +- 1.9147 [worst 70.0917] | 70.0917 |
| latency_p50 | 0.4017 +- 0.0130 [worst 0.4147] | 0.4147 |
| latency_p90 | 0.4286 +- 0.0005 [worst 0.4291] | 0.4291 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1334.8333 +- 41.3000 [worst 1293.5333] | 1293.5333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
