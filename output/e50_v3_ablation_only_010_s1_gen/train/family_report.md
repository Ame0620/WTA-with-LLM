# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:56:11

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6502 | n/a | 0.1911 | 95.4219 | 0.003 | 15.0 | 1439.6 | `beb0b43bad5e` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6983 | n/a | 0.1244 | 81.0557 | 0.003 | 15.0 | 1267.9 | `a7cd4382a89f` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.7187 | n/a | 0.1867 | 89.3943 | 0.004 | 15.0 | 1357.9 | `aea5fd786ff2` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.7604 | n/a | 0.1911 | 65.2081 | 0.003 | 15.0 | 988.6 | `443f5b0bf8d4` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.7773 | n/a | 0.3289 | 73.7532 | 0.003 | 15.0 | 1093.5 | `0a03097eca7c` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6624 | n/a | 0.1911 | 97.9737 | 0.003 | 15.0 | 1480.4 | `fe319c90c202` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6977 | n/a | 0.2489 | 84.4815 | 0.004 | 15.0 | 1283.5 | `5de9e50eb806` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6497 | n/a | 0.0022 | 120.2740 | 0.003 | 15.0 | 1835.9 | `27d7b3fa8e22` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.7218 | n/a | 0.1356 | 80.4459 | 0.003 | 15.0 | 1215.0 | `fcd4a9fffca8` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.7020 | n/a | 0.2533 | 99.1357 | 0.003 | 15.0 | 1505.1 | `678ecb24e447` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6720 | n/a | 0.1911 | 95.2287 | 0.004 | 15.0 | 1435.9 | `d5befb2806bc` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6542 | n/a | 0.1800 | 91.5048 | 0.003 | 15.0 | 1382.3 | `135cca2b08ca` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.7281 | n/a | 0.1311 | 74.8588 | 0.003 | 15.0 | 1129.4 | `a8eca5aa7f59` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6253 | n/a | 0.0667 | 103.2819 | 0.003 | 15.0 | 1558.2 | `c081e5a32bee` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.7006 | n/a | 0.2622 | 85.7651 | 0.004 | 15.0 | 1291.2 | `e6e342f268eb` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.7128 | n/a | 0.1289 | 82.1243 | 0.003 | 15.0 | 1233.1 | `eaec7c04c9b3` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6671 | n/a | 0.1867 | 92.8415 | 0.003 | 15.0 | 1410.3 | `7b6eaf710f78` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6450 | n/a | 0.1311 | 89.9629 | 0.003 | 15.0 | 1337.0 | `b4d9839a4d5d` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6622 | n/a | 0.2622 | 84.2170 | 0.004 | 15.0 | 1264.4 | `d93a8079341b` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6545 | n/a | 0.1267 | 105.5867 | 0.003 | 15.0 | 1601.6 | `a1b18f5130bc` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6628 | n/a | 0.1156 | 107.2492 | 0.003 | 15.0 | 1606.4 | `51a0e68f3abe` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6659 | n/a | 0.0578 | 98.5208 | 0.003 | 15.0 | 1487.0 | `7a117d57f784` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.7527 | n/a | 0.2333 | 60.6746 | 0.003 | 15.0 | 927.1 | `819d58128460` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.7158 | n/a | 0.0000 | 87.2605 | 0.003 | 15.0 | 1334.0 | `c1c031cb7946` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6899 +- 0.0393 [worst 0.7773] | 0.7773 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1636 +- 0.0801 [worst 0.3289] | 0.3289 |
| ammo_efficiency | 89.4259 +- 13.2336 [worst 60.6746] | 60.6746 |
| latency_p50 | 0.0032 +- 0.0003 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0035 +- 0.0006 [worst 0.0059] | 0.0059 |
| shots_total | 15.0000 +- 0.0000 [worst 15.0000] | 15.0000 |
| destroyed_value | 1352.7139 +- 200.6706 [worst 927.1000] | 927.1000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
