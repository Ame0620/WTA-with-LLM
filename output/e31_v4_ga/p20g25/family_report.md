# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **ga** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 17:46:09

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.7238 | 0.0546 | 0.1389 | 87.4656 | 0.601 | 30.0 | 2253.0 | `aa46768cba56` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.6940 | 0.0441 | 0.0333 | 78.1919 | 0.523 | 30.0 | 2330.6 | `cab04d4f3858` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7089 +- 0.0149 [worst 0.7238] | 0.7238 |
| gap_mean | 0.0493 +- 0.0053 [worst 0.0546] | 0.0546 |
| invalid_engagement_rate | 0.0861 +- 0.0528 [worst 0.1389] | 0.1389 |
| ammo_efficiency | 82.8287 +- 4.6369 [worst 78.1919] | 78.1919 |
| latency_p50 | 0.5621 +- 0.0387 [worst 0.6007] | 0.6007 |
| latency_p90 | 0.6802 +- 0.0037 [worst 0.6839] | 0.6839 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 2291.8333 +- 38.8000 [worst 2253.0333] | 2253.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
