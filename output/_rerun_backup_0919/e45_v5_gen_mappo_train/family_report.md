# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **mappo** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:02:53

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `90e6f0ad2954` |
| `dn_10x100_K10_s04.txt` | 8817 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `65d8523048b3` |
| `dn_10x100_K10_s05.txt` | 10196 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `7db64b7bd2ae` |
| `dn_10x100_K10_s06.txt` | 8176 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `e37eb70abd44` |
| `dn_10x100_K10_s07.txt` | 8985 | 1.0000 | n/a | 0.0000 | n/a | 0.010 | 0.0 | 0.0 | `364afa07cb3d` |
| `dn_10x100_K10_s08.txt` | 9141 | 1.0000 | n/a | 0.0000 | n/a | 0.012 | 0.0 | 0.0 | `4890605c18e7` |
| `dn_10x100_K10_s09.txt` | 8511 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `dcaa1d4cf732` |
| `dn_10x100_K10_s10.txt` | 9155 | 1.0000 | n/a | 0.0000 | n/a | 0.010 | 0.0 | 0.0 | `c03aa1087013` |
| `dn_10x100_K10_s11.txt` | 8850 | 1.0000 | n/a | 0.0000 | n/a | 0.010 | 0.0 | 0.0 | `fa38c8cba83b` |
| `dn_10x100_K10_s12.txt` | 8909 | 1.0000 | n/a | 0.0000 | n/a | 0.012 | 0.0 | 0.0 | `308a069c15ca` |
| `dn_10x100_K10_s13.txt` | 9905 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `247c90e9c36c` |
| `dn_10x100_K10_s14.txt` | 9190 | 1.0000 | n/a | 0.0000 | n/a | 0.010 | 0.0 | 0.0 | `8cbfa18cb9af` |
| `dn_10x100_K10_s15.txt` | 7913 | 1.0000 | n/a | 0.0000 | n/a | 0.012 | 0.0 | 0.0 | `0384619caa66` |
| `dn_10x100_K10_s16.txt` | 8526 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `0a28bd8d39f0` |
| `dn_10x100_K10_s17.txt` | 9044 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `465b8cfe67f4` |
| `dn_10x100_K10_s18.txt` | 9002 | 1.0000 | n/a | 0.0000 | n/a | 0.010 | 0.0 | 0.0 | `064e6930f4c4` |
| `dn_10x100_K10_s19.txt` | 8810 | 1.0000 | n/a | 0.0000 | n/a | 0.012 | 0.0 | 0.0 | `715f7907cf58` |
| `dn_10x100_K10_s20.txt` | 7875 | 1.0000 | n/a | 0.0000 | n/a | 0.012 | 0.0 | 0.0 | `c3cab5de278f` |
| `dn_10x100_K10_s21.txt` | 8376 | 1.0000 | n/a | 0.0000 | n/a | 0.010 | 0.0 | 0.0 | `9510479263c7` |
| `dn_10x100_K10_s22.txt` | 9389 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `243de5634adf` |
| `dn_10x100_K10_s23.txt` | 9402 | 1.0000 | n/a | 0.0000 | n/a | 0.012 | 0.0 | 0.0 | `41feb80c93ff` |
| `dn_10x100_K10_s24.txt` | 8684 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `b1b5a1513bdd` |
| `dn_10x100_K10_s25.txt` | 8264 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `814e9b02ffde` |
| `dn_10x100_K10_s26.txt` | 8976 | 1.0000 | n/a | 0.0000 | n/a | 0.012 | 0.0 | 0.0 | `71ac206cdcf4` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 1.0000 +- 0.0000 [worst 1.0000] | 1.0000 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| ammo_efficiency | n/a | n/a |
| latency_p50 | 0.0111 +- 0.0006 [worst 0.0122] | 0.0122 |
| latency_p90 | 0.0127 +- 0.0035 [worst 0.0289] | 0.0289 |
| shots_total | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| destroyed_value | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
