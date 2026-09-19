# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_5x100_K10_s03.txt', 'dn_5x100_K10_s04.txt', 'dn_5x100_K10_s05.txt', 'dn_5x100_K10_s06.txt', 'dn_5x100_K10_s07.txt', 'dn_5x100_K10_s08.txt', 'dn_5x100_K10_s09.txt', 'dn_5x100_K10_s10.txt', 'dn_5x100_K10_s11.txt', 'dn_5x100_K10_s12.txt', 'dn_5x100_K10_s13.txt', 'dn_5x100_K10_s14.txt', 'dn_5x100_K10_s15.txt', 'dn_5x100_K10_s16.txt', 'dn_5x100_K10_s17.txt', 'dn_5x100_K10_s18.txt', 'dn_5x100_K10_s19.txt', 'dn_5x100_K10_s20.txt', 'dn_5x100_K10_s21.txt', 'dn_5x100_K10_s22.txt', 'dn_5x100_K10_s23.txt', 'dn_5x100_K10_s24.txt', 'dn_5x100_K10_s25.txt', 'dn_5x100_K10_s26.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:27:22

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s03.txt` | 8419 | 0.6428 | n/a | 0.0755 | 106.8040 | 0.008 | 28.2 | 3007.3 | `2db134b90eb9` |
| `dn_5x100_K10_s04.txt` | 8817 | 0.6582 | n/a | 0.2133 | 101.7447 | 0.008 | 30.0 | 3013.7 | `95921bd712dd` |
| `dn_5x100_K10_s05.txt` | 10196 | 0.6764 | n/a | 0.1545 | 113.2118 | 0.008 | 29.1 | 3299.0 | `1a5a43135f94` |
| `dn_5x100_K10_s06.txt` | 8176 | 0.6352 | n/a | 0.1933 | 98.7280 | 0.008 | 30.0 | 2982.5 | `ad2bb66d8237` |
| `dn_5x100_K10_s07.txt` | 8985 | 0.6883 | n/a | 0.2856 | 91.6536 | 0.008 | 30.0 | 2800.5 | `6492795ea687` |
| `dn_5x100_K10_s08.txt` | 9141 | 0.6537 | n/a | 0.1933 | 106.4697 | 0.008 | 30.0 | 3165.4 | `b93f474e420b` |
| `dn_5x100_K10_s09.txt` | 8511 | 0.6672 | n/a | 0.2244 | 94.3614 | 0.009 | 30.0 | 2832.4 | `15257b432dfd` |
| `dn_5x100_K10_s10.txt` | 9155 | 0.6495 | n/a | 0.1956 | 108.1132 | 0.009 | 30.0 | 3208.8 | `8098af4ab34c` |
| `dn_5x100_K10_s11.txt` | 8850 | 0.6807 | n/a | 0.2690 | 96.5973 | 0.008 | 29.1 | 2826.1 | `a03bab6232b6` |
| `dn_5x100_K10_s12.txt` | 8909 | 0.6947 | n/a | 0.2437 | 97.2882 | 0.009 | 28.2 | 2720.3 | `981d7d89adae` |
| `dn_5x100_K10_s13.txt` | 9905 | 0.6581 | n/a | 0.1511 | 112.2369 | 0.008 | 30.0 | 3386.6 | `26f942bd18fe` |
| `dn_5x100_K10_s14.txt` | 9190 | 0.6373 | n/a | 0.1911 | 110.8334 | 0.008 | 30.0 | 3333.2 | `ea07931ae062` |
| `dn_5x100_K10_s15.txt` | 7913 | 0.6126 | n/a | 0.0834 | 104.1783 | 0.009 | 29.3 | 3065.6 | `5e425591a463` |
| `dn_5x100_K10_s16.txt` | 8526 | 0.6617 | n/a | 0.1420 | 99.1451 | 0.012 | 29.1 | 2884.5 | `f98ba45e5ac6` |
| `dn_5x100_K10_s17.txt` | 9044 | 0.6715 | n/a | 0.2148 | 98.6799 | 0.011 | 29.9 | 2971.3 | `375a97039892` |
| `dn_5x100_K10_s18.txt` | 9002 | 0.6274 | n/a | 0.0967 | 111.1709 | 0.010 | 30.0 | 3354.0 | `7e5b3b036b10` |
| `dn_5x100_K10_s19.txt` | 8810 | 0.6459 | n/a | 0.1589 | 104.2892 | 0.010 | 30.0 | 3119.6 | `7e3bb3dc6a1c` |
| `dn_5x100_K10_s20.txt` | 7875 | 0.6223 | n/a | 0.1767 | 99.3628 | 0.008 | 30.0 | 2974.3 | `abc586956f7a` |
| `dn_5x100_K10_s21.txt` | 8376 | 0.6778 | n/a | 0.1749 | 94.7809 | 0.008 | 28.2 | 2698.3 | `83c4efc81aab` |
| `dn_5x100_K10_s22.txt` | 9389 | 0.6768 | n/a | 0.1844 | 100.6796 | 0.008 | 30.0 | 3034.8 | `be3506d5d346` |
| `dn_5x100_K10_s23.txt` | 9402 | 0.7390 | n/a | 0.3246 | 83.8469 | 0.008 | 29.1 | 2454.2 | `0a26c393d15a` |
| `dn_5x100_K10_s24.txt` | 8684 | 0.6652 | n/a | 0.2511 | 95.8388 | 0.008 | 30.0 | 2907.7 | `829778869993` |
| `dn_5x100_K10_s25.txt` | 8264 | 0.6230 | n/a | 0.1621 | 106.5005 | 0.008 | 29.0 | 3115.6 | `11ef6ba8294e` |
| `dn_5x100_K10_s26.txt` | 8976 | 0.6507 | n/a | 0.0970 | 108.1355 | 0.008 | 28.5 | 3135.1 | `cc5602194a4e` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6590 +- 0.0272 [worst 0.7390] | 0.7390 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1857 +- 0.0616 [worst 0.3246] | 0.3246 |
| ammo_efficiency | 101.8604 +- 7.1166 [worst 83.8469] | 83.8469 |
| latency_p50 | 0.0087 +- 0.0011 [worst 0.0122] | 0.0122 |
| latency_p90 | 0.0108 +- 0.0019 [worst 0.0170] | 0.0170 |
| shots_total | 29.4889 +- 0.6619 [worst 30.0000] | 30.0000 |
| destroyed_value | 3012.1125 +- 222.0326 [worst 2454.2333] | 2454.2333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
