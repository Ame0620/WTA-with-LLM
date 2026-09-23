# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:11:31

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5861 | n/a | 0.1630 | 93.9453 | 0.003 | 18.0 | 1719.2 | `d1f19c84004a` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5756 | n/a | 0.0341 | 110.8348 | 0.003 | 17.4 | 1951.5 | `5ed59cc98f81` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6258 | n/a | 0.1611 | 104.0874 | 0.003 | 18.0 | 1781.3 | `1ac82276b678` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6397 | n/a | 0.1574 | 96.3386 | 0.003 | 18.0 | 1658.9 | `92100f154f35` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6068 +- 0.0267 [worst 0.6397] | 0.6397 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1289 +- 0.0548 [worst 0.1630] | 0.1630 |
| ammo_efficiency | 101.3015 +- 6.6594 [worst 93.9453] | 93.9453 |
| latency_p50 | 0.0031 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0040 +- 0.0012 [worst 0.0061] | 0.0061 |
| shots_total | 17.8583 +- 0.2454 [worst 18.0000] | 18.0000 |
| destroyed_value | 1777.7417 +- 109.2641 [worst 1658.9333] | 1658.9333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
