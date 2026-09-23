# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 3 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 16:26:22

## Per-instance metrics (mean +- std over 3 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6173 | n/a | 0.1667 | 88.5229 | 0.006 | 18.0 | 1575.0 | `d7c6d3a2b03e` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6883 | n/a | 0.0625 | 81.0072 | 0.004 | 16.0 | 1310.0 | `0ab637b6db8f` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.7483 | n/a | 0.2353 | 72.9456 | 0.004 | 17.0 | 1215.0 | `c242da37eae3` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.7340 | n/a | 0.1667 | 65.6237 | 0.004 | 16.0 | 1097.3 | `012d7fe1c6b9` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.7434 | n/a | 0.2157 | 80.7921 | 0.004 | 17.0 | 1260.0 | `bec3a4784e81` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.6303 | n/a | 0.1667 | 92.3657 | 0.004 | 18.0 | 1621.0 | `d7c7fd63539b` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6576 | n/a | 0.1250 | 92.7943 | 0.004 | 16.0 | 1454.0 | `788fd1bc2338` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6737 | n/a | 0.0784 | 107.2250 | 0.004 | 17.0 | 1710.3 | `a4de725202fe` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.7013 | n/a | 0.1422 | 87.3169 | 0.004 | 16.3 | 1304.3 | `cebea2984722` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6786 | n/a | 0.1667 | 91.1496 | 0.004 | 18.0 | 1623.3 | `4ad8522cbe11` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6791 | n/a | 0.1875 | 88.2743 | 0.004 | 16.0 | 1404.7 | `ad586559a6a7` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6423 | n/a | 0.1481 | 82.7575 | 0.004 | 18.0 | 1429.7 | `060cfe6e1d93` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.7233 | n/a | 0.1765 | 65.8748 | 0.004 | 17.0 | 1149.3 | `8a84243a9198` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6310 | n/a | 0.0588 | 94.0985 | 0.004 | 17.0 | 1534.7 | `d0d8abe152b1` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6474 | n/a | 0.2157 | 89.6235 | 0.004 | 17.0 | 1520.3 | `d17e665fdec2` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6996 | n/a | 0.1176 | 75.8792 | 0.004 | 17.0 | 1290.0 | `94290f3f68cd` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6154 | n/a | 0.0556 | 93.0340 | 0.004 | 18.0 | 1629.0 | `37ac854c78bb` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6678 | n/a | 0.2778 | 70.0101 | 0.005 | 18.0 | 1251.0 | `40b6bccddbfa` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6508 | n/a | 0.1667 | 81.3706 | 0.005 | 16.0 | 1307.0 | `41260dc10ee3` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6624 | n/a | 0.1133 | 91.1110 | 0.005 | 17.7 | 1564.7 | `8eb8981f608e` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6997 | n/a | 0.1667 | 89.5589 | 0.006 | 16.0 | 1430.7 | `c1781550fbcc` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6370 | n/a | 0.1296 | 92.7235 | 0.006 | 18.0 | 1615.3 | `5bc41444fba4` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6780 | n/a | 0.1667 | 76.4717 | 0.006 | 16.0 | 1207.3 | `961e9bbc4fca` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.7412 | n/a | 0.0000 | 78.5942 | 0.005 | 16.0 | 1214.7 | `ba863213e48d` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6770 +- 0.0395 [worst 0.7483] | 0.7483 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1461 +- 0.0619 [worst 0.2778] | 0.2778 |
| ammo_efficiency | 84.5469 +- 9.8252 [worst 65.6237] | 65.6237 |
| latency_p50 | 0.0047 +- 0.0006 [worst 0.0063] | 0.0063 |
| latency_p90 | 0.0094 +- 0.0181 [worst 0.0959] | 0.0959 |
| shots_total | 16.9583 +- 0.8126 [worst 18.0000] | 18.0000 |
| destroyed_value | 1404.9444 +- 174.2004 [worst 1097.3333] | 1097.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
