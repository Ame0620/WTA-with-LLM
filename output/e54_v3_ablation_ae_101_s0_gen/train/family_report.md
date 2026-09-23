# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:06:30

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5761 | n/a | 0.1593 | 94.7695 | 0.004 | 18.0 | 1744.8 | `d10893f451bf` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5790 | n/a | 0.1319 | 100.6664 | 0.003 | 17.4 | 1769.3 | `e64b5c6a9939` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6767 | n/a | 0.2074 | 86.7221 | 0.003 | 18.0 | 1561.1 | `63f2cc26945c` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6008 | n/a | 0.0353 | 94.8601 | 0.004 | 17.0 | 1647.2 | `9d84d9d21094` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.5844 | n/a | 0.1037 | 112.1282 | 0.003 | 18.0 | 2040.5 | `8037e533b20f` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5529 | n/a | 0.0852 | 109.3479 | 0.004 | 18.0 | 1960.4 | `7d1f07f7f350` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.5906 | n/a | 0.1407 | 93.9351 | 0.004 | 18.0 | 1738.2 | `2aedd7d87caa` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6028 | n/a | 0.0759 | 113.3509 | 0.004 | 18.0 | 2081.6 | `a0756f1b6547` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.5775 | n/a | 0.1111 | 102.1306 | 0.004 | 18.0 | 1845.1 | `3d9c612d0c0e` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.5886 | n/a | 0.1074 | 113.9018 | 0.004 | 18.0 | 2077.9 | `3438350c9da1` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5556 | n/a | 0.1574 | 110.4960 | 0.004 | 18.0 | 1945.0 | `394d717a7309` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5809 | n/a | 0.1630 | 92.4629 | 0.004 | 18.0 | 1675.3 | `0a88d211761d` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6186 | n/a | 0.1463 | 86.5582 | 0.004 | 18.0 | 1584.4 | `098f4c829722` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5604 | n/a | 0.0692 | 104.8751 | 0.004 | 17.2 | 1828.2 | `6b2507b2e830` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6470 | n/a | 0.2111 | 83.9363 | 0.004 | 18.0 | 1522.1 | `ea21b05119fb` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6393 | n/a | 0.2491 | 92.9979 | 0.004 | 17.9 | 1548.7 | `ff3812563b99` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5617 | n/a | 0.0926 | 102.8104 | 0.004 | 18.0 | 1856.8 | `cb5c93ed0dad` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5182 | n/a | 0.1389 | 99.7089 | 0.004 | 18.0 | 1814.4 | `4382d856daff` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5691 | n/a | 0.1259 | 90.2532 | 0.004 | 18.0 | 1612.8 | `a09c7e49e98a` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5838 | n/a | 0.0593 | 107.3590 | 0.004 | 18.0 | 1929.2 | `489a63b3a229` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6076 | n/a | 0.1574 | 102.9240 | 0.004 | 18.0 | 1869.3 | `661131af05ab` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5967 | n/a | 0.1037 | 99.1986 | 0.004 | 18.0 | 1794.9 | `f71bd48cb690` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5807 | n/a | 0.1296 | 88.3805 | 0.004 | 18.0 | 1572.1 | `1dfcfe3e9f95` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5795 | n/a | 0.0481 | 108.7721 | 0.004 | 18.0 | 1973.8 | `bd3a8ed402f9` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5887 +- 0.0324 [worst 0.6767] | 0.6767 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1254 +- 0.0513 [worst 0.2491] | 0.2491 |
| ammo_efficiency | 99.6894 +- 8.9729 [worst 83.9363] | 83.9363 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0040 +- 0.0005 [worst 0.0065] | 0.0065 |
| shots_total | 17.8972 +- 0.2692 [worst 18.0000] | 18.0000 |
| destroyed_value | 1791.3708 +- 170.1643 [worst 1522.0667] | 1522.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
