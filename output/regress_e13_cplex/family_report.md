# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **cplex** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-02 16:59:53

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.7428 | 0.0000 | 0.1500 | 64.6991 | 0.392 | 18.0 | 1014.1 | `df512d01e503` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6742 | 0.0000 | 0.0426 | 71.1370 | 0.375 | 18.0 | 1244.1 | `96d35c879acd` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7085 +- 0.0343 [worst 0.7428] | 0.7428 |
| gap_mean | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| invalid_engagement_rate | 0.0963 +- 0.0537 [worst 0.1500] | 0.1500 |
| ammo_efficiency | 67.9181 +- 3.2189 [worst 64.6991] | 64.6991 |
| latency_p50 | 0.3834 +- 0.0084 [worst 0.3918] | 0.3918 |
| latency_p90 | 0.4366 +- 0.0012 [worst 0.4377] | 0.4377 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1129.0833 +- 115.0167 [worst 1014.0667] | 1014.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
