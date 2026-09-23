# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:55:16

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.7186 | 0.4501 | 0.1778 | 60.7589 | 0.003 | 18.0 | 1109.4 | `d598df460ded` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6581 | 0.3513 | 0.1093 | 71.4667 | 0.004 | 18.0 | 1305.5 | `86b33c7cbc39` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6884 +- 0.0302 [worst 0.7186] | 0.7186 |
| gap_mean | 0.4007 +- 0.0494 [worst 0.4501] | 0.4501 |
| invalid_engagement_rate | 0.1435 +- 0.0343 [worst 0.1778] | 0.1778 |
| ammo_efficiency | 66.1128 +- 5.3539 [worst 60.7589] | 60.7589 |
| latency_p50 | 0.0034 +- 0.0002 [worst 0.0035] | 0.0035 |
| latency_p90 | 0.0109 +- 0.0069 [worst 0.0178] | 0.0178 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1207.4500 +- 98.0833 [worst 1109.3667] | 1109.3667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
