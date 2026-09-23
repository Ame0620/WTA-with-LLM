# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:50:26

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6995 | n/a | 0.1519 | 65.1235 | 0.004 | 18.0 | 1184.4 | `bd6e98f885a2` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6540 | n/a | 0.1481 | 72.3708 | 0.003 | 18.0 | 1321.4 | `60f05720353d` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6768 +- 0.0228 [worst 0.6995] | 0.6995 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1500 +- 0.0019 [worst 0.1519] | 0.1519 |
| ammo_efficiency | 68.7472 +- 3.6237 [worst 65.1235] | 65.1235 |
| latency_p50 | 0.0034 +- 0.0004 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0052 +- 0.0018 [worst 0.0070] | 0.0070 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1252.9167 +- 68.4833 [worst 1184.4333] | 1184.4333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
