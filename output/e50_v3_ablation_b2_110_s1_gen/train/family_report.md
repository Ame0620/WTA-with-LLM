# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:55:06

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5741 | n/a | 0.1611 | 96.6099 | 0.003 | 18.0 | 1753.2 | `e40422dc8d42` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6662 | n/a | 0.1784 | 81.3605 | 0.003 | 17.0 | 1403.1 | `97dff7d03423` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6919 | n/a | 0.1667 | 87.2056 | 0.004 | 17.0 | 1487.3 | `d0b9435f671f` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6959 | n/a | 0.1176 | 73.7078 | 0.003 | 17.0 | 1254.8 | `2610b4a7c16a` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6766 | n/a | 0.2216 | 93.2729 | 0.003 | 17.0 | 1588.1 | `7fa0404035e7` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6136 | n/a | 0.1771 | 104.8992 | 0.003 | 16.0 | 1694.4 | `497d4e64074f` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6683 | n/a | 0.1667 | 82.5891 | 0.003 | 17.0 | 1408.6 | `e4d5316e5706` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6334 | n/a | 0.0588 | 111.7395 | 0.003 | 17.0 | 1921.2 | `c2adc5734e46` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6520 | n/a | 0.0706 | 88.0364 | 0.003 | 17.0 | 1519.7 | `425ed0876344` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6874 | n/a | 0.2354 | 97.9391 | 0.003 | 16.0 | 1579.0 | `89bb39842117` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6631 | n/a | 0.2437 | 91.7670 | 0.003 | 16.0 | 1474.7 | `db476edb5db5` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6118 | n/a | 0.1059 | 90.4255 | 0.003 | 17.0 | 1551.7 | `1b63e6f05fdf` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6903 | n/a | 0.1229 | 80.0823 | 0.003 | 16.0 | 1286.4 | `3d76326898e6` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5680 | n/a | 0.0000 | 100.2204 | 0.003 | 18.0 | 1796.5 | `cad0cea23d2d` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6433 | n/a | 0.2216 | 89.6013 | 0.003 | 17.0 | 1538.2 | `24a813283a4f` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6895 | n/a | 0.1812 | 83.2342 | 0.004 | 16.0 | 1333.3 | `3f3bbe8a5201` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6073 | n/a | 0.1167 | 103.3883 | 0.003 | 16.0 | 1663.4 | `f6e95a265700` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6352 | n/a | 0.2843 | 79.6939 | 0.003 | 17.0 | 1373.8 | `865cf9e039dc` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6438 | n/a | 0.2417 | 82.3591 | 0.003 | 16.0 | 1333.1 | `8009aeec31a9` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6455 | n/a | 0.1137 | 97.0970 | 0.004 | 17.0 | 1643.2 | `f8664db47f23` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6807 | n/a | 0.1688 | 95.7511 | 0.003 | 16.0 | 1521.1 | `4b96bc99f0a4` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6422 | n/a | 0.0870 | 88.8219 | 0.003 | 18.0 | 1592.0 | `dc33954e9216` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.7194 | n/a | 0.2467 | 68.9726 | 0.003 | 15.0 | 1051.8 | `0e84795a5050` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6489 | n/a | 0.0000 | 96.6548 | 0.004 | 17.0 | 1648.1 | `20fdd4525b41` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6520 +- 0.0373 [worst 0.7194] | 0.7194 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1537 +- 0.0750 [worst 0.2843] | 0.2843 |
| ammo_efficiency | 90.2262 +- 9.9679 [worst 68.9726] | 68.9726 |
| latency_p50 | 0.0032 +- 0.0002 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0035 +- 0.0006 [worst 0.0060] | 0.0060 |
| shots_total | 16.7083 +- 0.7348 [worst 18.0000] | 18.0000 |
| destroyed_value | 1517.3583 +- 188.5481 [worst 1051.8333] | 1051.8333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
