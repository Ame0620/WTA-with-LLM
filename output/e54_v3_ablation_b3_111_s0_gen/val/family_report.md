# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:05:30

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5632 | n/a | 0.1167 | 100.3570 | 0.004 | 18.0 | 1814.4 | `f9478131f9a7` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5799 | n/a | 0.0834 | 105.3466 | 0.004 | 18.0 | 1931.8 | `54c86f6001ae` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6580 | n/a | 0.2130 | 96.2856 | 0.004 | 18.0 | 1627.8 | `2efbca8a6b67` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6547 | n/a | 0.2111 | 86.8127 | 0.004 | 18.0 | 1589.9 | `5e1539f51545` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6139 +- 0.0428 [worst 0.6580] | 0.6580 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1560 +- 0.0572 [worst 0.2130] | 0.2130 |
| ammo_efficiency | 97.2005 +- 6.8020 [worst 86.8127] | 86.8127 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0046 +- 0.0013 [worst 0.0068] | 0.0068 |
| shots_total | 17.9917 +- 0.0144 [worst 18.0000] | 18.0000 |
| destroyed_value | 1740.9833 +- 139.1220 [worst 1589.9333] | 1589.9333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
