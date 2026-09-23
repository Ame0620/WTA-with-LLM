# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **mappo** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:15:23

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.5730 | n/a | 0.3431 | 54.1931 | 0.015 | 65.0 | 3492.8 | `8106b8a65170` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.4471 | n/a | 0.2899 | 68.7426 | 0.015 | 69.0 | 4732.4 | `144eab674e89` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.5549 | n/a | 0.3085 | 57.2358 | 0.015 | 67.1 | 3806.9 | `20e54bbfc6ba` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.5533 | n/a | 0.2908 | 57.8173 | 0.015 | 65.0 | 3750.7 | `0d41ae38742a` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5321 +- 0.0497 [worst 0.5730] | 0.5730 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3080 +- 0.0215 [worst 0.3431] | 0.3431 |
| ammo_efficiency | 59.4972 +- 5.5124 [worst 54.1931] | 54.1931 |
| latency_p50 | 0.0149 +- 0.0002 [worst 0.0151] | 0.0151 |
| latency_p90 | 0.0186 +- 0.0037 [worst 0.0250] | 0.0250 |
| shots_total | 66.5250 +- 1.6664 [worst 69.0000] | 69.0000 |
| destroyed_value | 3945.7000 +- 469.3894 [worst 3492.8000] | 3492.8000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
