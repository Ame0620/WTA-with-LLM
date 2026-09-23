# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:07:59

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5837 | n/a | 0.1235 | 100.9193 | 0.003 | 17.0 | 1729.2 | `6eab7c17010d` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6132 | n/a | 0.1019 | 99.5330 | 0.003 | 18.0 | 1778.4 | `5fd3c22b4a29` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6478 | n/a | 0.1725 | 104.6610 | 0.003 | 17.0 | 1676.6 | `68bb9a7465e9` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6368 | n/a | 0.2148 | 91.0543 | 0.003 | 18.0 | 1672.2 | `26e1eb794ddd` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6204 +- 0.0246 [worst 0.6478] | 0.6478 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1532 +- 0.0438 [worst 0.2148] | 0.2148 |
| ammo_efficiency | 99.0419 +- 4.9785 [worst 91.0543] | 91.0543 |
| latency_p50 | 0.0030 +- 0.0002 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0040 +- 0.0012 [worst 0.0060] | 0.0060 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1714.0833 +- 43.3868 [worst 1672.1667] | 1672.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
