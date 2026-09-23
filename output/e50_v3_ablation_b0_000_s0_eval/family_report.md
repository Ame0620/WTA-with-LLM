# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:47:23

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6278 | 0.4877 | 0.0944 | 81.2181 | 0.003 | 18.0 | 1467.0 | `e04a2f9f8181` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6479 | 0.4767 | 0.1130 | 73.7550 | 0.003 | 18.0 | 1344.6 | `87e2802edbfd` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6379 +- 0.0100 [worst 0.6479] | 0.6479 |
| gap_mean | 0.4822 +- 0.0055 [worst 0.4877] | 0.4877 |
| invalid_engagement_rate | 0.1037 +- 0.0093 [worst 0.1130] | 0.1130 |
| ammo_efficiency | 77.4866 +- 3.7315 [worst 73.7550] | 73.7550 |
| latency_p50 | 0.0033 +- 0.0001 [worst 0.0034] | 0.0034 |
| latency_p90 | 0.0703 +- 0.0029 [worst 0.0732] | 0.0732 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1405.8000 +- 61.2333 [worst 1344.5667] | 1344.5667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
