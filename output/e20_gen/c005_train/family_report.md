# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-09 20:27:38

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.6108 | n/a | 0.2685 | 88.6186 | 0.004 | 18.0 | 1602.1 | `85a4f73924ca` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6129 | n/a | 0.1792 | 100.4908 | 0.005 | 16.4 | 1627.0 | `01a1c5ac3e77` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6069 | n/a | 0.1074 | 105.0465 | 0.004 | 18.0 | 1898.1 | `a6b140616b7f` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6292 | n/a | 0.0467 | 101.2897 | 0.005 | 15.0 | 1529.9 | `604f61dc3452` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6129 | n/a | 0.1746 | 107.7466 | 0.004 | 17.1 | 1900.5 | `27e5d02ff647` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5248 | n/a | 0.0519 | 116.7532 | 0.005 | 18.0 | 2083.6 | `72c5bb266d27` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6134 | n/a | 0.1199 | 100.4021 | 0.004 | 16.1 | 1641.3 | `cad398831f12` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.5840 | n/a | 0.0214 | 125.4929 | 0.004 | 17.1 | 2180.5 | `4568fe73f4fa` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6263 | n/a | 0.1968 | 103.5326 | 0.004 | 16.9 | 1632.1 | `d077c7301ede` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.5951 | n/a | 0.1352 | 113.3417 | 0.004 | 18.0 | 2045.4 | `1dad53821fd8` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5525 | n/a | 0.1556 | 107.5938 | 0.004 | 18.0 | 1958.7 | `5ff70e196cc6` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5810 | n/a | 0.1314 | 98.3895 | 0.005 | 17.0 | 1674.9 | `e9a091003dd5` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6215 | n/a | 0.1438 | 88.2417 | 0.005 | 17.6 | 1572.2 | `09c72e604e46` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5628 | n/a | 0.1059 | 105.3399 | 0.005 | 17.0 | 1818.4 | `5cb0886c1520` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6364 | n/a | 0.3185 | 86.2849 | 0.004 | 18.0 | 1568.0 | `6e0940f91633` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6712 | n/a | 0.3611 | 78.7044 | 0.004 | 18.0 | 1412.0 | `00360bf955b7` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.6106 | n/a | 0.2556 | 91.3147 | 0.004 | 18.0 | 1649.6 | `66287806d2a1` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5333 | n/a | 0.1389 | 97.4106 | 0.004 | 18.0 | 1757.6 | `76016eedfe57` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5741 | n/a | 0.1869 | 90.9531 | 0.004 | 17.1 | 1594.1 | `36b4eab883ba` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5645 | n/a | 0.0667 | 112.1728 | 0.005 | 18.0 | 2018.6 | `c1280d1bb039` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6145 | n/a | 0.2056 | 100.7980 | 0.004 | 18.0 | 1836.5 | `0c048e31b040` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5980 | n/a | 0.1556 | 99.4162 | 0.004 | 18.0 | 1788.9 | `e4a26e1c8c4d` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5935 | n/a | 0.1630 | 85.1411 | 0.005 | 18.0 | 1524.1 | `2713a2337852` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6178 | n/a | 0.1167 | 110.5016 | 0.004 | 16.0 | 1794.0 | `32fc3f60a25e` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5978 +- 0.0329 [worst 0.6712] | 0.6712 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1586 +- 0.0804 [worst 0.3611] | 0.3611 |
| ammo_efficiency | 100.6240 +- 10.8812 [worst 78.7044] | 78.7044 |
| latency_p50 | 0.0044 +- 0.0004 [worst 0.0053] | 0.0053 |
| latency_p90 | 0.0056 +- 0.0010 [worst 0.0084] | 0.0084 |
| shots_total | 17.3903 +- 0.8140 [worst 18.0000] | 18.0000 |
| destroyed_value | 1754.5028 +- 197.9583 [worst 1412.0000] | 1412.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
