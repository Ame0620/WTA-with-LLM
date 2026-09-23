# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:06:59

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5482 | n/a | 0.1481 | 107.9337 | 0.003 | 18.0 | 1859.7 | `32da32f99534` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6138 | n/a | 0.2211 | 98.5481 | 0.003 | 17.0 | 1623.2 | `78df45ad4e51` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.5987 | n/a | 0.0556 | 108.8645 | 0.003 | 18.0 | 1937.6 | `e98be6866a60` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6062 | n/a | 0.0370 | 98.6575 | 0.003 | 16.1 | 1624.8 | `84c1a8130982` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6033 | n/a | 0.1078 | 112.3531 | 0.003 | 17.0 | 1947.8 | `17752766899b` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5119 | n/a | 0.0519 | 117.9849 | 0.003 | 18.0 | 2140.1 | `f2633cb6fc44` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6315 | n/a | 0.2056 | 85.8257 | 0.003 | 18.0 | 1564.7 | `b6ed404bb73e` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6342 | n/a | 0.1167 | 105.4784 | 0.003 | 18.0 | 1916.9 | `686e957fea1d` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.5949 | n/a | 0.0621 | 111.5842 | 0.003 | 17.2 | 1769.0 | `27b4c63b1be5` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.5908 | n/a | 0.1481 | 125.5952 | 0.003 | 18.0 | 2067.1 | `10a9458fadfd` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5619 | n/a | 0.1630 | 103.1964 | 0.003 | 18.0 | 1917.5 | `ddbe84e58d20` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6122 | n/a | 0.1981 | 85.4167 | 0.003 | 18.0 | 1550.0 | `39a262b76f2c` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6735 | n/a | 0.2328 | 84.3257 | 0.003 | 16.0 | 1356.4 | `03f373d3c08b` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5635 | n/a | 0.0603 | 104.1706 | 0.003 | 17.1 | 1815.6 | `f5cc73eff868` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6365 | n/a | 0.3093 | 91.1821 | 0.003 | 18.0 | 1567.4 | `29c3815b78a3` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6724 | n/a | 0.3630 | 78.4316 | 0.003 | 18.0 | 1406.7 | `c67da0e214a9` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5587 | n/a | 0.1500 | 102.3693 | 0.003 | 18.0 | 1869.4 | `26f11851376f` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5315 | n/a | 0.1315 | 99.1656 | 0.003 | 18.0 | 1764.5 | `c57c2dd4aff2` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6018 | n/a | 0.2407 | 89.6776 | 0.003 | 18.0 | 1490.4 | `eed44e181ad3` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5933 | n/a | 0.0585 | 109.6251 | 0.003 | 17.1 | 1884.9 | `41758a490a33` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6311 | n/a | 0.2121 | 100.6608 | 0.003 | 17.3 | 1757.6 | `ac8639ce17eb` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5820 | n/a | 0.1019 | 102.9617 | 0.003 | 18.0 | 1860.3 | `c797aae646a9` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6131 | n/a | 0.2305 | 82.4587 | 0.003 | 17.6 | 1450.6 | `f73b3158eee1` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6019 | n/a | 0.1039 | 108.3649 | 0.003 | 17.0 | 1868.5 | `b09ef79856c5` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5986 +- 0.0386 [worst 0.6735] | 0.6735 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1546 +- 0.0840 [worst 0.3630] | 0.3630 |
| ammo_efficiency | 100.6180 +- 11.6438 [worst 78.4316] | 78.4316 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0033 +- 0.0005 [worst 0.0058] | 0.0058 |
| shots_total | 17.5597 +- 0.6029 [worst 18.0000] | 18.0000 |
| destroyed_value | 1750.4403 +- 206.9411 [worst 1356.4000] | 1356.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
