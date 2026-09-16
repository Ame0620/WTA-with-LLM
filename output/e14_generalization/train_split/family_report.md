# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-02 18:57:26

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.8483 | n/a | 0.2222 | 35.0654 | 0.005 | 18.0 | 624.4 | `a5b7cd185bec` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.9337 | n/a | 0.0759 | 16.2336 | 0.005 | 18.0 | 278.8 | `aa692b204dca` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.9189 | n/a | 0.0167 | 22.6316 | 0.005 | 18.0 | 391.4 | `129de50aa7e2` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.9000 | n/a | 0.1519 | 23.9639 | 0.004 | 18.0 | 412.7 | `27154930bf39` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.9540 | n/a | 0.0741 | 12.1002 | 0.004 | 18.0 | 226.1 | `84e559ac6c33` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.9310 | n/a | 0.0389 | 15.9480 | 0.004 | 18.0 | 302.4 | `1c706a90b291` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.8850 | n/a | 0.1056 | 24.5951 | 0.004 | 18.0 | 488.1 | `6aa08c470021` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.9142 | n/a | 0.0407 | 22.1846 | 0.004 | 18.0 | 449.9 | `a1737d74b6d4` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.9518 | n/a | 0.0389 | 12.1193 | 0.004 | 18.0 | 210.5 | `0a812c733a83` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.9091 | n/a | 0.0796 | 24.2174 | 0.004 | 18.0 | 459.0 | `67fcc43aefd9` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.8799 | n/a | 0.1907 | 27.6455 | 0.004 | 18.0 | 525.5 | `3b4d16795582` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.9240 | n/a | 0.0833 | 16.5305 | 0.004 | 18.0 | 303.9 | `e97b9dcf071c` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.9132 | n/a | 0.1444 | 18.8917 | 0.004 | 18.0 | 360.6 | `6485da42b1a6` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.9347 | n/a | 0.1222 | 12.8097 | 0.004 | 18.0 | 271.6 | `0debd1ec23c9` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.9255 | n/a | 0.1963 | 15.5234 | 0.004 | 18.0 | 321.3 | `b9745303c8bd` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.9469 | n/a | 0.1056 | 11.7899 | 0.004 | 18.0 | 227.9 | `7f5967bcf6cd` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.8944 | n/a | 0.1944 | 26.3595 | 0.004 | 18.0 | 447.4 | `c3a9c04677ba` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.8922 | n/a | 0.0389 | 21.6327 | 0.004 | 18.0 | 405.8 | `7ac8d4f2dd4d` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.9395 | n/a | 0.1315 | 12.7488 | 0.004 | 18.0 | 226.4 | `2f497b3f042c` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.9028 | n/a | 0.2130 | 22.3779 | 0.004 | 18.0 | 450.7 | `60324d312274` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.9344 | n/a | 0.1593 | 17.9840 | 0.004 | 18.0 | 312.6 | `6562ed97d987` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.9383 | n/a | 0.1370 | 14.0726 | 0.004 | 18.0 | 274.5 | `265cb5d472d0` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.9053 | n/a | 0.1019 | 20.1726 | 0.004 | 18.0 | 354.9 | `42c59cb04b30` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.9205 | n/a | 0.0722 | 22.7031 | 0.004 | 18.0 | 373.3 | `c8a031e5420e` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.9166 +- 0.0247 [worst 0.9540] | 0.9540 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1140 +- 0.0595 [worst 0.2222] | 0.2222 |
| ammo_efficiency | 19.5959 +- 5.7851 [worst 11.7899] | 11.7899 |
| latency_p50 | 0.0042 +- 0.0004 [worst 0.0054] | 0.0054 |
| latency_p90 | 0.0087 +- 0.0146 [worst 0.0774] | 0.0774 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 362.4958 +- 104.2647 [worst 210.5333] | 210.5333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
