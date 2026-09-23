# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:14:36

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5876 | n/a | 0.1192 | 105.2015 | 0.004 | 15.9 | 1712.9 | `5f0d6b3cd0e2` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6143 | n/a | 0.1096 | 100.7630 | 0.004 | 17.5 | 1773.5 | `85ff8ab9bc37` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6191 | n/a | 0.1022 | 106.2934 | 0.004 | 17.9 | 1813.1 | `d035c4239cdd` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6477 | n/a | 0.1627 | 98.5232 | 0.004 | 17.0 | 1622.0 | `dd23d0a0573f` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6172 +- 0.0213 [worst 0.6477] | 0.6477 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1234 +- 0.0235 [worst 0.1627] | 0.1627 |
| ammo_efficiency | 102.6953 +- 3.1768 [worst 98.5232] | 98.5232 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0046 +- 0.0013 [worst 0.0067] | 0.0067 |
| shots_total | 17.0917 +- 0.7459 [worst 17.9333] | 17.9333 |
| destroyed_value | 1730.3750 +- 72.0016 [worst 1622.0333] | 1622.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
