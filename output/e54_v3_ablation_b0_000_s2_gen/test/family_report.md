# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:13:02

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6559 | n/a | 0.2000 | 86.2765 | 0.003 | 17.0 | 1356.4 | `478b7b0f27e6` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5469 | n/a | 0.1185 | 96.6597 | 0.003 | 18.0 | 1730.5 | `661bca6445fa` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6014 +- 0.0545 [worst 0.6559] | 0.6559 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1593 +- 0.0407 [worst 0.2000] | 0.2000 |
| ammo_efficiency | 91.4681 +- 5.1916 [worst 86.2765] | 86.2765 |
| latency_p50 | 0.0032 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0046 +- 0.0011 [worst 0.0057] | 0.0057 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1543.4500 +- 187.0833 [worst 1356.3667] | 1356.3667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
