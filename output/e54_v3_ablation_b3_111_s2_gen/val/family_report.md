# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:13:32

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5643 | n/a | 0.1527 | 99.1436 | 0.004 | 17.9 | 1810.0 | `1a7bbdf08369` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6335 | n/a | 0.2204 | 93.1713 | 0.004 | 18.0 | 1685.0 | `939ac63f3089` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6232 | n/a | 0.1062 | 105.3523 | 0.004 | 17.9 | 1793.6 | `bcbe3bb620fb` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6476 | n/a | 0.2019 | 93.2940 | 0.004 | 18.0 | 1622.2 | `396c4ec0af10` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6172 +- 0.0317 [worst 0.6476] | 0.6476 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1703 +- 0.0445 [worst 0.2204] | 0.2204 |
| ammo_efficiency | 97.7403 +- 5.0139 [worst 93.1713] | 93.1713 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0047 +- 0.0014 [worst 0.0072] | 0.0072 |
| shots_total | 17.9500 +- 0.0553 [worst 18.0000] | 18.0000 |
| destroyed_value | 1727.7167 +- 77.5560 [worst 1622.2333] | 1622.2333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
