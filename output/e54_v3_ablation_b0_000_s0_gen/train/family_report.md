# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:04:54

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5624 | n/a | 0.1611 | 105.1752 | 0.003 | 18.0 | 1801.2 | `da94ee181d26` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6314 | n/a | 0.1130 | 91.2354 | 0.003 | 18.0 | 1549.4 | `225650d5664d` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6478 | n/a | 0.1648 | 94.0165 | 0.003 | 18.0 | 1700.6 | `7f47798eba39` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6346 | n/a | 0.1111 | 82.4266 | 0.003 | 18.0 | 1507.7 | `ec470e366db2` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6021 | n/a | 0.1130 | 106.3523 | 0.003 | 18.0 | 1953.6 | `67415695c45d` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5407 | n/a | 0.1111 | 111.1500 | 0.003 | 18.0 | 2014.0 | `52f4465283a4` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6504 | n/a | 0.2111 | 81.8235 | 0.003 | 18.0 | 1484.6 | `2e01909c5be3` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.5998 | n/a | 0.0556 | 114.8275 | 0.003 | 18.0 | 2097.5 | `fd4c91aa3882` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6213 | n/a | 0.1519 | 103.2745 | 0.003 | 18.0 | 1653.8 | `9d66eab96c99` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6169 | n/a | 0.1278 | 111.7902 | 0.003 | 18.0 | 1935.1 | `c556c1018479` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5485 | n/a | 0.0944 | 109.6241 | 0.003 | 18.0 | 1976.0 | `7f32aa8cd4fe` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6397 | n/a | 0.2870 | 79.0147 | 0.003 | 18.0 | 1440.0 | `21989d51b770` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6351 | n/a | 0.1519 | 83.5811 | 0.003 | 18.0 | 1515.7 | `48055bac3e82` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5637 | n/a | 0.0593 | 100.2842 | 0.003 | 18.0 | 1814.6 | `01f1d6b80ae0` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6325 | n/a | 0.3130 | 87.2366 | 0.003 | 18.0 | 1584.8 | `939f8091b00d` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6449 | n/a | 0.2630 | 84.1782 | 0.003 | 18.0 | 1524.7 | `d301ba711814` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5518 | n/a | 0.1000 | 103.8466 | 0.003 | 18.0 | 1898.4 | `62ab23791905` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5569 | n/a | 0.2148 | 92.8049 | 0.003 | 18.0 | 1668.7 | `8b4cabd62ce1` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6081 | n/a | 0.2463 | 88.1476 | 0.003 | 18.0 | 1466.9 | `65b314d8f20c` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5713 | n/a | 0.1074 | 110.4110 | 0.003 | 18.0 | 1986.8 | `fbe30ce6d16b` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6291 | n/a | 0.2074 | 98.2654 | 0.003 | 18.0 | 1766.9 | `3844553eb7f4` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5645 | n/a | 0.0574 | 108.5078 | 0.003 | 18.0 | 1938.0 | `84236698c276` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5982 | n/a | 0.1704 | 89.0659 | 0.003 | 18.0 | 1506.4 | `5f9ead0c8b5f` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6132 | n/a | 0.0519 | 100.3037 | 0.003 | 18.0 | 1815.4 | `9ee93d7a13f7` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6027 +- 0.0352 [worst 0.6504] | 0.6504 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1519 +- 0.0731 [worst 0.3130] | 0.3130 |
| ammo_efficiency | 97.3893 +- 10.9462 [worst 79.0147] | 79.0147 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0033] | 0.0033 |
| latency_p90 | 0.0033 +- 0.0006 [worst 0.0061] | 0.0061 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1733.3736 +- 203.2710 [worst 1440.0333] | 1440.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
