# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 14:02:47

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.4912 | n/a | 0.2982 | 67.4362 | 0.013 | 62.0 | 4162.0 | `b976aa38ea32` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.4336 | n/a | 0.2574 | 77.2070 | 0.013 | 63.2 | 4848.2 | `b4ead9686aea` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.4811 | n/a | 0.3142 | 67.1316 | 0.013 | 66.2 | 4438.1 | `ca019324f854` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.4007 | n/a | 0.2224 | 72.0713 | 0.013 | 70.0 | 5032.3 | `04354d725180` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4517 +- 0.0366 [worst 0.4912] | 0.4912 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2731 +- 0.0358 [worst 0.3142] | 0.3142 |
| ammo_efficiency | 70.9615 +- 4.1029 [worst 67.1316] | 67.1316 |
| latency_p50 | 0.0128 +- 0.0001 [worst 0.0129] | 0.0129 |
| latency_p90 | 0.0144 +- 0.0013 [worst 0.0166] | 0.0166 |
| shots_total | 65.3583 +- 3.0809 [worst 70.0000] | 70.0000 |
| destroyed_value | 4620.1500 +- 340.9177 [worst 4162.0333] | 4162.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
