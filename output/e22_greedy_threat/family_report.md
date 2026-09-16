# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **greedy_threat** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 16:20:51

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.8610 | 0.5293 | 0.5444 | 30.2131 | 0.530 | 18.0 | 548.0 | `c7b2126e1dfe` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.8578 | 0.5298 | 0.4463 | 30.0160 | 0.568 | 18.0 | 543.1 | `b396e2bb9a7e` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8594 +- 0.0016 [worst 0.8610] | 0.8610 |
| gap_mean | 0.5296 +- 0.0002 [worst 0.5298] | 0.5298 |
| invalid_engagement_rate | 0.4954 +- 0.0491 [worst 0.5444] | 0.5444 |
| ammo_efficiency | 30.1145 +- 0.0985 [worst 30.0160] | 30.0160 |
| latency_p50 | 0.5489 +- 0.0190 [worst 0.5679] | 0.5679 |
| latency_p90 | 0.6348 +- 0.0276 [worst 0.6625] | 0.6625 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 545.5333 +- 2.4667 [worst 543.0667] | 543.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
