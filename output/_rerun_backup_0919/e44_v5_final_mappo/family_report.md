# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **mappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:02:12

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 1.0000 | 2.6561 | 0.0000 | n/a | 0.763 | 0.0 | 0.0 | `d3e1e288249a` |
| `dn_10x100_K10_s02.txt` | 7616 | 1.0000 | 2.1073 | 0.0000 | n/a | 0.766 | 0.0 | 0.0 | `a869dc699720` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 1.0000 +- 0.0000 [worst 1.0000] | 1.0000 |
| gap_mean | 2.3817 +- 0.2744 [worst 2.6561] | 2.6561 |
| invalid_engagement_rate | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| ammo_efficiency | n/a | n/a |
| latency_p50 | 0.7645 +- 0.0011 [worst 0.7656] | 0.7656 |
| latency_p90 | 1.0063 +- 0.1809 [worst 1.1872] | 1.1872 |
| shots_total | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| destroyed_value | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
