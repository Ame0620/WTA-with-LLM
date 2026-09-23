# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:47:44

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6308 | n/a | 0.1556 | 83.9489 | 0.003 | 18.0 | 1519.6 | `704ba239cf16` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6663 | n/a | 0.1037 | 77.3270 | 0.004 | 18.0 | 1402.3 | `d40b86de62e8` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.7056 | n/a | 0.1630 | 78.4100 | 0.003 | 18.0 | 1421.2 | `977d205cd16b` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.7158 | n/a | 0.1105 | 68.1424 | 0.003 | 17.1 | 1172.6 | `427a074cb26c` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6724 | n/a | 0.0926 | 87.8278 | 0.003 | 18.0 | 1608.4 | `1f73f4356b04` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6128 | n/a | 0.1037 | 94.5016 | 0.004 | 18.0 | 1697.7 | `39e8dc7e1c52` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6165 | n/a | 0.1630 | 89.2964 | 0.003 | 18.0 | 1628.5 | `5042f77d6a26` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6366 | n/a | 0.0519 | 105.5165 | 0.003 | 18.0 | 1904.7 | `4e46d916a9af` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6290 | n/a | 0.1037 | 93.0896 | 0.003 | 18.0 | 1620.2 | `7e55cac465cc` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6745 | n/a | 0.1056 | 90.7678 | 0.003 | 18.0 | 1643.9 | `12196b910f87` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6337 | n/a | 0.1481 | 88.0407 | 0.003 | 18.0 | 1603.5 | `ed37a1a96562` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6510 | n/a | 0.1056 | 78.0484 | 0.003 | 18.0 | 1394.9 | `0df190af3b7b` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.7060 | n/a | 0.2037 | 66.6244 | 0.003 | 18.0 | 1221.4 | `749264369d7c` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5878 | n/a | 0.0519 | 94.6157 | 0.003 | 18.0 | 1714.4 | `3571d9cb8b0f` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6098 | n/a | 0.1556 | 91.6533 | 0.003 | 18.0 | 1682.6 | `99768f0adeff` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.7220 | n/a | 0.1574 | 65.7611 | 0.003 | 18.0 | 1193.7 | `9ebfaefe2791` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6129 | n/a | 0.0019 | 90.2235 | 0.003 | 18.0 | 1639.8 | `8d6ed2fed8a3` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5816 | n/a | 0.1574 | 85.4047 | 0.003 | 18.0 | 1575.8 | `96298e9145ba` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6350 | n/a | 0.2093 | 75.4635 | 0.004 | 18.0 | 1366.2 | `1b9e94eb73ee` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6243 | n/a | 0.1093 | 96.6712 | 0.003 | 18.0 | 1741.6 | `8235d9a19f1e` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6727 | n/a | 0.1549 | 91.5206 | 0.003 | 17.0 | 1559.5 | `7103f0beefc3` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6389 | n/a | 0.0963 | 90.6245 | 0.003 | 18.0 | 1607.1 | `1b258daf3a5b` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6383 | n/a | 0.0815 | 75.7703 | 0.004 | 18.0 | 1356.1 | `896357cf125d` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6640 | n/a | 0.0000 | 86.5969 | 0.003 | 18.0 | 1577.2 | `8e3b5cc1fee1` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6474 +- 0.0377 [worst 0.7220] | 0.7220 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1161 +- 0.0530 [worst 0.2093] | 0.2093 |
| ammo_efficiency | 85.2436 +- 9.8766 [worst 65.7611] | 65.7611 |
| latency_p50 | 0.0031 +- 0.0003 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0035 +- 0.0007 [worst 0.0062] | 0.0062 |
| shots_total | 17.9222 +- 0.2587 [worst 18.0000] | 18.0000 |
| destroyed_value | 1535.5361 +- 179.7003 [worst 1172.6333] | 1172.6333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
