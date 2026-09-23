# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:50:58

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.7436 | n/a | 0.1907 | 57.2066 | 0.003 | 18.0 | 1055.5 | `e049211e4494` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.7307 | n/a | 0.1537 | 61.8135 | 0.003 | 18.0 | 1131.7 | `30a4dfc40a06` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.7918 | n/a | 0.2648 | 55.5230 | 0.003 | 18.0 | 1005.0 | `4d84304a7e37` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.7862 | n/a | 0.1463 | 49.3690 | 0.003 | 18.0 | 882.3 | `fe1cd1fff993` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.7968 | n/a | 0.0889 | 55.2412 | 0.003 | 18.0 | 997.8 | `dcdd28371813` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.7368 | n/a | 0.0741 | 63.8004 | 0.003 | 18.0 | 1154.2 | `1a83cba21852` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.7930 | n/a | 0.0611 | 49.1715 | 0.004 | 18.0 | 879.0 | `32c7aeedced9` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.7535 | n/a | 0.0500 | 70.8657 | 0.003 | 18.0 | 1291.7 | `17447a4c6603` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.7909 | n/a | 0.1500 | 54.3762 | 0.003 | 18.0 | 913.3 | `184cebd19a83` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.8170 | n/a | 0.2019 | 51.2726 | 0.003 | 18.0 | 924.5 | `daad2bcf62c3` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.7580 | n/a | 0.2000 | 63.5246 | 0.004 | 18.0 | 1059.2 | `84a5734c80c6` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.7933 | n/a | 0.1556 | 45.0379 | 0.003 | 18.0 | 826.0 | `54f32a8e147f` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.8020 | n/a | 0.2056 | 44.3210 | 0.003 | 18.0 | 822.6 | `74323f2f4728` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.7373 | n/a | 0.0648 | 59.2801 | 0.003 | 18.0 | 1092.6 | `330b7822dfa1` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.7381 | n/a | 0.2130 | 61.9435 | 0.004 | 18.0 | 1129.1 | `c0233415bc1f` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.7522 | n/a | 0.1130 | 57.6123 | 0.003 | 18.0 | 1064.2 | `a0b6d9f1d987` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.7408 | n/a | 0.1852 | 60.6677 | 0.003 | 18.0 | 1097.8 | `d00c8a5c286d` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.7341 | n/a | 0.2037 | 55.5812 | 0.003 | 18.0 | 1001.5 | `e0e8643ab12d` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.8108 | n/a | 0.1148 | 39.4809 | 0.004 | 18.0 | 708.0 | `7985483b8ac7` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.7488 | n/a | 0.1093 | 64.5161 | 0.003 | 18.0 | 1164.2 | `0997061a49fc` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.7755 | n/a | 0.1370 | 58.8754 | 0.003 | 18.0 | 1069.7 | `ddd25b64286a` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.7657 | n/a | 0.0944 | 57.8888 | 0.003 | 18.0 | 1042.5 | `9a30dbbab605` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.7070 | n/a | 0.1778 | 61.3785 | 0.003 | 18.0 | 1098.4 | `072d82e303e1` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.7698 | n/a | 0.0926 | 59.4624 | 0.003 | 18.0 | 1080.3 | `7b88c160624c` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7656 +- 0.0290 [worst 0.8170] | 0.8170 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1437 +- 0.0565 [worst 0.2648] | 0.2648 |
| ammo_efficiency | 56.5921 +- 7.0918 [worst 39.4809] | 39.4809 |
| latency_p50 | 0.0031 +- 0.0002 [worst 0.0036] | 0.0036 |
| latency_p90 | 0.0035 +- 0.0006 [worst 0.0061] | 0.0061 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1020.4708 +- 129.1262 [worst 708.0333] | 708.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
