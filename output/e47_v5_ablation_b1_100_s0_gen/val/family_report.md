# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:47:30

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.5137 | n/a | 0.3873 | 61.8752 | 0.015 | 67.1 | 3978.3 | `c9c04926e1ba` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.4139 | n/a | 0.3267 | 71.7718 | 0.015 | 70.0 | 5016.8 | `9065f8641a69` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.4723 | n/a | 0.3567 | 68.2718 | 0.015 | 70.0 | 4513.5 | `4ad6932e2895` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.4725 | n/a | 0.3257 | 63.0744 | 0.015 | 70.0 | 4429.1 | `7ef1ac36d195` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4681 +- 0.0355 [worst 0.5137] | 0.5137 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3491 +- 0.0253 [worst 0.3873] | 0.3873 |
| ammo_efficiency | 66.2483 +- 3.9938 [worst 61.8752] | 61.8752 |
| latency_p50 | 0.0148 +- 0.0001 [worst 0.0150] | 0.0150 |
| latency_p90 | 0.0167 +- 0.0015 [worst 0.0193] | 0.0193 |
| shots_total | 69.2833 +- 1.2413 [worst 70.0000] | 70.0000 |
| destroyed_value | 4484.4333 +- 368.6083 [worst 3978.3000] | 3978.3000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
