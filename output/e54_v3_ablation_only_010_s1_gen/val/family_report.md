# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:11:59

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5607 | n/a | 0.0588 | 104.9140 | 0.003 | 17.0 | 1824.7 | `fd3662a986ee` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6410 | n/a | 0.2056 | 90.9205 | 0.003 | 18.0 | 1650.8 | `27ee0023bf0d` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6455 | n/a | 0.1686 | 105.1517 | 0.003 | 17.0 | 1687.6 | `690fac10001b` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6360 | n/a | 0.2148 | 91.3624 | 0.003 | 18.0 | 1676.0 | `6d5aeec69b1c` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6208 +- 0.0348 [worst 0.6455] | 0.6455 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1620 +- 0.0620 [worst 0.2148] | 0.2148 |
| ammo_efficiency | 98.0871 +- 6.9480 [worst 90.9205] | 90.9205 |
| latency_p50 | 0.0031 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0041 +- 0.0013 [worst 0.0063] | 0.0063 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1709.7500 +- 67.6653 [worst 1650.8000] | 1650.8000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
