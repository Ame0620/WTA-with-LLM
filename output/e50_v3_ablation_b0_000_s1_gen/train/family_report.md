# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:52:40

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5903 | n/a | 0.1556 | 91.9243 | 0.004 | 18.0 | 1686.2 | `119e0bc0ab0a` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6625 | n/a | 0.1059 | 82.7680 | 0.003 | 17.0 | 1418.6 | `8aa07bcb5bb8` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.7096 | n/a | 0.1611 | 77.6813 | 0.003 | 18.0 | 1401.8 | `8e565e3adbc5` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6966 | n/a | 0.1176 | 73.5566 | 0.003 | 17.0 | 1252.0 | `5d77115dc8e8` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.7030 | n/a | 0.2863 | 85.7918 | 0.004 | 17.0 | 1458.3 | `20c85bfc9e2f` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6100 | n/a | 0.1111 | 95.0406 | 0.003 | 18.0 | 1710.2 | `7418c6001092` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6163 | n/a | 0.1176 | 94.4848 | 0.003 | 17.0 | 1629.4 | `2685f6dd2de2` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6441 | n/a | 0.0519 | 103.3865 | 0.003 | 18.0 | 1865.5 | `4639638f8fea` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6556 | n/a | 0.1196 | 90.3618 | 0.004 | 17.0 | 1503.9 | `47bcf12a78df` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6534 | n/a | 0.1630 | 97.2756 | 0.003 | 18.0 | 1750.5 | `fb6a6d3f2d77` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6362 | n/a | 0.1630 | 88.0376 | 0.003 | 18.0 | 1592.4 | `bc4aeeab2e6e` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6105 | n/a | 0.1074 | 85.7298 | 0.003 | 18.0 | 1556.9 | `225ca6058f3b` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.7072 | n/a | 0.2056 | 66.1991 | 0.004 | 18.0 | 1216.2 | `6ae862285639` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5967 | n/a | 0.0000 | 93.3039 | 0.003 | 18.0 | 1677.1 | `a5712b1f3ff5` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6514 | n/a | 0.2216 | 87.3824 | 0.003 | 17.0 | 1503.3 | `a6b0e291217f` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6642 | n/a | 0.1157 | 82.7931 | 0.003 | 17.0 | 1442.0 | `a966a5547cf8` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6257 | n/a | 0.0611 | 87.4555 | 0.004 | 18.0 | 1585.6 | `03e1f0ee1a9f` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5760 | n/a | 0.2148 | 88.2920 | 0.003 | 18.0 | 1596.8 | `5af0e3574230` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6583 | n/a | 0.1667 | 75.0069 | 0.003 | 17.0 | 1279.1 | `25fe7ea6dda0` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6248 | n/a | 0.1093 | 96.7169 | 0.003 | 18.0 | 1739.0 | `6498633056a2` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6722 | n/a | 0.1569 | 91.3745 | 0.003 | 17.0 | 1561.7 | `e43c29db81de` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6353 | n/a | 0.0519 | 90.9046 | 0.003 | 18.0 | 1622.7 | `05033d778665` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6584 | n/a | 0.1569 | 74.1079 | 0.003 | 17.0 | 1280.6 | `815c362398c0` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6781 | n/a | 0.0000 | 83.7602 | 0.003 | 18.0 | 1510.8 | `0c20812ec074` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6474 +- 0.0361 [worst 0.7096] | 0.7096 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1300 +- 0.0663 [worst 0.2863] | 0.2863 |
| ammo_efficiency | 86.8057 +- 8.5648 [worst 66.1991] | 66.1991 |
| latency_p50 | 0.0031 +- 0.0003 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0035 +- 0.0009 [worst 0.0074] | 0.0074 |
| shots_total | 17.5833 +- 0.4930 [worst 18.0000] | 18.0000 |
| destroyed_value | 1535.0250 +- 165.6834 [worst 1216.1667] | 1216.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
