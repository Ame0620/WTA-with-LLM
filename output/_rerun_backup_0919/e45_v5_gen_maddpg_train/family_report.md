# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **maddpg** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:17:53

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.7234 | n/a | 0.4586 | 33.3663 | 0.011 | 70.0 | 2329.1 | `e2587a754556` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.7155 | n/a | 0.4271 | 35.6627 | 0.011 | 70.0 | 2508.5 | `8c3777d15282` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.7060 | n/a | 0.4286 | 43.1001 | 0.011 | 70.0 | 2997.3 | `af1f1b9f42e7` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.7055 | n/a | 0.4329 | 33.7514 | 0.011 | 70.0 | 2407.9 | `64313f6f2ff0` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.6797 | n/a | 0.4286 | 41.1551 | 0.010 | 70.0 | 2877.9 | `7effa9e99791` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.7062 | n/a | 0.4100 | 37.3005 | 0.012 | 70.0 | 2685.8 | `7417e3e2daae` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.7629 | n/a | 0.4800 | 29.5201 | 0.011 | 70.0 | 2017.9 | `0ea8abf69d7c` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.6760 | n/a | 0.4557 | 42.6031 | 0.010 | 70.0 | 2966.5 | `2fa1634edcf4` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.7017 | n/a | 0.4586 | 37.4185 | 0.010 | 70.0 | 2639.7 | `28ad2e411007` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.7673 | n/a | 0.4886 | 29.1755 | 0.012 | 70.0 | 2073.5 | `8465e39ac32b` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.7188 | n/a | 0.4229 | 40.6525 | 0.011 | 70.0 | 2785.0 | `ce5872ed9240` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.6974 | n/a | 0.4443 | 39.0552 | 0.010 | 70.0 | 2780.5 | `2a23f29d8bbe` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.7057 | n/a | 0.4286 | 34.5155 | 0.010 | 70.0 | 2328.5 | `286e9d9f3229` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.7340 | n/a | 0.4586 | 32.6678 | 0.010 | 70.0 | 2267.5 | `a189a3bc8bc6` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.7408 | n/a | 0.4914 | 32.8304 | 0.011 | 70.0 | 2343.9 | `56e58c0bfff7` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.7107 | n/a | 0.4557 | 37.1851 | 0.010 | 70.0 | 2604.5 | `0a620b8fdb6f` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.6872 | n/a | 0.4086 | 39.9546 | 0.012 | 70.0 | 2756.1 | `7295080c7817` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.6780 | n/a | 0.3886 | 36.8702 | 0.011 | 70.0 | 2535.6 | `416649a01646` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.7570 | n/a | 0.4743 | 29.6962 | 0.010 | 70.0 | 2035.1 | `4bcb418fb0a3` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.7118 | n/a | 0.4743 | 38.4580 | 0.010 | 70.0 | 2705.9 | `a3cd8a693576` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.7632 | n/a | 0.4614 | 32.0926 | 0.012 | 70.0 | 2226.1 | `44f7f792d70f` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.7085 | n/a | 0.4300 | 35.5783 | 0.011 | 70.0 | 2531.0 | `696bae5362d7` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.7243 | n/a | 0.4029 | 32.6134 | 0.010 | 70.0 | 2278.4 | `bb645c040b14` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.7500 | n/a | 0.4657 | 31.5682 | 0.010 | 70.0 | 2244.2 | `32fd0c4937cc` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7180 +- 0.0267 [worst 0.7673] | 0.7673 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.4448 +- 0.0274 [worst 0.4914] | 0.4914 |
| ammo_efficiency | 35.6996 +- 4.0170 [worst 29.1755] | 29.1755 |
| latency_p50 | 0.0107 +- 0.0006 [worst 0.0117] | 0.0117 |
| latency_p90 | 0.0120 +- 0.0019 [worst 0.0196] | 0.0196 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 2496.9333 +- 281.9722 [worst 2017.9000] | 2017.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
