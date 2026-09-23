# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:15:28

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5498 | n/a | 0.1500 | 107.6030 | 0.003 | 18.0 | 1853.2 | `efa659adef09` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5842 | n/a | 0.1838 | 105.0987 | 0.003 | 17.0 | 1747.6 | `47d7af3eec58` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.5992 | n/a | 0.0537 | 108.7450 | 0.003 | 18.0 | 1934.9 | `a12a3ed8638c` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6203 | n/a | 0.0375 | 96.8864 | 0.003 | 16.0 | 1566.7 | `b442027c110f` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6299 | n/a | 0.1742 | 103.1689 | 0.003 | 17.4 | 1817.4 | `103d367cf377` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5026 | n/a | 0.0019 | 120.9251 | 0.003 | 18.0 | 2181.2 | `73d891f95bc1` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6467 | n/a | 0.2183 | 85.8534 | 0.003 | 17.1 | 1500.0 | `01131a33f00b` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6097 | n/a | 0.1204 | 111.8361 | 0.003 | 18.0 | 2045.4 | `e03a10eeaa72` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.6162 | n/a | 0.1417 | 101.4082 | 0.003 | 17.9 | 1676.3 | `3575026c01d2` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.5939 | n/a | 0.1537 | 126.4150 | 0.003 | 18.0 | 2051.3 | `eeb23cfe499f` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5581 | n/a | 0.1278 | 106.1048 | 0.003 | 18.0 | 1934.0 | `75c754220f48` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5965 | n/a | 0.2037 | 89.3909 | 0.003 | 18.0 | 1612.7 | `dd754d64f029` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6396 | n/a | 0.1569 | 87.9866 | 0.003 | 17.0 | 1497.1 | `eeb824909a56` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5764 | n/a | 0.0603 | 101.3352 | 0.003 | 17.1 | 1761.9 | `9159517e1acc` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6496 | n/a | 0.3037 | 87.6692 | 0.003 | 18.0 | 1511.1 | `ab6fe22bbc45` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6542 | n/a | 0.3111 | 82.2373 | 0.003 | 18.0 | 1485.1 | `7583e4c47848` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5434 | n/a | 0.0889 | 105.4636 | 0.003 | 18.0 | 1934.0 | `a14301951549` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5264 | n/a | 0.1370 | 99.6602 | 0.003 | 18.0 | 1783.4 | `093e8a74debe` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5856 | n/a | 0.2278 | 91.9950 | 0.003 | 18.0 | 1551.0 | `80c7b6de64a9` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5796 | n/a | 0.0556 | 108.2001 | 0.003 | 18.0 | 1948.4 | `354b4eddd313` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6279 | n/a | 0.2037 | 98.4619 | 0.003 | 18.0 | 1772.8 | `127c6b592785` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5872 | n/a | 0.1037 | 101.4941 | 0.003 | 18.0 | 1837.1 | `b1008b115983` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5893 | n/a | 0.1156 | 90.3529 | 0.003 | 17.2 | 1539.9 | `ba5405c5f99e` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5908 | n/a | 0.0510 | 112.5392 | 0.003 | 17.0 | 1921.0 | `d11d772eda73` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5940 +- 0.0382 [worst 0.6542] | 0.6542 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1409 +- 0.0778 [worst 0.3111] | 0.3111 |
| ammo_efficiency | 101.2846 +- 10.7972 [worst 82.2373] | 82.2373 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0034 +- 0.0005 [worst 0.0058] | 0.0058 |
| shots_total | 17.6528 +- 0.5291 [worst 18.0000] | 18.0000 |
| destroyed_value | 1769.3153 +- 198.4759 [worst 1485.0667] | 1485.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
