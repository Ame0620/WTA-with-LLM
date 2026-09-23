# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:52:16

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6372 | n/a | 0.1167 | 80.5234 | 0.004 | 18.0 | 1430.1 | `54bea9d90e24` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5870 | n/a | 0.1019 | 86.9680 | 0.004 | 18.0 | 1577.1 | `180d6c255264` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6121 +- 0.0251 [worst 0.6372] | 0.6372 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1093 +- 0.0074 [worst 0.1167] | 0.1167 |
| ammo_efficiency | 83.7457 +- 3.2223 [worst 80.5234] | 80.5234 |
| latency_p50 | 0.0037 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0056 +- 0.0015 [worst 0.0071] | 0.0071 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1503.5833 +- 73.4833 [worst 1430.1000] | 1430.1000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
