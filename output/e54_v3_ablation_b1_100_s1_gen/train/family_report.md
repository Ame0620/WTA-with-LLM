# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:11:27

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5400 | n/a | 0.1093 | 109.2993 | 0.003 | 18.0 | 1893.3 | `0a13b94c187b` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6184 | n/a | 0.2704 | 93.7496 | 0.003 | 18.0 | 1604.0 | `27f04cbed4dc` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6131 | n/a | 0.0673 | 109.0333 | 0.003 | 17.2 | 1867.9 | `b6e45b7f42d1` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6108 | n/a | 0.0037 | 94.2054 | 0.003 | 17.2 | 1606.0 | `3f2011665923` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6239 | n/a | 0.2093 | 100.8298 | 0.003 | 18.0 | 1846.6 | `a0737fc3571e` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.4995 | n/a | 0.0111 | 120.2416 | 0.003 | 18.0 | 2194.8 | `a66fef7094a1` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6467 | n/a | 0.2183 | 85.8534 | 0.003 | 17.1 | 1500.0 | `01131a33f00b` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6060 | n/a | 0.1148 | 112.8265 | 0.003 | 18.0 | 2064.9 | `89e185290c25` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6253 | n/a | 0.1706 | 103.6932 | 0.003 | 17.0 | 1636.1 | `b66668705478` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.5898 | n/a | 0.1463 | 127.4483 | 0.003 | 18.0 | 2071.7 | `6c341345ef86` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5746 | n/a | 0.1883 | 101.8816 | 0.003 | 17.9 | 1862.0 | `a92a925e9a16` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6042 | n/a | 0.2481 | 86.9470 | 0.003 | 18.0 | 1581.9 | `eef8a5958140` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6577 | n/a | 0.1707 | 82.5282 | 0.003 | 17.2 | 1421.7 | `9e9f4f5eeae0` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5844 | n/a | 0.0644 | 100.2261 | 0.003 | 17.0 | 1728.3 | `c8b812bae314` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6260 | n/a | 0.2556 | 93.4606 | 0.003 | 18.0 | 1612.6 | `f8e2e3da1c1f` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6621 | n/a | 0.2719 | 84.5559 | 0.003 | 17.2 | 1451.0 | `3fd359fc39d0` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5364 | n/a | 0.0519 | 109.8004 | 0.003 | 18.0 | 1964.0 | `ca887cd70401` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5698 | n/a | 0.1870 | 91.1662 | 0.003 | 18.0 | 1620.0 | `82aa9466994b` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5764 | n/a | 0.2407 | 93.6216 | 0.003 | 18.0 | 1585.5 | `7b8849f138cf` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5897 | n/a | 0.1000 | 104.9314 | 0.003 | 18.0 | 1901.6 | `d93d113b3423` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6311 | n/a | 0.2121 | 100.6608 | 0.003 | 17.3 | 1757.6 | `ac8639ce17eb` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5976 | n/a | 0.1593 | 98.8335 | 0.003 | 18.0 | 1790.7 | `c52b1aca30ca` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6101 | n/a | 0.2267 | 83.5872 | 0.003 | 17.4 | 1461.6 | `9663d9bc683a` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5758 | n/a | 0.0481 | 109.6120 | 0.003 | 18.0 | 1991.0 | `db726e304505` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5987 +- 0.0376 [worst 0.6621] | 0.6621 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1561 +- 0.0815 [worst 0.2719] | 0.2719 |
| ammo_efficiency | 99.9580 +- 11.4491 [worst 82.5282] | 82.5282 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0033 +- 0.0005 [worst 0.0059] | 0.0059 |
| shots_total | 17.6847 +- 0.4023 [worst 18.0000] | 18.0000 |
| destroyed_value | 1750.6167 +- 211.6202 [worst 1421.7333] | 1421.7333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
