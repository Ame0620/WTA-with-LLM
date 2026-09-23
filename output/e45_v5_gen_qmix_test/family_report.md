# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **qmix** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:23:51

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.7219 | n/a | 0.4614 | 33.8315 | 0.014 | 70.0 | 2268.6 | `17b922f431f2` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.6394 | n/a | 0.3971 | 38.5922 | 0.014 | 70.0 | 2746.6 | `00326f54513d` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6806 +- 0.0413 [worst 0.7219] | 0.7219 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.4293 +- 0.0321 [worst 0.4614] | 0.4614 |
| ammo_efficiency | 36.2119 +- 2.3803 [worst 33.8315] | 33.8315 |
| latency_p50 | 0.0142 +- 0.0002 [worst 0.0144] | 0.0144 |
| latency_p90 | 0.0216 +- 0.0053 [worst 0.0269] | 0.0269 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 2507.6000 +- 239.0000 [worst 2268.6000] | 2268.6000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
