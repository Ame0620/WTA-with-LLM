# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:10:30

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5689 | n/a | 0.2111 | 103.9903 | 0.004 | 18.0 | 1774.4 | `c8ddb84007da` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6152 | n/a | 0.2218 | 99.0614 | 0.004 | 17.0 | 1617.2 | `138da0a4e02d` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6735 | n/a | 0.2074 | 86.9676 | 0.004 | 18.0 | 1576.3 | `c5db8019a4f5` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.5848 | n/a | 0.0412 | 97.2600 | 0.003 | 17.0 | 1713.2 | `c0ef2aecfb15` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6097 | n/a | 0.1659 | 108.6043 | 0.003 | 17.1 | 1916.2 | `0297578742c1` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5240 | n/a | 0.0519 | 115.7579 | 0.004 | 18.0 | 2087.4 | `d9519503e975` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6017 | n/a | 0.1500 | 91.3738 | 0.004 | 18.0 | 1691.2 | `19fe34d07858` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6304 | n/a | 0.1620 | 111.2078 | 0.004 | 17.1 | 1937.1 | `9aa793aa4e2a` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6159 | n/a | 0.1815 | 100.1779 | 0.004 | 18.0 | 1677.4 | `3268fd828c4e` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6336 | n/a | 0.1963 | 107.6511 | 0.004 | 18.0 | 1850.8 | `0a5092e1981c` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5683 | n/a | 0.1259 | 102.7396 | 0.004 | 18.0 | 1889.4 | `7cb75ab0b662` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6045 | n/a | 0.2667 | 86.8470 | 0.004 | 18.0 | 1580.8 | `21b5ac9437a5` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6057 | n/a | 0.1061 | 90.9274 | 0.004 | 17.8 | 1638.0 | `a29ead68502a` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5580 | n/a | 0.0247 | 105.6985 | 0.004 | 17.1 | 1838.5 | `48b96b5ff27d` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6300 | n/a | 0.2722 | 96.6410 | 0.004 | 18.0 | 1595.3 | `c28a7e4cba83` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6765 | n/a | 0.3185 | 77.4183 | 0.004 | 18.0 | 1389.2 | `6ab4f6ca97c5` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5833 | n/a | 0.1407 | 97.2562 | 0.004 | 18.0 | 1765.0 | `e57c3b9d74cb` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5324 | n/a | 0.1389 | 97.1166 | 0.004 | 18.0 | 1760.9 | `768e83ea6f4d` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6081 | n/a | 0.2412 | 93.3161 | 0.004 | 17.0 | 1466.9 | `d5b14f0cab29` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5813 | n/a | 0.0981 | 106.6748 | 0.004 | 18.0 | 1940.9 | `06d91f060669` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6287 | n/a | 0.1593 | 98.0568 | 0.004 | 18.0 | 1768.7 | `9e91229e300e` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5752 | n/a | 0.1056 | 106.1350 | 0.004 | 18.0 | 1890.3 | `ec3f758cf8b2` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5890 | n/a | 0.1444 | 85.3052 | 0.004 | 18.0 | 1540.8 | `5ba0eef03154` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5884 | n/a | 0.1037 | 107.5811 | 0.004 | 18.0 | 1932.3 | `ac7d47fd2afa` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5995 +- 0.0363 [worst 0.6765] | 0.6765 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1598 +- 0.0723 [worst 0.3185] | 0.3185 |
| ammo_efficiency | 98.9069 +- 9.0894 [worst 77.4183] | 77.4183 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0039 +- 0.0006 [worst 0.0065] | 0.0065 |
| shots_total | 17.7528 +- 0.4140 [worst 18.0000] | 18.0000 |
| destroyed_value | 1743.2528 +- 168.3945 [worst 1389.1667] | 1389.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
