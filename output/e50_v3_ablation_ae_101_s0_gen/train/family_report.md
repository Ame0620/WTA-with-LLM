# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:49:43

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6016 | n/a | 0.1593 | 90.4262 | 0.004 | 18.0 | 1640.0 | `732aa2a03cf4` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6375 | n/a | 0.1722 | 84.1862 | 0.004 | 18.0 | 1523.7 | `23692a8a937b` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6612 | n/a | 0.1056 | 90.6016 | 0.004 | 18.0 | 1635.8 | `77f52a8c3be6` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6615 | n/a | 0.0063 | 91.7829 | 0.004 | 15.2 | 1396.6 | `2db22e256e40` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6712 | n/a | 0.2667 | 89.4639 | 0.004 | 18.0 | 1614.6 | `79a9c30c8468` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5583 | n/a | 0.0667 | 107.9096 | 0.004 | 18.0 | 1936.9 | `10598c6e6737` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6052 | n/a | 0.1259 | 92.6632 | 0.004 | 18.0 | 1676.5 | `f6a7dae6decd` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6883 | n/a | 0.2481 | 89.5413 | 0.004 | 18.0 | 1633.6 | `bcc7baf69ee6` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6569 | n/a | 0.1204 | 83.0610 | 0.004 | 18.0 | 1498.2 | `da311cf564cf` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6548 | n/a | 0.0537 | 97.1765 | 0.004 | 18.0 | 1743.4 | `69ab00537ccc` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5827 | n/a | 0.2093 | 100.6132 | 0.004 | 18.0 | 1826.7 | `9dcc4cef7d7c` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6045 | n/a | 0.2667 | 86.8858 | 0.004 | 18.0 | 1580.8 | `21b5ac9437a5` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6372 | n/a | 0.0800 | 89.1439 | 0.004 | 16.8 | 1507.1 | `df8b7f17f3a8` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5895 | n/a | 0.1093 | 94.8452 | 0.004 | 18.0 | 1707.1 | `defc44185c58` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6387 | n/a | 0.2093 | 86.7237 | 0.004 | 18.0 | 1558.0 | `5a12d998ef9f` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6519 | n/a | 0.1611 | 83.1310 | 0.004 | 18.0 | 1494.6 | `87eacff706e9` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5929 | n/a | 0.0611 | 95.6604 | 0.004 | 18.0 | 1724.5 | `135dd2d390b0` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6190 | n/a | 0.2019 | 79.1652 | 0.004 | 18.0 | 1434.8 | `13b8f871a20b` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5834 | n/a | 0.1556 | 85.7596 | 0.004 | 18.0 | 1559.2 | `ec5e75a049c0` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6416 | n/a | 0.0556 | 92.6798 | 0.004 | 18.0 | 1661.0 | `d8496a540ab5` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6328 | n/a | 0.1574 | 96.2951 | 0.004 | 18.0 | 1749.6 | `79f1f1fc65e2` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6143 | n/a | 0.1037 | 95.7085 | 0.004 | 18.0 | 1716.6 | `c4fc3d4e81be` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6105 | n/a | 0.1510 | 82.1061 | 0.004 | 17.8 | 1460.4 | `490cfa375659` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6212 | n/a | 0.0963 | 97.6564 | 0.004 | 18.0 | 1778.0 | `a0c1225caff6` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6257 +- 0.0318 [worst 0.6883] | 0.6883 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1393 +- 0.0687 [worst 0.2667] | 0.2667 |
| ammo_efficiency | 90.9661 +- 6.5043 [worst 79.1652] | 79.1652 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0043 +- 0.0007 [worst 0.0068] | 0.0068 |
| shots_total | 17.8264 +- 0.5981 [worst 18.0000] | 18.0000 |
| destroyed_value | 1627.3944 +- 129.7011 [worst 1396.5667] | 1396.5667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
