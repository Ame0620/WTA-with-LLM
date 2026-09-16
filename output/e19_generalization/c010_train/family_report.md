# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 14:24:56

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6087 | n/a | 0.2667 | 89.0619 | 0.005 | 18.0 | 1610.7 | `70a37bc784a4` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6182 | n/a | 0.2222 | 88.0222 | 0.006 | 18.0 | 1604.9 | `983979d2efa8` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6490 | n/a | 0.1630 | 93.4863 | 0.006 | 18.0 | 1694.9 | `05c7c2123d09` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6093 | n/a | 0.1407 | 87.6981 | 0.006 | 18.0 | 1611.9 | `62ec34d5f1b5` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6058 | n/a | 0.1333 | 105.3692 | 0.005 | 18.0 | 1935.5 | `8656c8ddf3e7` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5538 | n/a | 0.1056 | 108.0192 | 0.005 | 18.0 | 1956.4 | `3b850510c8a1` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6215 | n/a | 0.1111 | 87.2989 | 0.005 | 18.0 | 1607.2 | `32346d98f988` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6021 | n/a | 0.0759 | 115.7647 | 0.005 | 18.0 | 2085.5 | `dcbcfdc23ab1` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6399 | n/a | 0.1500 | 87.7627 | 0.005 | 18.0 | 1572.7 | `4e45ff683ac1` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6015 | n/a | 0.0833 | 110.6761 | 0.005 | 18.0 | 2012.6 | `2dbe7aba98bd` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5341 | n/a | 0.0944 | 112.8230 | 0.005 | 18.0 | 2039.4 | `656c71c1f5ec` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5773 | n/a | 0.1370 | 93.5702 | 0.005 | 18.0 | 1689.6 | `c18b850726ea` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6236 | n/a | 0.1500 | 85.9809 | 0.005 | 18.0 | 1563.7 | `2a0502725684` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5732 | n/a | 0.0796 | 97.7630 | 0.005 | 18.0 | 1775.2 | `7ef7c8c2edcc` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6318 | n/a | 0.2704 | 88.5420 | 0.005 | 18.0 | 1587.6 | `06d1bfb5f9b9` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6539 | n/a | 0.2148 | 82.1209 | 0.005 | 18.0 | 1486.1 | `0ee663ea099b` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6319 | n/a | 0.2259 | 86.3228 | 0.005 | 18.0 | 1559.1 | `2bba01fc56af` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6165 | n/a | 0.2574 | 79.9343 | 0.005 | 18.0 | 1444.2 | `82960fda1750` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5857 | n/a | 0.1593 | 85.5308 | 0.005 | 18.0 | 1550.8 | `22c9f8434ff5` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5872 | n/a | 0.0907 | 104.9337 | 0.005 | 18.0 | 1913.3 | `b5876a00daf7` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6492 | n/a | 0.1944 | 91.2488 | 0.005 | 18.0 | 1671.4 | `d4cb062cc7d9` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6284 | n/a | 0.1611 | 92.7657 | 0.005 | 18.0 | 1653.8 | `0e8e68886186` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6298 | n/a | 0.1907 | 76.6275 | 0.005 | 18.0 | 1387.8 | `5c6f4295fb9b` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5605 | n/a | 0.0176 | 114.3693 | 0.005 | 17.9 | 2063.1 | `c000759bb0a6` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6080 +- 0.0309 [worst 0.6539] | 0.6539 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1540 +- 0.0650 [worst 0.2704] | 0.2704 |
| ammo_efficiency | 94.4039 +- 11.2459 [worst 76.6275] | 76.6275 |
| latency_p50 | 0.0054 +- 0.0003 [worst 0.0065] | 0.0065 |
| latency_p90 | 0.0073 +- 0.0009 [worst 0.0109] | 0.0109 |
| shots_total | 17.9958 +- 0.0200 [worst 18.0000] | 18.0000 |
| destroyed_value | 1711.5625 +- 203.8305 [worst 1387.8000] | 1387.8000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
