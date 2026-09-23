# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:49:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5800 | n/a | 0.2111 | 95.7151 | 0.004 | 18.0 | 1728.6 | `b385f0e1b795` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6440 | n/a | 0.1667 | 83.6720 | 0.004 | 18.0 | 1496.4 | `cab3b879f9c8` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6535 | n/a | 0.1667 | 92.5608 | 0.004 | 18.0 | 1672.7 | `ae1fbf5e06ba` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6837 | n/a | 0.1630 | 72.1220 | 0.004 | 18.0 | 1304.9 | `c1a4ab455077` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6704 | n/a | 0.3259 | 89.5371 | 0.004 | 18.0 | 1618.6 | `86478f7d89d8` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5385 | n/a | 0.1037 | 111.9472 | 0.004 | 18.0 | 2023.7 | `e5044f450d35` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6456 | n/a | 0.2111 | 83.5441 | 0.004 | 18.0 | 1504.7 | `aca823852b3e` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6109 | n/a | 0.0741 | 112.2432 | 0.004 | 18.0 | 2039.3 | `4c20986278ac` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6700 | n/a | 0.2093 | 79.4727 | 0.004 | 18.0 | 1441.0 | `216bd447632a` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6215 | n/a | 0.1556 | 105.5752 | 0.004 | 18.0 | 1911.8 | `6fc7b30d9aca` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5720 | n/a | 0.2019 | 102.3089 | 0.004 | 18.0 | 1873.3 | `5384dd51a8e8` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6337 | n/a | 0.2537 | 80.8067 | 0.004 | 18.0 | 1464.3 | `04d885c837a8` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6475 | n/a | 0.1463 | 81.1173 | 0.004 | 18.0 | 1464.1 | `f7399c0c630a` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6064 | n/a | 0.2130 | 90.4801 | 0.004 | 18.0 | 1637.1 | `cc99c825cc10` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6300 | n/a | 0.2667 | 88.1027 | 0.004 | 18.0 | 1595.4 | `f7a6b2e91530` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6662 | n/a | 0.3222 | 79.5986 | 0.004 | 18.0 | 1433.5 | `d0d69c37f15d` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6238 | n/a | 0.2611 | 87.7239 | 0.004 | 18.0 | 1593.6 | `8fc7462ab598` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6265 | n/a | 0.2648 | 77.2455 | 0.004 | 18.0 | 1406.6 | `f873269e283d` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5905 | n/a | 0.2074 | 85.0144 | 0.004 | 18.0 | 1532.8 | `77b1223f3796` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5744 | n/a | 0.1056 | 109.3529 | 0.004 | 18.0 | 1972.9 | `60a2416521b2` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6441 | n/a | 0.2056 | 94.3336 | 0.004 | 18.0 | 1695.6 | `9a7921392926` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5610 | n/a | 0.0148 | 108.0717 | 0.004 | 18.0 | 1953.5 | `9aa8401fd09b` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6140 | n/a | 0.2333 | 79.9498 | 0.004 | 18.0 | 1446.9 | `35096841967d` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5981 | n/a | 0.0537 | 104.6702 | 0.004 | 18.0 | 1886.3 | `b7d8ef6a0c63` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6211 +- 0.0371 [worst 0.6837] | 0.6837 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1890 +- 0.0772 [worst 0.3259] | 0.3259 |
| ammo_efficiency | 91.4652 +- 11.8583 [worst 72.1220] | 72.1220 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0043 +- 0.0007 [worst 0.0068] | 0.0068 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1654.0708 +- 215.5506 [worst 1304.9333] | 1304.9333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
