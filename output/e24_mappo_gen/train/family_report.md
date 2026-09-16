# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **mappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 17:34:09

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5624 | n/a | 0.1611 | 99.2193 | 0.005 | 18.0 | 1801.2 | `7bf263f1b716` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6330 | n/a | 0.0796 | 85.6661 | 0.006 | 18.0 | 1542.3 | `09863fcd5e09` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6370 | n/a | 0.1611 | 97.5025 | 0.004 | 18.0 | 1752.6 | `dea76c1df7c5` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6356 | n/a | 0.1111 | 82.3003 | 0.004 | 18.0 | 1503.5 | `eaf0eeaa3a86` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6113 | n/a | 0.1315 | 104.0068 | 0.004 | 18.0 | 1908.4 | `59af0c48a4d8` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5407 | n/a | 0.1111 | 111.1500 | 0.004 | 18.0 | 2014.0 | `52f4465283a4` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6507 | n/a | 0.1725 | 86.5573 | 0.004 | 17.0 | 1483.2 | `e2b044e21919` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6105 | n/a | 0.0549 | 118.8957 | 0.004 | 17.0 | 2041.5 | `91e9e4af2330` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6165 | n/a | 0.1074 | 101.4320 | 0.004 | 18.0 | 1674.8 | `75f6effb7da2` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6215 | n/a | 0.1556 | 105.9244 | 0.004 | 18.0 | 1911.6 | `85f980a94ce9` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5819 | n/a | 0.2167 | 101.2766 | 0.004 | 18.0 | 1829.9 | `c0252814c37f` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6257 | n/a | 0.2537 | 81.9462 | 0.004 | 18.0 | 1496.2 | `2bee44543e8e` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6343 | n/a | 0.1519 | 83.6983 | 0.004 | 18.0 | 1519.2 | `9a639c3397a7` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5631 | n/a | 0.0074 | 100.6251 | 0.004 | 18.0 | 1816.9 | `fce5ef031dbe` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6333 | n/a | 0.2722 | 96.5228 | 0.004 | 18.0 | 1581.3 | `e0e2d0917312` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6574 | n/a | 0.2611 | 81.7479 | 0.004 | 18.0 | 1471.1 | `859ac34d0c10` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5514 | n/a | 0.1000 | 103.8719 | 0.004 | 18.0 | 1900.4 | `190113647f72` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5569 | n/a | 0.2148 | 92.8049 | 0.004 | 18.0 | 1668.7 | `8b4cabd62ce1` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5857 | n/a | 0.2444 | 86.2298 | 0.004 | 18.0 | 1550.6 | `b033a01d594c` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5717 | n/a | 0.1074 | 110.2609 | 0.004 | 18.0 | 1985.0 | `2c262ca7d48a` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6179 | n/a | 0.1647 | 106.1636 | 0.004 | 17.0 | 1820.2 | `aa48149a232c` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5949 | n/a | 0.1019 | 101.4485 | 0.004 | 18.0 | 1802.8 | `cf93a22d9ff7` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6152 | n/a | 0.1796 | 85.8697 | 0.004 | 18.0 | 1442.7 | `8d7c59024c6d` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6102 | n/a | 0.1074 | 100.7403 | 0.004 | 18.0 | 1829.6 | `b7ae4a118560` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6050 +- 0.0326 [worst 0.6574] | 0.6574 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1512 +- 0.0663 [worst 0.2722] | 0.2722 |
| ammo_efficiency | 96.9109 +- 10.3133 [worst 81.7479] | 81.7479 |
| latency_p50 | 0.0040 +- 0.0005 [worst 0.0056] | 0.0056 |
| latency_p90 | 0.0056 +- 0.0014 [worst 0.0102] | 0.0102 |
| shots_total | 17.8750 +- 0.3307 [worst 18.0000] | 18.0000 |
| destroyed_value | 1722.8250 +- 186.9711 [worst 1442.7333] | 1442.7333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
