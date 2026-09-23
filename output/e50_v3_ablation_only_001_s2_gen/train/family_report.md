# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 02:01:27

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5778 | n/a | 0.1673 | 100.8064 | 0.004 | 17.1 | 1737.8 | `03de6598f9ee` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6070 | n/a | 0.1537 | 96.7106 | 0.004 | 18.0 | 1651.8 | `89279305ef90` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6071 | n/a | 0.0574 | 105.7432 | 0.004 | 18.0 | 1897.1 | `c99c8744a2bc` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6739 | n/a | 0.1168 | 78.1926 | 0.004 | 17.1 | 1345.4 | `8884c9b3e392` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6497 | n/a | 0.2630 | 103.7477 | 0.004 | 18.0 | 1720.1 | `3f2bc3c92ee5` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5895 | n/a | 0.1196 | 105.5405 | 0.004 | 17.0 | 1799.9 | `9332342bc532` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6102 | n/a | 0.1118 | 94.9662 | 0.004 | 17.0 | 1655.1 | `fab66fab3d5a` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6208 | n/a | 0.1630 | 108.4330 | 0.004 | 18.0 | 1987.2 | `326410354b27` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6095 | n/a | 0.1021 | 97.9241 | 0.004 | 18.0 | 1705.4 | `b31736c3a89a` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6147 | n/a | 0.1593 | 107.7064 | 0.004 | 18.0 | 1946.3 | `a9e50794bdf6` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5863 | n/a | 0.1706 | 104.9882 | 0.004 | 17.0 | 1810.6 | `c8fe20ed7eae` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6420 | n/a | 0.2667 | 83.2950 | 0.004 | 17.0 | 1430.8 | `29d9ced3442a` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6612 | n/a | 0.1513 | 81.5760 | 0.004 | 17.0 | 1407.4 | `f2ebf06ad1d8` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5833 | n/a | 0.0621 | 100.3363 | 0.004 | 17.1 | 1733.0 | `8e971dae0ad2` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6135 | n/a | 0.2667 | 101.9368 | 0.004 | 18.0 | 1666.6 | `b400d9163a8e` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6219 | n/a | 0.1635 | 89.6418 | 0.004 | 17.9 | 1623.6 | `d9ebc304e939` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6023 | n/a | 0.1148 | 92.5046 | 0.004 | 18.0 | 1684.5 | `5a395dfac16e` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5590 | n/a | 0.1648 | 92.0334 | 0.004 | 18.0 | 1661.0 | `73157c1827cb` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5923 | n/a | 0.1706 | 97.3768 | 0.004 | 17.0 | 1525.9 | `513625476fb5` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5713 | n/a | 0.1074 | 110.4110 | 0.004 | 18.0 | 1986.8 | `fbe30ce6d16b` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6110 | n/a | 0.1481 | 105.9774 | 0.004 | 18.0 | 1853.4 | `57e4d15da73e` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6020 | n/a | 0.0619 | 103.5416 | 0.004 | 17.2 | 1771.0 | `12d169c83273` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6565 | n/a | 0.2479 | 86.2928 | 0.004 | 16.0 | 1287.9 | `aa8211a97d96` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5794 | n/a | 0.0519 | 108.7905 | 0.004 | 18.0 | 1974.2 | `8bf8d4f94e83` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6101 +- 0.0288 [worst 0.6739] | 0.6739 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1484 +- 0.0625 [worst 0.2667] | 0.2667 |
| ammo_efficiency | 98.2697 +- 9.0276 [worst 78.1926] | 78.1926 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0044] | 0.0044 |
| latency_p90 | 0.0043 +- 0.0008 [worst 0.0075] | 0.0075 |
| shots_total | 17.5167 +- 0.5580 [worst 18.0000] | 18.0000 |
| destroyed_value | 1702.6167 +- 192.5737 [worst 1287.9000] | 1287.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
