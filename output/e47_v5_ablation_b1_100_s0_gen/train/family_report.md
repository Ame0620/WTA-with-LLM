# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:47:12

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.3951 | n/a | 0.2510 | 72.8075 | 0.015 | 70.0 | 5092.6 | `c12d335758c7` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.4202 | n/a | 0.2605 | 75.0138 | 0.015 | 70.0 | 5111.9 | `25511e60cf74` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.4438 | n/a | 0.2927 | 83.2959 | 0.015 | 68.1 | 5670.7 | `c4f600210135` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.4559 | n/a | 0.4043 | 67.4000 | 0.015 | 70.0 | 4448.6 | `62637b060e55` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.4387 | n/a | 0.3500 | 75.3177 | 0.015 | 70.0 | 5042.9 | `7c504b3a3d85` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.4438 | n/a | 0.3810 | 74.4907 | 0.015 | 68.2 | 5083.9 | `df3abcc82dd7` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.4234 | n/a | 0.2795 | 70.5741 | 0.015 | 70.0 | 4907.3 | `26a8dd1737a5` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.4147 | n/a | 0.3076 | 76.6707 | 0.015 | 70.0 | 5358.0 | `0ef86ad852d5` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.4502 | n/a | 0.3505 | 69.7087 | 0.015 | 70.0 | 4865.6 | `c8150ee765c8` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.4757 | n/a | 0.3624 | 67.0965 | 0.015 | 70.0 | 4671.2 | `77f538ad51f5` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.4513 | n/a | 0.3310 | 77.5650 | 0.015 | 70.0 | 5434.5 | `7500fb1653ad` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.4066 | n/a | 0.3155 | 78.7507 | 0.014 | 69.0 | 5453.3 | `b690ef03775a` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.4288 | n/a | 0.3362 | 67.8832 | 0.014 | 70.0 | 4519.8 | `cae3c9b6a952` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.4492 | n/a | 0.3633 | 70.0057 | 0.014 | 69.0 | 4695.8 | `4aa2488ed40e` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.4330 | n/a | 0.3471 | 73.3889 | 0.014 | 70.0 | 5128.3 | `14a4e8f6ea4b` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.4502 | n/a | 0.3463 | 79.1266 | 0.014 | 67.2 | 4949.2 | `5d3b7244a3e6` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.4214 | n/a | 0.3143 | 74.6865 | 0.014 | 70.0 | 5097.1 | `e87c0887c208` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.3773 | n/a | 0.3643 | 71.5225 | 0.014 | 70.0 | 4903.8 | `9126a9746c86` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.4410 | n/a | 0.2810 | 68.4140 | 0.014 | 70.0 | 4682.0 | `94ae80ae7c21` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.4395 | n/a | 0.2976 | 77.4477 | 0.014 | 70.0 | 5262.2 | `5f006e0c890d` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.4853 | n/a | 0.3743 | 69.0046 | 0.014 | 70.0 | 4839.0 | `092353c2b637` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.3998 | n/a | 0.3562 | 75.3621 | 0.014 | 70.0 | 5211.9 | `aa4f79dd9bfe` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.4536 | n/a | 0.3486 | 68.5691 | 0.015 | 70.0 | 4515.3 | `3cf127fc0604` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.4222 | n/a | 0.2657 | 75.5814 | 0.015 | 70.0 | 5186.6 | `a3f50bad3d7d` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4342 +- 0.0244 [worst 0.4853] | 0.4853 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3284 +- 0.0405 [worst 0.4043] | 0.4043 |
| ammo_efficiency | 73.3202 +- 4.2429 [worst 67.0965] | 67.0965 |
| latency_p50 | 0.0146 +- 0.0002 [worst 0.0151] | 0.0151 |
| latency_p90 | 0.0158 +- 0.0007 [worst 0.0191] | 0.0191 |
| shots_total | 69.6472 +- 0.7523 [worst 70.0000] | 70.0000 |
| destroyed_value | 5005.4889 +- 310.3451 [worst 4448.6000] | 4448.6000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
