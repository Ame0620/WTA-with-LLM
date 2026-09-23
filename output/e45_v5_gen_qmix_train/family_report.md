# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **qmix** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:22:49

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.6867 | n/a | 0.3771 | 38.0853 | 0.014 | 70.0 | 2637.5 | `e520677f614d` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.7049 | n/a | 0.4186 | 39.4651 | 0.014 | 70.0 | 2601.9 | `e89bd9950555` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.6463 | n/a | 0.3286 | 52.8852 | 0.014 | 70.0 | 3606.5 | `7c66bb04dc97` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.6698 | n/a | 0.3571 | 42.5916 | 0.014 | 70.0 | 2699.7 | `2820b7b9f6e6` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.6689 | n/a | 0.4271 | 45.4416 | 0.014 | 70.0 | 2975.0 | `fafed441528d` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.6575 | n/a | 0.3774 | 44.1840 | 0.014 | 69.7 | 3131.1 | `53aaad16e69f` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.7267 | n/a | 0.4314 | 34.4361 | 0.014 | 70.0 | 2326.0 | `b132e325970d` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.6352 | n/a | 0.3957 | 49.8290 | 0.014 | 70.0 | 3339.4 | `adde67ecbadb` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.6583 | n/a | 0.3857 | 44.1775 | 0.014 | 70.0 | 3024.2 | `f8417dd34d11` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.7381 | n/a | 0.4029 | 34.6668 | 0.014 | 70.0 | 2333.5 | `cb55078e01a4` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.7060 | n/a | 0.4343 | 44.6303 | 0.014 | 70.0 | 2911.7 | `eb0d7a8703d2` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.6829 | n/a | 0.3683 | 42.0599 | 0.014 | 69.5 | 2914.1 | `827eeb36572c` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.6991 | n/a | 0.4343 | 35.6990 | 0.014 | 70.0 | 2380.9 | `455d9d9778a8` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.7247 | n/a | 0.4271 | 34.2811 | 0.014 | 70.0 | 2347.4 | `83095361a29c` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.7132 | n/a | 0.3957 | 37.8547 | 0.014 | 70.0 | 2593.7 | `ef7c73176363` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.7350 | n/a | 0.4100 | 34.2186 | 0.014 | 70.0 | 2385.6 | `a3b2d7593f06` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.6758 | n/a | 0.3871 | 41.1850 | 0.014 | 70.0 | 2856.1 | `6dc472759349` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.6404 | n/a | 0.3529 | 40.9143 | 0.014 | 70.0 | 2832.2 | `caec0664aeff` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.7382 | n/a | 0.4557 | 31.4380 | 0.014 | 70.0 | 2192.7 | `f07f59778394` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.7347 | n/a | 0.4671 | 36.2580 | 0.014 | 70.0 | 2491.0 | `5417e9a9dcbf` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.7290 | n/a | 0.3714 | 39.3275 | 0.014 | 70.0 | 2547.9 | `1695023e415d` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.6705 | n/a | 0.3814 | 41.5319 | 0.014 | 70.0 | 2861.7 | `af8a40d20877` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.6967 | n/a | 0.3390 | 35.7489 | 0.014 | 69.9 | 2506.6 | `9b282620ebcd` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.7364 | n/a | 0.4286 | 34.9841 | 0.014 | 70.0 | 2365.9 | `78911b7005a9` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6948 +- 0.0332 [worst 0.7382] | 0.7382 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3981 +- 0.0354 [worst 0.4671] | 0.4671 |
| ammo_efficiency | 39.8289 +- 5.1924 [worst 31.4380] | 31.4380 |
| latency_p50 | 0.0141 +- 0.0002 [worst 0.0145] | 0.0145 |
| latency_p90 | 0.0162 +- 0.0020 [worst 0.0251] | 0.0251 |
| shots_total | 69.9625 +- 0.1148 [worst 70.0000] | 70.0000 |
| destroyed_value | 2702.5958 +- 344.7740 [worst 2192.7000] | 2192.7000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
