# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **greedy_threat** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 17:57:50

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.9156 | 0.6104 | 0.6611 | 22.8266 | 0.619 | 30.0 | 688.2 | `63137740ce2f` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.9072 | 0.5734 | 0.7089 | 23.5514 | 0.576 | 30.0 | 706.5 | `2d26276317b8` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.9114 +- 0.0042 [worst 0.9156] | 0.9156 |
| gap_mean | 0.5919 +- 0.0185 [worst 0.6104] | 0.6104 |
| invalid_engagement_rate | 0.6850 +- 0.0239 [worst 0.7089] | 0.7089 |
| ammo_efficiency | 23.1890 +- 0.3624 [worst 22.8266] | 22.8266 |
| latency_p50 | 0.5971 +- 0.0216 [worst 0.6187] | 0.6187 |
| latency_p90 | 0.7506 +- 0.0039 [worst 0.7546] | 0.7546 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 697.3500 +- 9.1833 [worst 688.1667] | 688.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
