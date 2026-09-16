# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **greedy** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-02 15:46:22

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.8008 | 0.2883 | 0.4148 | 45.9472 | 0.434 | 18.0 | 785.2 | `d96c7504044d` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.7818 | 0.2653 | 0.2796 | 47.3602 | 0.444 | 18.0 | 833.2 | `3446b7a8f986` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7913 +- 0.0095 [worst 0.8008] | 0.8008 |
| gap_mean | 0.2768 +- 0.0115 [worst 0.2883] | 0.2883 |
| invalid_engagement_rate | 0.3472 +- 0.0676 [worst 0.4148] | 0.4148 |
| ammo_efficiency | 46.6537 +- 0.7065 [worst 45.9472] | 45.9472 |
| latency_p50 | 0.4391 +- 0.0048 [worst 0.4439] | 0.4439 |
| latency_p90 | 0.5134 +- 0.0016 [worst 0.5149] | 0.5149 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 809.2000 +- 24.0333 [worst 785.1667] | 785.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
