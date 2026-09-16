# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **cplex** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 15:07:50

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.7198 | 0.0000 | 0.1433 | 91.7530 | 0.606 | 30.0 | 2285.5 | `cd2fe4324f5a` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.6765 | 0.0000 | 0.0333 | 82.4542 | 0.588 | 30.0 | 2464.0 | `185f4fcb6b1f` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6981 +- 0.0217 [worst 0.7198] | 0.7198 |
| gap_mean | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| invalid_engagement_rate | 0.0883 +- 0.0550 [worst 0.1433] | 0.1433 |
| ammo_efficiency | 87.1036 +- 4.6494 [worst 82.4542] | 82.4542 |
| latency_p50 | 0.5971 +- 0.0090 [worst 0.6061] | 0.6061 |
| latency_p90 | 0.6812 +- 0.0023 [worst 0.6835] | 0.6835 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 2374.7500 +- 89.2500 [worst 2285.5000] | 2285.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
