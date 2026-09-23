# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 3 (base 7) | solver timelimit 30s
- generated at: 2026-09-22 18:47:40

## Per-instance metrics (mean +- std over 3 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5721 | n/a | 0.1536 | 100.4204 | 0.004 | 17.3 | 1777.3 | `14033a95aab6` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6056 | n/a | 0.0926 | 104.5263 | 0.003 | 18.0 | 1813.7 | `9bcf547b1cd0` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6532 | n/a | 0.2222 | 101.4177 | 0.003 | 18.0 | 1650.7 | `2eef76a99f9b` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6539 | n/a | 0.1667 | 89.0962 | 0.003 | 18.0 | 1593.7 | `52dadbd4c31d` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6212 +- 0.0344 [worst 0.6539] | 0.6539 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1588 +- 0.0461 [worst 0.2222] | 0.2222 |
| ammo_efficiency | 98.8652 +- 5.8398 [worst 89.0962] | 89.0962 |
| latency_p50 | 0.0033 +- 0.0002 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0115 +- 0.0106 [worst 0.0297] | 0.0297 |
| shots_total | 17.8333 +- 0.2887 [worst 18.0000] | 18.0000 |
| destroyed_value | 1708.8333 +- 89.9013 [worst 1593.6667] | 1593.6667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
