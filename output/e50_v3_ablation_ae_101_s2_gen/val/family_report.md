# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:59:18

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5823 | n/a | 0.1519 | 95.2123 | 0.004 | 18.0 | 1735.3 | `ff8381489a28` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5873 | n/a | 0.0685 | 104.6566 | 0.004 | 18.0 | 1897.4 | `62dabee685e4` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.7408 | n/a | 0.3111 | 74.3131 | 0.004 | 18.0 | 1233.7 | `eb54720dcf78` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6841 | n/a | 0.2204 | 83.7362 | 0.004 | 18.0 | 1454.6 | `7c1a4f673840` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6486 +- 0.0669 [worst 0.7408] | 0.7408 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1880 +- 0.0891 [worst 0.3111] | 0.3111 |
| ammo_efficiency | 89.4796 +- 11.4696 [worst 74.3131] | 74.3131 |
| latency_p50 | 0.0039 +- 0.0004 [worst 0.0045] | 0.0045 |
| latency_p90 | 0.0050 +- 0.0017 [worst 0.0080] | 0.0080 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1580.2500 +- 255.2098 [worst 1233.7000] | 1233.7000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
