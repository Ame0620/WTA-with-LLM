# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:37:11

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4495 | 2.1317 | 0.3324 | 64.1872 | 0.681 | 70.0 | 4490.5 | `98e6a0de474f` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.3882 | 1.5654 | 0.3595 | 66.1856 | 0.667 | 70.0 | 4659.2 | `b1cfc526c66a` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4189 +- 0.0306 [worst 0.4495] | 0.4495 |
| gap_mean | 1.8486 +- 0.2832 [worst 2.1317] | 2.1317 |
| invalid_engagement_rate | 0.3460 +- 0.0136 [worst 0.3595] | 0.3595 |
| ammo_efficiency | 65.1864 +- 0.9992 [worst 64.1872] | 64.1872 |
| latency_p50 | 0.6740 +- 0.0070 [worst 0.6810] | 0.6810 |
| latency_p90 | 0.8519 +- 0.0504 [worst 0.9023] | 0.9023 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4574.8167 +- 84.3500 [worst 4490.4667] | 4490.4667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
