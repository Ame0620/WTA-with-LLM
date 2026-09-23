# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:14:39

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6526 | n/a | 0.2235 | 81.2581 | 0.004 | 17.0 | 1369.3 | `2e53d75eb815` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6282 | n/a | 0.2315 | 78.7161 | 0.004 | 18.0 | 1420.0 | `c722020aa646` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6404 +- 0.0122 [worst 0.6526] | 0.6526 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2275 +- 0.0040 [worst 0.2315] | 0.2315 |
| ammo_efficiency | 79.9871 +- 1.2710 [worst 78.7161] | 78.7161 |
| latency_p50 | 0.0037 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0057 +- 0.0016 [worst 0.0073] | 0.0073 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1394.6667 +- 25.3333 [worst 1369.3333] | 1369.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
