# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:55:38

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6734 | n/a | 0.1611 | 74.3143 | 0.003 | 18.0 | 1344.4 | `6cc24b011bd6` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.7053 | n/a | 0.1519 | 67.3553 | 0.003 | 18.0 | 1238.7 | `74a9db69bf48` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.7165 | n/a | 0.2167 | 75.8521 | 0.003 | 18.0 | 1368.9 | `90afb5b9c03b` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6715 | n/a | 0.0056 | 74.4039 | 0.003 | 18.0 | 1355.5 | `b6121708418e` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.7147 | n/a | 0.0685 | 77.8777 | 0.003 | 18.0 | 1401.0 | `d47710b84d41` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6022 | n/a | 0.0500 | 95.0784 | 0.003 | 18.0 | 1744.4 | `51386af25f3d` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6799 | n/a | 0.1593 | 73.0770 | 0.003 | 18.0 | 1359.0 | `d6010d2fde65` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6822 | n/a | 0.0519 | 91.8523 | 0.004 | 18.0 | 1665.7 | `2b7da0fdec63` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.7372 | n/a | 0.1148 | 63.2761 | 0.003 | 18.0 | 1147.7 | `ad82c23212a4` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.7026 | n/a | 0.1019 | 87.7780 | 0.003 | 18.0 | 1502.3 | `117311053584` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6902 | n/a | 0.2611 | 74.1031 | 0.003 | 18.0 | 1356.1 | `2c90203545db` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.7028 | n/a | 0.1537 | 64.7576 | 0.004 | 18.0 | 1187.8 | `72d4e0c2f166` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.7238 | n/a | 0.1574 | 63.7121 | 0.003 | 18.0 | 1147.5 | `d12c4ab21355` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.7003 | n/a | 0.0556 | 69.8901 | 0.003 | 18.0 | 1246.5 | `8e7228e3355b` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6392 | n/a | 0.1000 | 85.7559 | 0.003 | 18.0 | 1555.7 | `eab8d8a11c9f` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.7391 | n/a | 0.1093 | 62.4359 | 0.004 | 18.0 | 1120.1 | `88ac45654fd4` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6966 | n/a | 0.1093 | 70.3319 | 0.003 | 18.0 | 1285.0 | `dddea6ad2a49` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6850 | n/a | 0.1926 | 64.3241 | 0.003 | 18.0 | 1186.5 | `2398c60eb326` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6821 | n/a | 0.1093 | 66.4661 | 0.003 | 18.0 | 1189.9 | `9ab377b1f00f` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.7184 | n/a | 0.1111 | 72.6822 | 0.004 | 18.0 | 1305.1 | `7ed858fd2e39` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6908 | n/a | 0.1537 | 81.4735 | 0.003 | 18.0 | 1473.2 | `0675533742c3` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6737 | n/a | 0.1019 | 81.2206 | 0.003 | 18.0 | 1452.0 | `51566deaeec6` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6934 | n/a | 0.1074 | 63.5360 | 0.003 | 18.0 | 1149.6 | `23d90c862e8b` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.7084 | n/a | 0.0481 | 75.7282 | 0.003 | 18.0 | 1368.9 | `81f4574d8e7c` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6929 +- 0.0290 [worst 0.7391] | 0.7391 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1188 +- 0.0573 [worst 0.2611] | 0.2611 |
| ammo_efficiency | 74.0534 +- 9.1233 [worst 62.4359] | 62.4359 |
| latency_p50 | 0.0031 +- 0.0002 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0035 +- 0.0007 [worst 0.0068] | 0.0068 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1339.6417 +- 162.0414 [worst 1120.1000] | 1120.1000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
