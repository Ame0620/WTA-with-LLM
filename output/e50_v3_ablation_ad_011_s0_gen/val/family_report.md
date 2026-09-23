# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:49:08

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5818 | n/a | 0.1611 | 96.0464 | 0.004 | 18.0 | 1737.3 | `c9141524b9ee` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6106 | n/a | 0.1167 | 99.7578 | 0.004 | 18.0 | 1790.4 | `898b461bebe0` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6506 | n/a | 0.2056 | 91.2610 | 0.004 | 18.0 | 1663.3 | `7a287fdadae3` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6488 | n/a | 0.1611 | 88.8545 | 0.004 | 18.0 | 1617.0 | `63d21de491c9` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6229 +- 0.0286 [worst 0.6506] | 0.6506 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1611 +- 0.0314 [worst 0.2056] | 0.2056 |
| ammo_efficiency | 93.9799 +- 4.2225 [worst 88.8545] | 88.8545 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0048 +- 0.0012 [worst 0.0068] | 0.0068 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1701.9833 +- 66.6616 [worst 1617.0000] | 1617.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
