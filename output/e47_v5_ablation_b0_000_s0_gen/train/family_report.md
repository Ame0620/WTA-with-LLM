# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:02:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.4409 | n/a | 0.2893 | 68.2287 | 0.016 | 68.4 | 4707.3 | `0ccd2d6cf5a8` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.4511 | n/a | 0.2776 | 69.9410 | 0.017 | 69.3 | 4839.3 | `f145627002fd` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.4907 | n/a | 0.2962 | 78.4664 | 0.015 | 66.1 | 5192.3 | `1bdcd338900a` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.4527 | n/a | 0.3229 | 65.2048 | 0.021 | 68.1 | 4474.6 | `a62c26a69ccc` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.4567 | n/a | 0.2917 | 75.4800 | 0.015 | 65.1 | 4881.3 | `2c341826a9dc` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.4671 | n/a | 0.3513 | 77.5952 | 0.014 | 63.0 | 4871.6 | `175299698e09` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.4862 | n/a | 0.2747 | 66.9316 | 0.014 | 65.3 | 4373.3 | `886fa2890794` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.4387 | n/a | 0.2864 | 78.5268 | 0.015 | 66.0 | 5138.3 | `306ef9fd6bfa` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.4735 | n/a | 0.3052 | 68.6157 | 0.017 | 67.4 | 4659.9 | `9e234bc259fd` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.4883 | n/a | 0.2896 | 66.9548 | 0.018 | 69.2 | 4558.6 | `7ff9b7ddb6c3` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.5086 | n/a | 0.3681 | 70.5988 | 0.017 | 69.0 | 4867.6 | `ce1d392d4987` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.3824 | n/a | 0.2502 | 84.5620 | 0.017 | 67.0 | 5675.9 | `0e9813f988c7` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.4411 | n/a | 0.2609 | 64.2319 | 0.018 | 69.0 | 4422.6 | `3fd8bbf31af4` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.4506 | n/a | 0.3058 | 70.8320 | 0.018 | 66.1 | 4683.8 | `c48c6847e5a4` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.5207 | n/a | 0.3848 | 64.1435 | 0.016 | 68.0 | 4334.7 | `c39564105d04` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.5143 | n/a | 0.3365 | 69.1108 | 0.016 | 63.2 | 4372.3 | `53f11ce2e3bc` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.4841 | n/a | 0.2317 | 73.6019 | 0.015 | 62.1 | 4544.8 | `f1bb4cb29da9` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.4301 | n/a | 0.3370 | 67.7271 | 0.015 | 66.1 | 4488.3 | `1187fac196ff` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.4572 | n/a | 0.2202 | 72.0311 | 0.016 | 63.3 | 4546.7 | `180fb432063e` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.4931 | n/a | 0.3429 | 68.1307 | 0.015 | 70.0 | 4758.8 | `b1b8f3e1c347` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.5089 | n/a | 0.2973 | 73.1017 | 0.016 | 63.2 | 4617.4 | `13b1b447b0ec` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.4316 | n/a | 0.3525 | 73.1377 | 0.015 | 68.0 | 4936.4 | `e922aef29439` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.4593 | n/a | 0.3395 | 63.5272 | 0.015 | 70.0 | 4468.3 | `2be959f290bd` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.4451 | n/a | 0.2044 | 73.2443 | 0.015 | 68.0 | 4980.4 | `e7e1d8e598e9` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4655 +- 0.0319 [worst 0.5207] | 0.5207 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3007 +- 0.0455 [worst 0.3848] | 0.3848 |
| ammo_efficiency | 70.9969 +- 5.1401 [worst 63.5272] | 63.5272 |
| latency_p50 | 0.0162 +- 0.0016 [worst 0.0214] | 0.0214 |
| latency_p90 | 0.0203 +- 0.0038 [worst 0.0295] | 0.0295 |
| shots_total | 66.7000 +- 2.3496 [worst 70.0000] | 70.0000 |
| destroyed_value | 4724.7653 +- 307.5495 [worst 4334.7000] | 4334.7000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
