# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:52:48

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6379 | n/a | 0.1020 | 82.6373 | 0.003 | 17.0 | 1427.6 | `4bcc5356d382` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6327 | n/a | 0.0907 | 76.7760 | 0.003 | 18.0 | 1402.9 | `4b616a1fbd5c` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6353 +- 0.0026 [worst 0.6379] | 0.6379 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.0964 +- 0.0056 [worst 0.1020] | 0.1020 |
| ammo_efficiency | 79.7066 +- 2.9306 [worst 76.7760] | 76.7760 |
| latency_p50 | 0.0031 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0048 +- 0.0011 [worst 0.0059] | 0.0059 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1415.2333 +- 12.3333 [worst 1402.9000] | 1402.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
