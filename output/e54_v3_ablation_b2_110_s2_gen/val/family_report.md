# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:15:05

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5740 | n/a | 0.1211 | 102.2103 | 0.003 | 17.1 | 1769.4 | `67412e339545` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5817 | n/a | 0.0481 | 106.2198 | 0.003 | 18.0 | 1923.3 | `c68227fc47aa` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6401 | n/a | 0.1697 | 105.7248 | 0.003 | 17.1 | 1713.3 | `9304fb1b7a64` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6453 | n/a | 0.1444 | 94.5377 | 0.003 | 18.0 | 1633.3 | `ea8d6a2435af` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6103 +- 0.0326 [worst 0.6453] | 0.6453 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1209 +- 0.0454 [worst 0.1697] | 0.1697 |
| ammo_efficiency | 102.1732 +- 4.6715 [worst 94.5377] | 94.5377 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0031] | 0.0031 |
| latency_p90 | 0.0039 +- 0.0010 [worst 0.0057] | 0.0057 |
| shots_total | 17.5417 +- 0.4585 [worst 18.0000] | 18.0000 |
| destroyed_value | 1759.8167 +- 106.0673 [worst 1633.2667] | 1633.2667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
