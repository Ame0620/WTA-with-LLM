# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:16:28

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5488 | n/a | 0.1593 | 108.5080 | 0.004 | 18.0 | 1857.0 | `dbb97b565392` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6009 | n/a | 0.1733 | 96.4385 | 0.004 | 17.2 | 1677.3 | `98ddd1ab8cc0` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6707 | n/a | 0.2037 | 87.3630 | 0.004 | 18.0 | 1590.0 | `52c9f26b749a` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.5980 | n/a | 0.0412 | 95.5662 | 0.004 | 17.0 | 1658.7 | `70821e5fe9d9` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6006 | n/a | 0.1593 | 106.6519 | 0.004 | 18.0 | 1960.9 | `4357bc571bdf` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5130 | n/a | 0.0037 | 118.7757 | 0.004 | 18.0 | 2135.5 | `210194f35d27` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6120 | n/a | 0.1611 | 89.5037 | 0.004 | 18.0 | 1647.6 | `74686f804a03` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.5924 | n/a | 0.0725 | 117.3925 | 0.004 | 17.9 | 2136.1 | `50a50cc362a3` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6345 | n/a | 0.1926 | 97.5370 | 0.004 | 18.0 | 1596.3 | `cfdb974dbe42` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6169 | n/a | 0.1278 | 111.7902 | 0.004 | 18.0 | 1935.1 | `fe0510b4650e` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5549 | n/a | 0.1704 | 106.0790 | 0.004 | 18.0 | 1948.1 | `1011b1303c28` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6102 | n/a | 0.2347 | 91.2472 | 0.004 | 17.0 | 1557.9 | `1a164770441e` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6262 | n/a | 0.1481 | 85.1158 | 0.004 | 18.0 | 1552.7 | `aa321af9c514` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5520 | n/a | 0.0558 | 103.2921 | 0.004 | 18.0 | 1863.3 | `f5ea0f599cc7` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6351 | n/a | 0.2648 | 95.1705 | 0.004 | 18.0 | 1573.4 | `365c8d486b48` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6540 | n/a | 0.3130 | 82.4812 | 0.004 | 18.0 | 1485.8 | `bf9c805dfc07` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5746 | n/a | 0.1352 | 99.0010 | 0.004 | 18.0 | 1801.8 | `865ba573b5bd` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5515 | n/a | 0.1519 | 93.8489 | 0.004 | 18.0 | 1689.1 | `a52490d630e5` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5812 | n/a | 0.2407 | 93.3859 | 0.004 | 18.0 | 1567.6 | `4d2ee1705c5f` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5731 | n/a | 0.0593 | 110.6852 | 0.004 | 18.0 | 1978.7 | `e27076a84ce1` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6543 | n/a | 0.2074 | 91.3872 | 0.004 | 18.0 | 1647.1 | `4ff74a982fc2` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5500 | n/a | 0.0481 | 110.8828 | 0.004 | 18.0 | 2002.5 | `d1d2d3c9aa7b` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5677 | n/a | 0.0964 | 92.1004 | 0.004 | 17.4 | 1620.7 | `c9200184c183` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5884 | n/a | 0.1019 | 107.1589 | 0.004 | 18.0 | 1932.2 | `10e2cafffe73` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5942 +- 0.0387 [worst 0.6707] | 0.6707 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1468 +- 0.0755 [worst 0.3130] | 0.3130 |
| ammo_efficiency | 99.6401 +- 9.9896 [worst 82.4812] | 82.4812 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0039 +- 0.0005 [worst 0.0065] | 0.0065 |
| shots_total | 17.8556 +- 0.3157 [worst 18.0000] | 18.0000 |
| destroyed_value | 1767.3083 +- 193.5528 [worst 1485.7667] | 1485.7667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
