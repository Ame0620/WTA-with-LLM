# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:12:31

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5447 | n/a | 0.0667 | 104.6151 | 0.004 | 18.0 | 1891.3 | `57b623aee9c1` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5866 | n/a | 0.0759 | 104.9035 | 0.004 | 18.0 | 1900.8 | `66a14a7b61a8` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6486 | n/a | 0.1519 | 97.6636 | 0.004 | 18.0 | 1672.5 | `1b02df012b38` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6452 | n/a | 0.2630 | 88.4637 | 0.004 | 18.0 | 1633.4 | `8e1102b5fd0d` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6063 +- 0.0433 [worst 0.6486] | 0.6486 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1394 +- 0.0786 [worst 0.2630] | 0.2630 |
| ammo_efficiency | 98.9115 +- 6.6923 [worst 88.4637] | 88.4637 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0046 +- 0.0013 [worst 0.0069] | 0.0069 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1774.5000 +- 122.3621 [worst 1633.4333] | 1633.4333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
