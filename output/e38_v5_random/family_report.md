# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **random** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 20:06:16

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.6417 | n/a | 0.1185 | 44.9755 | 0.000 | 66.7 | 2922.6 | `638f7e7afdca` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.6375 | n/a | 0.1075 | 41.3083 | 0.000 | 65.9 | 2760.7 | `ae12f569d14a` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6396 +- 0.0021 [worst 0.6417] | 0.6417 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1130 +- 0.0055 [worst 0.1185] | 0.1185 |
| ammo_efficiency | 43.1419 +- 1.8336 [worst 41.3083] | 41.3083 |
| latency_p50 | 0.0004 +- 0.0000 [worst 0.0004] | 0.0004 |
| latency_p90 | 0.0006 +- 0.0000 [worst 0.0006] | 0.0006 |
| shots_total | 66.3000 +- 0.3667 [worst 66.6667] | 66.6667 |
| destroyed_value | 2841.6500 +- 80.9167 [worst 2760.7333] | 2760.7333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
