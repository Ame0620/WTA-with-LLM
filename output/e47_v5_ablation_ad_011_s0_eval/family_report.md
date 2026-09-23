# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:18:58

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.5794 | 2.3408 | 0.3599 | 63.5975 | 0.737 | 54.0 | 3431.1 | `26fbd575fbfe` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.5172 | 1.9419 | 0.3085 | 71.6754 | 0.690 | 51.0 | 3677.1 | `754eab6df3ab` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5483 +- 0.0311 [worst 0.5794] | 0.5794 |
| gap_mean | 2.1414 +- 0.1994 [worst 2.3408] | 2.3408 |
| invalid_engagement_rate | 0.3342 +- 0.0257 [worst 0.3599] | 0.3599 |
| ammo_efficiency | 67.6365 +- 4.0390 [worst 63.5975] | 63.5975 |
| latency_p50 | 0.7138 +- 0.0237 [worst 0.7375] | 0.7375 |
| latency_p90 | 0.9523 +- 0.0350 [worst 0.9873] | 0.9873 |
| shots_total | 52.5000 +- 1.5000 [worst 54.0000] | 54.0000 |
| destroyed_value | 3554.0833 +- 123.0167 [worst 3431.0667] | 3431.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
