# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:52:52

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6459 | 0.4237 | 0.1074 | 76.7862 | 0.004 | 18.0 | 1395.8 | `93f5e408f7a4` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5728 | 0.2853 | 0.0593 | 90.6008 | 0.004 | 18.0 | 1631.5 | `587675bedd96` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6094 +- 0.0366 [worst 0.6459] | 0.6459 |
| gap_mean | 0.3545 +- 0.0692 [worst 0.4237] | 0.4237 |
| invalid_engagement_rate | 0.0833 +- 0.0241 [worst 0.1074] | 0.1074 |
| ammo_efficiency | 83.6935 +- 6.9073 [worst 76.7862] | 76.7862 |
| latency_p50 | 0.0040 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0212 +- 0.0132 [worst 0.0344] | 0.0344 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1513.6500 +- 117.8500 [worst 1395.8000] | 1395.8000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
