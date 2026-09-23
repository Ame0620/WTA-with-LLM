# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:07:27

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5539 | n/a | 0.1130 | 106.7740 | 0.003 | 18.0 | 1836.1 | `2901fceea544` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6295 | n/a | 0.2481 | 99.9147 | 0.003 | 16.5 | 1557.2 | `a6b82f358e47` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6038 | n/a | 0.0741 | 106.5538 | 0.003 | 18.0 | 1912.6 | `40d3806431b7` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6494 | n/a | 0.0039 | 88.6495 | 0.003 | 16.3 | 1446.6 | `b59fd1a6e24a` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6202 | n/a | 0.1537 | 101.5743 | 0.003 | 18.0 | 1864.7 | `cebbe5ebbdb2` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5115 | n/a | 0.0352 | 119.7645 | 0.003 | 18.0 | 2141.9 | `bdf0ef38e3a6` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6329 | n/a | 0.1619 | 89.8340 | 0.003 | 17.3 | 1558.9 | `b17f1b497295` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6119 | n/a | 0.1093 | 111.8348 | 0.003 | 18.0 | 2033.9 | `7575a181d756` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6519 | n/a | 0.2114 | 96.4320 | 0.003 | 17.0 | 1520.1 | `20d3c477b36b` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.5860 | n/a | 0.1111 | 119.4674 | 0.003 | 18.0 | 2090.9 | `8f3a07f94c7c` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5745 | n/a | 0.2019 | 107.0446 | 0.003 | 18.0 | 1862.3 | `676118042eee` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5992 | n/a | 0.2130 | 88.9267 | 0.003 | 18.0 | 1601.9 | `741ecc04a055` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6569 | n/a | 0.1705 | 82.5696 | 0.003 | 17.2 | 1425.4 | `9b486dcaf660` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5696 | n/a | 0.1074 | 98.5314 | 0.003 | 18.0 | 1789.9 | `27184a39feb9` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6498 | n/a | 0.2537 | 88.0454 | 0.003 | 18.0 | 1509.9 | `167ec9e21f6f` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6405 | n/a | 0.2136 | 87.8727 | 0.003 | 17.2 | 1543.6 | `8930d3637596` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5288 | n/a | 0.0204 | 109.9612 | 0.003 | 18.0 | 1995.8 | `9da20f9a3bc5` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5505 | n/a | 0.1741 | 93.2263 | 0.003 | 18.0 | 1692.9 | `318a42a35543` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6107 | n/a | 0.2398 | 87.2880 | 0.003 | 17.9 | 1457.3 | `b9efb0d4ffef` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5759 | n/a | 0.0593 | 108.6638 | 0.003 | 18.0 | 1965.8 | `2ca8a1162fc9` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6253 | n/a | 0.2074 | 98.8806 | 0.003 | 18.0 | 1784.9 | `5b6213f2e504` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5975 | n/a | 0.1593 | 98.8440 | 0.003 | 18.0 | 1790.9 | `5a3589ee3aa8` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6076 | n/a | 0.1573 | 89.9704 | 0.003 | 17.4 | 1471.1 | `61764076a2db` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5866 | n/a | 0.0981 | 107.5696 | 0.003 | 18.0 | 1940.6 | `2e36770a4e4d` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6010 +- 0.0386 [worst 0.6569] | 0.6569 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1457 +- 0.0711 [worst 0.2537] | 0.2537 |
| ammo_efficiency | 99.5081 +- 10.3089 [worst 82.5696] | 82.5696 |
| latency_p50 | 0.0031 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0033 +- 0.0006 [worst 0.0059] | 0.0059 |
| shots_total | 17.7000 +- 0.5041 [worst 18.0000] | 18.0000 |
| destroyed_value | 1741.4708 +- 220.6941 [worst 1425.4000] | 1425.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
