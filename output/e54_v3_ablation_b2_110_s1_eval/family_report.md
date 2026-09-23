# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:04:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6682 | 0.4936 | 0.2667 | 76.1874 | 0.003 | 17.0 | 1307.9 | `fd53bf1b353c` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5860 | 0.4035 | 0.1676 | 91.9082 | 0.003 | 17.1 | 1581.2 | `f9cf88b720a8` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6271 +- 0.0411 [worst 0.6682] | 0.6682 |
| gap_mean | 0.4485 +- 0.0451 [worst 0.4936] | 0.4936 |
| invalid_engagement_rate | 0.2172 +- 0.0495 [worst 0.2667] | 0.2667 |
| ammo_efficiency | 84.0478 +- 7.8604 [worst 76.1874] | 76.1874 |
| latency_p50 | 0.0032 +- 0.0001 [worst 0.0033] | 0.0033 |
| latency_p90 | 0.0047 +- 0.0014 [worst 0.0062] | 0.0062 |
| shots_total | 17.0500 +- 0.0500 [worst 17.1000] | 17.1000 |
| destroyed_value | 1444.5667 +- 136.6333 [worst 1307.9333] | 1307.9333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
