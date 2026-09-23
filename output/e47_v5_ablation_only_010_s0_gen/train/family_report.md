# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:55:07

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.5540 | n/a | 0.3058 | 64.6502 | 0.011 | 58.1 | 3754.9 | `a6d3d20c2a3f` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.5396 | n/a | 0.2845 | 69.9565 | 0.011 | 58.0 | 4059.5 | `79f09c121df2` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.5996 | n/a | 0.3661 | 73.5228 | 0.010 | 56.0 | 4082.1 | `f46ac2cb1bb5` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.5290 | n/a | 0.2661 | 70.0669 | 0.011 | 55.0 | 3850.9 | `055675d78b85` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.5414 | n/a | 0.3557 | 71.7902 | 0.011 | 58.0 | 4120.9 | `9e5da6057005` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.5178 | n/a | 0.3483 | 73.8064 | 0.011 | 60.0 | 4408.1 | `fc05ef7bc850` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.6126 | n/a | 0.3030 | 60.2124 | 0.011 | 55.0 | 3296.9 | `58f6acf548d4` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.5015 | n/a | 0.2952 | 75.1502 | 0.010 | 60.3 | 4563.6 | `28f05b9fb5f4` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.5675 | n/a | 0.2709 | 69.4072 | 0.011 | 55.0 | 3827.9 | `ebc707d683a4` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.5837 | n/a | 0.2967 | 60.3786 | 0.010 | 61.0 | 3709.1 | `0eb0f7a04c8b` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.5583 | n/a | 0.2871 | 76.9776 | 0.011 | 57.0 | 4375.0 | `09c7a3896ea2` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.5041 | n/a | 0.2939 | 79.0626 | 0.011 | 58.1 | 4557.2 | `936ec5074940` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.5466 | n/a | 0.2718 | 61.6174 | 0.010 | 58.0 | 3587.5 | `175a78f73013` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.5432 | n/a | 0.3017 | 65.2297 | 0.011 | 60.1 | 3894.8 | `5f5244f787d1` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.5801 | n/a | 0.3374 | 66.6113 | 0.011 | 57.0 | 3797.9 | `6a8901dca398` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.5798 | n/a | 0.2890 | 67.5505 | 0.011 | 56.2 | 3782.7 | `727f3757a638` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.5683 | n/a | 0.3073 | 68.5891 | 0.011 | 55.0 | 3803.1 | `986f339baa23` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.5188 | n/a | 0.2780 | 71.8724 | 0.011 | 53.0 | 3789.5 | `9d4639113f7e` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.5520 | n/a | 0.2693 | 67.3160 | 0.010 | 55.6 | 3752.6 | `afe35d53056f` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.5933 | n/a | 0.3249 | 64.6930 | 0.011 | 59.0 | 3818.3 | `e267bee4917c` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.6575 | n/a | 0.3540 | 65.0567 | 0.011 | 50.0 | 3220.2 | `fa681e00e8e9` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.5299 | n/a | 0.3413 | 71.1727 | 0.011 | 57.0 | 4082.2 | `d7ce306e863a` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.5330 | n/a | 0.3290 | 62.5962 | 0.011 | 62.0 | 3859.1 | `b178ab66036d` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.5622 | n/a | 0.2555 | 68.8552 | 0.011 | 57.1 | 3929.4 | `b0efc6e9d33d` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5572 +- 0.0355 [worst 0.6575] | 0.6575 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3055 +- 0.0313 [worst 0.3661] | 0.3661 |
| ammo_efficiency | 68.5893 +- 4.9596 [worst 60.2124] | 60.2124 |
| latency_p50 | 0.0108 +- 0.0003 [worst 0.0112] | 0.0112 |
| latency_p90 | 0.0115 +- 0.0008 [worst 0.0150] | 0.0150 |
| shots_total | 57.1444 +- 2.6150 [worst 62.0000] | 62.0000 |
| destroyed_value | 3913.4583 +- 326.4580 [worst 3220.1667] | 3220.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
