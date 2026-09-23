# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:09:31

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5620 | n/a | 0.1537 | 98.9782 | 0.004 | 18.0 | 1819.5 | `5f097cca0360` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6229 | n/a | 0.2224 | 94.0054 | 0.004 | 18.0 | 1734.0 | `e964e4b0e87e` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6188 | n/a | 0.1426 | 104.4658 | 0.004 | 18.0 | 1814.6 | `00deca663f69` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6344 | n/a | 0.2278 | 91.3125 | 0.004 | 18.0 | 1683.0 | `df676aa50ac6` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6095 +- 0.0280 [worst 0.6344] | 0.6344 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1866 +- 0.0387 [worst 0.2278] | 0.2278 |
| ammo_efficiency | 97.1905 +- 5.0205 [worst 91.3125] | 91.3125 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0048 +- 0.0015 [worst 0.0074] | 0.0074 |
| shots_total | 17.9917 +- 0.0144 [worst 18.0000] | 18.0000 |
| destroyed_value | 1762.7750 +- 57.1989 [worst 1683.0333] | 1683.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
