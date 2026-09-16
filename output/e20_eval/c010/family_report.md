# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-09 20:27:08

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6131 | 0.4628 | 0.0634 | 85.9087 | 0.412 | 17.9 | 1525.1 | `d60f5cb6b3d3` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5795 | 0.3936 | 0.1556 | 88.5843 | 0.402 | 18.0 | 1605.7 | `60fa1cb9fc2b` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5963 +- 0.0168 [worst 0.6131] | 0.6131 |
| gap_mean | 0.4282 +- 0.0346 [worst 0.4628] | 0.4628 |
| invalid_engagement_rate | 0.1095 +- 0.0461 [worst 0.1556] | 0.1556 |
| ammo_efficiency | 87.2465 +- 1.3378 [worst 85.9087] | 85.9087 |
| latency_p50 | 0.4069 +- 0.0051 [worst 0.4120] | 0.4120 |
| latency_p90 | 0.4492 +- 0.0045 [worst 0.4536] | 0.4536 |
| shots_total | 17.9500 +- 0.0500 [worst 18.0000] | 18.0000 |
| destroyed_value | 1565.4333 +- 40.3000 [worst 1525.1333] | 1525.1333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
