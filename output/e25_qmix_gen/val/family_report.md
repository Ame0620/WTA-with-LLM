# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **qmix** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 17:15:24

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.8041 | n/a | 0.3222 | 45.4972 | 0.005 | 18.0 | 813.7 | `1590fc9b46b2` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.7687 | n/a | 0.3296 | 58.5904 | 0.005 | 18.0 | 1063.7 | `ac264dc13f0a` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.8347 | n/a | 0.4759 | 43.2781 | 0.004 | 18.0 | 786.6 | `608ba0fce176` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.8192 | n/a | 0.3722 | 45.9866 | 0.004 | 18.0 | 832.2 | `1b341c18dcc9` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8067 +- 0.0245 [worst 0.8347] | 0.8347 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3750 +- 0.0613 [worst 0.4759] | 0.4759 |
| ammo_efficiency | 48.3381 +- 6.0065 [worst 43.2781] | 43.2781 |
| latency_p50 | 0.0045 +- 0.0001 [worst 0.0046] | 0.0046 |
| latency_p90 | 0.0063 +- 0.0010 [worst 0.0081] | 0.0081 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 874.0417 +- 110.6747 [worst 786.6000] | 786.6000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
