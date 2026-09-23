# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:57:58

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5798 | n/a | 0.1637 | 99.7898 | 0.004 | 17.1 | 1729.7 | `77e49070c8f3` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6589 | n/a | 0.1315 | 78.9233 | 0.004 | 18.0 | 1433.5 | `30fec07bf127` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6408 | n/a | 0.1056 | 95.9824 | 0.004 | 18.0 | 1734.2 | `33461edffc88` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6288 | n/a | 0.1093 | 83.7935 | 0.004 | 18.0 | 1531.5 | `e575efa35f49` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6421 | n/a | 0.1987 | 99.2538 | 0.004 | 17.4 | 1757.5 | `566955ad046f` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5149 | n/a | 0.0463 | 117.9342 | 0.004 | 18.0 | 2127.1 | `bd975faacc18` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6507 | n/a | 0.1725 | 86.5573 | 0.004 | 17.0 | 1483.2 | `e2b044e21919` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6085 | n/a | 0.0588 | 118.8732 | 0.004 | 17.0 | 2052.0 | `42b92f0b218e` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6850 | n/a | 0.1863 | 85.4877 | 0.004 | 16.2 | 1375.8 | `20a66b5126d5` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6079 | n/a | 0.1074 | 109.4439 | 0.004 | 18.0 | 1980.4 | `b29496ce672a` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5699 | n/a | 0.1296 | 104.8643 | 0.004 | 18.0 | 1882.7 | `28d58f8463a8` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6154 | n/a | 0.2056 | 84.0726 | 0.004 | 18.0 | 1537.4 | `e2c3a8f8db5b` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6328 | n/a | 0.1519 | 83.5971 | 0.004 | 18.0 | 1525.4 | `a340422a848a` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6336 | n/a | 0.0556 | 84.3912 | 0.004 | 18.0 | 1523.9 | `d025965ea7bb` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6412 | n/a | 0.2704 | 85.3796 | 0.004 | 18.0 | 1547.2 | `4662e306c047` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6782 | n/a | 0.2667 | 77.0915 | 0.004 | 18.0 | 1381.9 | `52def17ef5d3` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5536 | n/a | 0.1000 | 108.6869 | 0.004 | 17.0 | 1891.0 | `63d94eafeee1` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6219 | n/a | 0.1630 | 78.4865 | 0.004 | 18.0 | 1423.8 | `4b73b2a096e2` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6061 | n/a | 0.2417 | 91.2531 | 0.004 | 16.0 | 1474.5 | `f87110fcbfd1` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5804 | n/a | 0.1088 | 112.8500 | 0.004 | 17.2 | 1944.9 | `3dd22f9b40d1` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6889 | n/a | 0.2019 | 82.0147 | 0.004 | 18.0 | 1481.9 | `856b7f137a4d` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6371 | n/a | 0.1537 | 89.7640 | 0.004 | 18.0 | 1614.8 | `45f07801a2a7` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6847 | n/a | 0.2185 | 65.7385 | 0.004 | 18.0 | 1182.0 | `c2ca2e8c69dd` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6396 | n/a | 0.1056 | 93.5547 | 0.004 | 18.0 | 1691.8 | `cb5f08151d25` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6250 +- 0.0421 [worst 0.6889] | 0.6889 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1522 +- 0.0618 [worst 0.2704] | 0.2704 |
| ammo_efficiency | 92.4077 +- 13.6178 [worst 65.7385] | 65.7385 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0044] | 0.0044 |
| latency_p90 | 0.0043 +- 0.0008 [worst 0.0078] | 0.0078 |
| shots_total | 17.6194 +- 0.5969 [worst 18.0000] | 18.0000 |
| destroyed_value | 1637.8347 +- 236.4425 [worst 1182.0333] | 1182.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
