# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:54:33

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5656 | n/a | 0.0537 | 98.7352 | 0.004 | 18.0 | 1787.8 | `77c5abc41a95` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6133 | n/a | 0.1759 | 96.1134 | 0.004 | 18.0 | 1625.3 | `2bc433101b96` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6807 | n/a | 0.2074 | 85.8116 | 0.004 | 18.0 | 1541.7 | `d46744c1c4de` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6219 | n/a | 0.0130 | 86.0461 | 0.004 | 18.0 | 1560.0 | `62466461486b` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6245 | n/a | 0.1500 | 109.2467 | 0.004 | 18.0 | 1843.7 | `c2ce71a43d1e` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5267 | n/a | 0.0573 | 117.9762 | 0.004 | 17.5 | 2075.5 | `e0646f018157` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6681 | n/a | 0.1556 | 77.6526 | 0.004 | 18.0 | 1409.4 | `3f210892f8af` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6246 | n/a | 0.0574 | 108.8426 | 0.004 | 18.0 | 1967.4 | `97c77d3ceb6f` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6982 | n/a | 0.2074 | 81.3489 | 0.004 | 18.0 | 1318.0 | `ec18ab3a80c7` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6173 | n/a | 0.1056 | 113.1003 | 0.004 | 18.0 | 1932.8 | `f68057bfc910` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6168 | n/a | 0.1926 | 92.1915 | 0.004 | 18.0 | 1677.3 | `16cb2e656a0c` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6214 | n/a | 0.2519 | 83.8974 | 0.004 | 18.0 | 1513.1 | `7543780049c6` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6659 | n/a | 0.0817 | 80.6452 | 0.004 | 16.9 | 1387.9 | `be87a2fdc74f` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6066 | n/a | 0.0704 | 92.2413 | 0.004 | 18.0 | 1636.2 | `9575da40046c` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6542 | n/a | 0.2519 | 86.9876 | 0.004 | 18.0 | 1491.0 | `f15ff79af4ae` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6699 | n/a | 0.2000 | 77.3685 | 0.004 | 18.0 | 1417.5 | `e8e1da2d7c58` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5742 | n/a | 0.1000 | 98.8424 | 0.004 | 18.0 | 1803.7 | `83f53a00b0af` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5875 | n/a | 0.2093 | 85.5279 | 0.004 | 18.0 | 1553.4 | `ce3721a5650f` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6755 | n/a | 0.2130 | 75.7781 | 0.004 | 18.0 | 1214.4 | `1cf20fa569b5` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6548 | n/a | 0.1019 | 88.5426 | 0.004 | 18.0 | 1600.0 | `1d410e256f3f` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6911 | n/a | 0.1574 | 81.4931 | 0.004 | 18.0 | 1471.5 | `1a036eaff5aa` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5894 | n/a | 0.0981 | 101.2538 | 0.004 | 18.0 | 1827.2 | `87a904fe5f4f` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6021 | n/a | 0.0759 | 82.1337 | 0.004 | 18.0 | 1491.6 | `a57bb355f36a` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6367 | n/a | 0.0481 | 94.5419 | 0.004 | 18.0 | 1705.5 | `1db097c1a8fe` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6286 +- 0.0419 [worst 0.6982] | 0.6982 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1348 +- 0.0695 [worst 0.2519] | 0.2519 |
| ammo_efficiency | 91.5133 +- 11.6338 [worst 75.7781] | 75.7781 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0042 +- 0.0007 [worst 0.0070] | 0.0070 |
| shots_total | 17.9333 +- 0.2375 [worst 18.0000] | 18.0000 |
| destroyed_value | 1618.8292 +- 210.9317 [worst 1214.4333] | 1214.4333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
