# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:11:55

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5624 | n/a | 0.1611 | 99.2193 | 0.003 | 18.0 | 1801.2 | `7bf263f1b716` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6258 | n/a | 0.1315 | 87.6343 | 0.003 | 18.0 | 1572.6 | `b8c1726ae9a3` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6186 | n/a | 0.1111 | 102.8436 | 0.003 | 18.0 | 1841.6 | `e6a46ae05188` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6694 | n/a | 0.1187 | 85.0354 | 0.003 | 16.0 | 1364.2 | `12c250a5331a` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6252 | n/a | 0.1852 | 100.9032 | 0.003 | 18.0 | 1840.4 | `be3ec6660149` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5384 | n/a | 0.1111 | 111.6778 | 0.003 | 18.0 | 2024.0 | `2eb6768676d4` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6586 | n/a | 0.1750 | 89.3731 | 0.003 | 16.0 | 1449.5 | `8809dfce3b7c` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6105 | n/a | 0.0549 | 118.8957 | 0.003 | 17.0 | 2041.5 | `91e9e4af2330` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6298 | n/a | 0.2039 | 105.5239 | 0.003 | 17.0 | 1616.8 | `459ce89664e0` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6225 | n/a | 0.1611 | 105.5954 | 0.003 | 18.0 | 1907.0 | `19af9560a39a` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5832 | n/a | 0.2204 | 100.9956 | 0.003 | 18.0 | 1824.5 | `c858725f53a9` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6280 | n/a | 0.2500 | 81.3819 | 0.003 | 18.0 | 1487.0 | `a6b4de7b006c` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6351 | n/a | 0.1519 | 83.5811 | 0.003 | 18.0 | 1515.7 | `48055bac3e82` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5778 | n/a | 0.0685 | 97.0231 | 0.003 | 18.0 | 1755.9 | `c302a76ba3a6` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6326 | n/a | 0.2941 | 103.1171 | 0.003 | 17.0 | 1584.3 | `3548f5e80ca7` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6809 | n/a | 0.3241 | 76.0420 | 0.003 | 18.0 | 1370.1 | `24d597f01d25` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5518 | n/a | 0.1000 | 103.8466 | 0.003 | 18.0 | 1898.4 | `62ab23791905` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5614 | n/a | 0.2611 | 90.4521 | 0.003 | 18.0 | 1651.6 | `469dc139119b` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6145 | n/a | 0.2741 | 87.1629 | 0.003 | 18.0 | 1442.8 | `ace69e167662` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5713 | n/a | 0.1074 | 110.4110 | 0.003 | 18.0 | 1986.8 | `fbe30ce6d16b` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6287 | n/a | 0.2074 | 98.0357 | 0.003 | 18.0 | 1769.0 | `e690b491f90c` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6027 | n/a | 0.1109 | 101.5336 | 0.003 | 17.1 | 1767.8 | `f905886e9bd6` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6110 | n/a | 0.1796 | 86.6225 | 0.003 | 18.0 | 1458.3 | `552765ec3691` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5799 | n/a | 0.0000 | 109.1218 | 0.003 | 18.0 | 1971.9 | `13c1f304e987` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6092 +- 0.0360 [worst 0.6809] | 0.6809 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1651 +- 0.0780 [worst 0.3241] | 0.3241 |
| ammo_efficiency | 97.3345 +- 10.6874 [worst 76.0420] | 76.0420 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0033 +- 0.0005 [worst 0.0058] | 0.0058 |
| shots_total | 17.6722 +- 0.6182 [worst 18.0000] | 18.0000 |
| destroyed_value | 1705.9625 +- 210.5840 [worst 1364.2333] | 1364.2333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
