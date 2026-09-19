# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **greedy_nearest** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 20:05:51

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.8466 | 2.4005 | 0.6319 | 18.0134 | 0.811 | 70.0 | 1251.0 | `b18edea6f625` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.8709 | 1.8996 | 0.6610 | 14.0687 | 0.812 | 70.0 | 983.2 | `260a1cc25301` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8588 +- 0.0121 [worst 0.8709] | 0.8709 |
| gap_mean | 2.1501 +- 0.2504 [worst 2.4005] | 2.4005 |
| invalid_engagement_rate | 0.6464 +- 0.0145 [worst 0.6610] | 0.6610 |
| ammo_efficiency | 16.0411 +- 1.9724 [worst 14.0687] | 14.0687 |
| latency_p50 | 0.8115 +- 0.0004 [worst 0.8119] | 0.8119 |
| latency_p90 | 1.0910 +- 0.2018 [worst 1.2928] | 1.2928 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 1117.1167 +- 133.9167 [worst 983.2000] | 983.2000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
