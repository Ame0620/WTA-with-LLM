# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 3 (base 7) | solver timelimit 30s
- generated at: 2026-09-22 18:47:38

## Per-instance metrics (mean +- std over 3 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5576 | n/a | 0.1481 | 100.3437 | 0.005 | 18.0 | 1837.7 | `b7d66b5c4526` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5966 | n/a | 0.1481 | 100.9724 | 0.004 | 18.0 | 1854.7 | `90cdc27ef2c4` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6517 | n/a | 0.1481 | 97.6829 | 0.004 | 18.0 | 1658.0 | `6a2fa25502cf` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6292 | n/a | 0.1111 | 98.9543 | 0.004 | 18.0 | 1707.0 | `4433fe5c1c72` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6088 +- 0.0354 [worst 0.6517] | 0.6517 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1389 +- 0.0160 [worst 0.1481] | 0.1481 |
| ammo_efficiency | 99.4883 +- 1.2727 [worst 97.6829] | 97.6829 |
| latency_p50 | 0.0041 +- 0.0007 [worst 0.0053] | 0.0053 |
| latency_p90 | 0.0120 +- 0.0139 [worst 0.0360] | 0.0360 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1764.3333 +- 83.8627 [worst 1658.0000] | 1658.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
