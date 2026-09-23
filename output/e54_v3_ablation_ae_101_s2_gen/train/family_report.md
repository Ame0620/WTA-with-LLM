# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:14:31

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5513 | n/a | 0.1137 | 114.2631 | 0.004 | 17.0 | 1846.7 | `6f5b2dc66461` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5778 | n/a | 0.0764 | 107.4835 | 0.004 | 16.5 | 1774.5 | `962af9865c6e` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6726 | n/a | 0.2148 | 87.6111 | 0.004 | 18.0 | 1580.5 | `089426cdd828` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.5921 | n/a | 0.0446 | 95.3409 | 0.004 | 17.2 | 1682.8 | `5c668c966cff` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.5871 | n/a | 0.1056 | 111.2173 | 0.004 | 18.0 | 2027.4 | `ec5d67b6f079` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5576 | n/a | 0.1037 | 107.3895 | 0.004 | 18.0 | 1939.9 | `ef339920a749` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.5724 | n/a | 0.0519 | 98.8102 | 0.004 | 18.0 | 1815.4 | `1fac43acd5b4` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6098 | n/a | 0.0059 | 117.2612 | 0.004 | 17.0 | 2045.1 | `9ee03ce3c975` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.5898 | n/a | 0.1537 | 97.9982 | 0.004 | 18.0 | 1791.3 | `8c6ce660cc52` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6002 | n/a | 0.0481 | 118.7017 | 0.004 | 18.0 | 2019.2 | `0b36178935be` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5411 | n/a | 0.0593 | 110.9700 | 0.004 | 18.0 | 2008.6 | `f462391d8a81` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5922 | n/a | 0.1820 | 94.9918 | 0.004 | 17.0 | 1630.0 | `053a09041f7d` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.5935 | n/a | 0.0574 | 93.1202 | 0.004 | 18.0 | 1688.6 | `7764276de278` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5698 | n/a | 0.0096 | 107.7001 | 0.004 | 16.4 | 1789.1 | `74377b3bb890` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6279 | n/a | 0.1593 | 88.6645 | 0.004 | 18.0 | 1604.7 | `ce7c00c6fd7e` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6667 | n/a | 0.2333 | 82.7801 | 0.004 | 18.0 | 1431.1 | `724f12c60ca8` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5262 | n/a | 0.0130 | 109.7551 | 0.004 | 18.0 | 2007.1 | `a263eaa7564f` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5130 | n/a | 0.0778 | 101.4437 | 0.004 | 18.0 | 1834.0 | `fe763415d780` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5577 | n/a | 0.0892 | 92.3219 | 0.004 | 17.9 | 1655.4 | `5ea6f57597de` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5826 | n/a | 0.0561 | 108.8667 | 0.004 | 17.8 | 1934.5 | `b621d9bc33b2` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6067 | n/a | 0.0630 | 102.4813 | 0.004 | 18.0 | 1873.8 | `34a5f1132b90` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5496 | n/a | 0.0037 | 110.7039 | 0.004 | 18.0 | 2004.1 | `c5b185fad601` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5901 | n/a | 0.0660 | 93.0371 | 0.004 | 16.4 | 1536.7 | `75a9799c87b8` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6088 | n/a | 0.0941 | 107.1779 | 0.004 | 17.0 | 1836.1 | `82ee0e3b5836` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5849 +- 0.0372 [worst 0.6726] | 0.6726 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.0868 +- 0.0616 [worst 0.2333] | 0.2333 |
| ammo_efficiency | 102.5038 +- 9.6832 [worst 82.7801] | 82.7801 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0040 +- 0.0005 [worst 0.0065] | 0.0065 |
| shots_total | 17.5931 +- 0.5869 [worst 18.0000] | 18.0000 |
| destroyed_value | 1806.5278 +- 171.2016 [worst 1431.0667] | 1431.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
