# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 14:01:06

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4416 | 2.0713 | 0.3268 | 68.1544 | 0.636 | 66.9 | 4554.5 | `f52da355eda3` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.3942 | 1.5971 | 0.3623 | 66.8232 | 0.619 | 69.0 | 4613.8 | `6fc00ecde469` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4179 +- 0.0237 [worst 0.4416] | 0.4416 |
| gap_mean | 1.8342 +- 0.2371 [worst 2.0713] | 2.0713 |
| invalid_engagement_rate | 0.3446 +- 0.0177 [worst 0.3623] | 0.3623 |
| ammo_efficiency | 67.4888 +- 0.6656 [worst 66.8232] | 66.8232 |
| latency_p50 | 0.6276 +- 0.0084 [worst 0.6360] | 0.6360 |
| latency_p90 | 0.7732 +- 0.0680 [worst 0.8412] | 0.8412 |
| shots_total | 67.9500 +- 1.0500 [worst 69.0000] | 69.0000 |
| destroyed_value | 4584.1500 +- 29.6500 [worst 4554.5000] | 4554.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
