# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-09 20:28:21

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5840 | n/a | 0.1574 | 95.5853 | 0.004 | 18.0 | 1728.1 | `60000a48a113` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5853 | n/a | 0.0537 | 105.4062 | 0.004 | 18.0 | 1906.9 | `7d149b1549cc` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6304 | n/a | 0.1160 | 102.2318 | 0.004 | 17.2 | 1759.5 | `fc3ea0ef0e6b` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6485 | n/a | 0.1667 | 89.0222 | 0.004 | 18.0 | 1618.1 | `9eb129534839` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6120 +- 0.0282 [worst 0.6485] | 0.6485 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1234 +- 0.0446 [worst 0.1667] | 0.1667 |
| ammo_efficiency | 98.0614 +- 6.3083 [worst 89.0222] | 89.0222 |
| latency_p50 | 0.0040 +- 0.0001 [worst 0.0041] | 0.0041 |
| latency_p90 | 0.0057 +- 0.0010 [worst 0.0072] | 0.0072 |
| shots_total | 17.8083 +- 0.3320 [worst 18.0000] | 18.0000 |
| destroyed_value | 1753.1667 +- 103.1456 [worst 1618.1000] | 1618.1000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
