# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **random** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 16:20:58

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.8926 | n/a | 0.1130 | 27.5808 | 0.000 | 18.0 | 423.6 | `da139477d0a9` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.8522 | n/a | 0.0278 | 31.8652 | 0.000 | 18.0 | 564.3 | `cefef1806cd8` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8724 +- 0.0202 [worst 0.8926] | 0.8926 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.0704 +- 0.0426 [worst 0.1130] | 0.1130 |
| ammo_efficiency | 29.7230 +- 2.1422 [worst 27.5808] | 27.5808 |
| latency_p50 | 0.0001 +- 0.0000 [worst 0.0001] | 0.0001 |
| latency_p90 | 0.0001 +- 0.0000 [worst 0.0001] | 0.0001 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 493.9167 +- 70.3500 [worst 423.5667] | 423.5667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
