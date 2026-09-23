# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:30:27

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.4323 | n/a | 0.2643 | 70.9030 | 0.021 | 67.2 | 4779.8 | `3490106d6506` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.4310 | n/a | 0.2942 | 73.8445 | 0.021 | 69.7 | 5017.0 | `4bacbc018867` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.4468 | n/a | 0.2675 | 85.5530 | 0.020 | 66.0 | 5640.2 | `69d3110a93be` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.4570 | n/a | 0.3515 | 65.5083 | 0.020 | 68.1 | 4439.6 | `33cd7873b778` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.4275 | n/a | 0.3388 | 79.4474 | 0.021 | 66.9 | 5143.9 | `e6dcf529f53d` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.4521 | n/a | 0.4005 | 72.0095 | 0.022 | 70.0 | 5008.6 | `e6a5db4836ac` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.4279 | n/a | 0.2687 | 70.2941 | 0.021 | 69.8 | 4869.2 | `cf2c40f67444` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.4233 | n/a | 0.3138 | 75.4441 | 0.020 | 70.0 | 5279.4 | `2213fc616f82` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.4582 | n/a | 0.3502 | 70.7525 | 0.024 | 68.4 | 4794.9 | `0550a5ee9557` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.4525 | n/a | 0.2990 | 69.7959 | 0.022 | 70.0 | 4877.5 | `cc54ead7ec04` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.4350 | n/a | 0.3343 | 80.6141 | 0.022 | 70.0 | 5596.2 | `e1fd666d1cc9` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.3966 | n/a | 0.2676 | 79.3031 | 0.021 | 70.0 | 5544.8 | `b46f56a0da43` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.4294 | n/a | 0.3032 | 65.9731 | 0.021 | 68.2 | 4515.5 | `29e2cdd09d1f` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.4518 | n/a | 0.3638 | 66.9749 | 0.021 | 70.0 | 4673.7 | `f7b0786fbf95` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.4495 | n/a | 0.3186 | 73.2298 | 0.021 | 68.0 | 4978.8 | `c7f9e450ec80` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.4344 | n/a | 0.2921 | 74.7140 | 0.021 | 68.2 | 5091.9 | `a7e320fa13ff` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.4214 | n/a | 0.2766 | 74.8340 | 0.021 | 68.7 | 5097.4 | `78542a52e950` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.3790 | n/a | 0.3220 | 72.9724 | 0.021 | 67.2 | 4890.7 | `37605bd65fb0` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.4121 | n/a | 0.2722 | 71.4840 | 0.021 | 69.9 | 4924.1 | `7f10988e8c16` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.4456 | n/a | 0.2633 | 74.8691 | 0.021 | 70.0 | 5205.2 | `f72be14a1d16` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.4798 | n/a | 0.3243 | 73.0019 | 0.021 | 66.4 | 4890.7 | `936830f5271a` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.3964 | n/a | 0.3381 | 75.0480 | 0.021 | 69.9 | 5241.7 | `fa6f177dfb81` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.4365 | n/a | 0.2876 | 68.0592 | 0.021 | 70.0 | 4656.5 | `b6e5861fb7d9` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.4060 | n/a | 0.2605 | 75.7488 | 0.021 | 70.0 | 5331.3 | `9494309cf084` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4326 +- 0.0225 [worst 0.4798] | 0.4798 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3072 +- 0.0369 [worst 0.4005] | 0.4005 |
| ammo_efficiency | 73.3491 +- 4.6491 [worst 65.5083] | 65.5083 |
| latency_p50 | 0.0210 +- 0.0007 [worst 0.0236] | 0.0236 |
| latency_p90 | 0.0244 +- 0.0033 [worst 0.0374] | 0.0374 |
| shots_total | 68.8583 +- 1.3165 [worst 70.0000] | 70.0000 |
| destroyed_value | 5020.3625 +- 309.9397 [worst 4439.6333] | 4439.6333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
