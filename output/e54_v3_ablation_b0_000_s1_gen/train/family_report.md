# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:08:54

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5678 | n/a | 0.1611 | 98.1393 | 0.003 | 18.0 | 1778.8 | `5280b8fb1a1c` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6059 | n/a | 0.1241 | 92.1643 | 0.003 | 18.0 | 1656.3 | `492dc46e48d6` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6099 | n/a | 0.1093 | 105.5787 | 0.003 | 18.0 | 1883.3 | `1f1895f99abc` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6378 | n/a | 0.1549 | 87.4157 | 0.003 | 17.0 | 1494.3 | `0d8d52e34177` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6246 | n/a | 0.2278 | 99.2394 | 0.003 | 18.0 | 1843.3 | `55b2bc162f98` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5164 | n/a | 0.0574 | 117.2998 | 0.003 | 18.0 | 2120.4 | `bf5d99cc5d9b` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6166 | n/a | 0.1037 | 88.5568 | 0.003 | 18.0 | 1628.0 | `854884a5e092` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.5978 | n/a | 0.0556 | 115.4425 | 0.003 | 18.0 | 2108.0 | `7825a7d774cd` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6016 | n/a | 0.1392 | 108.5182 | 0.003 | 17.0 | 1740.0 | `7cdc1cf22f99` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6138 | n/a | 0.1611 | 107.9782 | 0.003 | 18.0 | 1950.5 | `ab2125e46ce0` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5839 | n/a | 0.2204 | 100.9357 | 0.003 | 18.0 | 1821.1 | `d1aebbf73e86` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6668 | n/a | 0.3074 | 73.7107 | 0.003 | 18.0 | 1331.6 | `b39249ac1f47` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6340 | n/a | 0.1519 | 83.5098 | 0.003 | 18.0 | 1520.2 | `b9692895ff44` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5752 | n/a | 0.0362 | 102.8417 | 0.003 | 17.1 | 1766.7 | `652130fa859c` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6199 | n/a | 0.2722 | 100.4763 | 0.003 | 18.0 | 1638.9 | `6272543aad54` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6820 | n/a | 0.3148 | 75.3313 | 0.003 | 18.0 | 1365.6 | `43afaea7867d` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5570 | n/a | 0.0944 | 103.4517 | 0.003 | 18.0 | 1876.7 | `7ea9f109d334` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5530 | n/a | 0.2130 | 93.4714 | 0.003 | 18.0 | 1683.3 | `6007fa4527d8` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5720 | n/a | 0.1963 | 93.3563 | 0.003 | 18.0 | 1602.0 | `aeff00bc3ddb` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5819 | n/a | 0.1019 | 107.0251 | 0.003 | 18.0 | 1937.7 | `00290458f08a` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6066 | n/a | 0.1481 | 104.6025 | 0.003 | 18.0 | 1873.9 | `fe82bfcd7b5e` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5866 | n/a | 0.1019 | 101.5950 | 0.003 | 18.0 | 1839.7 | `246a81d7ce6d` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6156 | n/a | 0.1647 | 83.9188 | 0.003 | 17.0 | 1441.1 | `dc584e608cde` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6137 | n/a | 0.0588 | 106.8021 | 0.003 | 17.0 | 1813.3 | `954bac9f7fbd` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6017 +- 0.0354 [worst 0.6820] | 0.6820 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1532 +- 0.0751 [worst 0.3148] | 0.3148 |
| ammo_efficiency | 97.9734 +- 11.2151 [worst 73.7107] | 73.7107 |
| latency_p50 | 0.0031 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0033 +- 0.0005 [worst 0.0059] | 0.0059 |
| shots_total | 17.7944 +- 0.4009 [worst 18.0000] | 18.0000 |
| destroyed_value | 1738.1194 +- 205.3811 [worst 1331.6333] | 1331.6333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
