# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:15:57

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5520 | n/a | 0.1611 | 101.2459 | 0.003 | 18.0 | 1843.8 | `7b0d2917f1fb` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5855 | n/a | 0.0537 | 96.1019 | 0.003 | 18.0 | 1742.3 | `6fa59bed5975` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.5870 | n/a | 0.0574 | 110.7810 | 0.003 | 18.0 | 1993.8 | `1a3e182a50aa` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6453 | n/a | 0.2000 | 79.8595 | 0.003 | 18.0 | 1463.4 | `a7b7195deec1` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6246 | n/a | 0.2278 | 99.2394 | 0.003 | 18.0 | 1843.3 | `55b2bc162f98` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5164 | n/a | 0.0574 | 117.2998 | 0.003 | 18.0 | 2120.4 | `bf5d99cc5d9b` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6122 | n/a | 0.1037 | 90.8226 | 0.003 | 18.0 | 1646.4 | `8cf614398864` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.5988 | n/a | 0.0556 | 115.2170 | 0.003 | 18.0 | 2102.5 | `5c774bac5ab7` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.5902 | n/a | 0.1037 | 98.3369 | 0.003 | 18.0 | 1789.8 | `b4afd1433fbc` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6225 | n/a | 0.1611 | 105.5954 | 0.003 | 18.0 | 1907.0 | `19af9560a39a` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5927 | n/a | 0.2593 | 97.5659 | 0.003 | 18.0 | 1782.8 | `72664bf01f9e` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6120 | n/a | 0.2056 | 85.4098 | 0.003 | 18.0 | 1550.8 | `7320da4561eb` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6409 | n/a | 0.1519 | 81.3158 | 0.003 | 18.0 | 1491.8 | `42f619239a2b` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6072 | n/a | 0.2148 | 90.0907 | 0.003 | 18.0 | 1633.6 | `0b0017ab6654` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6162 | n/a | 0.2630 | 101.1207 | 0.003 | 18.0 | 1654.7 | `cc604c89d247` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6820 | n/a | 0.3148 | 75.3313 | 0.003 | 18.0 | 1365.6 | `43afaea7867d` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5722 | n/a | 0.1000 | 100.1128 | 0.003 | 18.0 | 1812.0 | `0370fe51e094` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5698 | n/a | 0.2574 | 88.1140 | 0.003 | 18.0 | 1620.3 | `23c75ba21cec` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5667 | n/a | 0.2111 | 88.7049 | 0.003 | 18.0 | 1621.7 | `ab7cefb9e890` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5654 | n/a | 0.0556 | 112.7680 | 0.003 | 18.0 | 2014.4 | `96fbcd486de2` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6349 | n/a | 0.1481 | 96.3657 | 0.003 | 18.0 | 1739.3 | `7a9ac74f9ab4` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5739 | n/a | 0.0574 | 104.4720 | 0.003 | 18.0 | 1896.0 | `01bcd7f385db` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6255 | n/a | 0.2796 | 76.0705 | 0.003 | 18.0 | 1404.1 | `9c327b6361a1` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5984 | n/a | 0.0556 | 104.7480 | 0.003 | 18.0 | 1885.3 | `cdb3a4a20ebe` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5997 +- 0.0345 [worst 0.6820] | 0.6820 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1565 +- 0.0836 [worst 0.3148] | 0.3148 |
| ammo_efficiency | 96.5287 +- 11.6105 [worst 75.3313] | 75.3313 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0034 +- 0.0005 [worst 0.0059] | 0.0059 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1746.8750 +- 204.2860 [worst 1365.5667] | 1365.5667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
