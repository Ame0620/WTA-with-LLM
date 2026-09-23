# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:04:59

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5564 | n/a | 0.0667 | 102.5095 | 0.003 | 18.0 | 1842.6 | `0107aa2d33db` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6410 | n/a | 0.2056 | 90.9205 | 0.003 | 18.0 | 1650.8 | `27ee0023bf0d` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6291 | n/a | 0.1611 | 103.5783 | 0.003 | 18.0 | 1765.4 | `0729be83aed4` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6360 | n/a | 0.2148 | 91.3885 | 0.003 | 18.0 | 1676.0 | `6d5aeec69b1c` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6156 +- 0.0344 [worst 0.6410] | 0.6410 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1620 +- 0.0587 [worst 0.2148] | 0.2148 |
| ammo_efficiency | 97.0992 +- 5.9590 [worst 90.9205] | 90.9205 |
| latency_p50 | 0.0031 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0040 +- 0.0011 [worst 0.0059] | 0.0059 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1733.6750 +- 75.9280 [worst 1650.8000] | 1650.8000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
