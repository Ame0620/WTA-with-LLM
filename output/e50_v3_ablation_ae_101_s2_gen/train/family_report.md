# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:59:12

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5794 | n/a | 0.0574 | 96.1714 | 0.004 | 18.0 | 1731.0 | `c1d79bb20bf6` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6196 | n/a | 0.1667 | 93.2750 | 0.004 | 18.0 | 1598.8 | `e1169dcd94c3` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6565 | n/a | 0.1074 | 91.6671 | 0.004 | 18.0 | 1658.4 | `dda811831876` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6258 | n/a | 0.1074 | 84.1088 | 0.004 | 18.0 | 1543.8 | `ca7ef0ae9e75` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6229 | n/a | 0.1574 | 100.9710 | 0.004 | 18.0 | 1851.7 | `a03166e033aa` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5378 | n/a | 0.0519 | 111.9961 | 0.004 | 18.0 | 2026.9 | `ce36fcfcdf56` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6313 | n/a | 0.1556 | 86.6001 | 0.004 | 18.0 | 1565.5 | `ab4956dee7df` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6602 | n/a | 0.1630 | 97.3161 | 0.004 | 18.0 | 1780.7 | `28e2aa0f0b63` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6773 | n/a | 0.2056 | 88.0624 | 0.004 | 18.0 | 1409.1 | `ea882fa6031f` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6426 | n/a | 0.1148 | 109.1850 | 0.004 | 18.0 | 1805.1 | `32ecdba667ca` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6404 | n/a | 0.1630 | 90.9443 | 0.004 | 18.0 | 1573.9 | `731d60d17edd` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6466 | n/a | 0.2537 | 78.3014 | 0.004 | 18.0 | 1412.4 | `e330c8161a5a` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6326 | n/a | 0.1056 | 83.9818 | 0.004 | 18.0 | 1526.0 | `770eb2996078` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.6425 | n/a | 0.1667 | 82.1085 | 0.004 | 18.0 | 1486.7 | `a1cb43d7cae4` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6515 | n/a | 0.2019 | 87.2325 | 0.004 | 18.0 | 1502.6 | `4e896532b731` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6489 | n/a | 0.1093 | 88.4109 | 0.004 | 18.0 | 1507.4 | `b452ae25522a` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5799 | n/a | 0.0611 | 97.9541 | 0.004 | 18.0 | 1779.4 | `225cd98cded0` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.6319 | n/a | 0.2500 | 75.2763 | 0.004 | 18.0 | 1386.3 | `084981cf103d` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6327 | n/a | 0.1556 | 75.8705 | 0.004 | 18.0 | 1375.0 | `fdc255552e52` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6315 | n/a | 0.0556 | 95.3937 | 0.004 | 18.0 | 1707.8 | `3b87649d58b0` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6186 | n/a | 0.2000 | 100.3652 | 0.004 | 18.0 | 1816.8 | `f655d5776267` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6152 | n/a | 0.1037 | 94.2672 | 0.004 | 18.0 | 1712.5 | `e3f396d3cdad` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6168 | n/a | 0.1241 | 85.8572 | 0.004 | 18.0 | 1436.7 | `814715b4e366` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6459 | n/a | 0.1593 | 90.2685 | 0.004 | 18.0 | 1662.0 | `d44ed8ca8fdd` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6287 +- 0.0288 [worst 0.6773] | 0.6773 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1415 +- 0.0558 [worst 0.2537] | 0.2537 |
| ammo_efficiency | 91.0660 +- 9.1246 [worst 75.2763] | 75.2763 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0043 +- 0.0007 [worst 0.0069] | 0.0069 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1619.0222 +- 167.7699 [worst 1374.9667] | 1374.9667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
