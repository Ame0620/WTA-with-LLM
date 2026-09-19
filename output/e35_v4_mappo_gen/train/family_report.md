# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_5x100_K10_s03.txt', 'dn_5x100_K10_s04.txt', 'dn_5x100_K10_s05.txt', 'dn_5x100_K10_s06.txt', 'dn_5x100_K10_s07.txt', 'dn_5x100_K10_s08.txt', 'dn_5x100_K10_s09.txt', 'dn_5x100_K10_s10.txt', 'dn_5x100_K10_s11.txt', 'dn_5x100_K10_s12.txt', 'dn_5x100_K10_s13.txt', 'dn_5x100_K10_s14.txt', 'dn_5x100_K10_s15.txt', 'dn_5x100_K10_s16.txt', 'dn_5x100_K10_s17.txt', 'dn_5x100_K10_s18.txt', 'dn_5x100_K10_s19.txt', 'dn_5x100_K10_s20.txt', 'dn_5x100_K10_s21.txt', 'dn_5x100_K10_s22.txt', 'dn_5x100_K10_s23.txt', 'dn_5x100_K10_s24.txt', 'dn_5x100_K10_s25.txt', 'dn_5x100_K10_s26.txt']) | policy: **mappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:26:11

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s03.txt` | 8419 | 0.6925 | n/a | 0.0289 | 85.2606 | 0.007 | 30.0 | 2588.9 | `9aa4e93e7665` |
| `dn_5x100_K10_s04.txt` | 8817 | 0.7048 | n/a | 0.1300 | 86.8729 | 0.006 | 30.0 | 2602.4 | `4bc3e338d801` |
| `dn_5x100_K10_s05.txt` | 10196 | 0.7118 | n/a | 0.1532 | 101.1859 | 0.006 | 28.9 | 2938.4 | `daabbab0b7f6` |
| `dn_5x100_K10_s06.txt` | 8176 | 0.7030 | n/a | 0.2036 | 86.1776 | 0.006 | 28.0 | 2428.4 | `ca339eb53c7c` |
| `dn_5x100_K10_s07.txt` | 8985 | 0.7033 | n/a | 0.0702 | 94.5173 | 0.006 | 28.0 | 2665.8 | `c6280b99aa7a` |
| `dn_5x100_K10_s08.txt` | 9141 | 0.6939 | n/a | 0.1533 | 93.1011 | 0.006 | 30.0 | 2798.4 | `8674eb7c7206` |
| `dn_5x100_K10_s09.txt` | 8511 | 0.7252 | n/a | 0.0944 | 76.9832 | 0.006 | 30.0 | 2339.1 | `905028ec00c2` |
| `dn_5x100_K10_s10.txt` | 9155 | 0.7095 | n/a | 0.1267 | 89.7140 | 0.006 | 30.0 | 2659.9 | `4a676a52b94d` |
| `dn_5x100_K10_s11.txt` | 8850 | 0.7425 | n/a | 0.1322 | 78.2471 | 0.006 | 29.0 | 2278.7 | `cbfa08ed57a6` |
| `dn_5x100_K10_s12.txt` | 8909 | 0.7157 | n/a | 0.0956 | 83.3352 | 0.006 | 30.0 | 2533.1 | `d2e95ad5421c` |
| `dn_5x100_K10_s13.txt` | 9905 | 0.7174 | n/a | 0.2511 | 93.4859 | 0.006 | 30.0 | 2799.1 | `4cfe24be3337` |
| `dn_5x100_K10_s14.txt` | 9190 | 0.7223 | n/a | 0.1931 | 87.9792 | 0.006 | 29.0 | 2551.7 | `401f3de0eef0` |
| `dn_5x100_K10_s15.txt` | 7913 | 0.7151 | n/a | 0.1278 | 74.2795 | 0.006 | 30.0 | 2254.0 | `a4d156ceab70` |
| `dn_5x100_K10_s16.txt` | 8526 | 0.7552 | n/a | 0.2411 | 69.5133 | 0.006 | 30.0 | 2087.5 | `0584f05276ec` |
| `dn_5x100_K10_s17.txt` | 9044 | 0.7648 | n/a | 0.1900 | 70.8994 | 0.006 | 30.0 | 2126.8 | `26f720358854` |
| `dn_5x100_K10_s18.txt` | 9002 | 0.7655 | n/a | 0.1691 | 77.9594 | 0.006 | 27.0 | 2111.3 | `a6901b1434b7` |
| `dn_5x100_K10_s19.txt` | 8810 | 0.7046 | n/a | 0.1522 | 86.3501 | 0.006 | 30.0 | 2602.3 | `a5b9950dec98` |
| `dn_5x100_K10_s20.txt` | 7875 | 0.6859 | n/a | 0.1286 | 87.9124 | 0.006 | 28.0 | 2473.8 | `a4af119edfc4` |
| `dn_5x100_K10_s21.txt` | 8376 | 0.7435 | n/a | 0.0967 | 70.2599 | 0.006 | 30.0 | 2148.1 | `54c0b57fab68` |
| `dn_5x100_K10_s22.txt` | 9389 | 0.7776 | n/a | 0.2189 | 69.4222 | 0.006 | 30.0 | 2088.4 | `71b17c53e9c1` |
| `dn_5x100_K10_s23.txt` | 9402 | 0.7437 | n/a | 0.1012 | 85.3432 | 0.006 | 28.0 | 2409.7 | `1bf23029de9a` |
| `dn_5x100_K10_s24.txt` | 8684 | 0.6912 | n/a | 0.0966 | 91.7849 | 0.006 | 29.0 | 2681.7 | `4dca4133128a` |
| `dn_5x100_K10_s25.txt` | 8264 | 0.7096 | n/a | 0.0589 | 79.0126 | 0.006 | 30.0 | 2400.3 | `bf297aca9a1b` |
| `dn_5x100_K10_s26.txt` | 8976 | 0.7363 | n/a | 0.0653 | 84.2281 | 0.006 | 28.1 | 2366.7 | `d548058b90e1` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7223 +- 0.0252 [worst 0.7776] | 0.7776 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1366 +- 0.0572 [worst 0.2511] | 0.2511 |
| ammo_efficiency | 83.4927 +- 8.5156 [worst 69.4222] | 69.4222 |
| latency_p50 | 0.0058 +- 0.0003 [worst 0.0066] | 0.0066 |
| latency_p90 | 0.0070 +- 0.0008 [worst 0.0102] | 0.0102 |
| shots_total | 29.2917 +- 0.9317 [worst 30.0000] | 30.0000 |
| destroyed_value | 2455.5986 +- 239.1712 [worst 2087.4667] | 2087.4667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
