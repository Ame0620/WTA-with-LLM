# r2 等价性验收报告（E1/E2/E3）

- 日期：2026-09-21
- 需求：《需求文档_v3消融实验_第二轮.md》§S3
- 改造前基线：git `39e24a7`（工作区状态=上轮实验后）；关键源文件 md5 记录于 `r2_pre_mod_md5.txt`
- 改造文件：`marl/reward.py`（+phi_scale）、`marl/train.py`（CLI 三参数 / process_batch α·β / 埋点 / 元数据 / 日志第二行）、`marl/policy.py`（reshaping 校验 + _env 注入）
- 对比口径：承上轮 S2.2 —— train_log 剔除 elapsed/wall/time 字段后逐位一致；best.pt 全部张量 `torch.equal`；非张量元数据一致（豁免 r2 新增键 `reshaping`/`versions.recal`——after 侧必然新增）

## E1 改造前后位级等价 —— PASS

- 命令（前后同一条，仅输出目录不同）：
  `python marl/train.py --data-dir data/dn-data-v3 --seed 0 --iters 50 --eval-every 25 --use-dcca 1 --use-eaps 1 --use-casp 1 --output <dir>`
- before：`output/_pre_ablation_ref/r2_e1_before/`（改造前代码，MPS，403s，best val 0.7233）
- after：`output/_pre_ablation_ref/r2_e1_after/`（改造后代码缺省参数，MPS）
- 结果：train_log 50 行全部数值字段逐位一致（含 train_leak=0.7366044955090036、val_leak_mean=0.7750613286441125、policy_loss 等全部训练量）；best.pt 全部张量 `torch.equal`。
- 剔除口径补充：本轮新增纯观测列 `r_shape_share` / `credit_adv_share`（before 侧不存在该键）与 wall/time 同列剔除——它们只读不写任何训练路径（审计 E10 + 本报告 E1 张量位级一致共同佐证）。

## E2 全关隔离性 —— PASS

- 命令（三组同构，CPU，25 iters）：`(0,0,0)` + `--phi-scale/--credit-alpha/--cf-beta ∈ {1.0,1.0,1.0} / {0.2,0.2,0.2} / {2.0,2.0,2.0}`
- 结果：三组 train_log 逐位一致 + best.pt 张量位级一致 → λ/α/β 在全关配置下完全惰性（任何极端取值不进计算图）。

## E3 审计测试扩展 35 → 45 项 —— PASS（45/45）

新增 E 组 10 项（`tests/test_ablation_switches.py`）：

| # | 检查 | 结果 |
|---|---|---|
| E1 | eaps=0 时 λ 位级惰性（同 RNG 流 R_shaped 流逐位相同） | PASS |
| E2 | dcca=0 时 α/β 位级惰性（adv 流逐位相同） | PASS |
| E3 | λ=0.5 将塑形项精确减半（舍入紧致，max dev ≤1e-12；R_team 流位级相同） | PASS |
| E4 | dcca=1 时 α=0.5 实际改变注入优势 | PASS |
| E5 | CLI 缺省锁定 1.0 + `[reshaping]` 第二行 | PASS |
| E6 | best.pt reshaping 三元组与 trainer 标量逐字相等 | PASS |
| E7 | 缺 `reshaping` 元数据拒载（上轮 e49 checkpoint 由此被拒，R11 预期行为） | PASS |
| E8 | `MARL_EXPECT_RESHAPING` 不匹配 → raise（运行时可达） | PASS |
| E9 | `MARL_EXPECT_RESHAPING` 匹配 → 正常加载 | PASS |
| E10 | 机制计数器：全开时 shape_abs/credit_abs > 0，全关时 == 0 | PASS |

## 结论

S2/S3 管线改造满足 R1（缺省位级等价）、R2（全关隔离）、R11（上轮 checkpoint 拒载）全部验收条件，e52 调参轮可以启动。
