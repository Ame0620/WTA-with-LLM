# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:55:27

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.5947 | n/a | 0.3718 | 57.5630 | 0.011 | 58.0 | 3305.9 | `10040b9ae568` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4808 | n/a | 0.3269 | 71.9952 | 0.011 | 55.3 | 3954.6 | `22592795463a` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5377 +- 0.0570 [worst 0.5947] | 0.5947 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3494 +- 0.0225 [worst 0.3718] | 0.3718 |
| ammo_efficiency | 64.7791 +- 7.2161 [worst 57.5630] | 57.5630 |
| latency_p50 | 0.0112 +- 0.0002 [worst 0.0114] | 0.0114 |
| latency_p90 | 0.0135 +- 0.0018 [worst 0.0153] | 0.0153 |
| shots_total | 56.6333 +- 1.3667 [worst 58.0000] | 58.0000 |
| destroyed_value | 3630.2167 +- 324.3500 [worst 3305.8667] | 3305.8667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
