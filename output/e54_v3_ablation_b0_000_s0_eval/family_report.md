# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:03:27

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6335 | 0.5003 | 0.1981 | 79.5443 | 0.003 | 18.0 | 1444.6 | `79720421e6f1` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5565 | 0.3772 | 0.1426 | 93.8338 | 0.003 | 18.0 | 1693.7 | `05b287977248` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5950 +- 0.0385 [worst 0.6335] | 0.6335 |
| gap_mean | 0.4388 +- 0.0615 [worst 0.5003] | 0.5003 |
| invalid_engagement_rate | 0.1704 +- 0.0278 [worst 0.1981] | 0.1981 |
| ammo_efficiency | 86.6890 +- 7.1448 [worst 79.5443] | 79.5443 |
| latency_p50 | 0.0031 +- 0.0002 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0076 +- 0.0041 [worst 0.0117] | 0.0117 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1569.1500 +- 124.5167 [worst 1444.6333] | 1444.6333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
