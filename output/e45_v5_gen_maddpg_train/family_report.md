# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **maddpg** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:30:50

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.5439 | n/a | 0.2357 | 54.9299 | 0.015 | 70.0 | 3839.7 | `1329a48be1a0` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.5946 | n/a | 0.2700 | 50.4785 | 0.014 | 70.0 | 3574.4 | `bd92d4469518` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.5369 | n/a | 0.2743 | 67.3513 | 0.014 | 70.0 | 4721.7 | `941147d31f41` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.5282 | n/a | 0.2629 | 55.7717 | 0.015 | 70.0 | 3857.8 | `10187a111be2` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.5603 | n/a | 0.2743 | 57.5630 | 0.014 | 70.0 | 3950.7 | `990a4bae00f4` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.5381 | n/a | 0.3143 | 59.6236 | 0.014 | 70.0 | 4222.5 | `b917752228db` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.5910 | n/a | 0.2443 | 49.2081 | 0.015 | 70.0 | 3480.9 | `d199b38fa2e8` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.5403 | n/a | 0.3271 | 60.6446 | 0.014 | 70.0 | 4208.4 | `cd37ae43ebe0` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.5700 | n/a | 0.3186 | 54.3456 | 0.015 | 70.0 | 3805.9 | `db056e847b45` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.5800 | n/a | 0.2186 | 53.1680 | 0.014 | 70.0 | 3742.0 | `53000ac7f10d` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.5598 | n/a | 0.2757 | 63.2594 | 0.015 | 70.0 | 4360.1 | `e2bfc142843b` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.5224 | n/a | 0.2771 | 62.4522 | 0.014 | 70.0 | 4389.4 | `23ee14c41271` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.5310 | n/a | 0.2186 | 53.5700 | 0.014 | 70.0 | 3711.5 | `195d40f5fb36` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.5861 | n/a | 0.3243 | 50.1689 | 0.014 | 70.0 | 3529.1 | `dd732c88fc19` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.6351 | n/a | 0.3786 | 47.6428 | 0.014 | 70.0 | 3300.0 | `beb619620beb` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.5804 | n/a | 0.2771 | 54.6675 | 0.015 | 70.0 | 3777.4 | `deb783142438` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.5404 | n/a | 0.2014 | 57.5855 | 0.014 | 70.0 | 4049.3 | `16db3e73d219` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.4956 | n/a | 0.2657 | 57.8468 | 0.014 | 70.0 | 3972.4 | `0b1581d1b008` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.6052 | n/a | 0.2643 | 47.5937 | 0.014 | 70.0 | 3306.7 | `eed13298641d` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.6189 | n/a | 0.3229 | 51.7976 | 0.014 | 70.0 | 3578.4 | `cbc1bb3fe748` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.5881 | n/a | 0.2814 | 55.8688 | 0.015 | 70.0 | 3873.1 | `81689508c1fa` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.5247 | n/a | 0.3129 | 59.6138 | 0.014 | 70.0 | 4127.6 | `85fa47ed9402` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.6215 | n/a | 0.3114 | 45.2616 | 0.014 | 70.0 | 3128.2 | `2183a7a6ccdf` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.5936 | n/a | 0.2100 | 52.1453 | 0.015 | 70.0 | 3647.7 | `d6f40a48d533` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5661 +- 0.0356 [worst 0.6351] | 0.6351 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2776 +- 0.0424 [worst 0.3786] | 0.3786 |
| ammo_efficiency | 55.1066 +- 5.3181 [worst 45.2616] | 45.2616 |
| latency_p50 | 0.0144 +- 0.0001 [worst 0.0148] | 0.0148 |
| latency_p90 | 0.0164 +- 0.0021 [worst 0.0259] | 0.0259 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 3839.7875 +- 371.0860 [worst 3128.2000] | 3128.2000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
