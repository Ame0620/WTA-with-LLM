# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **mappo** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:03:03

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 1.0000 | n/a | 0.0000 | n/a | 0.012 | 0.0 | 0.0 | `941266e7b2a8` |
| `dn_10x100_K10_s28.txt` | 8560 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `9b73c570fb30` |
| `dn_10x100_K10_s29.txt` | 8553 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `87c59a92bfd2` |
| `dn_10x100_K10_s30.txt` | 8397 | 1.0000 | n/a | 0.0000 | n/a | 0.011 | 0.0 | 0.0 | `d203f687f76d` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 1.0000 +- 0.0000 [worst 1.0000] | 1.0000 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| ammo_efficiency | n/a | n/a |
| latency_p50 | 0.0114 +- 0.0006 [worst 0.0124] | 0.0124 |
| latency_p90 | 0.0144 +- 0.0042 [worst 0.0216] | 0.0216 |
| shots_total | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| destroyed_value | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
