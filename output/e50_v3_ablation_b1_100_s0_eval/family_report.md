# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:50:36

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.7978 | 0.1552 | 0.2648 | 46.1902 | 0.006 | 18.0 | 797.2 | `5cf55da535b5` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.7169 | 0.1310 | 0.0907 | 59.1009 | 0.004 | 18.0 | 1081.2 | `00bf05edd591` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7573 +- 0.0404 [worst 0.7978] | 0.7978 |
| gap_mean | 0.1431 +- 0.0121 [worst 0.1552] | 0.1552 |
| invalid_engagement_rate | 0.1778 +- 0.0870 [worst 0.2648] | 0.2648 |
| ammo_efficiency | 52.6455 +- 6.4554 [worst 46.1902] | 46.1902 |
| latency_p50 | 0.0048 +- 0.0011 [worst 0.0059] | 0.0059 |
| latency_p90 | 0.0714 +- 0.0392 [worst 0.1106] | 0.1106 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 939.1667 +- 142.0000 [worst 797.1667] | 797.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
