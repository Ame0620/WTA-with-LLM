# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:16:01

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5607 | n/a | 0.0588 | 104.9140 | 0.003 | 17.0 | 1824.7 | `fd3662a986ee` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6299 | n/a | 0.1704 | 95.0212 | 0.003 | 18.0 | 1701.8 | `e08fc1e0cc58` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6448 | n/a | 0.2093 | 92.7522 | 0.003 | 18.0 | 1691.0 | `9a8cc56228a2` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6337 | n/a | 0.1648 | 92.0616 | 0.003 | 18.0 | 1686.2 | `71cfeb0590b2` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6173 +- 0.0331 [worst 0.6448] | 0.6448 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1508 +- 0.0558 [worst 0.2093] | 0.2093 |
| ammo_efficiency | 96.1872 +- 5.1560 [worst 92.0616] | 92.0616 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0041 +- 0.0013 [worst 0.0063] | 0.0063 |
| shots_total | 17.7500 +- 0.4330 [worst 18.0000] | 18.0000 |
| destroyed_value | 1725.9167 +- 57.2919 [worst 1686.2333] | 1686.2333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
