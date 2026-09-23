# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:11:34

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6598 | n/a | 0.2098 | 78.8716 | 0.003 | 17.0 | 1341.1 | `6de145dd5059` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5873 | n/a | 0.1728 | 91.4890 | 0.003 | 17.2 | 1576.0 | `22d640815325` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6236 +- 0.0362 [worst 0.6598] | 0.6598 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1913 +- 0.0185 [worst 0.2098] | 0.2098 |
| ammo_efficiency | 85.1803 +- 6.3087 [worst 78.8716] | 78.8716 |
| latency_p50 | 0.0032 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0049 +- 0.0013 [worst 0.0062] | 0.0062 |
| shots_total | 17.0833 +- 0.0833 [worst 17.1667] | 17.1667 |
| destroyed_value | 1458.5833 +- 117.4500 [worst 1341.1333] | 1341.1333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
