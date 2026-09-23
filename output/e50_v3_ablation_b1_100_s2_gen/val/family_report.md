# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 02:00:23

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.8076 | n/a | 0.2648 | 44.2539 | 0.003 | 18.0 | 799.1 | `cb7b348942b9` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.7559 | n/a | 0.2019 | 61.6625 | 0.003 | 18.0 | 1122.6 | `085d589caaa8` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.8104 | n/a | 0.3130 | 54.6207 | 0.003 | 18.0 | 902.7 | `7f566fd3e65e` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.7856 | n/a | 0.2630 | 55.4599 | 0.004 | 18.0 | 987.2 | `064c8d49f3ae` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7899 +- 0.0219 [worst 0.8104] | 0.8104 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2606 +- 0.0394 [worst 0.3130] | 0.3130 |
| ammo_efficiency | 53.9992 +- 6.2493 [worst 44.2539] | 44.2539 |
| latency_p50 | 0.0032 +- 0.0003 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0042 +- 0.0012 [worst 0.0062] | 0.0062 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 952.9000 +- 118.4694 [worst 799.1000] | 799.1000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
