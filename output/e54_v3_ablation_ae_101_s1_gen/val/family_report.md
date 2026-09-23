# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:10:36

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5772 | n/a | 0.1686 | 101.1829 | 0.004 | 17.0 | 1756.5 | `c7599abfd3c1` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5936 | n/a | 0.0984 | 105.9647 | 0.004 | 17.5 | 1868.4 | `dc61a615b798` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6266 | n/a | 0.1574 | 103.8947 | 0.004 | 18.0 | 1777.2 | `1cc771c780bd` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6367 | n/a | 0.1722 | 96.4873 | 0.004 | 18.0 | 1672.8 | `ef1173789771` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6085 +- 0.0241 [worst 0.6367] | 0.6367 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1492 +- 0.0298 [worst 0.1722] | 0.1722 |
| ammo_efficiency | 101.8824 +- 3.5465 [worst 96.4873] | 96.4873 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0047 +- 0.0015 [worst 0.0073] | 0.0073 |
| shots_total | 17.6167 +- 0.4173 [worst 18.0000] | 18.0000 |
| destroyed_value | 1768.7333 +- 69.5675 [worst 1672.8000] | 1672.8000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
