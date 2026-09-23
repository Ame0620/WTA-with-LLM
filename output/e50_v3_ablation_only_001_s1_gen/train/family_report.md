# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:56:48

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5408 | n/a | 0.0889 | 104.9003 | 0.004 | 18.0 | 1890.2 | `82f389d29b72` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6093 | n/a | 0.0611 | 89.7048 | 0.004 | 18.0 | 1642.3 | `04f8a458353f` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6527 | n/a | 0.1648 | 92.8821 | 0.004 | 18.0 | 1676.8 | `186edb0092d3` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6567 | n/a | 0.1130 | 78.2203 | 0.004 | 18.0 | 1416.5 | `42ead3d1f8ec` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6667 | n/a | 0.1744 | 111.6152 | 0.004 | 14.6 | 1636.6 | `07c7f9f00436` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6013 | n/a | 0.1608 | 102.7133 | 0.004 | 17.0 | 1748.3 | `54cc36bcc332` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6417 | n/a | 0.2056 | 82.5146 | 0.004 | 18.0 | 1521.3 | `78562d75a6c3` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6294 | n/a | 0.1648 | 105.8651 | 0.004 | 18.0 | 1942.6 | `8596507b6607` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6427 | n/a | 0.1556 | 85.7261 | 0.004 | 18.0 | 1560.4 | `b15d42a2e471` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6338 | n/a | 0.1704 | 101.5934 | 0.004 | 18.0 | 1849.4 | `1a6debca598f` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5723 | n/a | 0.2130 | 102.3204 | 0.004 | 18.0 | 1871.9 | `aaf44a4947d5` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6520 | n/a | 0.2224 | 85.2709 | 0.004 | 16.2 | 1391.1 | `6cfbafce9c33` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6601 | n/a | 0.1066 | 80.9230 | 0.004 | 17.2 | 1412.0 | `e0ef109af427` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5796 | n/a | 0.0000 | 107.8277 | 0.004 | 16.1 | 1748.3 | `27abd0aba432` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6476 | n/a | 0.3130 | 83.6524 | 0.004 | 18.0 | 1519.3 | `1b4ef90b3888` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6594 | n/a | 0.2180 | 84.3189 | 0.004 | 17.2 | 1462.6 | `4d364e1bfe3a` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5877 | n/a | 0.1556 | 95.9294 | 0.004 | 18.0 | 1746.4 | `c61826195bbe` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5822 | n/a | 0.2037 | 85.7515 | 0.004 | 18.0 | 1573.5 | `373d4bf4aa0b` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5663 | n/a | 0.1648 | 89.0572 | 0.004 | 18.0 | 1623.2 | `90a8a9aa55aa` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6324 | n/a | 0.2167 | 94.9137 | 0.004 | 18.0 | 1703.8 | `db218d532e97` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6403 | n/a | 0.1556 | 93.6775 | 0.004 | 18.0 | 1713.5 | `96a31fd45dbb` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6128 | n/a | 0.1074 | 95.0017 | 0.004 | 18.0 | 1723.1 | `3852de10d89b` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6277 | n/a | 0.2130 | 77.2646 | 0.004 | 18.0 | 1395.7 | `1f230c079e08` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6428 | n/a | 0.1074 | 92.0884 | 0.004 | 18.0 | 1676.5 | `14df02b3ab87` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6224 +- 0.0341 [worst 0.6667] | 0.6667 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1607 +- 0.0629 [worst 0.3130] | 0.3130 |
| ammo_efficiency | 92.6555 +- 9.6165 [worst 77.2646] | 77.2646 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0043 +- 0.0007 [worst 0.0069] | 0.0069 |
| shots_total | 17.5958 +- 0.8352 [worst 18.0000] | 18.0000 |
| destroyed_value | 1643.5569 +- 158.1209 [worst 1391.1000] | 1391.1000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
