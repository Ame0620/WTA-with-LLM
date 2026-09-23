# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 02:01:33

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5686 | n/a | 0.0627 | 102.9244 | 0.004 | 17.0 | 1792.2 | `b35269ab3028` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6494 | n/a | 0.1686 | 94.1890 | 0.004 | 17.0 | 1611.9 | `fa723f6b5bd8` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6428 | n/a | 0.1647 | 105.9273 | 0.004 | 17.0 | 1700.1 | `e216d66decd4` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6737 | n/a | 0.2167 | 84.0268 | 0.004 | 18.0 | 1502.4 | `9a59802c171d` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6336 +- 0.0393 [worst 0.6737] | 0.6737 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1532 +- 0.0561 [worst 0.2167] | 0.2167 |
| ammo_efficiency | 96.7669 +- 8.5262 [worst 84.0268] | 84.0268 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0049 +- 0.0014 [worst 0.0073] | 0.0073 |
| shots_total | 17.2500 +- 0.4330 [worst 18.0000] | 18.0000 |
| destroyed_value | 1651.6500 +- 107.1883 [worst 1502.4000] | 1502.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
