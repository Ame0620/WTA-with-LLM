# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 14:02:56

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4416 | n/a | 0.3268 | 68.1544 | 0.013 | 66.9 | 4554.5 | `f52da355eda3` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.3942 | n/a | 0.3623 | 66.8232 | 0.013 | 69.0 | 4613.8 | `6fc00ecde469` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4179 +- 0.0237 [worst 0.4416] | 0.4416 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3446 +- 0.0177 [worst 0.3623] | 0.3623 |
| ammo_efficiency | 67.4888 +- 0.6656 [worst 66.8232] | 66.8232 |
| latency_p50 | 0.0127 +- 0.0001 [worst 0.0128] | 0.0128 |
| latency_p90 | 0.0196 +- 0.0060 [worst 0.0256] | 0.0256 |
| shots_total | 67.9500 +- 1.0500 [worst 69.0000] | 69.0000 |
| destroyed_value | 4584.1500 +- 29.6500 [worst 4554.5000] | 4554.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
