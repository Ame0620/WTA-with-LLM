# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:48:22

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5872 | n/a | 0.1667 | 99.2231 | 0.004 | 17.0 | 1698.9 | `fbf56d1a261b` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.6210 | n/a | 0.2036 | 93.1218 | 0.004 | 17.1 | 1593.1 | `c4d1c0c1d9bf` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6666 | n/a | 0.1686 | 94.3618 | 0.004 | 17.0 | 1609.6 | `7c88bbfe513e` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6812 | n/a | 0.1256 | 81.3715 | 0.004 | 16.2 | 1315.4 | `e82440ecb94c` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6783 | n/a | 0.2871 | 92.4838 | 0.003 | 17.1 | 1579.6 | `92a291fc4022` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5710 | n/a | 0.1059 | 110.2598 | 0.004 | 17.0 | 1881.0 | `624e988aa7cf` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.5986 | n/a | 0.0651 | 103.2681 | 0.004 | 16.3 | 1704.4 | `ae41a43166ca` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6401 | n/a | 0.1719 | 109.1791 | 0.003 | 17.1 | 1886.2 | `7a01ae6c433f` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6783 | n/a | 0.0272 | 95.6452 | 0.003 | 14.7 | 1404.7 | `feb1dd2e517a` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6151 | n/a | 0.1574 | 107.5954 | 0.004 | 18.0 | 1944.3 | `3d9d68bff879` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.6045 | n/a | 0.2255 | 101.2515 | 0.004 | 17.0 | 1730.9 | `8ae473f7affd` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.6082 | n/a | 0.1232 | 95.1384 | 0.003 | 16.3 | 1565.8 | `cb968c5b525d` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6486 | n/a | 0.1566 | 86.2431 | 0.003 | 16.8 | 1459.6 | `de9c25b7862b` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5795 | n/a | 0.0565 | 101.8863 | 0.004 | 17.1 | 1749.0 | `3bdce5ddd23e` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6715 | n/a | 0.3241 | 78.3139 | 0.003 | 18.0 | 1416.5 | `d57a914a6de4` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6289 | n/a | 0.1706 | 92.7289 | 0.003 | 17.0 | 1593.4 | `93f803ea5bf1` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5694 | n/a | 0.0619 | 101.6446 | 0.004 | 17.8 | 1824.2 | `9b2736c4cd63` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5931 | n/a | 0.1671 | 88.8987 | 0.004 | 17.2 | 1532.5 | `d345a4b515a3` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5896 | n/a | 0.1686 | 89.8502 | 0.003 | 17.0 | 1536.1 | `f3e903d72d14` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.6005 | n/a | 0.0963 | 101.9012 | 0.004 | 18.0 | 1851.7 | `b45e7e9a6bfa` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6079 | n/a | 0.1106 | 104.3176 | 0.004 | 17.8 | 1867.8 | `8b865301fa9f` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.6059 | n/a | 0.0501 | 101.8347 | 0.003 | 17.3 | 1753.5 | `c814fe4d2394` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.6545 | n/a | 0.2325 | 81.2504 | 0.003 | 15.9 | 1295.3 | `d3b2ccc346fc` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.6315 | n/a | 0.1153 | 102.3124 | 0.004 | 16.8 | 1729.9 | `f8d5d48877f6` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6221 +- 0.0346 [worst 0.6812] | 0.6812 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1474 +- 0.0720 [worst 0.3241] | 0.3241 |
| ammo_efficiency | 96.4201 +- 8.6726 [worst 78.3139] | 78.3139 |
| latency_p50 | 0.0037 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0042 +- 0.0007 [worst 0.0071] | 0.0071 |
| shots_total | 16.9722 +- 0.7291 [worst 18.0000] | 18.0000 |
| destroyed_value | 1646.8153 +- 181.2419 [worst 1295.3333] | 1295.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
