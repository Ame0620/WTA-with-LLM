# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:09:01

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6591 | n/a | 0.2250 | 93.3864 | 0.003 | 16.0 | 1343.8 | `2d1a082f72d9` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5669 | n/a | 0.1093 | 90.3440 | 0.003 | 18.0 | 1654.0 | `3def7e601bdd` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6130 +- 0.0461 [worst 0.6591] | 0.6591 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1671 +- 0.0579 [worst 0.2250] | 0.2250 |
| ammo_efficiency | 91.8652 +- 1.5212 [worst 90.3440] | 90.3440 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0047 +- 0.0012 [worst 0.0059] | 0.0059 |
| shots_total | 17.0000 +- 1.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1498.9333 +- 155.1000 [worst 1343.8333] | 1343.8333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
