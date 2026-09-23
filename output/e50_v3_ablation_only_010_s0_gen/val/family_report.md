# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:51:35

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.7037 | n/a | 0.2622 | 82.5116 | 0.003 | 15.0 | 1230.6 | `e5d50e165877` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6521 | n/a | 0.1812 | 99.6800 | 0.004 | 16.0 | 1599.7 | `14892448f03e` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.8163 | n/a | 0.4556 | 58.8287 | 0.003 | 15.0 | 874.2 | `b92da3afc2cf` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.8381 | n/a | 0.5867 | 49.7681 | 0.003 | 15.0 | 745.5 | `37f14692b5db` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7526 +- 0.0772 [worst 0.8381] | 0.8381 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3714 +- 0.1593 [worst 0.5867] | 0.5867 |
| ammo_efficiency | 72.6971 +- 19.6371 [worst 49.7681] | 49.7681 |
| latency_p50 | 0.0032 +- 0.0003 [worst 0.0036] | 0.0036 |
| latency_p90 | 0.0041 +- 0.0012 [worst 0.0061] | 0.0061 |
| shots_total | 15.2500 +- 0.4330 [worst 16.0000] | 16.0000 |
| destroyed_value | 1112.5000 +- 332.7235 [worst 745.4667] | 745.4667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
