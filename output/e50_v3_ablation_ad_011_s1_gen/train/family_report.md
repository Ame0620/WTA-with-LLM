# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:53:55

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5614 | n/a | 0.1111 | 99.8550 | 0.004 | 18.0 | 1805.3 | `7f5f3ed40d19` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6146 | n/a | 0.0722 | 90.4864 | 0.004 | 18.0 | 1619.7 | `85b7fab6aa1a` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6599 | n/a | 0.1093 | 90.5009 | 0.004 | 18.0 | 1641.9 | `696357163b94` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6698 | n/a | 0.1111 | 75.1154 | 0.004 | 18.0 | 1362.3 | `66a987c159c3` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6951 | n/a | 0.3259 | 83.1958 | 0.004 | 18.0 | 1496.9 | `89a8b632e4b9` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5598 | n/a | 0.1019 | 107.3335 | 0.004 | 18.0 | 1930.3 | `a0c70b9f58c2` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6389 | n/a | 0.1593 | 85.2026 | 0.004 | 18.0 | 1533.1 | `55d6e7454c69` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6248 | n/a | 0.1148 | 107.7989 | 0.004 | 18.0 | 1966.6 | `9431ae611668` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.5953 | n/a | 0.0130 | 97.4233 | 0.004 | 18.0 | 1767.2 | `ddd908062845` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6210 | n/a | 0.1556 | 105.9574 | 0.004 | 18.0 | 1914.5 | `0d748f662631` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5552 | n/a | 0.1611 | 106.2099 | 0.004 | 18.0 | 1946.7 | `c7b246606e17` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6067 | n/a | 0.1556 | 86.3804 | 0.004 | 18.0 | 1572.0 | `f02d68cd5eb4` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6494 | n/a | 0.1500 | 81.0643 | 0.004 | 18.0 | 1456.4 | `5f43eff6bf3f` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6064 | n/a | 0.2130 | 90.4801 | 0.004 | 18.0 | 1637.1 | `cc99c825cc10` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6345 | n/a | 0.2685 | 87.5061 | 0.004 | 18.0 | 1576.1 | `606f6e40c784` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6636 | n/a | 0.2722 | 80.0043 | 0.004 | 18.0 | 1444.6 | `3047f6c7abfb` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6034 | n/a | 0.1593 | 92.6246 | 0.004 | 18.0 | 1680.0 | `3dd0484140cf` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5589 | n/a | 0.1556 | 90.7404 | 0.004 | 18.0 | 1661.2 | `269ad3880d41` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5905 | n/a | 0.2074 | 85.0144 | 0.004 | 18.0 | 1532.8 | `77b1223f3796` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5820 | n/a | 0.0611 | 107.3508 | 0.004 | 18.0 | 1937.3 | `d268b3180aed` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6425 | n/a | 0.2056 | 94.4612 | 0.004 | 18.0 | 1703.2 | `8a9f3f103a9c` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6286 | n/a | 0.0556 | 91.9993 | 0.004 | 18.0 | 1652.9 | `9e3cb328a78a` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6511 | n/a | 0.3204 | 72.2178 | 0.004 | 18.0 | 1308.1 | `0b909e817193` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6261 | n/a | 0.0556 | 97.6660 | 0.004 | 18.0 | 1755.1 | `6c96384e2ec2` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6183 +- 0.0372 [worst 0.6951] | 0.6951 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1548 +- 0.0811 [worst 0.3259] | 0.3259 |
| ammo_efficiency | 91.9412 +- 10.0402 [worst 72.2178] | 72.2178 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0043 +- 0.0007 [worst 0.0071] | 0.0071 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1662.5569 +- 183.8465 [worst 1308.0667] | 1308.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
