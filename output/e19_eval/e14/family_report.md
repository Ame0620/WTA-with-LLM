# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-07 19:20:34

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.8713 | 0.6671 | 0.2019 | 28.4043 | 0.460 | 18.0 | 507.2 | `3931af8e9607` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.9304 | 0.7394 | 0.0241 | 15.0966 | 0.462 | 18.0 | 265.7 | `ae69d2700fd8` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.9009 +- 0.0295 [worst 0.9304] | 0.9304 |
| gap_mean | 0.7032 +- 0.0361 [worst 0.7394] | 0.7394 |
| invalid_engagement_rate | 0.1130 +- 0.0889 [worst 0.2019] | 0.2019 |
| ammo_efficiency | 21.7505 +- 6.6539 [worst 15.0966] | 15.0966 |
| latency_p50 | 0.4612 +- 0.0012 [worst 0.4624] | 0.4624 |
| latency_p90 | 0.4875 +- 0.0010 [worst 0.4884] | 0.4884 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 386.4333 +- 120.7333 [worst 265.7000] | 265.7000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
