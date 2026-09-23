# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:05:25

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5874 | n/a | 0.2630 | 93.9946 | 0.004 | 18.0 | 1698.5 | `488214d4d2f3` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6062 | n/a | 0.2100 | 94.9141 | 0.004 | 17.9 | 1655.3 | `1f7ed8378e80` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6199 | n/a | 0.1039 | 101.9889 | 0.004 | 17.9 | 1835.3 | `c18959edf2f3` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6535 | n/a | 0.0000 | 89.2598 | 0.004 | 16.0 | 1429.6 | `98d8e9028fad` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6517 | n/a | 0.2648 | 95.0528 | 0.004 | 18.0 | 1710.1 | `b1cffd8a6035` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5192 | n/a | 0.0481 | 117.6320 | 0.004 | 18.0 | 2108.4 | `caa455daef07` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.5991 | n/a | 0.1019 | 92.5332 | 0.004 | 18.0 | 1702.4 | `49de34a8dd7b` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6394 | n/a | 0.2155 | 104.1989 | 0.004 | 17.9 | 1889.8 | `1bc7be958758` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6372 | n/a | 0.1944 | 93.6384 | 0.004 | 18.0 | 1584.2 | `7687dfd02738` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6267 | n/a | 0.0963 | 110.2815 | 0.004 | 18.0 | 1885.5 | `95a6e082abb2` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5536 | n/a | 0.1463 | 105.8199 | 0.004 | 18.0 | 1954.0 | `43fa2ca6bab2` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6087 | n/a | 0.2275 | 91.3190 | 0.004 | 17.0 | 1564.0 | `77f4d78d0bb0` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6546 | n/a | 0.1526 | 83.8002 | 0.004 | 17.0 | 1435.0 | `fe3824424f39` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5734 | n/a | 0.0630 | 98.5775 | 0.003 | 18.0 | 1774.0 | `f7167fb110bf` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6365 | n/a | 0.2111 | 96.1796 | 0.003 | 18.0 | 1567.4 | `c42a723725a4` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6229 | n/a | 0.1629 | 92.9254 | 0.004 | 17.2 | 1619.3 | `bca86d597efa` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5456 | n/a | 0.0111 | 106.4113 | 0.004 | 18.0 | 1924.9 | `a3f98ec0692b` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5602 | n/a | 0.1593 | 91.3849 | 0.004 | 18.0 | 1656.2 | `d30c194f028f` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5764 | n/a | 0.1981 | 95.0608 | 0.004 | 18.0 | 1585.4 | `eabbd47d5b7b` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5649 | n/a | 0.0704 | 112.5002 | 0.004 | 18.0 | 2016.7 | `06d2630a2cf5` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6484 | n/a | 0.1593 | 92.3156 | 0.004 | 18.0 | 1675.2 | `09dde0a3ee90` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6053 | n/a | 0.1060 | 99.1699 | 0.004 | 17.9 | 1756.3 | `0edda5192bb9` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6242 | n/a | 0.3185 | 77.4741 | 0.004 | 18.0 | 1408.9 | `da87e51b7262` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5713 | n/a | 0.0485 | 111.6247 | 0.004 | 17.9 | 2012.4 | `da1d05e3eeee` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6036 +- 0.0376 [worst 0.6546] | 0.6546 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1472 +- 0.0822 [worst 0.3185] | 0.3185 |
| ammo_efficiency | 97.8357 +- 9.2654 [worst 77.4741] | 77.4741 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0039 +- 0.0006 [worst 0.0065] | 0.0065 |
| shots_total | 17.7847 +- 0.4806 [worst 18.0000] | 18.0000 |
| destroyed_value | 1727.0333 +- 189.4521 [worst 1408.9333] | 1408.9333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
