# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:53:17

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6711 | n/a | 0.2722 | 75.1973 | 0.004 | 18.0 | 1353.7 | `b4d2c70b7139` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6242 | n/a | 0.1779 | 90.3650 | 0.004 | 17.4 | 1579.6 | `308fdc471c69` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6475 | n/a | 0.1037 | 93.8403 | 0.004 | 18.0 | 1702.0 | `d3157fb21203` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6497 | n/a | 0.1111 | 79.9427 | 0.004 | 18.0 | 1445.1 | `854474367bfd` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6933 | n/a | 0.2667 | 82.5638 | 0.004 | 18.0 | 1505.7 | `4ae00cab6cbe` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5805 | n/a | 0.0519 | 103.1223 | 0.004 | 18.0 | 1839.6 | `1f06520bc1b5` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.5766 | n/a | 0.0593 | 99.7135 | 0.004 | 18.0 | 1797.6 | `1019d290e40b` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6608 | n/a | 0.2130 | 96.6744 | 0.004 | 18.0 | 1777.9 | `26c79c80d052` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6595 | n/a | 0.1593 | 82.3020 | 0.004 | 18.0 | 1487.1 | `d2cacb4e952c` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6595 | n/a | 0.1056 | 94.7697 | 0.004 | 18.0 | 1720.1 | `7013251951fa` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6135 | n/a | 0.2093 | 92.3983 | 0.004 | 18.0 | 1691.9 | `b587b7e5a172` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6403 | n/a | 0.2481 | 79.7998 | 0.004 | 18.0 | 1437.5 | `f4958fa85397` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6543 | n/a | 0.1593 | 79.1597 | 0.004 | 18.0 | 1436.2 | `38e70a886d90` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6313 | n/a | 0.1148 | 85.3631 | 0.004 | 18.0 | 1533.5 | `dde3f8220e64` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6771 | n/a | 0.2648 | 77.2803 | 0.004 | 18.0 | 1392.2 | `12ce42d8e3ce` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6357 | n/a | 0.1389 | 85.5075 | 0.004 | 18.0 | 1564.3 | `613c84af1b2c` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6037 | n/a | 0.1093 | 92.8926 | 0.004 | 18.0 | 1678.7 | `0430af6a75b5` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6163 | n/a | 0.1963 | 79.6918 | 0.004 | 18.0 | 1444.8 | `7f6c3214dd29` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6173 | n/a | 0.2185 | 79.4041 | 0.004 | 18.0 | 1432.4 | `e495c51d6d6d` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6112 | n/a | 0.1056 | 99.6353 | 0.004 | 18.0 | 1801.9 | `e6cb06eb6d82` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6730 | n/a | 0.2093 | 86.0488 | 0.004 | 18.0 | 1557.7 | `aa86aff6c5be` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5981 | n/a | 0.0593 | 99.5058 | 0.004 | 18.0 | 1788.3 | `aac72df4cdaa` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6286 | n/a | 0.2222 | 76.5833 | 0.004 | 18.0 | 1392.3 | `69d788aca54c` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6233 | n/a | 0.0537 | 98.1015 | 0.004 | 18.0 | 1768.4 | `e82fee32b7d0` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6353 +- 0.0298 [worst 0.6933] | 0.6933 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1596 +- 0.0705 [worst 0.2722] | 0.2722 |
| ammo_efficiency | 87.9110 +- 8.6143 [worst 75.1973] | 75.1973 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0042 +- 0.0007 [worst 0.0069] | 0.0069 |
| shots_total | 17.9750 +- 0.1199 [worst 18.0000] | 18.0000 |
| destroyed_value | 1588.6833 +- 154.7862 [worst 1353.7000] | 1353.7000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
