# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:57:21

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5903 | n/a | 0.1556 | 91.9243 | 0.004 | 18.0 | 1686.2 | `119e0bc0ab0a` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6407 | n/a | 0.1074 | 84.2115 | 0.003 | 18.0 | 1510.3 | `8df3580fbe26` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6963 | n/a | 0.1148 | 81.2728 | 0.003 | 18.0 | 1466.3 | `56b8b176bfae` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6744 | n/a | 0.0500 | 73.4933 | 0.003 | 18.0 | 1343.3 | `78ace1075077` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6928 | n/a | 0.2019 | 82.9264 | 0.004 | 18.0 | 1508.1 | `5b4b85c43043` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6100 | n/a | 0.1111 | 95.0406 | 0.003 | 18.0 | 1710.2 | `7418c6001092` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6165 | n/a | 0.1630 | 89.2964 | 0.003 | 18.0 | 1628.5 | `5042f77d6a26` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6441 | n/a | 0.0519 | 103.3865 | 0.003 | 18.0 | 1865.5 | `4639638f8fea` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6193 | n/a | 0.1019 | 93.7024 | 0.004 | 18.0 | 1662.4 | `c7ff00503f40` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6337 | n/a | 0.1056 | 102.3898 | 0.003 | 18.0 | 1850.0 | `fc23001c6ef1` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6362 | n/a | 0.1630 | 88.0376 | 0.003 | 18.0 | 1592.4 | `bc4aeeab2e6e` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6105 | n/a | 0.1074 | 85.7298 | 0.003 | 18.0 | 1556.9 | `225ca6058f3b` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.7072 | n/a | 0.2056 | 66.1991 | 0.004 | 18.0 | 1216.2 | `6ae862285639` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5957 | n/a | 0.0000 | 93.2719 | 0.003 | 18.0 | 1681.3 | `bf510aafc2f1` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6409 | n/a | 0.2167 | 85.4670 | 0.003 | 18.0 | 1548.6 | `5df0e06bb06b` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6551 | n/a | 0.0667 | 82.0485 | 0.003 | 18.0 | 1480.9 | `5a00d874f21c` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6257 | n/a | 0.0611 | 87.4555 | 0.003 | 18.0 | 1585.6 | `03e1f0ee1a9f` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5780 | n/a | 0.2037 | 86.6039 | 0.003 | 18.0 | 1589.4 | `c5e5e03da191` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6396 | n/a | 0.1574 | 74.5004 | 0.003 | 18.0 | 1348.8 | `080535257385` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6248 | n/a | 0.1093 | 96.7169 | 0.003 | 18.0 | 1739.0 | `6498633056a2` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6536 | n/a | 0.1352 | 92.2679 | 0.003 | 18.0 | 1650.5 | `1f387e1eade0` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6353 | n/a | 0.0519 | 90.9046 | 0.003 | 18.0 | 1622.7 | `05033d778665` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6583 | n/a | 0.1981 | 69.6841 | 0.003 | 18.0 | 1281.1 | `8cba58ea5528` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6551 | n/a | 0.0000 | 89.7065 | 0.003 | 18.0 | 1619.1 | `fc91308223de` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6389 +- 0.0317 [worst 0.7072] | 0.7072 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1183 +- 0.0624 [worst 0.2167] | 0.2167 |
| ammo_efficiency | 86.9266 +- 9.0983 [worst 66.1991] | 66.1991 |
| latency_p50 | 0.0032 +- 0.0003 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0035 +- 0.0008 [worst 0.0071] | 0.0071 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1572.6375 +- 158.1249 [worst 1216.1667] | 1216.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
