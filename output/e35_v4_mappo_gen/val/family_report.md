# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_5x100_K10_s27.txt', 'dn_5x100_K10_s28.txt', 'dn_5x100_K10_s29.txt', 'dn_5x100_K10_s30.txt']) | policy: **mappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:26:19

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s27.txt` | 8180 | 0.7172 | n/a | 0.0878 | 76.2896 | 0.006 | 30.0 | 2313.6 | `102bd4809129` |
| `dn_5x100_K10_s28.txt` | 8560 | 0.7083 | n/a | 0.1667 | 91.0121 | 0.006 | 27.0 | 2496.6 | `bc5a40fcb6e4` |
| `dn_5x100_K10_s29.txt` | 8553 | 0.7034 | n/a | 0.0310 | 87.3970 | 0.006 | 29.0 | 2536.9 | `3d6125ca42f7` |
| `dn_5x100_K10_s30.txt` | 8397 | 0.7290 | n/a | 0.1589 | 75.8866 | 0.006 | 30.0 | 2275.6 | `5edefb16d355` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7145 +- 0.0097 [worst 0.7290] | 0.7290 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1111 +- 0.0555 [worst 0.1667] | 0.1667 |
| ammo_efficiency | 82.6463 +- 6.6831 [worst 75.8866] | 75.8866 |
| latency_p50 | 0.0061 +- 0.0002 [worst 0.0063] | 0.0063 |
| latency_p90 | 0.0089 +- 0.0019 [worst 0.0116] | 0.0116 |
| shots_total | 29.0000 +- 1.2247 [worst 30.0000] | 30.0000 |
| destroyed_value | 2405.7000 +- 112.7814 [worst 2275.6333] | 2275.6333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
