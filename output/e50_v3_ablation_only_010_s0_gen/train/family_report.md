# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:51:31

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6653 | n/a | 0.2396 | 84.5807 | 0.003 | 16.0 | 1377.5 | `fe3d05d38771` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6814 | n/a | 0.1792 | 83.3257 | 0.004 | 16.0 | 1339.1 | `cb1dd6a90abb` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.8052 | n/a | 0.4854 | 58.6899 | 0.003 | 16.0 | 940.6 | `a2ef8f7d62ed` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.7090 | n/a | 0.1729 | 74.0952 | 0.003 | 16.0 | 1200.9 | `36ae8f1416f8` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.7498 | n/a | 0.3646 | 76.6379 | 0.003 | 16.0 | 1228.6 | `8bf1cf321c71` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6712 | n/a | 0.2578 | 95.3825 | 0.004 | 15.0 | 1441.8 | `642955b76a5e` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.7370 | n/a | 0.3244 | 74.9850 | 0.003 | 15.0 | 1116.8 | `11c66011c7c8` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6979 | n/a | 0.1978 | 105.3429 | 0.003 | 15.0 | 1583.2 | `3feee7b6f66b` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.7113 | n/a | 0.2313 | 78.2400 | 0.003 | 16.0 | 1260.8 | `6356a24bceca` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.7431 | n/a | 0.3200 | 86.6273 | 0.004 | 15.0 | 1297.8 | `5c40230e2b6e` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.7351 | n/a | 0.4467 | 77.0488 | 0.003 | 15.0 | 1159.4 | `f58385cc0fc1` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.7553 | n/a | 0.4467 | 65.1837 | 0.003 | 15.0 | 978.2 | `c34c0217fcfd` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.7139 | n/a | 0.2533 | 77.9978 | 0.003 | 15.0 | 1188.4 | `fea6e1ed56f5` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6598 | n/a | 0.1771 | 88.4421 | 0.003 | 16.0 | 1415.1 | `0e9cbc1354d7` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.7187 | n/a | 0.3604 | 75.0401 | 0.003 | 16.0 | 1213.1 | `4ee8702b9cdb` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6919 | n/a | 0.2578 | 87.7916 | 0.003 | 15.0 | 1323.1 | `d6f96179f989` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6996 | n/a | 0.2417 | 79.4022 | 0.003 | 16.0 | 1272.5 | `612a4bc82556` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6026 | n/a | 0.1833 | 93.8140 | 0.003 | 16.0 | 1496.4 | `dcb9e80aeaa3` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6848 | n/a | 0.1867 | 78.4431 | 0.003 | 15.0 | 1179.7 | `f28fa046e767` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6505 | n/a | 0.1222 | 107.1378 | 0.003 | 15.0 | 1620.0 | `8ea57c6e813e` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.7031 | n/a | 0.1911 | 93.1399 | 0.003 | 15.0 | 1414.5 | `96ac917e53cb` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6932 | n/a | 0.2489 | 90.4495 | 0.003 | 15.0 | 1365.2 | `9e0cc38934e9` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.7492 | n/a | 0.4208 | 58.0210 | 0.004 | 16.0 | 940.1 | `f0f7bde0862c` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.7144 | n/a | 0.1137 | 77.6861 | 0.003 | 17.0 | 1340.7 | `60009af81d37` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7060 +- 0.0408 [worst 0.8052] | 0.8052 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2676 +- 0.1034 [worst 0.4854] | 0.4854 |
| ammo_efficiency | 81.9794 +- 12.0390 [worst 58.0210] | 58.0210 |
| latency_p50 | 0.0032 +- 0.0003 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0035 +- 0.0007 [worst 0.0064] | 0.0064 |
| shots_total | 15.5417 +- 0.5758 [worst 17.0000] | 17.0000 |
| destroyed_value | 1278.8931 +- 175.3770 [worst 940.1333] | 940.1333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
