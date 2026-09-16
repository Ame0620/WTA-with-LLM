# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **mappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 17:34:14

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5562 | n/a | 0.0667 | 102.5464 | 0.004 | 18.0 | 1843.5 | `b03768df9a7b` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6272 | n/a | 0.2056 | 94.3756 | 0.004 | 18.0 | 1714.3 | `050f045bafc5` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6451 | n/a | 0.1667 | 98.0518 | 0.004 | 17.0 | 1689.4 | `6a42551a41de` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6360 | n/a | 0.2148 | 91.3885 | 0.004 | 18.0 | 1676.0 | `6d5aeec69b1c` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6161 +- 0.0352 [worst 0.6451] | 0.6451 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1634 +- 0.0587 [worst 0.2148] | 0.2148 |
| ammo_efficiency | 96.5906 +- 4.1706 [worst 91.3885] | 91.3885 |
| latency_p50 | 0.0039 +- 0.0002 [worst 0.0042] | 0.0042 |
| latency_p90 | 0.0062 +- 0.0016 [worst 0.0089] | 0.0089 |
| shots_total | 17.7500 +- 0.4330 [worst 18.0000] | 18.0000 |
| destroyed_value | 1730.7833 +- 66.5150 [worst 1675.9667] | 1675.9667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
