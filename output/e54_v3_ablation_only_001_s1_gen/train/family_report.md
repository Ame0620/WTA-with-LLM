# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:12:26

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5600 | n/a | 0.1537 | 99.4561 | 0.004 | 18.0 | 1811.0 | `c0a61768a2ed` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6102 | n/a | 0.2007 | 94.3185 | 0.004 | 17.2 | 1638.2 | `ce7cfd191af6` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6264 | n/a | 0.1094 | 105.5878 | 0.004 | 17.0 | 1803.7 | `66edd2fbdc6f` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6300 | n/a | 0.0021 | 93.6580 | 0.004 | 16.0 | 1526.7 | `5a051f14497c` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6260 | n/a | 0.2148 | 101.1185 | 0.004 | 18.0 | 1836.2 | `1aaab99e65fe` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5234 | n/a | 0.0944 | 115.0674 | 0.004 | 18.0 | 2089.9 | `b367aa5d6afd` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.5963 | n/a | 0.1089 | 97.6770 | 0.004 | 17.1 | 1714.3 | `b4e6c46d6bae` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.5826 | n/a | 0.0648 | 118.8496 | 0.004 | 18.0 | 2187.6 | `1c33c1723f2a` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.5747 | n/a | 0.1352 | 109.2418 | 0.004 | 18.0 | 1857.1 | `c6318dc4be92` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.5828 | n/a | 0.1093 | 115.1020 | 0.004 | 18.0 | 2107.1 | `5e0ee6078ef6` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5447 | n/a | 0.1630 | 108.8579 | 0.004 | 18.0 | 1992.8 | `5d7f8693aae3` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6256 | n/a | 0.2798 | 87.7173 | 0.004 | 17.0 | 1496.3 | `476bb34c6bff` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6567 | n/a | 0.1537 | 79.2016 | 0.004 | 18.0 | 1426.3 | `4e65cbc281ce` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5751 | n/a | 0.0111 | 107.8823 | 0.004 | 16.3 | 1767.3 | `8521f04912fe` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.5998 | n/a | 0.2111 | 94.6774 | 0.004 | 18.0 | 1725.7 | `ef42c71d5f77` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6098 | n/a | 0.1685 | 92.5315 | 0.004 | 18.0 | 1675.6 | `859170e5e238` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5932 | n/a | 0.1019 | 95.1089 | 0.004 | 18.0 | 1723.3 | `feeb6a90fd7f` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5223 | n/a | 0.1259 | 99.2312 | 0.004 | 18.0 | 1799.2 | `ba175734ca20` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5536 | n/a | 0.1593 | 92.8263 | 0.004 | 18.0 | 1670.8 | `9962f2fb890e` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5719 | n/a | 0.0500 | 109.5283 | 0.004 | 18.0 | 1984.0 | `7fa9288a41da` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6048 | n/a | 0.1593 | 103.8724 | 0.004 | 18.0 | 1882.7 | `7e1b06f7c362` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5724 | n/a | 0.1019 | 105.6006 | 0.004 | 18.0 | 1902.6 | `e2de5e861efc` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5835 | n/a | 0.1764 | 86.3002 | 0.004 | 18.0 | 1561.5 | `bebac4f94670` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5910 | n/a | 0.0510 | 112.1799 | 0.004 | 17.0 | 1919.8 | `9265f8f7ab8d` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5882 +- 0.0326 [worst 0.6567] | 0.6567 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1294 +- 0.0647 [worst 0.2798] | 0.2798 |
| ammo_efficiency | 101.0664 +- 9.8668 [worst 79.2016] | 79.2016 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0040 +- 0.0005 [worst 0.0065] | 0.0065 |
| shots_total | 17.6514 +- 0.5877 [worst 18.0000] | 18.0000 |
| destroyed_value | 1795.8167 +- 191.1882 [worst 1426.2667] | 1426.2667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
