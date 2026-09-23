# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:12:55

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5653 | n/a | 0.1500 | 97.7805 | 0.003 | 18.0 | 1789.1 | `4ab944d93b63` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5933 | n/a | 0.0833 | 94.6447 | 0.003 | 18.0 | 1709.6 | `5ba930d33e8d` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6431 | n/a | 0.1630 | 95.0228 | 0.003 | 18.0 | 1722.9 | `0e451a9be02a` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6232 | n/a | 0.1389 | 85.0098 | 0.003 | 18.0 | 1554.6 | `3623f2ea01dc` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6200 | n/a | 0.1722 | 102.1984 | 0.003 | 18.0 | 1866.0 | `8c6949b34026` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5216 | n/a | 0.0627 | 120.6976 | 0.003 | 17.0 | 2097.6 | `72c00832a61e` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6156 | n/a | 0.1118 | 94.5028 | 0.003 | 17.0 | 1632.2 | `64b8cb1495f4` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6076 | n/a | 0.1074 | 112.7212 | 0.003 | 18.0 | 2056.7 | `021638f2d0b6` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6170 | n/a | 0.1019 | 102.1240 | 0.003 | 18.0 | 1672.4 | `60c20202b90a` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6186 | n/a | 0.1167 | 107.1392 | 0.003 | 18.0 | 1926.2 | `8db8472020e3` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5792 | n/a | 0.2130 | 101.8909 | 0.003 | 18.0 | 1841.7 | `b390096992ce` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6280 | n/a | 0.2500 | 81.3819 | 0.003 | 18.0 | 1487.0 | `a6b4de7b006c` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6356 | n/a | 0.1630 | 82.7065 | 0.003 | 18.0 | 1513.6 | `d81f6c8d4a86` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5534 | n/a | 0.0074 | 102.3810 | 0.003 | 18.0 | 1857.4 | `ce84ffac17d2` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6158 | n/a | 0.2704 | 100.5459 | 0.003 | 18.0 | 1656.7 | `f63246559b9f` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6223 | n/a | 0.2074 | 88.1738 | 0.003 | 18.0 | 1621.7 | `aaf1f90f5bd0` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5467 | n/a | 0.0685 | 107.0604 | 0.003 | 18.0 | 1920.1 | `405cab951acc` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5569 | n/a | 0.2148 | 92.8049 | 0.003 | 18.0 | 1668.7 | `8b4cabd62ce1` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5679 | n/a | 0.2093 | 89.5360 | 0.003 | 18.0 | 1617.4 | `1ab1b95b28a7` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5632 | n/a | 0.0537 | 113.2505 | 0.003 | 18.0 | 2024.5 | `d3a4cec97ffe` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6182 | n/a | 0.2074 | 99.1847 | 0.003 | 18.0 | 1818.9 | `0e0c3a0d9a7b` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5978 | n/a | 0.1019 | 100.7616 | 0.003 | 18.0 | 1789.9 | `3b46065ce8ab` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5975 | n/a | 0.1611 | 83.6809 | 0.003 | 18.0 | 1509.0 | `6a2cf528811b` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6102 | n/a | 0.1074 | 100.7403 | 0.003 | 18.0 | 1829.6 | `b7ae4a118560` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5966 +- 0.0315 [worst 0.6431] | 0.6431 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1435 +- 0.0652 [worst 0.2704] | 0.2704 |
| ammo_efficiency | 98.1642 +- 9.8591 [worst 81.3819] | 81.3819 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0033 +- 0.0005 [worst 0.0058] | 0.0058 |
| shots_total | 17.9167 +- 0.2764 [worst 18.0000] | 18.0000 |
| destroyed_value | 1757.6542 +- 169.4764 [worst 1487.0333] | 1487.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
