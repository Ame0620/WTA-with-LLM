# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:50:19

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6531 | n/a | 0.1556 | 77.4258 | 0.003 | 18.0 | 1427.8 | `0958cc6f1068` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6888 | n/a | 0.0667 | 75.6579 | 0.004 | 17.0 | 1308.2 | `6b0c2abe589f` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.7125 | n/a | 0.1648 | 76.0700 | 0.003 | 18.0 | 1387.8 | `486fca75f2b8` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.7478 | n/a | 0.2255 | 60.3410 | 0.003 | 17.0 | 1040.6 | `5b2d486f2100` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6889 | n/a | 0.1163 | 86.3706 | 0.003 | 17.2 | 1527.6 | `bfc284105de6` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6179 | n/a | 0.1426 | 92.1124 | 0.004 | 18.0 | 1675.7 | `e51e486eebdf` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6422 | n/a | 0.1630 | 83.0484 | 0.003 | 18.0 | 1519.3 | `228641cdad5c` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6371 | n/a | 0.0519 | 105.3283 | 0.003 | 18.0 | 1902.1 | `05d47672a32f` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6630 | n/a | 0.1137 | 88.6597 | 0.003 | 17.0 | 1471.8 | `448700dc051f` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6716 | n/a | 0.1056 | 92.2558 | 0.004 | 18.0 | 1658.6 | `47fabd5fed6a` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6711 | n/a | 0.2519 | 79.1883 | 0.003 | 18.0 | 1439.6 | `2c8c73ddf7aa` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6828 | n/a | 0.1741 | 69.2781 | 0.003 | 18.0 | 1268.0 | `97a73f6db855` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.7183 | n/a | 0.1630 | 62.9302 | 0.003 | 18.0 | 1170.3 | `7e5074cbbc11` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6590 | n/a | 0.1588 | 82.1799 | 0.003 | 17.0 | 1418.2 | `6783beaeec5d` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6801 | n/a | 0.2216 | 80.3045 | 0.003 | 17.0 | 1379.4 | `460d31fe88e9` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.7208 | n/a | 0.1574 | 66.0443 | 0.003 | 18.0 | 1198.8 | `716ddfcc8fcd` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6002 | n/a | 0.0019 | 93.3947 | 0.003 | 18.0 | 1693.4 | `668e8f809743` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6528 | n/a | 0.2759 | 73.5847 | 0.003 | 18.0 | 1307.5 | `d2f7c433c644` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6475 | n/a | 0.2196 | 76.2144 | 0.004 | 17.0 | 1319.3 | `73354b3b3396` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6549 | n/a | 0.1648 | 88.9458 | 0.003 | 18.0 | 1599.7 | `3c7a7171a8cc` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6539 | n/a | 0.1020 | 94.8783 | 0.003 | 17.0 | 1648.7 | `02bec89d8cbe` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6268 | n/a | 0.0870 | 90.9028 | 0.003 | 18.0 | 1660.9 | `8c763163c870` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6557 | n/a | 0.0537 | 71.6917 | 0.004 | 18.0 | 1290.8 | `f3ca437ed815` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.7168 | n/a | 0.0000 | 73.7754 | 0.003 | 18.0 | 1329.5 | `9d36d07c2b75` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6693 +- 0.0349 [worst 0.7478] | 0.7478 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1390 +- 0.0712 [worst 0.2759] | 0.2759 |
| ammo_efficiency | 80.8576 +- 10.8831 [worst 60.3410] | 60.3410 |
| latency_p50 | 0.0031 +- 0.0003 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0035 +- 0.0007 [worst 0.0063] | 0.0063 |
| shots_total | 17.6736 +- 0.4627 [worst 18.0000] | 18.0000 |
| destroyed_value | 1443.4875 +- 196.2828 [worst 1040.6000] | 1040.6000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
