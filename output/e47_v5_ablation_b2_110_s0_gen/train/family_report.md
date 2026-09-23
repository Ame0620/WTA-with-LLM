# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:38:54

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.4254 | n/a | 0.2448 | 69.8368 | 0.018 | 70.0 | 4837.9 | `0c7a2548c862` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.4418 | n/a | 0.2633 | 70.0448 | 0.017 | 70.0 | 4921.7 | `43bed0d12996` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.4773 | n/a | 0.3055 | 77.5616 | 0.018 | 68.3 | 5329.9 | `8db671ac17d3` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.4502 | n/a | 0.3384 | 65.0640 | 0.015 | 69.2 | 4495.4 | `8bfff80be6ad` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.4067 | n/a | 0.2843 | 76.4296 | 0.016 | 70.0 | 5330.6 | `16648a4212a2` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.4549 | n/a | 0.3560 | 73.1335 | 0.016 | 69.0 | 4982.8 | `b003b25fcfcc` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.4618 | n/a | 0.2688 | 66.2352 | 0.015 | 69.1 | 4580.5 | `9b25f350e41e` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.4655 | n/a | 0.2976 | 70.1851 | 0.015 | 70.0 | 4893.6 | `63803bc26d3b` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.4952 | n/a | 0.3469 | 64.8815 | 0.015 | 69.3 | 4467.5 | `2f02e8cde62e` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.4712 | n/a | 0.2348 | 67.8683 | 0.015 | 69.0 | 4711.0 | `0931cdcaa883` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.4568 | n/a | 0.3038 | 76.9844 | 0.015 | 70.0 | 5380.4 | `83d993e2496e` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.4207 | n/a | 0.2867 | 76.4908 | 0.015 | 70.0 | 5324.0 | `8d645f36afe3` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.4344 | n/a | 0.2743 | 63.8001 | 0.015 | 70.0 | 4475.3 | `f44b80a3f5ef` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.4914 | n/a | 0.3560 | 63.0269 | 0.015 | 69.0 | 4336.1 | `d9fe7dde2dc1` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.4864 | n/a | 0.3171 | 66.4058 | 0.015 | 70.0 | 4645.3 | `be8dfb52cbc8` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.4776 | n/a | 0.2919 | 67.1056 | 0.015 | 70.0 | 4702.2 | `de591b8764bc` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.4579 | n/a | 0.2794 | 70.5715 | 0.015 | 68.0 | 4776.0 | `7b5918e7769e` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.4194 | n/a | 0.3263 | 66.3040 | 0.015 | 69.2 | 4572.2 | `b1afaa056d7d` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.4230 | n/a | 0.2333 | 68.9665 | 0.015 | 70.0 | 4833.3 | `0677eec392de` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.4795 | n/a | 0.3067 | 69.4493 | 0.015 | 70.0 | 4886.5 | `1cbb25cc48fc` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.5229 | n/a | 0.3541 | 64.9275 | 0.015 | 69.0 | 4485.6 | `e8a65877216e` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.4241 | n/a | 0.3148 | 71.3263 | 0.015 | 70.0 | 5000.9 | `07690ffbd921` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.4844 | n/a | 0.3395 | 61.1612 | 0.015 | 70.0 | 4260.9 | `9aaddde1bac5` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.4461 | n/a | 0.1776 | 70.8185 | 0.015 | 70.0 | 4972.0 | `e79a05ff5446` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4573 +- 0.0286 [worst 0.5229] | 0.5229 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2959 +- 0.0438 [worst 0.3560] | 0.3560 |
| ammo_efficiency | 69.1075 +- 4.4697 [worst 61.1612] | 61.1612 |
| latency_p50 | 0.0154 +- 0.0009 [worst 0.0179] | 0.0179 |
| latency_p90 | 0.0169 +- 0.0022 [worst 0.0241] | 0.0241 |
| shots_total | 69.5403 +- 0.5991 [worst 70.0000] | 70.0000 |
| destroyed_value | 4800.0653 +- 314.0107 [worst 4260.9000] | 4260.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
