# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:21:18

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.5434 | n/a | 0.2586 | 71.9177 | 0.020 | 54.0 | 3844.1 | `31631bc30866` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.5711 | n/a | 0.2660 | 72.5837 | 0.021 | 52.0 | 3781.9 | `7841dc6ed9ad` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.5950 | n/a | 0.3132 | 77.8842 | 0.021 | 53.0 | 4129.2 | `e86b71586c4a` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.5773 | n/a | 0.3145 | 64.8269 | 0.023 | 53.0 | 3455.8 | `bb497d38d317` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.5410 | n/a | 0.2641 | 81.6400 | 0.022 | 51.0 | 4123.9 | `bfb33285a369` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.5707 | n/a | 0.3393 | 78.3603 | 0.023 | 50.0 | 3924.5 | `e7a56e491adf` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.6059 | n/a | 0.2680 | 65.7865 | 0.021 | 51.0 | 3354.0 | `ef70fee17759` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.5433 | n/a | 0.2500 | 80.5826 | 0.021 | 52.0 | 4181.2 | `970da18b03bd` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.6007 | n/a | 0.3531 | 66.5312 | 0.021 | 54.0 | 3534.0 | `e89612634720` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.6076 | n/a | 0.2151 | 66.2640 | 0.021 | 53.0 | 3495.5 | `49e941433b40` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.6003 | n/a | 0.2705 | 76.0165 | 0.021 | 52.0 | 3958.7 | `b3445bcc1c70` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.5330 | n/a | 0.2920 | 79.2683 | 0.021 | 54.0 | 4291.8 | `eab1985daf05` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.5789 | n/a | 0.2508 | 62.7020 | 0.021 | 53.3 | 3331.9 | `0cb93ed5b75e` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.5305 | n/a | 0.2468 | 76.6809 | 0.021 | 52.0 | 4003.3 | `3e8f5454f5b7` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.5939 | n/a | 0.3564 | 70.1685 | 0.021 | 52.0 | 3673.1 | `fc025e3e1cf0` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.5969 | n/a | 0.2519 | 69.6744 | 0.021 | 52.1 | 3629.0 | `f72dd9d7968b` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.5456 | n/a | 0.2327 | 73.8119 | 0.021 | 54.0 | 4003.1 | `bd65f046a92e` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.5428 | n/a | 0.3064 | 69.6412 | 0.021 | 52.0 | 3600.2 | `b65298fc2e81` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.5365 | n/a | 0.2216 | 71.5924 | 0.021 | 54.0 | 3882.4 | `d869e56aae18` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.6341 | n/a | 0.3291 | 63.0221 | 0.021 | 55.0 | 3435.1 | `b684b0c08469` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.6373 | n/a | 0.3549 | 67.2697 | 0.021 | 51.0 | 3410.6 | `2e5e62b9123e` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.5235 | n/a | 0.2811 | 77.5661 | 0.021 | 53.0 | 4138.3 | `57c538e15e48` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.5997 | n/a | 0.3278 | 61.4498 | 0.021 | 54.0 | 3308.0 | `c99c825b387c` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.5751 | n/a | 0.2340 | 74.0673 | 0.021 | 51.0 | 3813.7 | `1ef0547f1133` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5743 +- 0.0326 [worst 0.6373] | 0.6373 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2832 +- 0.0431 [worst 0.3564] | 0.3564 |
| ammo_efficiency | 71.6379 +- 5.9033 [worst 61.4498] | 61.4498 |
| latency_p50 | 0.0211 +- 0.0006 [worst 0.0231] | 0.0231 |
| latency_p90 | 0.0237 +- 0.0017 [worst 0.0286] | 0.0286 |
| shots_total | 52.6014 +- 1.2588 [worst 55.0000] | 55.0000 |
| destroyed_value | 3762.6389 +- 297.6289 [worst 3307.9667] | 3307.9667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
