# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:52:13

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5666 | n/a | 0.1056 | 98.6009 | 0.004 | 18.0 | 1800.3 | `ff1c4929832e` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5973 | n/a | 0.1111 | 101.9757 | 0.004 | 18.0 | 1851.5 | `911bea569933` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6838 | n/a | 0.2130 | 90.2079 | 0.004 | 18.0 | 1504.9 | `9b0931765f10` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6780 | n/a | 0.2759 | 80.7338 | 0.004 | 18.0 | 1482.3 | `e0463a602985` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6314 +- 0.0507 [worst 0.6838] | 0.6838 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1764 +- 0.0716 [worst 0.2759] | 0.2759 |
| ammo_efficiency | 92.8796 +- 8.2178 [worst 80.7338] | 80.7338 |
| latency_p50 | 0.0039 +- 0.0004 [worst 0.0044] | 0.0044 |
| latency_p90 | 0.0053 +- 0.0019 [worst 0.0084] | 0.0084 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1659.7750 +- 167.3318 [worst 1482.3333] | 1482.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
