# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_5x100_K10_s03.txt', 'dn_5x100_K10_s04.txt', 'dn_5x100_K10_s05.txt', 'dn_5x100_K10_s06.txt', 'dn_5x100_K10_s07.txt', 'dn_5x100_K10_s08.txt', 'dn_5x100_K10_s09.txt', 'dn_5x100_K10_s10.txt', 'dn_5x100_K10_s11.txt', 'dn_5x100_K10_s12.txt', 'dn_5x100_K10_s13.txt', 'dn_5x100_K10_s14.txt', 'dn_5x100_K10_s15.txt', 'dn_5x100_K10_s16.txt', 'dn_5x100_K10_s17.txt', 'dn_5x100_K10_s18.txt', 'dn_5x100_K10_s19.txt', 'dn_5x100_K10_s20.txt', 'dn_5x100_K10_s21.txt', 'dn_5x100_K10_s22.txt', 'dn_5x100_K10_s23.txt', 'dn_5x100_K10_s24.txt', 'dn_5x100_K10_s25.txt', 'dn_5x100_K10_s26.txt']) | policy: **qmix** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:25:19

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s03.txt` | 8419 | 0.8226 | n/a | 0.1278 | 49.2186 | 0.006 | 30.0 | 1493.5 | `267be8eb9f22` |
| `dn_5x100_K10_s04.txt` | 8817 | 0.8454 | n/a | 0.0922 | 44.4056 | 0.006 | 30.0 | 1363.0 | `b6cd5ffb3611` |
| `dn_5x100_K10_s05.txt` | 10196 | 0.8273 | n/a | 0.1433 | 57.9408 | 0.006 | 30.0 | 1760.5 | `0806007d15ce` |
| `dn_5x100_K10_s06.txt` | 8176 | 0.8560 | n/a | 0.2211 | 38.7513 | 0.006 | 30.0 | 1177.6 | `b983f3fbb868` |
| `dn_5x100_K10_s07.txt` | 8985 | 0.8563 | n/a | 0.1700 | 43.7989 | 0.006 | 30.0 | 1291.3 | `68a01c11908d` |
| `dn_5x100_K10_s08.txt` | 9141 | 0.8418 | n/a | 0.2289 | 47.7134 | 0.006 | 30.0 | 1446.5 | `b6d9b8fd3e44` |
| `dn_5x100_K10_s09.txt` | 8511 | 0.8404 | n/a | 0.0767 | 43.7552 | 0.006 | 30.0 | 1358.1 | `8912cf440125` |
| `dn_5x100_K10_s10.txt` | 9155 | 0.8525 | n/a | 0.2078 | 43.8618 | 0.006 | 30.0 | 1350.2 | `114cd90a0c03` |
| `dn_5x100_K10_s11.txt` | 8850 | 0.8462 | n/a | 0.1978 | 43.3470 | 0.006 | 30.0 | 1361.2 | `427316c39666` |
| `dn_5x100_K10_s12.txt` | 8909 | 0.8458 | n/a | 0.1367 | 45.3250 | 0.006 | 30.0 | 1373.9 | `056e12b00956` |
| `dn_5x100_K10_s13.txt` | 9905 | 0.8240 | n/a | 0.1922 | 57.9061 | 0.006 | 30.0 | 1743.6 | `1e333cc62a63` |
| `dn_5x100_K10_s14.txt` | 9190 | 0.8639 | n/a | 0.1611 | 39.3982 | 0.006 | 30.0 | 1250.5 | `6d8e368bb636` |
| `dn_5x100_K10_s15.txt` | 7913 | 0.8220 | n/a | 0.1000 | 45.9955 | 0.006 | 30.0 | 1408.9 | `f02e36fe93c7` |
| `dn_5x100_K10_s16.txt` | 8526 | 0.8588 | n/a | 0.1422 | 38.0881 | 0.006 | 30.0 | 1203.5 | `13047cf9ac3f` |
| `dn_5x100_K10_s17.txt` | 9044 | 0.8610 | n/a | 0.2489 | 40.9131 | 0.006 | 30.0 | 1257.4 | `51e3921bd3a1` |
| `dn_5x100_K10_s18.txt` | 9002 | 0.8354 | n/a | 0.1289 | 48.9528 | 0.006 | 30.0 | 1481.6 | `080a311c7b11` |
| `dn_5x100_K10_s19.txt` | 8810 | 0.8858 | n/a | 0.1311 | 33.8844 | 0.006 | 30.0 | 1006.5 | `c068c4486ea6` |
| `dn_5x100_K10_s20.txt` | 7875 | 0.8690 | n/a | 0.3011 | 34.2886 | 0.006 | 30.0 | 1031.9 | `cab95087a73a` |
| `dn_5x100_K10_s21.txt` | 8376 | 0.8750 | n/a | 0.1344 | 34.6055 | 0.006 | 30.0 | 1047.1 | `edfc510b3e10` |
| `dn_5x100_K10_s22.txt` | 9389 | 0.8246 | n/a | 0.0956 | 54.0444 | 0.006 | 30.0 | 1647.2 | `d69bc8ad4671` |
| `dn_5x100_K10_s23.txt` | 9402 | 0.8373 | n/a | 0.2122 | 48.4607 | 0.006 | 30.0 | 1529.6 | `fc688365e2b7` |
| `dn_5x100_K10_s24.txt` | 8684 | 0.8251 | n/a | 0.1111 | 48.7429 | 0.006 | 30.0 | 1518.5 | `fb34e6840d34` |
| `dn_5x100_K10_s25.txt` | 8264 | 0.8282 | n/a | 0.1289 | 48.4081 | 0.006 | 30.0 | 1419.6 | `1696a80c28a3` |
| `dn_5x100_K10_s26.txt` | 8976 | 0.8502 | n/a | 0.1233 | 43.4632 | 0.006 | 30.0 | 1344.2 | `ca4c3b8ae66c` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8456 +- 0.0175 [worst 0.8858] | 0.8858 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1589 +- 0.0549 [worst 0.3011] | 0.3011 |
| ammo_efficiency | 44.8029 +- 6.4075 [worst 33.8844] | 33.8844 |
| latency_p50 | 0.0058 +- 0.0001 [worst 0.0061] | 0.0061 |
| latency_p90 | 0.0069 +- 0.0007 [worst 0.0092] | 0.0092 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 1369.4042 +- 194.0588 [worst 1006.5000] | 1006.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
