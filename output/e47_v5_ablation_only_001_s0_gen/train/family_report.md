# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 14:02:32

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.4167 | n/a | 0.2443 | 70.0155 | 0.013 | 70.0 | 4910.9 | `9f8b5cf9ad40` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.4460 | n/a | 0.2456 | 76.5242 | 0.013 | 63.9 | 4884.4 | `e68b74ff9406` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.4838 | n/a | 0.2747 | 84.5903 | 0.013 | 62.0 | 5263.7 | `38ea2c17274b` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.4778 | n/a | 0.3428 | 68.8681 | 0.013 | 62.4 | 4269.1 | `e3c6661019fc` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.4432 | n/a | 0.3225 | 73.8208 | 0.013 | 68.0 | 5002.6 | `6efdb8fa9862` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.4501 | n/a | 0.3626 | 77.0680 | 0.013 | 66.0 | 5027.0 | `367a6d9d6a1d` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.4738 | n/a | 0.3133 | 67.6294 | 0.013 | 66.1 | 4478.6 | `c7aae689934c` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.4109 | n/a | 0.3039 | 78.3132 | 0.013 | 69.0 | 5393.6 | `98fb1b7cc26a` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.4458 | n/a | 0.3273 | 72.7221 | 0.013 | 67.8 | 4905.1 | `dabdf0381204` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.4745 | n/a | 0.3152 | 66.9783 | 0.013 | 69.9 | 4681.3 | `2e11fbdfbab0` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.4308 | n/a | 0.2695 | 83.5630 | 0.013 | 68.0 | 5638.2 | `0caa185adf38` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.4166 | n/a | 0.2672 | 83.2443 | 0.013 | 64.0 | 5361.6 | `5eced5ce7b6e` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.4469 | n/a | 0.2908 | 67.8347 | 0.013 | 65.2 | 4376.3 | `c0a3fe44eacf` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.4648 | n/a | 0.3561 | 69.7371 | 0.013 | 65.3 | 4563.5 | `1e5d06fb309c` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.5438 | n/a | 0.4108 | 64.1108 | 0.013 | 65.0 | 4126.3 | `641803b8ef22` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.5117 | n/a | 0.3156 | 73.8432 | 0.013 | 60.3 | 4395.7 | `ab37d3881871` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.4837 | n/a | 0.2557 | 70.9986 | 0.013 | 64.0 | 4548.2 | `5b4d92f4303b` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.3946 | n/a | 0.3353 | 71.6859 | 0.013 | 66.9 | 4767.4 | `213b514e06ba` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.4284 | n/a | 0.2282 | 73.6586 | 0.013 | 65.0 | 4787.9 | `7d4defdf4208` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.4522 | n/a | 0.2671 | 73.5809 | 0.013 | 70.0 | 5143.4 | `01e7f0335164` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.5323 | n/a | 0.3335 | 70.0950 | 0.013 | 63.1 | 4397.6 | `bc3f12c3a832` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.3987 | n/a | 0.3061 | 79.1657 | 0.013 | 66.0 | 5221.9 | `cb8895541a34` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.4602 | n/a | 0.3427 | 66.0112 | 0.012 | 67.9 | 4461.0 | `89bb4945b8e7` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.4579 | n/a | 0.2371 | 69.4819 | 0.013 | 70.0 | 4865.8 | `a679e36db335` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4560 +- 0.0374 [worst 0.5438] | 0.5438 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3028 +- 0.0448 [worst 0.4108] | 0.4108 |
| ammo_efficiency | 73.0642 +- 5.5190 [worst 64.1108] | 64.1108 |
| latency_p50 | 0.0129 +- 0.0002 [worst 0.0133] | 0.0133 |
| latency_p90 | 0.0137 +- 0.0008 [worst 0.0172] | 0.0172 |
| shots_total | 66.0778 +- 2.6879 [worst 70.0000] | 70.0000 |
| destroyed_value | 4811.2958 +- 387.2489 [worst 4126.2667] | 4126.2667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
