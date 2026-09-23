# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:59:45

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6322 | n/a | 0.2093 | 83.3617 | 0.004 | 18.0 | 1514.1 | `97bdd9fdd97d` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6625 | n/a | 0.0608 | 82.0008 | 0.003 | 17.0 | 1418.4 | `2ab2ba8be8f8` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.7260 | n/a | 0.2056 | 73.2467 | 0.003 | 18.0 | 1322.8 | `a70a74e63745` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.7407 | n/a | 0.2255 | 61.8885 | 0.003 | 17.0 | 1070.1 | `8a9c80926521` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.7099 | n/a | 0.1352 | 76.2848 | 0.004 | 18.0 | 1424.5 | `e30819137ff7` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6008 | n/a | 0.1426 | 96.9180 | 0.003 | 18.0 | 1750.4 | `2df9a58d1e3f` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6163 | n/a | 0.1093 | 89.5237 | 0.003 | 18.0 | 1629.1 | `3ff725b9d35d` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6444 | n/a | 0.0519 | 103.2598 | 0.003 | 18.0 | 1863.8 | `a2a348d92866` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6465 | n/a | 0.0667 | 86.7451 | 0.003 | 18.0 | 1543.8 | `798b008e7bd3` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6687 | n/a | 0.1630 | 92.3599 | 0.003 | 18.0 | 1673.3 | `ce6fadfa3518` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6697 | n/a | 0.1750 | 88.5437 | 0.003 | 16.0 | 1445.8 | `d393ec15ce2e` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6360 | n/a | 0.2000 | 80.3009 | 0.003 | 18.0 | 1455.0 | `bdbf5cabe700` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.7167 | n/a | 0.1630 | 63.2296 | 0.003 | 18.0 | 1176.6 | `ead60e30934f` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5936 | n/a | 0.0519 | 94.0495 | 0.004 | 18.0 | 1690.1 | `9e8030c845ea` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6545 | n/a | 0.2216 | 86.6751 | 0.003 | 17.0 | 1489.6 | `f053faf079ba` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6852 | n/a | 0.1157 | 77.8454 | 0.003 | 17.0 | 1351.7 | `ff0bdbc02726` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6085 | n/a | 0.0611 | 91.7316 | 0.003 | 18.0 | 1658.6 | `512e7a7d2f42` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6888 | n/a | 0.2759 | 66.0436 | 0.004 | 18.0 | 1172.0 | `70c8fc7cb831` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6589 | n/a | 0.2176 | 74.1849 | 0.003 | 17.0 | 1276.6 | `ecd358f7c851` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6440 | n/a | 0.1093 | 91.7236 | 0.003 | 18.0 | 1650.0 | `37fe12f1769a` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6745 | n/a | 0.1569 | 91.0343 | 0.003 | 17.0 | 1550.6 | `c65d9ca5dd94` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6192 | n/a | 0.0593 | 94.9769 | 0.004 | 18.0 | 1694.4 | `22b337fc906e` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6554 | n/a | 0.1741 | 70.7352 | 0.003 | 18.0 | 1292.0 | `ef73e8d5805a` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.7245 | n/a | 0.0000 | 71.7631 | 0.003 | 18.0 | 1293.3 | `fdb10169f622` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6616 +- 0.0402 [worst 0.7407] | 0.7407 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1396 +- 0.0698 [worst 0.2759] | 0.2759 |
| ammo_efficiency | 82.8511 +- 11.0457 [worst 61.8885] | 61.8885 |
| latency_p50 | 0.0032 +- 0.0003 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0035 +- 0.0008 [worst 0.0069] | 0.0069 |
| shots_total | 17.6667 +- 0.5528 [worst 18.0000] | 18.0000 |
| destroyed_value | 1475.2750 +- 199.6854 [worst 1070.0667] | 1070.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
