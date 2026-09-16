# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-07 18:52:13

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6340 | 0.1865 | 0.1767 | 78.9001 | 0.404 | 20.0 | 1442.6 | `a07c89011139` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6048 | 0.2616 | 0.1654 | 76.9577 | 0.381 | 19.2 | 1509.1 | `acac020f7e47` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6194 +- 0.0146 [worst 0.6340] | 0.6340 |
| gap_mean | 0.2240 +- 0.0376 [worst 0.2616] | 0.2616 |
| invalid_engagement_rate | 0.1710 +- 0.0057 [worst 0.1767] | 0.1767 |
| ammo_efficiency | 77.9289 +- 0.9712 [worst 76.9577] | 76.9577 |
| latency_p50 | 0.3926 +- 0.0112 [worst 0.4038] | 0.4038 |
| latency_p90 | 0.4263 +- 0.0093 [worst 0.4356] | 0.4356 |
| shots_total | 19.5833 +- 0.4167 [worst 20.0000] | 20.0000 |
| destroyed_value | 1475.8833 +- 33.2500 [worst 1442.6333] | 1442.6333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
