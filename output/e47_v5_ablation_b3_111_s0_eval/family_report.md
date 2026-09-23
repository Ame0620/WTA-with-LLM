# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:09:27

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4473 | 2.0877 | 0.3446 | 64.9426 | 0.741 | 69.1 | 4508.7 | `cc28a0cf448f` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4039 | 1.5562 | 0.3938 | 64.9117 | 0.781 | 70.0 | 4539.7 | `70c04983e8d0` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4256 +- 0.0217 [worst 0.4473] | 0.4473 |
| gap_mean | 1.8220 +- 0.2657 [worst 2.0877] | 2.0877 |
| invalid_engagement_rate | 0.3692 +- 0.0246 [worst 0.3938] | 0.3938 |
| ammo_efficiency | 64.9272 +- 0.0154 [worst 64.9117] | 64.9117 |
| latency_p50 | 0.7611 +- 0.0202 [worst 0.7813] | 0.7813 |
| latency_p90 | 0.9659 +- 0.1106 [worst 1.0765] | 1.0765 |
| shots_total | 69.5333 +- 0.4667 [worst 70.0000] | 70.0000 |
| destroyed_value | 4524.1667 +- 15.5000 [worst 4508.6667] | 4508.6667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
