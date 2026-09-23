# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:55:50

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.7060 | 0.5794 | 0.1244 | 77.3325 | 0.003 | 15.0 | 1158.9 | `4ec8d761e87f` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6749 | 0.5757 | 0.1267 | 81.9299 | 0.004 | 15.0 | 1241.5 | `210def567b51` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6905 +- 0.0156 [worst 0.7060] | 0.7060 |
| gap_mean | 0.5775 +- 0.0018 [worst 0.5794] | 0.5794 |
| invalid_engagement_rate | 0.1256 +- 0.0011 [worst 0.1267] | 0.1267 |
| ammo_efficiency | 79.6312 +- 2.2987 [worst 77.3325] | 77.3325 |
| latency_p50 | 0.0034 +- 0.0002 [worst 0.0036] | 0.0036 |
| latency_p90 | 0.0320 +- 0.0138 [worst 0.0458] | 0.0458 |
| shots_total | 15.0000 +- 0.0000 [worst 15.0000] | 15.0000 |
| destroyed_value | 1200.2167 +- 41.3167 [worst 1158.9000] | 1158.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
