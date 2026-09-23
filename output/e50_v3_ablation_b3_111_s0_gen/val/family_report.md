# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:48:27

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5623 | n/a | 0.0719 | 106.1668 | 0.004 | 17.1 | 1818.1 | `0ba0ace55baf` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6117 | n/a | 0.1094 | 102.8877 | 0.004 | 17.1 | 1785.3 | `e6b163aca51b` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6558 | n/a | 0.1706 | 95.7761 | 0.004 | 17.0 | 1638.3 | `f1cff64f4e1c` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6923 | n/a | 0.2804 | 82.7353 | 0.004 | 17.0 | 1416.9 | `14008268437e` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6305 +- 0.0486 [worst 0.6923] | 0.6923 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1581 +- 0.0789 [worst 0.2804] | 0.2804 |
| ammo_efficiency | 96.8915 +- 8.9948 [worst 82.7353] | 82.7353 |
| latency_p50 | 0.0037 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0048 +- 0.0013 [worst 0.0068] | 0.0068 |
| shots_total | 17.0333 +- 0.0333 [worst 17.0667] | 17.0667 |
| destroyed_value | 1664.6583 +- 158.2723 [worst 1416.8667] | 1416.8667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
