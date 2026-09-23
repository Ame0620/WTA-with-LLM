# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:00:12

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4448 | 2.2088 | 0.3372 | 65.4390 | 0.721 | 69.0 | 4528.5 | `109cce635513` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4134 | 1.6546 | 0.3684 | 65.4280 | 0.702 | 68.1 | 4467.3 | `2c6ddf932ae7` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4291 +- 0.0157 [worst 0.4448] | 0.4448 |
| gap_mean | 1.9317 +- 0.2771 [worst 2.2088] | 2.2088 |
| invalid_engagement_rate | 0.3528 +- 0.0156 [worst 0.3684] | 0.3684 |
| ammo_efficiency | 65.4335 +- 0.0055 [worst 65.4280] | 65.4280 |
| latency_p50 | 0.7116 +- 0.0096 [worst 0.7213] | 0.7213 |
| latency_p90 | 0.9253 +- 0.0117 [worst 0.9370] | 0.9370 |
| shots_total | 68.5667 +- 0.4333 [worst 69.0000] | 69.0000 |
| destroyed_value | 4497.8667 +- 30.6000 [worst 4467.2667] | 4467.2667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
