# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:09:26

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5527 | n/a | 0.1556 | 106.9236 | 0.004 | 18.0 | 1841.2 | `c2d4275ba170` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5754 | n/a | 0.1327 | 101.6835 | 0.004 | 17.1 | 1784.7 | `272bc6ec3af5` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6089 | n/a | 0.0705 | 105.2020 | 0.004 | 18.0 | 1888.2 | `43c6abd7d325` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6096 | n/a | 0.0333 | 99.1241 | 0.004 | 16.0 | 1611.0 | `ed55fc4b86f8` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.5784 | n/a | 0.0657 | 119.6699 | 0.004 | 16.8 | 2070.1 | `efa4a0a34618` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5078 | n/a | 0.0444 | 118.8656 | 0.004 | 18.0 | 2158.2 | `562d92598486` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6305 | n/a | 0.1574 | 85.5341 | 0.004 | 18.0 | 1568.7 | `fa102da52389` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6272 | n/a | 0.1538 | 112.2235 | 0.004 | 17.2 | 1954.0 | `a8baf81f9ae7` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.5994 | n/a | 0.0626 | 101.6704 | 0.004 | 17.0 | 1749.3 | `e50cc2baa13c` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.5864 | n/a | 0.1370 | 126.6933 | 0.004 | 18.0 | 2089.3 | `ce5f1bc0c656` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5759 | n/a | 0.1926 | 102.4596 | 0.004 | 18.0 | 1856.5 | `ae959a72796c` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5917 | n/a | 0.2012 | 90.3247 | 0.004 | 17.9 | 1632.0 | `867d850b554a` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6042 | n/a | 0.1148 | 90.7133 | 0.004 | 18.0 | 1644.0 | `9e155c194c0a` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5495 | n/a | 0.0549 | 109.1837 | 0.004 | 17.0 | 1873.5 | `5e22183bbb0e` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6287 | n/a | 0.2648 | 98.4897 | 0.004 | 18.0 | 1601.1 | `6640ca1213c7` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6408 | n/a | 0.2391 | 91.2497 | 0.004 | 18.0 | 1542.4 | `35594401a25c` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5434 | n/a | 0.0796 | 106.4504 | 0.004 | 18.0 | 1934.0 | `b83078ab0f43` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5136 | n/a | 0.1204 | 100.6150 | 0.004 | 18.0 | 1831.7 | `1fc0bfaff832` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5620 | n/a | 0.1463 | 97.7218 | 0.004 | 18.0 | 1639.4 | `2593610dc606` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5590 | n/a | 0.0519 | 113.6595 | 0.004 | 18.0 | 2044.3 | `b1059b2467fc` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6267 | n/a | 0.1593 | 97.9572 | 0.004 | 18.0 | 1778.5 | `77eb86a2b2dd` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5735 | n/a | 0.1056 | 106.4684 | 0.004 | 18.0 | 1897.9 | `5101ba9149d8` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6074 | n/a | 0.1790 | 89.8476 | 0.004 | 17.2 | 1471.9 | `48bdb1a8a540` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5951 | n/a | 0.0510 | 112.1014 | 0.004 | 17.0 | 1900.6 | `084613e2d2b4` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5853 +- 0.0351 [worst 0.6408] | 0.6408 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1239 +- 0.0626 [worst 0.2648] | 0.2648 |
| ammo_efficiency | 103.5347 +- 10.1529 [worst 85.5341] | 85.5341 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0040 +- 0.0006 [worst 0.0066] | 0.0066 |
| shots_total | 17.6319 +- 0.5461 [worst 18.0000] | 18.0000 |
| destroyed_value | 1806.7736 +- 183.5247 [worst 1471.9000] | 1471.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
