# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **mappo** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:14:50

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.4984 | n/a | 0.2855 | 63.9806 | 0.015 | 66.2 | 4223.1 | `c7c0419e05c4` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.4975 | n/a | 0.2797 | 64.9158 | 0.015 | 69.0 | 4430.5 | `7a0c5d5f436e` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.5471 | n/a | 0.3532 | 69.6460 | 0.015 | 67.1 | 4618.2 | `46af1bae4ccb` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.4706 | n/a | 0.2818 | 64.8653 | 0.015 | 66.0 | 4328.5 | `15b7b3ebd456` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.5827 | n/a | 0.3311 | 59.0471 | 0.015 | 63.7 | 3749.2 | `ee67388507af` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.4783 | n/a | 0.2922 | 75.4821 | 0.014 | 64.0 | 4768.7 | `8550c363cb78` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.5689 | n/a | 0.2920 | 56.2293 | 0.014 | 65.7 | 3669.1 | `328a28f966d9` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.4979 | n/a | 0.2939 | 69.4207 | 0.015 | 66.0 | 4596.4 | `acfc1d9d518b` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.5254 | n/a | 0.3090 | 62.6277 | 0.015 | 67.0 | 4200.2 | `f1d25dc9128d` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.5387 | n/a | 0.2928 | 60.1918 | 0.015 | 69.0 | 4110.1 | `799c4141d995` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.5908 | n/a | 0.4254 | 60.4496 | 0.015 | 67.0 | 4053.1 | `e009ad530a42` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.4878 | n/a | 0.3200 | 73.7187 | 0.015 | 65.0 | 4707.0 | `3ea628a0301a` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.5031 | n/a | 0.2667 | 57.3124 | 0.015 | 69.0 | 3931.6 | `0aa3e0fa3860` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.4859 | n/a | 0.2672 | 65.5513 | 0.015 | 67.0 | 4383.1 | `5f5b7556e896` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.5468 | n/a | 0.3957 | 58.9850 | 0.015 | 70.0 | 4098.9 | `514c73ed7415` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.5641 | n/a | 0.3403 | 58.1783 | 0.015 | 67.0 | 3923.9 | `85232e749c5d` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.5435 | n/a | 0.2727 | 60.8761 | 0.015 | 66.0 | 4021.9 | `ddd423eeba49` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.5128 | n/a | 0.3031 | 59.2371 | 0.015 | 65.0 | 3836.9 | `8f6153e6d80e` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.5352 | n/a | 0.2338 | 58.8489 | 0.015 | 66.3 | 3893.1 | `63b893296860` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.5832 | n/a | 0.3224 | 59.1075 | 0.015 | 67.0 | 3913.5 | `bab10b56a20d` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.6143 | n/a | 0.3594 | 56.5248 | 0.015 | 64.0 | 3626.0 | `605950484e67` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.4665 | n/a | 0.3574 | 68.5224 | 0.015 | 68.0 | 4632.7 | `d9f07166eab4` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.5494 | n/a | 0.3629 | 53.0218 | 0.015 | 70.0 | 3723.6 | `d272549d6d9f` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.5541 | n/a | 0.2758 | 60.4459 | 0.015 | 66.0 | 4002.6 | `74643fc0cb6e` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5310 +- 0.0403 [worst 0.6143] | 0.6143 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3131 +- 0.0443 [worst 0.4254] | 0.4254 |
| ammo_efficiency | 62.3828 +- 5.5484 [worst 53.0218] | 53.0218 |
| latency_p50 | 0.0148 +- 0.0003 [worst 0.0155] | 0.0155 |
| latency_p90 | 0.0164 +- 0.0020 [worst 0.0257] | 0.0257 |
| shots_total | 66.7083 +- 1.7402 [worst 70.0000] | 70.0000 |
| destroyed_value | 4143.4125 +- 337.5791 [worst 3626.0000] | 3626.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
