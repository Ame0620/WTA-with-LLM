# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:13:27

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5961 | n/a | 0.2093 | 97.7975 | 0.004 | 18.0 | 1662.4 | `8ea2d34b19aa` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5888 | n/a | 0.1648 | 95.1426 | 0.004 | 18.0 | 1728.1 | `3e6484ceeca9` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6345 | n/a | 0.1296 | 98.3522 | 0.004 | 18.0 | 1764.9 | `c258d2d1caba` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6190 | n/a | 0.0354 | 97.3328 | 0.004 | 16.0 | 1572.2 | `31977b387fd4` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6187 | n/a | 0.2003 | 102.7421 | 0.004 | 17.9 | 1872.4 | `2e1f73bf586f` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5125 | n/a | 0.0389 | 118.6165 | 0.004 | 18.0 | 2137.8 | `ca5c2314e089` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.5988 | n/a | 0.1093 | 93.1890 | 0.004 | 18.0 | 1703.6 | `101d99445a2f` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6037 | n/a | 0.1000 | 113.5118 | 0.004 | 18.0 | 2076.8 | `af06dbb68005` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6170 | n/a | 0.1209 | 97.9201 | 0.004 | 17.1 | 1672.7 | `cf5b5ed9c0cf` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.5944 | n/a | 0.1130 | 117.5582 | 0.004 | 18.0 | 2048.9 | `8e2eaddc2767` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5489 | n/a | 0.1167 | 113.8622 | 0.004 | 18.0 | 1974.6 | `8f736120ed0e` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5806 | n/a | 0.1630 | 92.5508 | 0.004 | 18.0 | 1676.3 | `987ab0d3787b` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6274 | n/a | 0.0666 | 90.1641 | 0.004 | 17.0 | 1547.7 | `f762b8e07b4f` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5984 | n/a | 0.1289 | 95.0947 | 0.004 | 17.2 | 1670.4 | `d4413356f316` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6313 | n/a | 0.2630 | 87.1034 | 0.004 | 18.0 | 1589.7 | `122c252fb4e6` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6296 | n/a | 0.1717 | 92.9421 | 0.004 | 17.1 | 1590.4 | `bc46dfda3562` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5301 | n/a | 0.0278 | 109.6369 | 0.004 | 18.0 | 1990.4 | `9f2e2889f731` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5416 | n/a | 0.1500 | 95.1645 | 0.004 | 18.0 | 1726.4 | `fee48ba6016a` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5649 | n/a | 0.1444 | 97.2160 | 0.004 | 18.0 | 1628.4 | `ada0ec319eaf` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5475 | n/a | 0.0148 | 116.2029 | 0.004 | 18.0 | 2097.4 | `855e52342a73` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6263 | n/a | 0.2022 | 98.1628 | 0.004 | 18.0 | 1780.5 | `1eb10d6869bf` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5895 | n/a | 0.0907 | 100.0395 | 0.004 | 18.0 | 1826.7 | `b1980585ced1` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5948 | n/a | 0.1650 | 86.5850 | 0.004 | 18.0 | 1519.2 | `08e354b00c70` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5908 | n/a | 0.0510 | 112.3926 | 0.004 | 17.0 | 1920.7 | `4ee403227216` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5910 +- 0.0335 [worst 0.6345] | 0.6345 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1240 +- 0.0625 [worst 0.2630] | 0.2630 |
| ammo_efficiency | 100.8033 +- 9.6318 [worst 86.5850] | 86.5850 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0036] | 0.0036 |
| latency_p90 | 0.0039 +- 0.0005 [worst 0.0064] | 0.0064 |
| shots_total | 17.7167 +- 0.5195 [worst 18.0000] | 18.0000 |
| destroyed_value | 1782.4389 +- 185.0346 [worst 1519.2000] | 1519.2000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
