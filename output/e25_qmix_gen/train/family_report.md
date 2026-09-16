# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **qmix** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 17:15:17

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.7795 | n/a | 0.3556 | 49.6954 | 0.007 | 18.0 | 907.7 | `d06a0c086242` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.8237 | n/a | 0.3796 | 41.1153 | 0.004 | 18.0 | 741.2 | `80a8fc9d672c` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.7618 | n/a | 0.3407 | 62.8974 | 0.004 | 18.0 | 1150.2 | `4c8d7fc46e6e` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.7876 | n/a | 0.2611 | 48.1616 | 0.004 | 18.0 | 876.4 | `4e8d367a71fa` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.8002 | n/a | 0.2815 | 54.8385 | 0.004 | 18.0 | 981.1 | `23c7cf6ca8c1` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.7324 | n/a | 0.2185 | 65.2418 | 0.004 | 18.0 | 1173.6 | `1932184f5a0d` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.8067 | n/a | 0.3481 | 45.9194 | 0.004 | 18.0 | 820.9 | `e627b446ae87` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.7605 | n/a | 0.1648 | 67.9858 | 0.005 | 18.0 | 1255.0 | `4f1b70bcd806` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.7842 | n/a | 0.2963 | 51.5764 | 0.005 | 18.0 | 942.5 | `d2145c19d7f8` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.7636 | n/a | 0.2148 | 65.7913 | 0.004 | 18.0 | 1193.9 | `4f96185e4281` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.7628 | n/a | 0.3148 | 56.5623 | 0.004 | 18.0 | 1038.3 | `1f2510869e4a` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.7977 | n/a | 0.3037 | 44.1576 | 0.004 | 18.0 | 808.4 | `8359a9c0c90f` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.8155 | n/a | 0.4074 | 42.7387 | 0.004 | 18.0 | 766.5 | `97a2fa77f830` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.7451 | n/a | 0.3037 | 58.2829 | 0.004 | 18.0 | 1060.2 | `9f4b5d84137c` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.7992 | n/a | 0.3259 | 48.3413 | 0.004 | 18.0 | 865.7 | `85c993be62d0` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.7804 | n/a | 0.3981 | 51.6940 | 0.004 | 18.0 | 942.8 | `6ecac56ea52a` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.7859 | n/a | 0.3407 | 50.6679 | 0.004 | 18.0 | 906.9 | `1ca29edce1f9` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.8091 | n/a | 0.4278 | 37.8496 | 0.004 | 18.0 | 719.0 | `a83afe63a2a3` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.7333 | n/a | 0.2370 | 54.0958 | 0.004 | 18.0 | 998.4 | `93be19081884` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.8019 | n/a | 0.3241 | 50.8995 | 0.004 | 18.0 | 918.1 | `b9fdff5fce82` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.7953 | n/a | 0.2278 | 53.5149 | 0.004 | 18.0 | 975.2 | `b406b1d2e1dd` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.7578 | n/a | 0.4000 | 59.7871 | 0.004 | 18.0 | 1077.7 | `ed421c729f09` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.7875 | n/a | 0.4833 | 43.9327 | 0.004 | 18.0 | 796.6 | `0d36d45166e7` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.8162 | n/a | 0.2130 | 47.3797 | 0.004 | 18.0 | 862.6 | `99b34e2cf006` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7828 +- 0.0252 [worst 0.8237] | 0.8237 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3154 +- 0.0771 [worst 0.4833] | 0.4833 |
| ammo_efficiency | 52.2136 +- 7.9070 [worst 37.8496] | 37.8496 |
| latency_p50 | 0.0045 +- 0.0005 [worst 0.0066] | 0.0066 |
| latency_p90 | 0.0067 +- 0.0059 [worst 0.0347] | 0.0347 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 949.1181 +- 144.1304 [worst 719.0000] | 719.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
