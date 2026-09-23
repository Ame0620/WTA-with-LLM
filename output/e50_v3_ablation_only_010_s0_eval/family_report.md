# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:51:09

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6540 | 0.5345 | 0.0771 | 83.2193 | 0.003 | 16.0 | 1363.8 | `eb71103c3563` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.7130 | 0.5998 | 0.2622 | 73.0138 | 0.003 | 15.0 | 1096.2 | `58d9dbc53486` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6835 +- 0.0295 [worst 0.7130] | 0.7130 |
| gap_mean | 0.5672 +- 0.0326 [worst 0.5998] | 0.5998 |
| invalid_engagement_rate | 0.1697 +- 0.0926 [worst 0.2622] | 0.2622 |
| ammo_efficiency | 78.1165 +- 5.1027 [worst 73.0138] | 73.0138 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0031] | 0.0031 |
| latency_p90 | 0.0221 +- 0.0019 [worst 0.0240] | 0.0240 |
| shots_total | 15.5000 +- 0.5000 [worst 16.0000] | 16.0000 |
| destroyed_value | 1230.0000 +- 133.7667 [worst 1096.2333] | 1096.2333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
