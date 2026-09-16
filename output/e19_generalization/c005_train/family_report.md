# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 14:24:10

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5879 | n/a | 0.2111 | 94.4786 | 0.005 | 18.0 | 1696.3 | `a1e841b2455b` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5984 | n/a | 0.0963 | 92.2245 | 0.005 | 18.0 | 1688.0 | `80e90a2c5606` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6549 | n/a | 0.1926 | 92.5703 | 0.005 | 18.0 | 1666.2 | `4f63e5f953ca` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6489 | n/a | 0.1074 | 79.8199 | 0.005 | 18.0 | 1448.6 | `dbc7956c89c2` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6303 | n/a | 0.1204 | 100.0910 | 0.005 | 18.0 | 1815.3 | `d5b98b80c64f` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5202 | n/a | 0.0519 | 116.7704 | 0.005 | 18.0 | 2103.9 | `56ca03ac26d6` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.5759 | n/a | 0.0537 | 97.6434 | 0.006 | 18.0 | 1800.7 | `42349fe8c763` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6385 | n/a | 0.1611 | 103.5968 | 0.005 | 18.0 | 1894.8 | `0d7ea85792db` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6219 | n/a | 0.1537 | 89.5339 | 0.005 | 18.0 | 1651.3 | `ab3372bdf1c9` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6245 | n/a | 0.0759 | 104.1071 | 0.005 | 18.0 | 1896.5 | `55f292c4a9e2` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5446 | n/a | 0.0907 | 108.5745 | 0.005 | 18.0 | 1993.5 | `c7be1064f6b1` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6348 | n/a | 0.2519 | 81.0038 | 0.005 | 18.0 | 1459.9 | `1976ea6ad6de` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6141 | n/a | 0.1519 | 89.0593 | 0.005 | 18.0 | 1603.0 | `7de456d24c87` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6161 | n/a | 0.1037 | 88.4535 | 0.005 | 18.0 | 1596.6 | `c79b19406efe` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.5920 | n/a | 0.2167 | 97.3016 | 0.005 | 18.0 | 1759.2 | `c377d2590ce7` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6493 | n/a | 0.2222 | 83.0526 | 0.005 | 18.0 | 1506.1 | `fe892fe08087` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6123 | n/a | 0.2611 | 90.2721 | 0.006 | 18.0 | 1642.3 | `2cc11e47ef3b` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5506 | n/a | 0.1370 | 92.3205 | 0.005 | 18.0 | 1692.4 | `2c3ef30ef8f2` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5726 | n/a | 0.2093 | 85.4003 | 0.005 | 18.0 | 1599.8 | `4aa163b4b4ca` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6378 | n/a | 0.1981 | 93.2356 | 0.005 | 18.0 | 1678.8 | `b679a2c17686` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6416 | n/a | 0.1963 | 94.9373 | 0.005 | 18.0 | 1707.3 | `c5ba4189b76e` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5937 | n/a | 0.1056 | 100.1591 | 0.005 | 18.0 | 1808.1 | `1faba76a4ec5` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5972 | n/a | 0.1537 | 81.3008 | 0.005 | 18.0 | 1510.0 | `9f791407a9ac` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6133 | n/a | 0.0630 | 99.9546 | 0.005 | 18.0 | 1815.4 | `af6cba234338` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6071 +- 0.0346 [worst 0.6549] | 0.6549 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1494 +- 0.0617 [worst 0.2611] | 0.2611 |
| ammo_efficiency | 93.9942 +- 8.8591 [worst 79.8199] | 79.8199 |
| latency_p50 | 0.0052 +- 0.0002 [worst 0.0059] | 0.0059 |
| latency_p90 | 0.0074 +- 0.0017 [worst 0.0154] | 0.0154 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1709.7458 +- 159.1275 [worst 1448.5667] | 1448.5667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
