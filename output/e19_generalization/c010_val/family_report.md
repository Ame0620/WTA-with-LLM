# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 14:25:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5784 | n/a | 0.1648 | 95.9741 | 0.005 | 18.0 | 1751.3 | `ec2081d48506` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5946 | n/a | 0.1019 | 103.4126 | 0.005 | 18.0 | 1863.9 | `d853d5b0c470` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6334 | n/a | 0.1037 | 95.3194 | 0.005 | 18.0 | 1745.2 | `aae29b4ea780` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6511 | n/a | 0.1852 | 86.1116 | 0.005 | 18.0 | 1606.1 | `b2b935bb9184` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6144 +- 0.0291 [worst 0.6511] | 0.6511 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1389 +- 0.0368 [worst 0.1852] | 0.1852 |
| ammo_efficiency | 95.2044 +- 6.1372 [worst 86.1116] | 86.1116 |
| latency_p50 | 0.0052 +- 0.0001 [worst 0.0053] | 0.0053 |
| latency_p90 | 0.0078 +- 0.0017 [worst 0.0107] | 0.0107 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1741.6417 +- 91.4108 [worst 1606.1333] | 1606.1333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
