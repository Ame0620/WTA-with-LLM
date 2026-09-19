# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ga** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 19:43:38

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4925 | 0.3603 | 0.1467 | 67.0215 | 0.640 | 70.0 | 4140.0 | `00162ffe49ee` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4437 | 0.3864 | 0.1114 | 63.2824 | 0.594 | 70.0 | 4236.7 | `18e6303d3b84` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4681 +- 0.0244 [worst 0.4925] | 0.4925 |
| gap_mean | 0.3733 +- 0.0131 [worst 0.3864] | 0.3864 |
| invalid_engagement_rate | 0.1290 +- 0.0176 [worst 0.1467] | 0.1467 |
| ammo_efficiency | 65.1519 +- 1.8695 [worst 63.2824] | 63.2824 |
| latency_p50 | 0.6170 +- 0.0232 [worst 0.6403] | 0.6403 |
| latency_p90 | 0.6989 +- 0.0192 [worst 0.7181] | 0.7181 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4188.3333 +- 48.3667 [worst 4139.9667] | 4139.9667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
