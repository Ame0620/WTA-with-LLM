# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:57:31

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6609 | 0.4999 | 0.1574 | 73.5586 | 0.004 | 18.0 | 1336.7 | `72a7f7cbfb8d` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6135 | 0.3947 | 0.0926 | 82.7844 | 0.004 | 18.0 | 1475.9 | `3e253b8d3e9d` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6372 +- 0.0237 [worst 0.6609] | 0.6609 |
| gap_mean | 0.4473 +- 0.0526 [worst 0.4999] | 0.4999 |
| invalid_engagement_rate | 0.1250 +- 0.0324 [worst 0.1574] | 0.1574 |
| ammo_efficiency | 78.1715 +- 4.6129 [worst 73.5586] | 73.5586 |
| latency_p50 | 0.0040 +- 0.0004 [worst 0.0045] | 0.0045 |
| latency_p90 | 0.0061 +- 0.0021 [worst 0.0082] | 0.0082 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1406.3000 +- 69.5667 [worst 1336.7333] | 1336.7333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
