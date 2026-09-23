# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:10:59

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5640 | n/a | 0.2019 | 104.8208 | 0.003 | 18.0 | 1794.5 | `28fe136cd5d5` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5977 | n/a | 0.1608 | 103.8823 | 0.003 | 16.2 | 1691.1 | `fb7635145370` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6151 | n/a | 0.0620 | 109.0193 | 0.003 | 17.1 | 1858.1 | `2747bd796527` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.5934 | n/a | 0.0392 | 96.5297 | 0.003 | 17.0 | 1677.7 | `62aad797df36` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6211 | n/a | 0.1102 | 112.6236 | 0.003 | 16.2 | 1860.4 | `23d0ceb28fb8` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5055 | n/a | 0.0481 | 118.5541 | 0.003 | 18.0 | 2168.4 | `44a9628b2f0d` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6335 | n/a | 0.1654 | 89.6604 | 0.003 | 17.1 | 1556.0 | `4eed708a2504` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6168 | n/a | 0.1611 | 109.8439 | 0.003 | 18.0 | 2008.5 | `93a2fd3ee73a` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6188 | n/a | 0.1185 | 110.2911 | 0.003 | 16.0 | 1664.7 | `78cbbc1446c0` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.5921 | n/a | 0.1463 | 126.5486 | 0.003 | 18.0 | 2060.4 | `f38027f832d9` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5823 | n/a | 0.1695 | 104.2322 | 0.003 | 17.1 | 1828.2 | `99dc12094504` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6027 | n/a | 0.2027 | 91.4715 | 0.003 | 17.3 | 1588.1 | `ff2ca69aac1c` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6244 | n/a | 0.1154 | 90.3704 | 0.003 | 17.0 | 1560.2 | `07d6bd4e161d` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5600 | n/a | 0.0692 | 104.8613 | 0.003 | 17.2 | 1829.8 | `3fda94f34d05` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6308 | n/a | 0.3074 | 92.9121 | 0.003 | 18.0 | 1591.8 | `5fb566627f27` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6353 | n/a | 0.2611 | 92.9034 | 0.003 | 18.0 | 1565.8 | `8f73b1a86388` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5804 | n/a | 0.2037 | 97.4740 | 0.003 | 18.0 | 1777.4 | `387570669f0d` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5254 | n/a | 0.1013 | 103.4136 | 0.003 | 17.4 | 1787.5 | `6d8b42ad37f2` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5825 | n/a | 0.2222 | 92.5426 | 0.003 | 18.0 | 1562.6 | `ae2b904014c8` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5760 | n/a | 0.1037 | 108.5845 | 0.003 | 18.0 | 1965.3 | `34c53e1e7890` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6410 | n/a | 0.2137 | 101.7171 | 0.003 | 17.0 | 1710.2 | `9b7fa06621e0` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5918 | n/a | 0.1056 | 102.6827 | 0.003 | 18.0 | 1816.4 | `f176df9f99f1` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5834 | n/a | 0.1318 | 88.0217 | 0.003 | 17.4 | 1561.7 | `aff08443cb9b` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5717 | n/a | 0.0537 | 110.5196 | 0.003 | 18.0 | 2010.7 | `41164422f431` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5936 +- 0.0330 [worst 0.6410] | 0.6410 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1448 +- 0.0682 [worst 0.3074] | 0.3074 |
| ammo_efficiency | 102.6450 +- 9.5768 [worst 88.0217] | 88.0217 |
| latency_p50 | 0.0030 +- 0.0001 [worst 0.0031] | 0.0031 |
| latency_p90 | 0.0032 +- 0.0005 [worst 0.0055] | 0.0055 |
| shots_total | 17.4208 +- 0.6269 [worst 18.0000] | 18.0000 |
| destroyed_value | 1770.6458 +- 174.9048 [worst 1556.0000] | 1556.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
