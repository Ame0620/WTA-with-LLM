# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:56:56

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6280 | n/a | 0.1191 | 84.9226 | 0.004 | 17.1 | 1466.4 | `b082594da6f8` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6032 | n/a | 0.1742 | 89.0812 | 0.004 | 17.0 | 1515.4 | `96c12756c810` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6156 +- 0.0124 [worst 0.6280] | 0.6280 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1466 +- 0.0276 [worst 0.1742] | 0.1742 |
| ammo_efficiency | 87.0019 +- 2.0793 [worst 84.9226] | 84.9226 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0053 +- 0.0015 [worst 0.0068] | 0.0068 |
| shots_total | 17.0500 +- 0.0167 [worst 17.0667] | 17.0667 |
| destroyed_value | 1490.9000 +- 24.4667 [worst 1466.4333] | 1466.4333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
