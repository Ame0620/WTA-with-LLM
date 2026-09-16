# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 14:24:18

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5417 | n/a | 0.0667 | 106.0925 | 0.005 | 18.0 | 1903.9 | `4786cf8a2029` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6006 | n/a | 0.1037 | 101.2853 | 0.005 | 18.0 | 1836.3 | `5ba3bad0da55` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6701 | n/a | 0.2074 | 85.6217 | 0.005 | 18.0 | 1570.2 | `2a47e4eb2d20` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6444 | n/a | 0.1667 | 88.4637 | 0.005 | 18.0 | 1637.3 | `a50dc53782c0` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6142 +- 0.0487 [worst 0.6701] | 0.6701 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1361 +- 0.0545 [worst 0.2074] | 0.2074 |
| ammo_efficiency | 95.3658 +- 8.5541 [worst 85.6217] | 85.6217 |
| latency_p50 | 0.0053 +- 0.0001 [worst 0.0054] | 0.0054 |
| latency_p90 | 0.0081 +- 0.0015 [worst 0.0107] | 0.0107 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1736.9167 +- 137.3768 [worst 1570.2000] | 1570.2000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
