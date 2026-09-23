# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:31:04

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4362 | n/a | 0.3438 | 65.7386 | 0.021 | 70.0 | 4598.5 | `64753ac0bf42` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4103 | n/a | 0.3729 | 64.0681 | 0.021 | 70.0 | 4491.1 | `a9c6798c1fe1` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4233 +- 0.0130 [worst 0.4362] | 0.4362 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3583 +- 0.0145 [worst 0.3729] | 0.3729 |
| ammo_efficiency | 64.9033 +- 0.8353 [worst 64.0681] | 64.0681 |
| latency_p50 | 0.0207 +- 0.0000 [worst 0.0207] | 0.0207 |
| latency_p90 | 0.0242 +- 0.0018 [worst 0.0261] | 0.0261 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4544.8167 +- 53.7167 [worst 4491.1000] | 4491.1000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
