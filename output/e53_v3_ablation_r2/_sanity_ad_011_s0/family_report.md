# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 3 (base 7) | solver timelimit 30s
- generated at: 2026-09-22 18:47:37

## Per-instance metrics (mean +- std over 3 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5748 | n/a | 0.1111 | 100.2803 | 0.004 | 18.0 | 1766.3 | `2c1ae71aab50` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5919 | n/a | 0.0926 | 108.2596 | 0.004 | 18.0 | 1876.3 | `53f16293cc1c` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6317 | n/a | 0.1176 | 103.4300 | 0.004 | 17.0 | 1753.3 | `4007b75ff5de` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6600 | n/a | 0.2963 | 84.6729 | 0.004 | 18.0 | 1565.3 | `e7d1384c1593` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6146 +- 0.0334 [worst 0.6600] | 0.6600 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1544 +- 0.0824 [worst 0.2963] | 0.2963 |
| ammo_efficiency | 99.1607 +- 8.8341 [worst 84.6729] | 84.6729 |
| latency_p50 | 0.0038 +- 0.0002 [worst 0.0042] | 0.0042 |
| latency_p90 | 0.0108 +- 0.0119 [worst 0.0314] | 0.0314 |
| shots_total | 17.7500 +- 0.4330 [worst 18.0000] | 18.0000 |
| destroyed_value | 1740.3333 +- 111.7654 [worst 1565.3333] | 1565.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
