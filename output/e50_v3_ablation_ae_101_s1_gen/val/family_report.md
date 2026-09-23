# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:54:38

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5892 | n/a | 0.1593 | 93.7721 | 0.004 | 18.0 | 1706.4 | `708b316cca7f` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6190 | n/a | 0.1426 | 97.8046 | 0.004 | 18.0 | 1751.9 | `48ea28eeb9b2` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6854 | n/a | 0.1741 | 85.7516 | 0.004 | 18.0 | 1497.3 | `62349bc2a0bf` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6998 | n/a | 0.2611 | 80.7462 | 0.004 | 18.0 | 1382.1 | `5f54c5ab0e47` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6484 +- 0.0458 [worst 0.6998] | 0.6998 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1843 +- 0.0457 [worst 0.2611] | 0.2611 |
| ammo_efficiency | 89.5187 +- 6.6689 [worst 80.7462] | 80.7462 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0049 +- 0.0012 [worst 0.0069] | 0.0069 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1584.4083 +- 151.2186 [worst 1382.0667] | 1382.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
