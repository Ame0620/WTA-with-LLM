# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **rh-cplex** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 16:52:46

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6884 | 0.2443 | 0.0926 | 69.5997 | 1.018 | 18.0 | 1228.5 | `83e709895d38` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6732 | 0.2401 | 0.0389 | 68.9292 | 0.995 | 18.0 | 1247.9 | `17e81c010a26` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6808 +- 0.0076 [worst 0.6884] | 0.6884 |
| gap_mean | 0.2422 +- 0.0021 [worst 0.2443] | 0.2443 |
| invalid_engagement_rate | 0.0657 +- 0.0269 [worst 0.0926] | 0.0926 |
| ammo_efficiency | 69.2644 +- 0.3352 [worst 68.9292] | 68.9292 |
| latency_p50 | 1.0067 +- 0.0113 [worst 1.0180] | 1.0180 |
| latency_p90 | 1.1015 +- 0.0073 [worst 1.1088] | 1.1088 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1238.1833 +- 9.7167 [worst 1228.4667] | 1228.4667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
