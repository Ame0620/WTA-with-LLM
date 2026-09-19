# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **qmix** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:11:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.8454 | 0.3344 | 0.1833 | 40.8746 | 0.719 | 30.0 | 1260.9 | `fece09983fe3` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.8748 | 0.3629 | 0.2578 | 32.4191 | 0.725 | 30.0 | 953.2 | `344596ffcd21` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8601 +- 0.0147 [worst 0.8748] | 0.8748 |
| gap_mean | 0.3486 +- 0.0143 [worst 0.3629] | 0.3629 |
| invalid_engagement_rate | 0.2206 +- 0.0372 [worst 0.2578] | 0.2578 |
| ammo_efficiency | 36.6469 +- 4.2277 [worst 32.4191] | 32.4191 |
| latency_p50 | 0.7217 +- 0.0031 [worst 0.7249] | 0.7249 |
| latency_p90 | 0.7865 +- 0.0002 [worst 0.7867] | 0.7867 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 1107.0667 +- 153.8333 [worst 953.2333] | 953.2333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
