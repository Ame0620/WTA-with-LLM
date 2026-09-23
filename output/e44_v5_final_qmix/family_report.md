# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **qmix** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:22:15

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.7187 | 2.2244 | 0.4638 | 33.3221 | 0.664 | 70.0 | 2294.2 | `66f7deada2fc` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.6389 | 2.1856 | 0.4014 | 39.1432 | 0.654 | 70.0 | 2749.9 | `c312220ff7b2` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6788 +- 0.0399 [worst 0.7187] | 0.7187 |
| gap_mean | 2.2050 +- 0.0194 [worst 2.2244] | 2.2244 |
| invalid_engagement_rate | 0.4326 +- 0.0312 [worst 0.4638] | 0.4638 |
| ammo_efficiency | 36.2327 +- 2.9105 [worst 33.3221] | 33.3221 |
| latency_p50 | 0.6592 +- 0.0052 [worst 0.6644] | 0.6644 |
| latency_p90 | 0.7781 +- 0.0015 [worst 0.7797] | 0.7797 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 2522.0667 +- 227.8667 [worst 2294.2000] | 2294.2000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
