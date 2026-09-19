# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ga** | seeds: 3 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 19:23:45

## Per-instance metrics (mean +- std over 3 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4861 | 0.0000 | 0.1095 | 69.4034 | 0.010 | 70.0 | 4191.7 | `331e3359d4a5` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4302 | 0.0000 | 0.1000 | 64.6903 | 0.009 | 70.0 | 4339.3 | `f7b6a7c01c7e` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4582 +- 0.0279 [worst 0.4861] | 0.4861 |
| gap_mean | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| invalid_engagement_rate | 0.1048 +- 0.0048 [worst 0.1095] | 0.1095 |
| ammo_efficiency | 67.0469 +- 2.3566 [worst 64.6903] | 64.6903 |
| latency_p50 | 0.0098 +- 0.0003 [worst 0.0101] | 0.0101 |
| latency_p90 | 0.0143 +- 0.0007 [worst 0.0150] | 0.0150 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4265.5000 +- 73.8333 [worst 4191.6667] | 4191.6667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
