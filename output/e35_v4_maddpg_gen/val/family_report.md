# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_5x100_K10_s27.txt', 'dn_5x100_K10_s28.txt', 'dn_5x100_K10_s29.txt', 'dn_5x100_K10_s30.txt']) | policy: **maddpg** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:24:36

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s27.txt` | 8180 | 0.8095 | n/a | 0.1611 | 53.3666 | 0.006 | 30.0 | 1558.3 | `d35c481d029f` |
| `dn_5x100_K10_s28.txt` | 8560 | 0.7850 | n/a | 0.1033 | 61.3982 | 0.006 | 30.0 | 1840.5 | `d9ac2b0bed84` |
| `dn_5x100_K10_s29.txt` | 8553 | 0.8139 | n/a | 0.1244 | 52.6790 | 0.006 | 30.0 | 1591.5 | `29ca96faf419` |
| `dn_5x100_K10_s30.txt` | 8397 | 0.7801 | n/a | 0.1911 | 61.8857 | 0.006 | 30.0 | 1846.8 | `495d524ed7ff` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7971 +- 0.0148 [worst 0.8139] | 0.8139 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1450 +- 0.0337 [worst 0.1911] | 0.1911 |
| ammo_efficiency | 57.3324 +- 4.3199 [worst 52.6790] | 52.6790 |
| latency_p50 | 0.0059 +- 0.0002 [worst 0.0062] | 0.0062 |
| latency_p90 | 0.0079 +- 0.0013 [worst 0.0093] | 0.0093 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 1709.2750 +- 134.9383 [worst 1558.2667] | 1558.2667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
