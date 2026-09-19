# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **ga** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 17:49:51

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.7222 | 0.0041 | 0.1589 | 91.0036 | 0.598 | 30.0 | 2266.0 | `aa74cf94a104` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.6849 | 0.0125 | 0.0344 | 80.9643 | 0.541 | 30.0 | 2399.4 | `619b092b6af6` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7036 +- 0.0186 [worst 0.7222] | 0.7222 |
| gap_mean | 0.0083 +- 0.0042 [worst 0.0125] | 0.0125 |
| invalid_engagement_rate | 0.0967 +- 0.0622 [worst 0.1589] | 0.1589 |
| ammo_efficiency | 85.9840 +- 5.0197 [worst 80.9643] | 80.9643 |
| latency_p50 | 0.5692 +- 0.0286 [worst 0.5978] | 0.5978 |
| latency_p90 | 0.6950 +- 0.0037 [worst 0.6987] | 0.6987 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 2332.7333 +- 66.7000 [worst 2266.0333] | 2266.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
