# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 3 (base 7) | solver timelimit 30s
- generated at: 2026-09-22 18:47:42

## Per-instance metrics (mean +- std over 3 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5706 | n/a | 0.0980 | 101.2249 | 0.004 | 17.0 | 1783.7 | `2e766df4e59d` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6161 | n/a | 0.1296 | 97.4613 | 0.003 | 18.0 | 1765.3 | `24734a356343` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6606 | n/a | 0.1765 | 105.1534 | 0.003 | 17.0 | 1615.7 | `650aa9f57ecc` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6281 | n/a | 0.1852 | 91.5256 | 0.003 | 18.0 | 1712.3 | `893d2531ffdb` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6188 +- 0.0323 [worst 0.6606] | 0.6606 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1473 +- 0.0354 [worst 0.1852] | 0.1852 |
| ammo_efficiency | 98.8413 +- 5.0236 [worst 91.5256] | 91.5256 |
| latency_p50 | 0.0033 +- 0.0003 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0102 +- 0.0113 [worst 0.0298] | 0.0298 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1719.2500 +- 65.2888 [worst 1615.6667] | 1615.6667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
