# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:07:33

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6498 | n/a | 0.1926 | 76.1154 | 0.003 | 18.0 | 1380.3 | `4ff62c7710dd` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5955 | n/a | 0.1513 | 89.6878 | 0.003 | 17.3 | 1544.7 | `af1bf9f0b96f` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6227 +- 0.0272 [worst 0.6498] | 0.6498 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1719 +- 0.0206 [worst 0.1926] | 0.1926 |
| ammo_efficiency | 82.9016 +- 6.7862 [worst 76.1154] | 76.1154 |
| latency_p50 | 0.0029 +- 0.0000 [worst 0.0030] | 0.0030 |
| latency_p90 | 0.0044 +- 0.0012 [worst 0.0057] | 0.0057 |
| shots_total | 17.6333 +- 0.3667 [worst 18.0000] | 18.0000 |
| destroyed_value | 1462.5000 +- 82.1667 [worst 1380.3333] | 1380.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
