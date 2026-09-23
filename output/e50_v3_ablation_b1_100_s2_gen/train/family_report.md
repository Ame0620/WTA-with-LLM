# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 02:00:18

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.7656 | n/a | 0.2259 | 52.2860 | 0.003 | 18.0 | 964.7 | `c90bb3125a60` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.7299 | n/a | 0.2167 | 64.9876 | 0.003 | 18.0 | 1135.3 | `1d279596a704` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.7556 | n/a | 0.2333 | 65.4059 | 0.003 | 18.0 | 1179.8 | `4f7950e43ee5` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.7804 | n/a | 0.1519 | 50.0428 | 0.004 | 18.0 | 906.1 | `28f98bde565d` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.7939 | n/a | 0.2167 | 55.5389 | 0.003 | 18.0 | 1012.0 | `920680cd16b1` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.8104 | n/a | 0.2833 | 45.6371 | 0.003 | 18.0 | 831.4 | `8358aecb034e` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.8354 | n/a | 0.1944 | 38.4058 | 0.003 | 18.0 | 699.0 | `2f057c5c3ac9` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.7611 | n/a | 0.1574 | 69.1080 | 0.003 | 18.0 | 1252.3 | `c7b7e4ab8857` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.7681 | n/a | 0.1481 | 62.0310 | 0.003 | 18.0 | 1012.7 | `1d60b62acf2a` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.8112 | n/a | 0.2019 | 52.9165 | 0.003 | 18.0 | 953.5 | `16737c62da36` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.7601 | n/a | 0.2093 | 63.7166 | 0.003 | 18.0 | 1050.1 | `b9b2e59519f9` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.8112 | n/a | 0.2648 | 40.9835 | 0.003 | 18.0 | 754.8 | `c51fee29c129` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.8222 | n/a | 0.1833 | 40.9619 | 0.004 | 18.0 | 738.6 | `7c51b1b43a40` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.7302 | n/a | 0.0630 | 62.1688 | 0.003 | 18.0 | 1121.9 | `84c0d720be09` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.7715 | n/a | 0.2611 | 54.2018 | 0.003 | 18.0 | 985.4 | `42dd6a5a5a65` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.7588 | n/a | 0.2019 | 57.0241 | 0.003 | 18.0 | 1035.6 | `319e580d3883` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.7796 | n/a | 0.1926 | 52.0065 | 0.004 | 18.0 | 933.8 | `dd7305b8caf9` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.7958 | n/a | 0.2648 | 42.5128 | 0.003 | 18.0 | 769.1 | `1a89589d4ce1` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.7882 | n/a | 0.2204 | 43.7084 | 0.003 | 18.0 | 792.8 | `7947b1b09fb9` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.7857 | n/a | 0.2130 | 55.2724 | 0.003 | 18.0 | 993.4 | `98239254ad3d` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.7687 | n/a | 0.1444 | 64.6029 | 0.004 | 18.0 | 1101.7 | `4a1303916364` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.7671 | n/a | 0.1352 | 57.8665 | 0.003 | 18.0 | 1036.5 | `f2531858f9a6` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.7523 | n/a | 0.3074 | 51.6689 | 0.003 | 18.0 | 928.5 | `8073e0b9cad3` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.8014 | n/a | 0.0537 | 51.7407 | 0.003 | 18.0 | 932.3 | `bf119ab4fdbb` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7793 +- 0.0266 [worst 0.8354] | 0.8354 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1977 +- 0.0606 [worst 0.3074] | 0.3074 |
| ammo_efficiency | 53.9498 +- 8.5875 [worst 38.4058] | 38.4058 |
| latency_p50 | 0.0031 +- 0.0002 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0035 +- 0.0008 [worst 0.0070] | 0.0070 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 963.3917 +- 141.8637 [worst 698.9667] | 698.9667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
