# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:09:58

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5474 | n/a | 0.1098 | 108.5203 | 0.004 | 17.0 | 1862.7 | `466a1fafee78` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5892 | n/a | 0.0648 | 95.0285 | 0.004 | 18.0 | 1726.4 | `5b999cbbfa56` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.5927 | n/a | 0.0111 | 108.8184 | 0.004 | 18.0 | 1966.6 | `f551a6e43d04` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6150 | n/a | 0.0000 | 98.2916 | 0.004 | 16.0 | 1588.3 | `ac79c69e1c77` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.6208 | n/a | 0.1460 | 110.7236 | 0.004 | 16.3 | 1862.1 | `194748b594b3` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.5220 | n/a | 0.0611 | 115.9495 | 0.004 | 18.0 | 2096.1 | `04a10e04a74d` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.6020 | n/a | 0.1146 | 103.8530 | 0.004 | 16.0 | 1690.1 | `5e33cc203dfc` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6180 | n/a | 0.0578 | 121.1938 | 0.004 | 16.1 | 2002.2 | `84bc9b43f676` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.5940 | n/a | 0.0519 | 97.7774 | 0.004 | 18.0 | 1773.0 | `f6fc1aecf9cb` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6155 | n/a | 0.1706 | 113.7777 | 0.004 | 17.0 | 1942.2 | `a9a4695a4db0` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5745 | n/a | 0.1647 | 106.5909 | 0.004 | 17.0 | 1862.2 | `6ba1870a72ff` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5913 | n/a | 0.1150 | 100.2886 | 0.004 | 16.2 | 1633.4 | `c586f60c590d` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6242 | n/a | 0.1630 | 85.9954 | 0.004 | 18.0 | 1561.2 | `4af64467eff9` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5372 | n/a | 0.0056 | 106.3640 | 0.004 | 18.0 | 1924.9 | `953436f0443e` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.5797 | n/a | 0.1815 | 100.0486 | 0.004 | 18.0 | 1812.4 | `275dadb5ffc9` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.6667 | n/a | 0.2222 | 79.8669 | 0.004 | 18.0 | 1431.4 | `99c06fe9bbea` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5558 | n/a | 0.1556 | 103.1523 | 0.004 | 18.0 | 1881.6 | `bd9de3f73057` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5433 | n/a | 0.1611 | 93.9293 | 0.004 | 18.0 | 1719.8 | `3d40663dfa99` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5648 | n/a | 0.1680 | 94.6345 | 0.004 | 17.1 | 1628.9 | `2fca2e601f65` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5581 | n/a | 0.0537 | 112.9647 | 0.004 | 18.0 | 2048.1 | `f16ee560abad` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.5879 | n/a | 0.0981 | 107.3719 | 0.004 | 18.0 | 1963.2 | `eb6380f1091e` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5698 | n/a | 0.0481 | 106.0844 | 0.004 | 18.0 | 1914.2 | `a40bd684c008` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5749 | n/a | 0.1093 | 89.2903 | 0.004 | 18.0 | 1593.7 | `9191b98c9b96` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5633 | n/a | 0.0059 | 113.7386 | 0.004 | 17.9 | 2050.1 | `9f799e4ccfdb` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5837 +- 0.0324 [worst 0.6667] | 0.6667 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1016 +- 0.0633 [worst 0.2222] | 0.2222 |
| ammo_efficiency | 103.0939 +- 9.7903 [worst 79.8669] | 79.8669 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0039 +- 0.0005 [worst 0.0065] | 0.0065 |
| shots_total | 17.4417 +- 0.7644 [worst 18.0000] | 18.0000 |
| destroyed_value | 1813.9528 +- 174.5997 [worst 1431.4000] | 1431.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
