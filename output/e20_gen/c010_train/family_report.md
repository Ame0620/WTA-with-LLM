# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-09 20:28:15

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6187 | n/a | 0.2167 | 87.9106 | 0.005 | 18.0 | 1569.5 | `59d7fe536842` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5989 | n/a | 0.1759 | 92.2161 | 0.005 | 18.0 | 1685.8 | `5f49f268d16f` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6333 | n/a | 0.1074 | 98.2739 | 0.005 | 18.0 | 1770.6 | `ca802baf5fdd` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.5982 | n/a | 0.0000 | 96.2336 | 0.006 | 17.0 | 1657.7 | `c1849c9616c7` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6433 | n/a | 0.2648 | 96.0863 | 0.005 | 18.0 | 1751.3 | `5d372b5ce73f` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5238 | n/a | 0.0519 | 115.8980 | 0.005 | 18.0 | 2088.3 | `31afd4520759` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.5961 | n/a | 0.1537 | 92.5455 | 0.005 | 18.0 | 1715.2 | `db1e912923c3` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6136 | n/a | 0.1630 | 110.4831 | 0.005 | 18.0 | 2025.0 | `b46025bbd28a` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6692 | n/a | 0.2074 | 80.7129 | 0.004 | 18.0 | 1444.6 | `9e6156ac5f17` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6350 | n/a | 0.1185 | 102.5930 | 0.004 | 18.0 | 1843.5 | `9f787b187e88` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5632 | n/a | 0.1204 | 105.7440 | 0.004 | 18.0 | 1911.8 | `e0f5ae4e82c8` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5890 | n/a | 0.2037 | 89.7629 | 0.004 | 18.0 | 1642.9 | `56dbceaeee3c` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6307 | n/a | 0.1019 | 84.7073 | 0.004 | 18.0 | 1534.0 | `1e61aba105b9` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5972 | n/a | 0.0667 | 93.8280 | 0.004 | 18.0 | 1675.2 | `20bfa4c976b9` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6504 | n/a | 0.2648 | 83.0349 | 0.004 | 18.0 | 1507.5 | `2b71d499ec85` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.5994 | n/a | 0.1093 | 94.0875 | 0.004 | 18.0 | 1720.3 | `7ff979e5ce77` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5783 | n/a | 0.0815 | 100.0586 | 0.004 | 18.0 | 1786.1 | `c13248ea969f` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5961 | n/a | 0.2093 | 83.9835 | 0.004 | 18.0 | 1521.1 | `401566abcbbb` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5375 | n/a | 0.1074 | 94.8843 | 0.004 | 18.0 | 1731.3 | `d378577e97e7` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5812 | n/a | 0.0963 | 106.7550 | 0.004 | 18.0 | 1941.1 | `6ffea92c337d` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6379 | n/a | 0.1981 | 95.3895 | 0.004 | 18.0 | 1724.9 | `332cb409b042` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6333 | n/a | 0.1519 | 91.8137 | 0.004 | 18.0 | 1631.9 | `96296debea1b` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6050 | n/a | 0.2074 | 81.2145 | 0.004 | 18.0 | 1480.7 | `c6a50320608d` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5886 | n/a | 0.0565 | 111.7325 | 0.004 | 17.1 | 1930.9 | `65bf429caa57` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6049 +- 0.0337 [worst 0.6692] | 0.6692 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1431 +- 0.0679 [worst 0.2648] | 0.2648 |
| ammo_efficiency | 95.4145 +- 9.5114 [worst 80.7129] | 80.7129 |
| latency_p50 | 0.0043 +- 0.0006 [worst 0.0057] | 0.0057 |
| latency_p90 | 0.0055 +- 0.0016 [worst 0.0097] | 0.0097 |
| shots_total | 17.9208 +- 0.2630 [worst 18.0000] | 18.0000 |
| destroyed_value | 1720.4653 +- 168.0766 [worst 1444.6333] | 1444.6333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
