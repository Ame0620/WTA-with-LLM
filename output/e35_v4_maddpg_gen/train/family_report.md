# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_5x100_K10_s03.txt', 'dn_5x100_K10_s04.txt', 'dn_5x100_K10_s05.txt', 'dn_5x100_K10_s06.txt', 'dn_5x100_K10_s07.txt', 'dn_5x100_K10_s08.txt', 'dn_5x100_K10_s09.txt', 'dn_5x100_K10_s10.txt', 'dn_5x100_K10_s11.txt', 'dn_5x100_K10_s12.txt', 'dn_5x100_K10_s13.txt', 'dn_5x100_K10_s14.txt', 'dn_5x100_K10_s15.txt', 'dn_5x100_K10_s16.txt', 'dn_5x100_K10_s17.txt', 'dn_5x100_K10_s18.txt', 'dn_5x100_K10_s19.txt', 'dn_5x100_K10_s20.txt', 'dn_5x100_K10_s21.txt', 'dn_5x100_K10_s22.txt', 'dn_5x100_K10_s23.txt', 'dn_5x100_K10_s24.txt', 'dn_5x100_K10_s25.txt', 'dn_5x100_K10_s26.txt']) | policy: **maddpg** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:24:28

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s03.txt` | 8419 | 0.8102 | n/a | 0.1711 | 52.7048 | 0.006 | 30.0 | 1598.3 | `14045b2835ca` |
| `dn_5x100_K10_s04.txt` | 8817 | 0.8233 | n/a | 0.1378 | 51.8557 | 0.006 | 30.0 | 1557.6 | `7e25b073965d` |
| `dn_5x100_K10_s05.txt` | 10196 | 0.8014 | n/a | 0.1733 | 69.3233 | 0.006 | 30.0 | 2024.5 | `9b09177af2c8` |
| `dn_5x100_K10_s06.txt` | 8176 | 0.8344 | n/a | 0.1067 | 44.9000 | 0.006 | 30.0 | 1354.3 | `769933386002` |
| `dn_5x100_K10_s07.txt` | 8985 | 0.8328 | n/a | 0.1911 | 49.8621 | 0.008 | 30.0 | 1501.9 | `78ecf90717e2` |
| `dn_5x100_K10_s08.txt` | 9141 | 0.8108 | n/a | 0.2178 | 57.4703 | 0.006 | 30.0 | 1729.3 | `d96318aa29ed` |
| `dn_5x100_K10_s09.txt` | 8511 | 0.8220 | n/a | 0.1578 | 49.9824 | 0.006 | 30.0 | 1514.6 | `4ca57671991f` |
| `dn_5x100_K10_s10.txt` | 9155 | 0.7829 | n/a | 0.2244 | 66.2984 | 0.007 | 30.0 | 1987.3 | `233ca6eaaad1` |
| `dn_5x100_K10_s11.txt` | 8850 | 0.8306 | n/a | 0.1667 | 49.8110 | 0.006 | 30.0 | 1499.1 | `6671f2761435` |
| `dn_5x100_K10_s12.txt` | 8909 | 0.7929 | n/a | 0.1322 | 61.3003 | 0.006 | 30.0 | 1845.1 | `76f6780b87a4` |
| `dn_5x100_K10_s13.txt` | 9905 | 0.8355 | n/a | 0.2444 | 54.3050 | 0.006 | 30.0 | 1629.4 | `3ed459d24d52` |
| `dn_5x100_K10_s14.txt` | 9190 | 0.8156 | n/a | 0.1189 | 55.9089 | 0.006 | 30.0 | 1694.5 | `31c05ef6dac1` |
| `dn_5x100_K10_s15.txt` | 7913 | 0.8253 | n/a | 0.1844 | 46.1754 | 0.006 | 30.0 | 1382.4 | `5a010fda76de` |
| `dn_5x100_K10_s16.txt` | 8526 | 0.8333 | n/a | 0.2189 | 47.3667 | 0.006 | 30.0 | 1420.9 | `3accd6ff746a` |
| `dn_5x100_K10_s17.txt` | 9044 | 0.8580 | n/a | 0.2044 | 42.5917 | 0.006 | 30.0 | 1284.7 | `f51c44a07e6c` |
| `dn_5x100_K10_s18.txt` | 9002 | 0.8420 | n/a | 0.1944 | 46.9955 | 0.006 | 30.0 | 1422.3 | `74da23f4f1fd` |
| `dn_5x100_K10_s19.txt` | 8810 | 0.8154 | n/a | 0.1644 | 57.8687 | 0.006 | 30.0 | 1626.2 | `298716ad7bdd` |
| `dn_5x100_K10_s20.txt` | 7875 | 0.8604 | n/a | 0.3122 | 36.4193 | 0.006 | 30.0 | 1099.2 | `2ffa6782dfb9` |
| `dn_5x100_K10_s21.txt` | 8376 | 0.8629 | n/a | 0.1789 | 38.2580 | 0.006 | 30.0 | 1148.5 | `76c8acb7c1f3` |
| `dn_5x100_K10_s22.txt` | 9389 | 0.8192 | n/a | 0.2200 | 55.6523 | 0.006 | 30.0 | 1697.7 | `5aca8171cb18` |
| `dn_5x100_K10_s23.txt` | 9402 | 0.8547 | n/a | 0.2533 | 45.7274 | 0.006 | 30.0 | 1366.1 | `18108bff07be` |
| `dn_5x100_K10_s24.txt` | 8684 | 0.8109 | n/a | 0.1400 | 54.1876 | 0.006 | 30.0 | 1642.4 | `2e5b62adcfad` |
| `dn_5x100_K10_s25.txt` | 8264 | 0.8324 | n/a | 0.1556 | 46.2639 | 0.006 | 30.0 | 1385.4 | `11cedfd41a4c` |
| `dn_5x100_K10_s26.txt` | 8976 | 0.8464 | n/a | 0.1344 | 46.1732 | 0.006 | 30.0 | 1378.6 | `5133f518696c` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8272 +- 0.0203 [worst 0.8629] | 0.8629 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1835 +- 0.0468 [worst 0.3122] | 0.3122 |
| ammo_efficiency | 51.1417 +- 7.7663 [worst 36.4193] | 36.4193 |
| latency_p50 | 0.0060 +- 0.0005 [worst 0.0080] | 0.0080 |
| latency_p90 | 0.0079 +- 0.0019 [worst 0.0149] | 0.0149 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 1532.9319 +- 225.9244 [worst 1099.1667] | 1099.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
