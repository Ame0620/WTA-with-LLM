# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:11:43

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.4473 | n/a | 0.3074 | 67.6115 | 0.023 | 68.7 | 4653.4 | `e22613f15823` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.4238 | n/a | 0.2795 | 77.5623 | 0.021 | 67.5 | 5080.4 | `f2e403cc7299` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.4469 | n/a | 0.2946 | 82.7209 | 0.019 | 68.0 | 5639.8 | `834781f7799f` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.4581 | n/a | 0.3729 | 63.5078 | 0.021 | 70.0 | 4430.2 | `bbf8b595453d` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.4107 | n/a | 0.3082 | 77.2905 | 0.019 | 70.0 | 5294.6 | `885a093b3f8c` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.4849 | n/a | 0.4179 | 68.6863 | 0.019 | 69.0 | 4708.7 | `12cad06fe2e5` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.4204 | n/a | 0.2627 | 70.3409 | 0.019 | 69.9 | 4933.1 | `5e5f4f0b51bf` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.4770 | n/a | 0.3848 | 72.6595 | 0.019 | 65.9 | 4788.5 | `0c2ceee06839` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.4679 | n/a | 0.3702 | 70.5636 | 0.019 | 67.3 | 4709.5 | `26f9ea8d7754` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.4378 | n/a | 0.2871 | 72.5223 | 0.019 | 69.2 | 5008.5 | `31187cf897b7` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.4483 | n/a | 0.3458 | 80.0308 | 0.019 | 68.2 | 5464.5 | `898eacd95d9f` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.4028 | n/a | 0.3052 | 79.7116 | 0.019 | 70.0 | 5487.9 | `642aa1d2aab6` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.4434 | n/a | 0.2939 | 67.4445 | 0.019 | 65.3 | 4404.4 | `19a3f4656ab6` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.4605 | n/a | 0.3762 | 65.2286 | 0.019 | 70.0 | 4599.5 | `5bc396065f16` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.4469 | n/a | 0.3106 | 71.7668 | 0.019 | 70.0 | 5001.8 | `033e93691fdb` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.4565 | n/a | 0.3155 | 72.3912 | 0.019 | 68.0 | 4892.3 | `5d6913809b75` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.4002 | n/a | 0.2731 | 78.7041 | 0.019 | 67.6 | 5284.0 | `9beaa3963a56` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.3858 | n/a | 0.3562 | 71.3743 | 0.019 | 67.9 | 4836.5 | `5863d4c44fe7` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.4071 | n/a | 0.2758 | 72.2942 | 0.022 | 68.5 | 4966.5 | `168cd68b7413` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.4571 | n/a | 0.2890 | 72.5387 | 0.023 | 70.0 | 5097.5 | `c3c6271819bf` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.4830 | n/a | 0.3276 | 75.8847 | 0.024 | 64.0 | 4861.1 | `a1dabf89f3cf` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.4110 | n/a | 0.3370 | 77.4193 | 0.024 | 65.9 | 5115.2 | `88cc39d4f451` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.4549 | n/a | 0.3741 | 66.5491 | 0.024 | 69.6 | 4504.5 | `bccac2acdd29` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.4250 | n/a | 0.2274 | 78.5914 | 0.025 | 66.4 | 5160.8 | `fadae9b15f7f` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4399 +- 0.0269 [worst 0.4849] | 0.4849 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3205 +- 0.0452 [worst 0.4179] | 0.4179 |
| ammo_efficiency | 73.0581 +- 5.0373 [worst 63.5078] | 63.5078 |
| latency_p50 | 0.0204 +- 0.0020 [worst 0.0247] | 0.0247 |
| latency_p90 | 0.0241 +- 0.0037 [worst 0.0379] | 0.0379 |
| shots_total | 68.2111 +- 1.6748 [worst 70.0000] | 70.0000 |
| destroyed_value | 4955.1292 +- 324.0549 [worst 4404.3667] | 4404.3667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
