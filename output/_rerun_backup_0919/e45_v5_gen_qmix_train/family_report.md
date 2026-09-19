# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **qmix** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:10:53

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.7490 | n/a | 0.3871 | 33.1751 | 0.012 | 70.0 | 2113.2 | `e8fd5995ada5` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.7512 | n/a | 0.2886 | 31.2117 | 0.011 | 70.0 | 2193.8 | `6915a2c36d1b` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.7814 | n/a | 0.4243 | 35.1326 | 0.010 | 70.0 | 2229.3 | `21eb8ac8b957` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.7607 | n/a | 0.4114 | 32.8192 | 0.010 | 70.0 | 1956.7 | `da02875e5377` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.7749 | n/a | 0.3814 | 32.6752 | 0.012 | 70.0 | 2022.3 | `f16865ae69e9` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.7632 | n/a | 0.4643 | 33.0264 | 0.011 | 70.0 | 2164.3 | `a76e0d7f1efd` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.7121 | n/a | 0.3786 | 39.6513 | 0.010 | 70.0 | 2450.7 | `ec7bf9461309` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.7303 | n/a | 0.4843 | 35.7050 | 0.011 | 70.0 | 2469.0 | `4198b01b8270` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.7593 | n/a | 0.4043 | 36.1380 | 0.011 | 70.0 | 2130.3 | `014c3daa9e84` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.7763 | n/a | 0.3886 | 32.4328 | 0.011 | 70.0 | 1993.3 | `e0c42e23563a` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.7300 | n/a | 0.4086 | 38.2816 | 0.010 | 70.0 | 2674.7 | `1f14a571aa1e` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.7476 | n/a | 0.4129 | 34.0104 | 0.011 | 70.0 | 2319.8 | `b3d86fcefcf9` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.7434 | n/a | 0.4014 | 29.7126 | 0.011 | 70.0 | 2030.7 | `1d51ce812ecb` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.7476 | n/a | 0.3914 | 31.2680 | 0.010 | 70.0 | 2152.0 | `726905fe6e87` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.7271 | n/a | 0.3886 | 40.9063 | 0.010 | 70.0 | 2468.1 | `c36652fef6b7` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.7684 | n/a | 0.3643 | 34.5552 | 0.011 | 70.0 | 2085.2 | `fc67e1564cb4` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.7568 | n/a | 0.3671 | 32.4100 | 0.011 | 70.0 | 2142.2 | `840adb0855dc` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.7791 | n/a | 0.4614 | 28.0214 | 0.010 | 70.0 | 1739.3 | `4a632bbed3d2` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.8017 | n/a | 0.4343 | 23.7238 | 0.010 | 70.0 | 1661.2 | `b8bd57a151bd` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.7484 | n/a | 0.4286 | 37.3477 | 0.011 | 70.0 | 2362.4 | `70aa217e1296` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.7690 | n/a | 0.4643 | 33.2862 | 0.011 | 70.0 | 2172.3 | `9457469e5fe1` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.7370 | n/a | 0.3314 | 32.6732 | 0.010 | 70.0 | 2283.8 | `901cf33b8575` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.7896 | n/a | 0.3986 | 28.1787 | 0.011 | 70.0 | 1738.7 | `c977c97a4be0` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.7742 | n/a | 0.3757 | 29.3582 | 0.011 | 70.0 | 2027.0 | `e484831ce346` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7574 +- 0.0212 [worst 0.8017] | 0.8017 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.4017 +- 0.0425 [worst 0.4843] | 0.4843 |
| ammo_efficiency | 33.1542 +- 3.7832 [worst 23.7238] | 23.7238 |
| latency_p50 | 0.0108 +- 0.0007 [worst 0.0125] | 0.0125 |
| latency_p90 | 0.0121 +- 0.0024 [worst 0.0228] | 0.0228 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 2149.1792 +- 238.0286 [worst 1661.2000] | 1661.2000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
