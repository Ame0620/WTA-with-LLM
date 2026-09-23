# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:16:04

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6371 | n/a | 0.1981 | 78.8844 | 0.003 | 18.0 | 1430.4 | `0c31e8913a77` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5707 | n/a | 0.1093 | 89.6632 | 0.003 | 18.0 | 1639.7 | `8383e9529722` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6039 +- 0.0332 [worst 0.6371] | 0.6371 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1537 +- 0.0444 [worst 0.1981] | 0.1981 |
| ammo_efficiency | 84.2738 +- 5.3894 [worst 78.8844] | 78.8844 |
| latency_p50 | 0.0031 +- 0.0000 [worst 0.0031] | 0.0031 |
| latency_p90 | 0.0046 +- 0.0012 [worst 0.0059] | 0.0059 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1535.0500 +- 104.6167 [worst 1430.4333] | 1430.4333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
