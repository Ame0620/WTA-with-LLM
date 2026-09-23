# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:08:59

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5454 | n/a | 0.0647 | 108.2837 | 0.003 | 17.0 | 1888.4 | `9a936fa7825e` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6264 | n/a | 0.1593 | 95.1110 | 0.003 | 18.0 | 1717.8 | `eaeb712cbf38` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6460 | n/a | 0.1686 | 97.7373 | 0.003 | 17.0 | 1685.0 | `8fa0c80ffad6` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6558 | n/a | 0.2185 | 87.7704 | 0.003 | 18.0 | 1584.7 | `d64c68b54432` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6184 +- 0.0434 [worst 0.6558] | 0.6558 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1528 +- 0.0556 [worst 0.2185] | 0.2185 |
| ammo_efficiency | 97.2256 +- 7.3556 [worst 87.7704] | 87.7704 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0040 +- 0.0013 [worst 0.0063] | 0.0063 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1718.9833 +- 109.3935 [worst 1584.7333] | 1584.7333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
