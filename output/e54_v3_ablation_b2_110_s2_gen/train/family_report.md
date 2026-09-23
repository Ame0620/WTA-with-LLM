# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:15:00

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5331 | n/a | 0.1056 | 111.6875 | 0.003 | 18.0 | 1921.6 | `c6858ca9ca1f` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6357 | n/a | 0.1704 | 89.9932 | 0.003 | 18.0 | 1531.2 | `8317cb47d3f7` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6616 | n/a | 0.1667 | 90.6519 | 0.003 | 18.0 | 1634.0 | `b8f62c524adc` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6598 | n/a | 0.0537 | 76.3159 | 0.003 | 18.0 | 1403.5 | `f90c3fb5939d` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6644 | n/a | 0.2455 | 98.1766 | 0.003 | 16.6 | 1648.0 | `ac8a8cf90f9f` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5369 | n/a | 0.0537 | 112.7841 | 0.003 | 18.0 | 2030.5 | `5af071a61387` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6514 | n/a | 0.1593 | 80.3558 | 0.003 | 18.0 | 1480.4 | `1adad3dec9a7` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6631 | n/a | 0.1593 | 96.2855 | 0.003 | 18.0 | 1765.6 | `78b8b812cd71` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6199 | n/a | 0.1481 | 102.6672 | 0.003 | 18.0 | 1659.9 | `25bf7df4970a` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6017 | n/a | 0.0611 | 117.2797 | 0.003 | 18.0 | 2012.0 | `7f444ee7afa2` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6191 | n/a | 0.1593 | 91.2702 | 0.003 | 18.0 | 1667.4 | `1749e6eeb5c3` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6534 | n/a | 0.2519 | 76.9604 | 0.003 | 18.0 | 1385.2 | `7602069fc1f5` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6682 | n/a | 0.2093 | 76.7542 | 0.003 | 18.0 | 1378.2 | `ce1576968495` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5604 | n/a | 0.0537 | 99.7534 | 0.003 | 18.0 | 1828.3 | `794295342672` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6266 | n/a | 0.2667 | 90.3417 | 0.003 | 18.0 | 1610.0 | `c2d4eecc6bac` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6357 | n/a | 0.2204 | 86.4901 | 0.003 | 18.0 | 1564.2 | `4ba7a349c95e` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5381 | n/a | 0.0556 | 107.4870 | 0.003 | 18.0 | 1956.6 | `88e1420e6fd0` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5880 | n/a | 0.2093 | 85.4329 | 0.003 | 18.0 | 1551.6 | `5ce65879f4db` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6148 | n/a | 0.2500 | 86.0178 | 0.003 | 18.0 | 1441.8 | `a9c2b7253bb9` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6012 | n/a | 0.1037 | 101.3980 | 0.003 | 18.0 | 1848.4 | `7ceb6cbc9255` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6659 | n/a | 0.1944 | 87.7663 | 0.003 | 18.0 | 1591.5 | `7659366751b6` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6052 | n/a | 0.1019 | 97.1528 | 0.003 | 18.0 | 1756.8 | `d9687d750508` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6626 | n/a | 0.2333 | 70.2363 | 0.003 | 18.0 | 1264.8 | `0118321c01f9` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6356 | n/a | 0.0981 | 93.5057 | 0.003 | 18.0 | 1710.3 | `ae468915ea5a` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6209 +- 0.0423 [worst 0.6682] | 0.6682 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1554 +- 0.0701 [worst 0.2667] | 0.2667 |
| ammo_efficiency | 92.7819 +- 12.0443 [worst 70.2363] | 70.2363 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0033 +- 0.0005 [worst 0.0058] | 0.0058 |
| shots_total | 17.9431 +- 0.2731 [worst 18.0000] | 18.0000 |
| destroyed_value | 1651.7444 +- 204.6596 [worst 1264.8333] | 1264.8333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
