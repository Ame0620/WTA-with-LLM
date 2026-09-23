# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:07:54

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5547 | n/a | 0.1093 | 100.6653 | 0.003 | 18.0 | 1832.7 | `fbd5752139fb` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6023 | n/a | 0.1093 | 97.7224 | 0.003 | 18.0 | 1671.4 | `b78632ae9f16` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6662 | n/a | 0.2111 | 89.3801 | 0.003 | 18.0 | 1611.6 | `b66bf24ca998` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6589 | n/a | 0.1196 | 82.2325 | 0.003 | 17.0 | 1407.2 | `459ccae3be63` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6232 | n/a | 0.2229 | 102.9457 | 0.003 | 17.2 | 1850.2 | `1f9f99dbcbd6` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5339 | n/a | 0.1056 | 111.9654 | 0.003 | 18.0 | 2043.9 | `2eef681a007c` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6491 | n/a | 0.1667 | 86.5035 | 0.003 | 17.0 | 1490.0 | `0ed96ac49243` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6246 | n/a | 0.1078 | 113.6609 | 0.003 | 17.0 | 1967.5 | `a0c4e8d1a8a5` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6269 | n/a | 0.1519 | 102.4048 | 0.003 | 18.0 | 1629.3 | `c2a4fbe28c85` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6002 | n/a | 0.1111 | 117.6550 | 0.003 | 18.0 | 2019.2 | `1fc7a6febbfc` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5536 | n/a | 0.1093 | 107.3844 | 0.003 | 18.0 | 1953.9 | `0aed7d2f4673` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6256 | n/a | 0.2500 | 82.2490 | 0.003 | 18.0 | 1496.5 | `996e37cc301f` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6618 | n/a | 0.2056 | 77.3524 | 0.003 | 18.0 | 1404.9 | `e17220a28ccd` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5619 | n/a | 0.0074 | 100.1478 | 0.003 | 18.0 | 1822.0 | `ba7ccae80617` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6333 | n/a | 0.3167 | 87.4282 | 0.003 | 18.0 | 1581.1 | `8a6edd69a94a` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6695 | n/a | 0.2725 | 82.4770 | 0.003 | 17.0 | 1419.0 | `5f0098945241` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5395 | n/a | 0.0630 | 107.1764 | 0.003 | 18.0 | 1950.6 | `f63885b72b54` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5158 | n/a | 0.1593 | 100.7003 | 0.003 | 18.0 | 1823.6 | `7b126e61c68f` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.6008 | n/a | 0.2745 | 94.2134 | 0.003 | 17.0 | 1494.1 | `542923a6eaf9` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5927 | n/a | 0.1074 | 104.8455 | 0.003 | 18.0 | 1887.9 | `ceb2d1c0956f` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6298 | n/a | 0.1588 | 103.2564 | 0.003 | 17.0 | 1763.6 | `7a0f71ff0c74` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5903 | n/a | 0.0574 | 102.2683 | 0.003 | 18.0 | 1823.0 | `80f39cf10cbf` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6167 | n/a | 0.2037 | 85.3930 | 0.003 | 18.0 | 1436.8 | `204bd34f1a5b` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6347 | n/a | 0.0519 | 94.5730 | 0.003 | 18.0 | 1714.6 | `12382a502b08` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6069 +- 0.0432 [worst 0.6695] | 0.6695 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1522 +- 0.0771 [worst 0.3167] | 0.3167 |
| ammo_efficiency | 97.2750 +- 10.8189 [worst 77.3524] | 77.3524 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0031] | 0.0031 |
| latency_p90 | 0.0033 +- 0.0005 [worst 0.0056] | 0.0056 |
| shots_total | 17.7153 +- 0.4448 [worst 18.0000] | 18.0000 |
| destroyed_value | 1712.2875 +- 205.8550 [worst 1404.9000] | 1404.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
