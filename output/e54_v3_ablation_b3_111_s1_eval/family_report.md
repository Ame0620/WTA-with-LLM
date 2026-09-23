# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:03:54

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6514 | 0.4346 | 0.2098 | 81.4030 | 0.004 | 17.0 | 1374.0 | `765ec89c0561` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5608 | 0.3214 | 0.1167 | 93.4220 | 0.004 | 18.0 | 1677.4 | `f3f984d674b2` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6061 +- 0.0453 [worst 0.6514] | 0.6514 |
| gap_mean | 0.3780 +- 0.0566 [worst 0.4346] | 0.4346 |
| invalid_engagement_rate | 0.1632 +- 0.0466 [worst 0.2098] | 0.2098 |
| ammo_efficiency | 87.4125 +- 6.0095 [worst 81.4030] | 81.4030 |
| latency_p50 | 0.0038 +- 0.0000 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0055 +- 0.0013 [worst 0.0068] | 0.0068 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1525.7167 +- 151.7167 [worst 1374.0000] | 1374.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
