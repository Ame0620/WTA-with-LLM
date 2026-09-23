# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:13:59

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6010 | n/a | 0.2111 | 90.3136 | 0.004 | 18.0 | 1642.2 | `76869264e04c` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6118 | n/a | 0.1772 | 93.6895 | 0.004 | 17.2 | 1631.4 | `3f9427a8d572` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6460 | n/a | 0.1574 | 94.9449 | 0.004 | 18.0 | 1709.2 | `539152eac152` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6275 | n/a | 0.1130 | 84.1551 | 0.004 | 18.0 | 1536.9 | `84d8da2f2a4d` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6259 | n/a | 0.2200 | 104.3500 | 0.004 | 17.1 | 1836.8 | `2e29af1f16f7` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5159 | n/a | 0.0481 | 118.4040 | 0.004 | 18.0 | 2122.8 | `f722ce2548c2` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6190 | n/a | 0.1642 | 92.8271 | 0.004 | 17.3 | 1617.8 | `f23fed7b6958` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6125 | n/a | 0.1630 | 110.3996 | 0.004 | 18.0 | 2030.7 | `cf0eab4aa086` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6222 | n/a | 0.1070 | 104.2702 | 0.004 | 17.1 | 1649.7 | `ae725430e265` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.5998 | n/a | 0.1463 | 118.3506 | 0.004 | 18.0 | 2021.6 | `aa25332d0f6a` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5510 | n/a | 0.1611 | 107.3826 | 0.004 | 18.0 | 1965.4 | `c3186ca46b0a` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5864 | n/a | 0.1784 | 96.4358 | 0.004 | 17.0 | 1653.2 | `f45351a6d24e` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6258 | n/a | 0.1444 | 85.3245 | 0.004 | 18.0 | 1554.5 | `d73117e8c83f` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5603 | n/a | 0.0537 | 100.2950 | 0.004 | 18.0 | 1828.6 | `b6c85549d4e2` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6436 | n/a | 0.3167 | 84.7468 | 0.004 | 18.0 | 1536.9 | `27cfe13e4d95` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6184 | n/a | 0.1593 | 90.9079 | 0.004 | 18.0 | 1638.6 | `9a27fa902c20` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5893 | n/a | 0.0963 | 96.3664 | 0.004 | 18.0 | 1739.8 | `9e07c91e4e57` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5892 | n/a | 0.2167 | 85.7139 | 0.004 | 18.0 | 1546.9 | `57449dee526f` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5568 | n/a | 0.1593 | 92.4792 | 0.004 | 18.0 | 1659.0 | `0d43013e32b6` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5447 | n/a | 0.0130 | 117.7204 | 0.004 | 18.0 | 2110.2 | `6e347a07213f` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6309 | n/a | 0.2019 | 97.0599 | 0.004 | 18.0 | 1758.6 | `e9aa41c79b87` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5695 | n/a | 0.1056 | 105.5205 | 0.004 | 18.0 | 1915.6 | `1b204d4c74f2` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5962 | n/a | 0.1630 | 82.4971 | 0.004 | 18.0 | 1513.8 | `850ac61a04eb` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6028 | n/a | 0.1072 | 108.1426 | 0.004 | 17.1 | 1864.4 | `fda3f7e5edfc` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5978 +- 0.0328 [worst 0.6460] | 0.6460 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1493 +- 0.0627 [worst 0.3167] | 0.3167 |
| ammo_efficiency | 98.4290 +- 10.8414 [worst 82.4971] | 82.4971 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0040 +- 0.0005 [worst 0.0066] | 0.0066 |
| shots_total | 17.7847 +- 0.3755 [worst 18.0000] | 18.0000 |
| destroyed_value | 1753.5306 +- 186.2762 [worst 1513.7667] | 1513.7667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
