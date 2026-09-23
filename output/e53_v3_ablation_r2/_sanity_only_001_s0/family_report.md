# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 3 (base 7) | solver timelimit 30s
- generated at: 2026-09-22 18:47:44

## Per-instance metrics (mean +- std over 3 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5745 | n/a | 0.1296 | 101.8980 | 0.004 | 18.0 | 1767.7 | `d440dcb287f5` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6067 | n/a | 0.1667 | 101.6590 | 0.007 | 18.0 | 1808.3 | `f01fefe80f7e` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6422 | n/a | 0.1667 | 102.6300 | 0.004 | 18.0 | 1703.0 | `7ac0fc63d3e4` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6615 | n/a | 0.2037 | 93.0760 | 0.004 | 18.0 | 1558.3 | `5e9199ffe6e8` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6212 +- 0.0334 [worst 0.6615] | 0.6615 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1667 +- 0.0262 [worst 0.2037] | 0.2037 |
| ammo_efficiency | 99.8157 +- 3.9076 [worst 93.0760] | 93.0760 |
| latency_p50 | 0.0046 +- 0.0013 [worst 0.0069] | 0.0069 |
| latency_p90 | 0.0150 +- 0.0132 [worst 0.0369] | 0.0369 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1709.3333 +- 94.9275 [worst 1558.3333] | 1558.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
