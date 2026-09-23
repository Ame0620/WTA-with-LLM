# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 02:00:51

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6768 | n/a | 0.2631 | 87.4931 | 0.004 | 15.1 | 1330.4 | `d1d0307b263a` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.7284 | n/a | 0.2417 | 71.0458 | 0.003 | 16.0 | 1141.4 | `6b97c9e7e858` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.7123 | n/a | 0.3000 | 86.6915 | 0.003 | 16.0 | 1389.2 | `1aa7a2aefce2` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.7388 | n/a | 0.2354 | 66.6574 | 0.003 | 16.0 | 1077.9 | `06ae9dac8923` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.7496 | n/a | 0.3431 | 71.7507 | 0.004 | 17.0 | 1229.5 | `59336a9c3386` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6835 | n/a | 0.3222 | 92.1356 | 0.003 | 15.0 | 1388.0 | `d37c1668bf62` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.7056 | n/a | 0.2354 | 77.2087 | 0.003 | 16.0 | 1249.8 | `2dd3bf4759fd` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6979 | n/a | 0.1978 | 105.3429 | 0.003 | 15.0 | 1583.2 | `3feee7b6f66b` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6533 | n/a | 0.1216 | 86.8825 | 0.004 | 17.0 | 1514.2 | `52be281036e7` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.7496 | n/a | 0.3200 | 83.5601 | 0.003 | 15.0 | 1264.6 | `75eb9dc8e3bf` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6962 | n/a | 0.3822 | 88.1589 | 0.003 | 15.0 | 1329.7 | `dde8a97e1900` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.7162 | n/a | 0.2622 | 75.1593 | 0.003 | 15.0 | 1134.5 | `9453ad7a2f5e` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.7428 | n/a | 0.3267 | 71.1243 | 0.004 | 15.0 | 1068.6 | `4287c3ebf808` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6393 | n/a | 0.0771 | 93.3066 | 0.003 | 16.0 | 1500.0 | `0dc9a2516ae6` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.7016 | n/a | 0.3583 | 79.2906 | 0.003 | 16.0 | 1286.5 | `00575f3220bd` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.7252 | n/a | 0.3222 | 77.8946 | 0.003 | 15.0 | 1179.9 | `3a8a4669d121` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6832 | n/a | 0.2089 | 88.9770 | 0.004 | 15.0 | 1341.8 | `6516859c1809` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6485 | n/a | 0.2437 | 81.9647 | 0.003 | 16.0 | 1323.6 | `660c43e4835c` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6472 | n/a | 0.2143 | 94.2337 | 0.003 | 14.0 | 1320.4 | `61e81ef69e7e` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6942 | n/a | 0.3178 | 92.9980 | 0.003 | 15.0 | 1417.3 | `39467b216f1d` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6699 | n/a | 0.1267 | 103.8464 | 0.004 | 15.0 | 1572.5 | `81391e7a0a6b` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.7139 | n/a | 0.3222 | 84.4911 | 0.003 | 15.0 | 1273.3 | `4e56d4fb1408` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.7522 | n/a | 0.4208 | 57.3352 | 0.003 | 16.0 | 929.1 | `2f4c5798b4c3` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.7271 | n/a | 0.1137 | 75.0268 | 0.003 | 17.0 | 1281.2 | `5216bd08596a` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7022 +- 0.0336 [worst 0.7522] | 0.7522 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2615 +- 0.0876 [worst 0.4208] | 0.4208 |
| ammo_efficiency | 83.0240 +- 11.1787 [worst 57.3352] | 57.3352 |
| latency_p50 | 0.0033 +- 0.0003 [worst 0.0040] | 0.0040 |
| latency_p90 | 0.0037 +- 0.0008 [worst 0.0070] | 0.0070 |
| shots_total | 15.5444 +- 0.7608 [worst 17.0000] | 17.0000 |
| destroyed_value | 1296.9486 +- 156.9862 [worst 929.1333] | 929.1333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
