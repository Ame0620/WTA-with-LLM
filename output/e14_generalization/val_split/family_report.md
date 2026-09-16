# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-02 18:57:02

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.8760 | n/a | 0.0667 | 29.2176 | 0.007 | 18.0 | 515.2 | `5064e8957e9a` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.8940 | n/a | 0.0556 | 27.1922 | 0.006 | 18.0 | 487.5 | `3036d0334c3e` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.8803 | n/a | 0.1000 | 29.6471 | 0.005 | 18.0 | 569.7 | `db17357381b6` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.9104 | n/a | 0.1796 | 22.4207 | 0.005 | 18.0 | 412.5 | `6f244433469e` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8902 +- 0.0134 [worst 0.9104] | 0.9104 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1005 +- 0.0485 [worst 0.1796] | 0.1796 |
| ammo_efficiency | 27.1194 +- 2.8668 [worst 22.4207] | 22.4207 |
| latency_p50 | 0.0057 +- 0.0005 [worst 0.0065] | 0.0065 |
| latency_p90 | 0.0106 +- 0.0057 [worst 0.0205] | 0.0205 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 496.2250 +- 56.6671 [worst 412.5000] | 412.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
