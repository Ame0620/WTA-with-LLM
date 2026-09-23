# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:52:08

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5945 | n/a | 0.1111 | 92.2422 | 0.004 | 18.0 | 1669.1 | `5969b2660072` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5961 | n/a | 0.1778 | 97.1986 | 0.004 | 18.0 | 1697.6 | `017fbb36521d` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6344 | n/a | 0.1093 | 97.5384 | 0.004 | 18.0 | 1765.2 | `8cd20312f376` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6512 | n/a | 0.1056 | 79.5442 | 0.004 | 18.0 | 1439.2 | `17f6b44dbfc2` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6517 | n/a | 0.2648 | 95.0771 | 0.004 | 18.0 | 1710.1 | `b1cffd8a6035` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5157 | n/a | 0.0481 | 117.4124 | 0.004 | 18.0 | 2123.6 | `6102a2759085` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6129 | n/a | 0.1157 | 95.9695 | 0.004 | 17.0 | 1643.8 | `95b3ceeead77` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6451 | n/a | 0.1648 | 101.7301 | 0.004 | 18.0 | 1860.1 | `35556892033e` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6087 | n/a | 0.0562 | 98.4131 | 0.004 | 17.2 | 1708.7 | `49a50d146051` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6600 | n/a | 0.1074 | 94.8145 | 0.004 | 18.0 | 1717.2 | `ecdd90dfc3ef` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5694 | n/a | 0.1667 | 103.1041 | 0.004 | 18.0 | 1884.6 | `b2895ab91ba8` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6122 | n/a | 0.1229 | 90.7541 | 0.004 | 17.1 | 1550.2 | `73f1aa043c4a` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6291 | n/a | 0.1093 | 84.4399 | 0.004 | 18.0 | 1540.7 | `6b925bb05d62` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5942 | n/a | 0.0593 | 94.6361 | 0.004 | 18.0 | 1687.8 | `2a2f73394fd2` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6364 | n/a | 0.2056 | 86.8527 | 0.004 | 18.0 | 1568.0 | `862827e23742` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6471 | n/a | 0.2111 | 84.2835 | 0.004 | 18.0 | 1515.5 | `ae1c5bf09fa3` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6568 | n/a | 0.2574 | 80.3385 | 0.004 | 18.0 | 1453.9 | `6f01bbd62ae2` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6025 | n/a | 0.1944 | 82.1247 | 0.004 | 18.0 | 1497.0 | `5b23dec629e8` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5953 | n/a | 0.1225 | 95.5253 | 0.004 | 17.1 | 1514.7 | `b70864f31d5b` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6167 | n/a | 0.1019 | 97.9192 | 0.004 | 18.0 | 1776.6 | `fcf1d9019ddd` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6375 | n/a | 0.1630 | 95.7580 | 0.004 | 18.0 | 1727.2 | `426c7635995d` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6066 | n/a | 0.0556 | 97.2044 | 0.004 | 18.0 | 1750.8 | `62fd761160f4` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6273 | n/a | 0.2678 | 77.3009 | 0.004 | 17.9 | 1397.2 | `21e2dd2079e7` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5998 | n/a | 0.0074 | 104.3018 | 0.004 | 18.0 | 1878.4 | `fb79076bf68f` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6167 +- 0.0316 [worst 0.6600] | 0.6600 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1377 +- 0.0694 [worst 0.2678] | 0.2678 |
| ammo_efficiency | 93.5201 +- 8.9832 [worst 77.3009] | 77.3009 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0042 +- 0.0008 [worst 0.0074] | 0.0074 |
| shots_total | 17.8458 +- 0.3388 [worst 18.0000] | 18.0000 |
| destroyed_value | 1669.8819 +- 166.1468 [worst 1397.2333] | 1397.2333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
