# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:58:35

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6308 | n/a | 0.2704 | 84.5685 | 0.004 | 18.0 | 1519.7 | `81c197c67e2d` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6652 | n/a | 0.2611 | 77.4961 | 0.004 | 18.0 | 1407.1 | `4e583982c7b4` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6989 | n/a | 0.2704 | 80.6224 | 0.004 | 18.0 | 1453.8 | `2ab3949b667a` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6752 | n/a | 0.1176 | 78.6550 | 0.004 | 17.0 | 1339.9 | `b5980bc3187e` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.7257 | n/a | 0.3980 | 79.3692 | 0.004 | 17.0 | 1346.9 | `cccede572d5a` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5919 | n/a | 0.1537 | 99.0876 | 0.004 | 18.0 | 1789.4 | `e98b50328ebd` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.7087 | n/a | 0.2396 | 77.3481 | 0.004 | 16.0 | 1236.9 | `47d89f218a22` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6582 | n/a | 0.2185 | 99.0866 | 0.004 | 18.0 | 1791.5 | `a1a2da4bf9ee` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6261 | n/a | 0.1157 | 94.9017 | 0.004 | 17.0 | 1632.9 | `40077d4885c0` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6510 | n/a | 0.2593 | 97.0877 | 0.004 | 18.0 | 1762.7 | `7473b9f2c8c5` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6007 | n/a | 0.2314 | 102.5089 | 0.004 | 17.0 | 1747.5 | `a8f6b6e32122` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6270 | n/a | 0.2704 | 83.2059 | 0.004 | 18.0 | 1490.9 | `da5b25c97679` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6671 | n/a | 0.2648 | 75.9371 | 0.004 | 18.0 | 1383.1 | `f522d281027c` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6432 | n/a | 0.2648 | 81.9096 | 0.004 | 18.0 | 1483.9 | `4aa0b9bb5781` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6537 | n/a | 0.3167 | 81.9941 | 0.004 | 18.0 | 1493.3 | `0773418243ec` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6484 | n/a | 0.2685 | 83.6109 | 0.004 | 18.0 | 1509.9 | `0f2be58a9b3d` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6496 | n/a | 0.2093 | 82.5117 | 0.004 | 18.0 | 1484.4 | `b0db384470a8` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5702 | n/a | 0.2130 | 89.1494 | 0.004 | 18.0 | 1618.8 | `0b84b8fdd993` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6190 | n/a | 0.1167 | 89.4341 | 0.004 | 16.0 | 1426.2 | `5ad5fe4db85b` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5862 | n/a | 0.1093 | 106.1355 | 0.004 | 18.0 | 1918.0 | `7cf89227716f` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6229 | n/a | 0.1611 | 99.3830 | 0.004 | 18.0 | 1796.6 | `cda0bc07e401` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6221 | n/a | 0.1648 | 93.8187 | 0.004 | 18.0 | 1681.5 | `96b4e8354102` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.7321 | n/a | 0.4815 | 54.3560 | 0.004 | 18.0 | 1004.5 | `f4b7ccfd29b1` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6453 | n/a | 0.1074 | 93.3373 | 0.004 | 18.0 | 1664.8 | `b203b710cb83` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6466 +- 0.0406 [worst 0.7321] | 0.7321 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2285 +- 0.0898 [worst 0.4815] | 0.4815 |
| ammo_efficiency | 86.8965 +- 11.0986 [worst 54.3560] | 54.3560 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0043 +- 0.0007 [worst 0.0071] | 0.0071 |
| shots_total | 17.6667 +- 0.6236 [worst 18.0000] | 18.0000 |
| destroyed_value | 1541.0111 +- 204.9486 [worst 1004.5333] | 1004.5333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
