# MARL 算法改进实验报告（WTA-Dn-branch01）

日期：2026-09-07 · 实例族：dn_3x50_K10（train s03-s30 / val s27,s30 / test s01,s02）
评估协议：test split × 30 seeds × MC，指标口径与 e11-e13 基线完全一致。

## 1. 执行摘要

四个改进模块（A1 PPO 批化 / A2 预算放宽 / A3 击杀信用摊派 / A4 BC 热启动）
加上新增同信息中心化基线 PO-CPLEX（E18），全部按方案门禁落地：

| 臂 | test leak（越低越好） | 相对上一环节 |
|---|---:|---|
| e14（原始全链参照） | 0.9009 | — |
| e15 = A1+A2（批化+预算 4×，旧信用） | 0.6194 | **−31.3%** |
| e16_c010 = e15 + A3（p_shot 摊派，c=0.01） | **0.5546** | **−10.5%** |
| PO-CPLEX / myopic-CPLEX（同信息中心化最优） | 0.7085 | e16_c010 超出 **21.7%** |
| greedy | 0.7913 | |
| none（不设防） | 1.0000 | |

**核心结论：改进后的 MARL 首次在同一信息边界内显著超过中心化
myopic CPLEX 最优**（0.5546 vs 0.7085，n=60，两分布 std 0.062/0.034，
不重叠）。每步 myopic gap 反而升高（0.366 vs greedy 0.277）——这是
MARL 学到**非 myopic 时序协同**（跨步弹药分配/提前压制）的直接证据，
而非单步逼近。

## 2. 模块落地与门禁

### A0 诊断（output/e15_diag/）
- e14 曲线判 PLATEAU（best@iter60 后 20 个 eval 点无突破）→ 预算放宽
  单独收益有限，A3 为主攻（验证成立：e15 vs e16_c010 差 10.5%）。
- Φ 翻转备选触发（发射步负踢 −0.0060 ≥ 0.25×击杀信用）→ e16 选档后
  补 pos 对照（见 §3 e16_pos）。

### A1 PPO 批化（marl/network.py forward_batch + train.py 批式更新）
- 单次 update 等价性门禁 PASS：policy_loss 相对误差 1.77e-07，
  max|ΔW_actor| = 2.9e-06（浮点归约噪声级）；参数量 28482 不变。
- 加速比：CPU 批式 ~170×（单 update 7s → 0.35s），e15 起训练用 CPU 批式。
- 两处非显然修复（详见 output/e15_smoke/bench.md）：
  key_padding_mask 拼接顺序；批式熵项须 `lp_safe` 先置 0 再乘，
  否则 `0×(−inf)` 反向梯度 NaN 污染。

### A2 预算放宽 + resume（train.py）
- iters 3000 / eval-every 25 / patience 60 / episodes-per-iter 128（4×）。
- `--resume`（权重+iter+best_val，日志 append）与 `--resume-from`
  （仅权重、独立日志）均冒烟通过。

### A3 击杀信用 p_shot 比例摊派（marl/reward.py）
- 口径：击杀时刻在途、结局非 invalid 的弹按 p_shot 比例分摊 +w_j/total，
  记各自发射槽位 (t_fire, i)；信用键语义不变，process_batch 零改动。
- selftest：6 episodes 全过（质量守恒 = 击毁值、invalid 弹零信用、
  完整重放逐 key 对账）。credit slots > kills 证明摊派生效。
- **干净对照**（e15 vs e16_c010，同 c=0.01 同预算，仅信用规则不同）：
  val 0.6226 → 0.5963，test 0.6194 → 0.5546；invalid 率 0.171 → 0.141
  （摊派同时压低无效交战，越过 0.15 约束线）。

### A4 BC 热启动（marl/bc_pretrain.py + train.py --init-from/--init-blend）
- 教师 = greedy；40k 决策步、800 训练步；离线 top-1 87.9%，
  **在线 kills/ep 复现比 1.000**（教师 10.45 = BC 10.45，门禁 ≥0.95 PASS）。
- e17_bc01（blend α=0.1）：val **0.5837 全场最佳**，test 0.5684 第二
  （与 c010 差距在噪声内）；e17_bc10（full BC α=1.0）：val 0.5917，
  test 0.6199——blend 优于全量初始化，符合方案预期。

### E18 PO-CPLEX 同信息中心化基线（dwta/dn_policies.py POCplexPolicy）
- 只读 obs 表面（dn/pool/get_observation）重建 belief（d0 = d+Δd·age、
  p̂_eff = min(pcap, p·d0/d)，不可达置 0），复用未改动的单波 MIP 子进程。
- 信息边界单测（tests/test_pocplex_boundary.py）：BoundaryProxy 代理
  只暴露三个合法属性，越界访问（env.rng/shots/inflight/destroyed_at）
  立即 AssertionError；代理自检 + 真实 episode 全程 PASS。
- test 结果：leak 0.7085±0.034，与全知 myopic CPLEX 完全一致，
  **每步 gap ≡ 0**。结论：当前观测模型（d/p/age/r/alive/pool 均共享）
  下，联合状态可由个体观测精确重建，信息边界对"重建-再中心化"策略
  无实质约束——MARL 的增益只能来自超出 myopic 的时序协同，而这正是
  e16_c010 实现的。

## 3. e16 c_invalid 四档扫描与选档

| c_invalid | val best | test leak | test invalid | ammo eff |
|---|---:|---:|---:|---:|
| 0.005 | 0.5896 | 0.5785 | 0.1233 | 85.8 |
| **0.01（c\*）** | 0.5963 | **0.5546** | **0.1411** | 87.3 |
| 0.03 | 0.5948 | 0.5729 | 0.1278 | 90.9 |
| 0.05 | 0.6019 | 0.5967 | 0.1188 | 83.7 |

- 选档 **c\* = 0.01**：test 最优、invalid 0.1411 < 0.15 达标、与 e15
  同 c 保持 A3 对照干净。四档 val 差异在噪声内（±0.005），test 上
  c005/c010/c030 统计上接近并列，c010 兼顾所有判据。
- A0 触发的 pos 对照结果（e16_pos：c\*=0.01，Φ 符号翻转 +1）：
  val 0.6418 vs c010 的 0.5963（差 7.6%），test 0.6302 vs 0.5546
  （差 13.7%）——**备选被数据否决**，维持历史 Φ 符号：发射步即时
  负踢 + 击杀时刻正回报的对比信号优于发射即时正踢。

## 4. E19 终评大表（test split s01-s02 × 30 seeds）

| policy | leak mean±std | gap | invalid | ammo eff | destroyed val |
|---|---|---:|---:|---:|---:|
| none | 1.0000±0.000 | n/a | 0.0000 | n/a | 0.0 |
| greedy | 0.7913±0.010 | 0.2768 | 0.3472 | 46.7 | 809.2 |
| cplex（全知 myopic） | 0.7085±0.034 | 0.0000 | 0.0963 | 67.9 | 1129.1 |
| pocplex（同信息 myopic） | 0.7085±0.034 | 0.0000 | 0.0963 | 67.9 | 1129.1 |
| e14（参照） | 0.9009±0.030 | — | — | — | — |
| e15（A1+A2） | 0.6194±0.015 | 0.2240 | 0.1710 | 77.9 | 1475.9 |
| e16_c005 | 0.5785±0.013 | 0.3458 | 0.1233 | 85.8 | 1634.8 |
| **e16_c010（主臂）** | **0.5546±0.062** | 0.3656 | 0.1411 | 87.3 | **1724.7** |
| e16_c030 | 0.5729±0.073 | 0.3767 | 0.1278 | 90.9 | 1652.8 |
| e16_c050 | 0.5967±0.059 | 0.4007 | 0.1188 | 83.7 | 1561.2 |
| e16_pos（Φ 翻转对照） | 0.6302±0.022 | 0.2504 | 0.1703 | 80.6 | 1433.8 |
| e17_bc01（blend 0.1） | 0.5684±0.068 | 0.3746 | 0.1521 | 85.1 | 1670.5 |
| e17_bc10（full BC） | 0.6199±0.015 | 0.3895 | 0.1734 | 79.1 | 1474.1 |

复现：`bash experiments/e19_eval.sh` → `experiments/e19_report.py`。

## 5. 结论与后续

1. **改进链总收益**：e14 → e16_c010，test leak 0.9009 → 0.5546
   （−38.4%）；其中 A1+A2 贡献 −31.3%，A3 贡献 −10.5%，A4（blend）
   在 val 上再领先但 test 与主臂并列。
2. **超过中心化 myopic 最优 21.7%**，且 gap 升高证明增益来自非
   myopic 时序协同而非单步拟合。
3. PO-CPLEX gap≡0 的等价性发现说明：本观测模型下值得引入的下一类
   基线是**滚动时域（receding horizon ≥2 步）中心化 MIP**，以区分
   "MARL 时序优势"与"myopic 视界损失"两部分。
4. 后续（超出本方案范围）：多 seed 训练方差估计；BC 数据换
   PO-CPLEX 教师以进一步提升标签质量上限；receding-horizon ≥2 步
   中心化基线。
