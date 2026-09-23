# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **qmix** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:23:23

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.7032 | n/a | 0.4286 | 35.0695 | 0.014 | 70.0 | 2427.5 | `4fe528308e84` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.6687 | n/a | 0.3329 | 40.7444 | 0.014 | 70.0 | 2836.0 | `bbf6790c64e6` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.7413 | n/a | 0.4243 | 31.6163 | 0.014 | 70.0 | 2212.7 | `6bb5464ecd8a` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.6955 | n/a | 0.3643 | 37.2200 | 0.014 | 70.0 | 2556.9 | `986076b87550` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7022 +- 0.0260 [worst 0.7413] | 0.7413 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3875 +- 0.0405 [worst 0.4286] | 0.4286 |
| ammo_efficiency | 36.1626 +- 3.3157 [worst 31.6163] | 31.6163 |
| latency_p50 | 0.0140 +- 0.0003 [worst 0.0143] | 0.0143 |
| latency_p90 | 0.0184 +- 0.0048 [worst 0.0267] | 0.0267 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 2508.2750 +- 225.6420 [worst 2212.7000] | 2212.7000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
