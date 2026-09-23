# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:05:33

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6450 | n/a | 0.1486 | 79.3209 | 0.004 | 17.7 | 1399.5 | `188c0b946da6` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5571 | n/a | 0.0704 | 92.9137 | 0.004 | 18.0 | 1691.5 | `e327e35fdec8` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6010 +- 0.0439 [worst 0.6450] | 0.6450 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1095 +- 0.0391 [worst 0.1486] | 0.1486 |
| ammo_efficiency | 86.1173 +- 6.7964 [worst 79.3209] | 79.3209 |
| latency_p50 | 0.0037 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0055 +- 0.0017 [worst 0.0072] | 0.0072 |
| shots_total | 17.8333 +- 0.1667 [worst 18.0000] | 18.0000 |
| destroyed_value | 1545.5333 +- 146.0000 [worst 1399.5333] | 1399.5333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
