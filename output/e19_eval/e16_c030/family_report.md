# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-07 19:02:45

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6463 | 0.4652 | 0.2093 | 87.0301 | 0.398 | 18.0 | 1394.3 | `5b891024fca9` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.4995 | 0.2882 | 0.0463 | 94.7389 | 0.386 | 19.8 | 1911.3 | `96595a81f2c5` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5729 +- 0.0734 [worst 0.6463] | 0.6463 |
| gap_mean | 0.3767 +- 0.0885 [worst 0.4652] | 0.4652 |
| invalid_engagement_rate | 0.1278 +- 0.0815 [worst 0.2093] | 0.2093 |
| ammo_efficiency | 90.8845 +- 3.8544 [worst 87.0301] | 87.0301 |
| latency_p50 | 0.3917 +- 0.0059 [worst 0.3976] | 0.3976 |
| latency_p90 | 0.4261 +- 0.0097 [worst 0.4358] | 0.4358 |
| shots_total | 18.9000 +- 0.9000 [worst 19.8000] | 19.8000 |
| destroyed_value | 1652.8167 +- 258.4833 [worst 1394.3333] | 1394.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
