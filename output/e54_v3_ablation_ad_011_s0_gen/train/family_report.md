# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:05:58

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6334 | n/a | 0.2667 | 83.5347 | 0.004 | 18.0 | 1508.9 | `33309f755143` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6303 | n/a | 0.1917 | 90.2464 | 0.004 | 17.0 | 1553.9 | `39608b725530` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6217 | n/a | 0.0667 | 101.2566 | 0.004 | 18.0 | 1826.7 | `cb7bac2c257f` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6304 | n/a | 0.1111 | 83.8174 | 0.004 | 18.0 | 1524.8 | `508a9832f59f` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6417 | n/a | 0.2185 | 96.8328 | 0.004 | 18.0 | 1759.0 | `dd8488603bdb` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5242 | n/a | 0.0519 | 115.8580 | 0.004 | 18.0 | 2086.5 | `445836c6e290` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.5939 | n/a | 0.1463 | 93.1363 | 0.004 | 18.0 | 1724.4 | `7760ec965324` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6152 | n/a | 0.1685 | 109.8579 | 0.004 | 18.0 | 2016.5 | `f4d1c47b0da7` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6834 | n/a | 0.2537 | 76.6296 | 0.004 | 18.0 | 1382.4 | `ae192f824160` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6158 | n/a | 0.1593 | 107.0500 | 0.004 | 18.0 | 1940.7 | `131766ba0a79` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5750 | n/a | 0.2000 | 101.5956 | 0.004 | 18.0 | 1860.2 | `bc75d4fd3d1f` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5780 | n/a | 0.1574 | 93.1271 | 0.004 | 18.0 | 1686.9 | `8555eab65c8a` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6492 | n/a | 0.1500 | 80.7185 | 0.004 | 18.0 | 1457.1 | `645810655ef1` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5672 | n/a | 0.0537 | 99.3749 | 0.004 | 18.0 | 1800.0 | `c0ef96493cfd` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6352 | n/a | 0.2630 | 86.3036 | 0.004 | 18.0 | 1572.9 | `cd7674c3b329` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6032 | n/a | 0.1519 | 94.0478 | 0.004 | 18.0 | 1704.0 | `843a258ef3fa` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5530 | n/a | 0.0556 | 104.6835 | 0.004 | 18.0 | 1893.4 | `5c08901eb751` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5802 | n/a | 0.2130 | 87.5955 | 0.004 | 18.0 | 1580.8 | `5968a407832d` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5620 | n/a | 0.2130 | 89.6739 | 0.004 | 18.0 | 1639.3 | `7bcdbefec565` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5774 | n/a | 0.0574 | 108.5152 | 0.004 | 18.0 | 1958.8 | `829e5174ef5b` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6104 | n/a | 0.1556 | 100.5363 | 0.004 | 18.0 | 1856.2 | `46583aa96d87` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5934 | n/a | 0.1037 | 102.1940 | 0.004 | 18.0 | 1809.4 | `a87d3b368437` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5920 | n/a | 0.1611 | 84.3679 | 0.004 | 18.0 | 1529.4 | `4abaa5b29c03` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5729 | n/a | 0.0481 | 110.4513 | 0.004 | 18.0 | 2005.0 | `b19fb1e8b5eb` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6016 +- 0.0352 [worst 0.6834] | 0.6834 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1507 +- 0.0683 [worst 0.2667] | 0.2667 |
| ammo_efficiency | 95.8919 +- 10.3781 [worst 76.6296] | 76.6296 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0039 +- 0.0006 [worst 0.0066] | 0.0066 |
| shots_total | 17.9597 +- 0.1932 [worst 18.0000] | 18.0000 |
| destroyed_value | 1736.5528 +- 191.1358 [worst 1382.4000] | 1382.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
