# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:04:17

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6650 | 0.3786 | 0.2133 | 80.9485 | 0.004 | 17.0 | 1320.6 | `32ee72049fea` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5902 | 0.3739 | 0.1667 | 86.3969 | 0.004 | 18.0 | 1565.0 | `69ba26b80d5f` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6276 +- 0.0374 [worst 0.6650] | 0.6650 |
| gap_mean | 0.3763 +- 0.0024 [worst 0.3786] | 0.3786 |
| invalid_engagement_rate | 0.1900 +- 0.0233 [worst 0.2133] | 0.2133 |
| ammo_efficiency | 83.6727 +- 2.7242 [worst 80.9485] | 80.9485 |
| latency_p50 | 0.0038 +- 0.0000 [worst 0.0039] | 0.0039 |
| latency_p90 | 0.0055 +- 0.0014 [worst 0.0069] | 0.0069 |
| shots_total | 17.5167 +- 0.4833 [worst 18.0000] | 18.0000 |
| destroyed_value | 1442.8000 +- 122.2333 [worst 1320.5667] | 1320.5667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
