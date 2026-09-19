# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **greedy_nearest** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 17:53:51

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.9164 | 0.6074 | 0.4844 | 22.5223 | 0.619 | 30.0 | 682.0 | `5304fcc08766` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.9332 | 0.6028 | 0.4867 | 17.2342 | 0.585 | 30.0 | 509.0 | `e675812956cb` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.9248 +- 0.0084 [worst 0.9332] | 0.9332 |
| gap_mean | 0.6051 +- 0.0023 [worst 0.6074] | 0.6074 |
| invalid_engagement_rate | 0.4856 +- 0.0011 [worst 0.4867] | 0.4867 |
| ammo_efficiency | 19.8782 +- 2.6440 [worst 17.2342] | 17.2342 |
| latency_p50 | 0.6021 +- 0.0173 [worst 0.6193] | 0.6193 |
| latency_p90 | 0.7558 +- 0.0046 [worst 0.7605] | 0.7605 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 595.4833 +- 86.4833 [worst 509.0000] | 509.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
