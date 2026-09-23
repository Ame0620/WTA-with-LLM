# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:30:51

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.4721 | n/a | 0.3186 | 67.6900 | 0.021 | 66.7 | 4318.0 | `eed76593aee2` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.3856 | n/a | 0.2632 | 76.9292 | 0.021 | 68.3 | 5259.1 | `75cd97a6a8fe` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.4477 | n/a | 0.3166 | 67.7388 | 0.021 | 69.8 | 4723.5 | `9713307bd5e3` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.4432 | n/a | 0.2867 | 67.0999 | 0.021 | 70.0 | 4675.8 | `457b63adbb10` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4372 +- 0.0317 [worst 0.4721] | 0.4721 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2963 +- 0.0229 [worst 0.3186] | 0.3186 |
| ammo_efficiency | 69.8645 +- 4.0866 [worst 67.0999] | 67.0999 |
| latency_p50 | 0.0207 +- 0.0001 [worst 0.0209] | 0.0209 |
| latency_p90 | 0.0233 +- 0.0012 [worst 0.0254] | 0.0254 |
| shots_total | 68.7000 +- 1.3187 [worst 70.0000] | 70.0000 |
| destroyed_value | 4744.1000 +- 336.0940 [worst 4318.0000] | 4318.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
