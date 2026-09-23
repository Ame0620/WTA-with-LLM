# EC-MAPPO 项目事实底稿（代码与实验审计版）

> **文档定位**：本文件是 `WTA-Dn-branch01/` 仓库的**代码级 + 实验级事实底稿**，由审计提示词驱动、基于对仓库源码、数据、实验产物与报告文档的直接核验生成（生成方式：根据提示词《EC-MAPPO项目事实底稿_提示词.md》生成）。目标读者：后续 AI（代码助手/论文写作助手/实验分析助手）与需要快速掌握项目真实状态的人类协作者。
> **审计基准时点**：2026-09-21（仓库处于"第二轮消融管线改造已完成、e52-e55 实验未启动"状态，详见 §7.3）。
> **引用规范**：源码引用使用相对于仓库根目录的路径（如 `marl/train.py`）+ 函数/类名；不引用行号（随编辑漂移）。
> **核心原则（绿字原则）**：只收录可在仓库内直接核验的事实，每条带出处；推测/计划/不可验证结论显式标注。

---

## 0. 方法论声明

- 所有事实来自对仓库的直接读取（源码、配置、数据文件、实验产物 JSON/日志、报告文档），不引入外部知识修饰。
- 出处标签：`[源码]`、`[数据]`（数据集与 MANIFEST）、`[产物]`（output/ 实验结果）、`[报告]`（仓库内 Markdown）、`[日志]`、`[Git]`；核验等级标注 **[已验证] / [部分验证] / [推测·待验证]**，另用 **[失败实验] / [已废弃]** 显式标记。
- 审计覆盖：`dwta/`、`marl/`、`experiments/`、`cplex/`、`tests/`、`data/`（三版）、`output/`（e11-e50 系）、`logs/`、根目录全部 Markdown。
- 不覆盖：`.git/` 对象历史、`__pycache__`、checkpoint 张量逐位比对（仅核验元数据结构）。

---

## 1. 项目使命与问题定义（代码可验证事实）

### 1.1 问题域

项目求解**动态网络化武器目标分配（DN-WTA）**：多防御平台在多决策回合内对持续到达的目标动态分配拦截弹，最小化加权目标泄漏率。

**环境实现**（`dwta/dn_env.py::DNEnv`，实例 `dwta/dn_instance.py::DNInstance`）[源码，已验证]：

- **动作**：每决策步每平台至多对 1 个目标发射 1 枚拦截弹（hold 合法）；
- **全局弹药池**：全平台共享 N_pool（v3=18 / v4=30 / v5=70，§4.1）；
- **交战窗**：目标带窗约束，平台对 j 的合法发射窗 = 到达后 H_j 回合内（`feasible_targets` 过滤）；
- **拦截效能**：`p_eff = p0 × visibility_{t,j} × readiness_{t,i} × reliability`（乘性分解）；
- **存活动力学**：`p_surv(j,t+1) = p_surv(j,t) × Π_{shots on j}(1−p_eff)`，毁伤随机结算；
- **目标**：`泄漏率 = Σ_j w_j·p_surv(j,K) / Σ_j w_j`；
- **随机源**：可见性、毁伤判定、感知噪声（独立随机流，种子可复现）；
- **可观测性分级**：4 级（0=完全 / 1=可见性遮蔽 / 2=+感知精度 / 3=+后勤），主实验运行在 level 2。

### 1.2 方法主张（EC-MAPPO）

权威定义《EC-MAPPO三模块界定.md》[报告，已验证]：

| 模块 | 全称 | 定义 | 代码落点 |
|---|---|---|---|
| MAPPO⁰ | 骨架 | 共享演员 MAPPO + 团队价值函数（无任何 EC 模块） | `marl/train.py::Trainer` + `marl/baseline_net.py` |
| DCCA | Decentralized Cooperative Credit Assignment | 联合动作 Critic + 事件回溯信用 + 反事实个体优势 | `marl/network.py::JointActionCritic` + `marl/reward.py` + `marl/train.py::Trainer.process_batch` |
| EAPS | Event-driven Adaptive Potential Shaping | 事件驱动势函数塑形 | `marl/reward.py::build_rewards` |
| CASP | Cooperative Attentive Set Policy | 集合注意力演员 + 协同门控 | `marl/network.py::MarlNet` + `marl/perceive.py` |

**命名红线**：消融臂 `c1=(0,0,0)=MAPPO⁰` 是纯骨架（PoolMLPNet 演员 + StateCritic），不得另解；`c8=(1,1,1)` 才是完整 EC-MAPPO。

### 1.3 当前位置（一句话）

v5 全算法对比完成（EC-MAPPO 仅次于 CPLEX、优于全部规则与学习基线）；v3/v5 两族第一轮消融完成并出具报告；第一轮暴露的 EAPS/DCCA 负贡献问题驱动第二轮"重标定消融"（e52-e55），**其管线改造已实施、实验未启动** [Git+源码+产物综合，已验证]。

---

## 2. 仓库快照与文件索引

### 2.1 版本状态 [Git，已验证]

- 分支 `main`；HEAD = **"S0: 消融实验改造前基线快照（v5 工作区完整状态存档）"**；
- 工作区大量未提交改动：第二轮脚本（`experiments/e52_select.py`、`experiments/e53_lock_budget.py`、`experiments/e53_checkpoint_sanity.py`、`scripts/run_e54_batch.sh`）、《需求文档_v3消融实验_第二轮.md》、删除 `marl/train_mappo.py` 与 `output/e24_mappo/`（v4 时代废弃）；
- 语义：HEAD 是第二轮改造前存档点，工作区即"改造后"状态（`marl/train.py` 已含三重标定参数，§7.3）。

### 2.2 目录结构（顶层）

```
WTA-Dn-branch01/
├── main.py                  # [已废弃] 静态 WTA 入口（v1/v2 时代）
├── dwta/                    # DN-WTA 环境 + 策略族 + GA 求解器
├── marl/                    # MARL 算法（EC-MAPPO + 学习基线）
├── experiments/             # e11→e53 实验脚本 + gen_dn_data.py
├── cplex/                   # MILP 求解核心（wta_cplex.py + validator.py）
├── scripts/                 # 批处理/无人值守驱动
├── tests/                   # 7 个测试文件
├── data/                    # dn-data-v3 / v4 / v5
├── output/                  # e11→e50 系产物 + _cplex_ref_cache + _pre_ablation_ref
├── logs/                    # 运行日志 + 3 个汇总 JSON + heartbeat/pipeline_status
└── *.md                     # 设计/需求/报告文档（约 20 份）
```

### 2.3 源码模块清单（行数实测）[源码，已验证]

| 路径 | 行数 | 职责 |
|---|---|---|
| `dwta/dn_env.py` | 669 | 环境核心（动力学/可见性/感知/弹药池） |
| `dwta/dn_instance.py` | 352 | 实例解析（目标流/权重/几何/协同表） |
| `dwta/dn_policies.py` | 819 | 策略族注册（build_policy）与实现 |
| `dwta/ga_solver.py` | 192 | GA 核心（纯函数，零 torch/cplex 依赖） |
| `dwta/wave_runner.py` | 93 | 子进程求解运行器 |
| `dwta/simulator.py` / `instance.py` | 291/123 | [已废弃] 静态 WTA 仿真 |
| `marl/train.py` | 1067 | 统一训练器（消融三开关 + r2 三重标定参数） |
| `marl/network.py` | 197 | MarlNet / JointActionCritic / 集合 Critic |
| `marl/baseline_net.py` | 119 | PoolMLPNet / StateCritic（MAPPO⁰ 结构） |
| `marl/reward.py` | 259 | 团队奖励/势塑形/击杀信用（含 selftest） |
| `marl/perceive.py` | 205 | 10 维特征 + 8×3 协同矩阵 |
| `marl/masking.py` | 191 | 非法动作软惩罚 |
| `marl/policy.py` | 171 | MarlPolicy 推理封装（元数据驱动结构重建） |
| `marl/train_qmix.py` / `train_maddpg.py` / `maddpg_net.py` | 338/355/134 | QMIX / MADDPG 基线 |
| `marl/bc_pretrain.py` | 149 | [部分验证] BC 预训练（A4 项，主表未再使用） |
| `marl/data_split.py` | 32 | 统一划分发现 |
| `cplex/wta_cplex.py` | ~500+ | CPLEX MILP 核心（子进程复用） |

### 2.4 关键文档索引 [报告，已验证]

| 文档 | 性质 | 内容 |
|---|---|---|
| `EC-MAPPO三模块界定.md` | **权威规范** | 模块语义/公式/组合记号/红线 |
| `实验报告_v5全算法总览.md` | **正式报告** | v5 主表（12 策略）全套结论 |
| `实验报告_v3消融.md` | **正式报告** | 第一轮 v3 消融（e49-e51）结果 |
| `实验报告_v3全算法总览.md` | 正式报告 | v3 主表 |
| `实验报告_MARL核心框架.md` | 正式报告 | e15-e25 迭代史（A1-A4） |
| `需求文档_v3消融实验_第二轮.md` | **现行需求** | e52-e55 设计 + 根因诊断 |
| `v5全算法实验-需求文档.md` | 需求 | v5 管线 S0-S5 协议 |
| `需求文档_v3消融实验.md` | 需求 | 第一轮消融设计 |
| `评价指标体系_精简三层版.md` | 规范 | 三层指标体系 |
| `DN-WTA_v3/v4/v5_数据集说明.md` | 规范 | 数据集口径 |
| `项目总结.md` | [已废弃] | v2 时代口径 |
| `output/REPORT.md` | [已废弃] | 核心框架报告早期版 |
| `logs/ablation_v3_summary.json` 等 3 个 | 产物 | 消融机器可读汇总 |

### 2.5 运行环境 [源码/日志，已验证]

解释器 `/opt/anaconda3/envs/wta/bin/python`（macOS/zsh）；设备 `--device auto`（实测 MPS/CPU；e53 计划锁 CPU——小模型上 MPS 约慢 6 倍，见 `experiments/e53_lock_budget.py` docstring）；torch 2.13.0、cplex、numpy/scipy。

---

## 3. 系统架构与真实调用链

### 3.1 入口矩阵 [源码，已验证]

| 入口 | 用途 |
|---|---|
| `experiments/dn_family_eval.py` | **统一评估器**：任一策略 × 固定 split × MC 种群 → family_report.json/md |
| `experiments/e50_eval_entry.py` | 消融评估入口：monkey-patch `CplexPolicy._solve` 加 md5 参考解缓存（`output/_cplex_ref_cache/`），跨臂复用 per-step MIP 最优解 |
| `marl/train.py` | **统一训练器**：MAPPO⁰/EC-MAPPO 全部变体（含消融开关与重标定参数） |
| `marl/train_qmix.py` / `train_maddpg.py` | 学习基线训练 |
| `experiments/run_v5_pipeline.py` | v5 全算法无人值守管线（S0-S5，幂等） |
| `scripts/run_e49_batch.sh` / `run_e54_batch.sh` | 消融批驱动 |
| `main.py` | [已废弃] 静态 WTA 入口 |

### 3.2 策略注册表（`dwta/dn_policies.py::build_policy`）[源码，已验证]

注册名：`none` / `greedy` / `greedy_threat` / `greedy_nearest` / `random`（--p-hold/--policy-seed 私有随机流）/ `cplex` / `pocplex`（信念态 MIP）/ `rh-cplex`（滚动时域）/ `ga` / `marl` / `mappo` / `ecmappo` / `qmix` / `maddpg` / `iql`。

**CPLEX 系调用链**：`CplexPolicy` 把当前步 MIP 写临时文件 `dn_t<t>_inst.txt`，经 `dwta/wave_runner.py::DEFAULT_PYTHON` 子进程调 `cplex/wta_cplex.py`（timelimit 30s），解析 `.sol` 回读。greedy 系/pocplex/rh-cplex/学习策略评估时自动挂 per-step CPLEX 参考计算 gap。

### 3.3 学习侧调用链 [源码，已验证]

```
训练 marl/train.py::main → Trainer(args)
  ├─ 数据 marl/data_split.py::discover_split（train s03-26 / val s27-30）
  ├─ 结构选择（按开关）：use_casp=1→MarlNet 演员；0→PoolMLPNet（8 维）
  │                    use_dcca=1→JointActionCritic；0→StateCritic
  ├─ 采样 DNEnv.run(policy) → run_rec
  ├─ 特征 perceive.py::build_features(10 维)/build_collab_matrix(8×3)
  ├─ 奖励 reward.py::build_rewards（R_team/R_shaped/credit）
  ├─ 更新 Trainer.process_batch（GAE + 三通道优势 + PPO clip）
  └─ 产物 best.pt/last.pt（含 ablation + reshaping 元数据）+ train_log.json
推理 marl/policy.py::MarlPolicy → 注册为 ecmappo/mappo → dn_family_eval 统一评估
```

**结构重建红线**：加载 ckpt 只从内嵌元数据（ablation/reshaping/structure 字段）重建结构，绝不从路径推断；评估器对 reshaping 与预选值一致性校验（不一致 raise）。

### 3.4 v5 管线（`experiments/run_v5_pipeline.py`）[源码，已验证]

S0 冒烟门（tests+GA 延迟探针+短率标定）→ S1 求解器终评 → S2 规则终评（7 策略×30 seeds）→ S3 学习重训（3h/12h 档）→ S4 学习终评+泛化（--no-ref）→ S5 汇总。看门狗：30s 心跳（`logs/heartbeat.json`）、15min 停滞杀重启（--resume 续跑）、崩溃重启上限 3 次、状态 `logs/pipeline_status.json`。

---

## 4. 数据与环境核验

### 4.1 三版数据集 [数据/MANIFEST，已验证]

| 版本 | 目录 | 形状 | N_pool | 池/需求 | 定位 |
|---|---|---|---|---|---|
| v3 | `data/dn-data-v3/` | 3 平台 × 50 目标 × K=10，30 实例 | 18 | 0.67 | 主消融基准 |
| v4 | `data/dn-data-v4/` | 5 平台 × 100 目标 × K=10，30 实例 | 30 | 0.67 | 算法迁移验证（e30-e35） |
| v5 | `data/dn-data-v5/` | 10 平台 × 100 目标 × K=10，30 实例 | 70 | 0.78 | 资源扩展基准（Agent ×2、弹药 ×2.33） |

- 实例命名 `dn_<m>x<n>_K<k>_s<nn>.txt`（实测 v3=`dn_3x50_K10_s01.txt`，v5=`dn_10x100_K10_s01.txt`）；
- **划分协议跨版本冻结**：s01-02 test / s03-26 train / s27-30 val（`marl/data_split.py` 单一实现）；
- 指纹锚：v3 s01/s02 md5 前缀 `9134a16f`/`e717a4c1`，总价值 3942/3819，none 泄漏率 1.0000；v5 s01 W=6358；
- 生成器 `experiments/gen_dn_data.py`；形状测试 `tests/test_v3/v4/v5_dataset.py`；
- 训练器缺省 v3（`marl/train.py` 模块级 `DATA_DIR`、`TRAIN_INSTS=dn_3x50_K10_s03..s26`）。

### 4.2 观测特征（`marl/perceive.py::build_features`，10 维）[源码，已验证]

`x_ij = [j_norm, w_norm, p_eff_norm, in_pool 独热(4), h_left_norm, l_obs_ij, est_l_ij, t_norm]`；MAPPO⁰（PoolMLPNet）用其中 8 维（丢弃 l_obs/est_l 两个 M1 增补列）。

### 4.3 协同矩阵（`marl/perceive.py::build_collab_matrix`，8×3）[源码，已验证]

实例协同表（`dwta/dn_instance.py` 解析）硬编码映射为 `[竞争压力, 互补增益, 协同时机]` 三通道（竞争按威胁×距离档表、互补/时机按关系×威胁档表）；作为 CASP 联合观测输入。

### 4.4 评估指标（`experiments/dn_family_eval.py::FAMILY_KEYS`）[源码，已验证]

结果层：`leak_rate`（主指标）、`destroyed_value`、`gap_mean`（vs per-step CPLEX 参考）；过程层：`invalid_engagement_rate`、`ammo_efficiency`、`shots_total`、`latency_p50/p90`。跨实例聚合取 worst-case 方向（leak/gap/invalid/latency 取 max，ammo/destroyed 取 min）。

---

## 5. 方法身份与核心公式审计（源码级还原）

### 5.1 MAPPO⁰ 骨架（`marl/train.py::Trainer`）[源码，已验证]

PPO clip 目标（`PPO_CLIP=0.2`）；GAE（`GAE_LAMBDA=0.95`，`GAMMA=0.99`）；Actor/Critic 独立 Adam（`LR=3e-4`），梯度范数裁剪 0.5；熵正则 `ENT_COEF=0.01`（模块级常量）；早停 patience（档 A=60/档 D=20），`eval_every=25`；档 A 缺省 `--iters 3000 --episodes-per-iter 128`。

### 5.2 团队奖励与事件流（`marl/reward.py::build_rewards`）[源码，已验证]

```
R_team(t) = Σ_{leak@t}(−w_j/total) + Σ_{kill@t}(+w_j/total) − C_INVALID·|invalid@t|
C_INVALID = 0.01（锁定；0.005-0.05 区间由 e16 扫描选定）
```
selftest 断言（容差 1e-9）：`Σ R_pure = (destroyed−leak)/total`；击杀数=destroyed_at 计数；信用键⊆发射键；`Σ credit = destroyed/total`（质量守恒）。

### 5.3 EAPS 势塑形 [源码，已验证]

```
Φ(s_t) = −Σ_{j alive} w_j·pbar_j(t)/total，Φ(terminal)=0
pbar_j(t) = 1 − Π_{k in-flight on j}(1−p_shot_k)
R_shaped(t) = R_team(t) + phi_scale·phi_sign·(GAMMA_SHAPE·Φ(t+1) − Φ(t))
GAMMA_SHAPE=0.99（硬编码）；phi_sign=−1.0（冻结，R7 禁止以翻转/置零 phi_sign 关闭 EAPS）
```
- `use_eaps=0` 语义：Φ 构建**整体移除**（不计算），`R_shaped=R_team`；
- 第二轮 `phi_scale`（λ）仅在 use_eaps 分支乘性生效；λ=1.0 与改造前逐位一致（IEEE754）；use_eaps=0 时 λ 不进计算图（E2 隔离门）；
- Φ 用"发射后即在途"的弹（t_fire≤t<t_hit），属训练侧全局信息（critic 视野）——docstring 明示。

### 5.4 DCCA 三通道个体信用 [源码，已验证]

1. **结构**：`JointActionCritic`——联合动作图（11×11 联合 one-hot 含 hold）→ MLP(121→128→64→32) → 图向量(59→64) → V；`use_dcca=0` 换 `StateCritic` 且不建联合图；
2. **回溯信用**（`credit_mode="credit_kill"`）：击杀 (t_kill,j) 的 +w_j/total 按 p_shot 比例分裂给结算时在途弹（t_fire≤t_kill≤t_hit），**invalid 弹零分成**，单一杀手全额；记在各发射槽位 (t_fire,i)；
3. **反事实差**：`cf_row[i] = V(s,a) − V(s,a_{−i}, hold_i)`；
4. **注入**：`adv_i = GAE_team + credit_alpha·credit.get((t,i),0) + cf_beta·cf_row[i]`（α/β 缺省 1.0=历史行为，仅 use_dcca=1 分支生效）。

### 5.5 CASP 集合注意力（`marl/network.py::MarlNet`）[源码，已验证]

```
x(≤10×10 维) → MLP(10→64→128) → LN → MHA(d=128,heads=4)×2 → FFN(256) → LN
→ 取目标 i 行 → MLP(128→64→3)
协同矩阵摊平 → MLP(448→64) → 2·tanh·sigmoid 门
Critic(DCCA 开)：集合均值池化 → MLP(448→128→64→1)
```
`use_casp=0` 换 PoolMLPNet+StateCritic——**结构替换**而非置零，语义由 `tests/test_ablation_switches.py` 静态审计锁定。

### 5.6 学习基线身份 [源码，已验证]

- **MAPPO⁰**：即 `--use-dcca 0 --use-eaps 0 --use-casp 0` 的同一训练器（结构自动降级），不是独立代码路径；
- **QMIX**（`marl/train_qmix.py`，QMIXNet）：混合网络单调性约束的标准实现；
- **MADDPG**（`marl/train_maddpg.py`+`maddpg_net.py`）：集中 critic 确定性策略梯度；
- 参数量硬约束：Actor/Critic ∈ [1e3, 1e5]（消融需求 §2 硬不变量）。

---

## 6. 实验谱系全景（e11 → e55）

### 6.1 演化主线 [产物/日志/报告，已验证]

| 阶段 | 实验编号 | 内容 | 关键结论 |
|---|---|---|---|
| v3 基线 | e11-e13 | none/greedy/cplex/pocplex/random × v3 test | 建立规则与求解器基线（e13） |
| 首版 MARL | e14 | IndependentA2C+LSTM | 初版学习基线（后被 MAPPO 系取代） |
| 框架迭代 | e15-e25 | A1 特征工程→A2 MAPPO 核→A3 集合注意力→A4 BC 预训练+DCCA+EAPS | e20 主表：EC-MAPPO test 0.5963 vs MAPPO⁰ 0.6362 vs CPLEX 0.4280（v3） |
| v4 迁移 | e30-e35 | v4 全算法（含 GA 40×50、MADDPG、QMIX） | 协议跨资源可复现 |
| v5 基线 | e38-e42 | cplex/rh/pocplex/greedy 系/random/ga/ga 敏感档 | v5 传统求解器锚点 |
| v5 学习 | e43-e44 | mappo/qmix/maddpg（3h 档）+ ecmappo（12h 档）训练+终评 | v5 主表定稿 |
| v5 泛化+消融烟测 | e45 | 泛化协议验证 + 消融 smoke | 管线打通 |
| v5 消融 | e46-e47 | 8 组合×1 seed（e46 短跑/e47 正式档 A）+泛化+hash 复检 | DCCA 在 v5 为正边际，EAPS/CASP 为负 |
| v3 消融第一轮 | e49-e51 | 24 臂（8 组合×3 seeds）档 D 训练→评估→汇总 | c8−c1=−0.0147 显著但单开臂恶化，驱动第二轮 |
| **第二轮（现行）** | e52-e55 | 重标定调参→正式训练→终评/泛化/OOD→汇总 | **未运行**（脚本就绪） |

### 6.2 v5 主表（test 泄漏率 ± std，30 MC seeds）[报告《实验报告_v5全算法总览.md》+产物，已验证]

| 排名 | 策略 | leak_rate | 备注 |
|---|---|---|---|
| 1 | cplex | 0.2283 ± 0.0112 | per-step MILP 上界性质 |
| 2 | **ecmappo** | **0.3485 ± 0.0155** | gap_mean 4.5%（vs CPLEX 参考） |
| 3 | mappo | 0.4226 ± 0.0205 | MAPPO⁰ |
| 4 | rh_cplex | 0.4399 ± 0.0179 | 滚动时域 |
| 5 | pocplex | 0.4751 ± 0.0184 | 部分可观测信念 MIP |
| 6 | qmix | 0.5904 ± 0.0206 | |
| 7 | maddpg | 0.6628 ± 0.0237 | |
| 8-12 | greedy / greedy_threat / greedy_nearest / random / none | 0.7733 / 0.8080 / 0.9295 / 0.9487 / 1.0000 | none 指纹 = 全泄漏 |

配套事实：EC-MAPPO 训练预算 12h 档（其余学习算法 3h 档）；泛化梯度平缓（train/val/test 差异小）；延迟 p50 毫秒级（满足 40s 决策窗）[报告，已验证]。

### 6.3 v3 主表（e20，test 泄漏率）[报告，已验证]

EC-MAPPO 0.5963 / MAPPO⁰(基线结构) 0.6362 / CPLEX 0.4280；v3 上 EC-MAPPO 对 MAPPO⁰ 提升 −0.040。

### 6.4 产物目录命名规律 [产物，已验证]

`output/e<编号>_<语义>/`；消融臂目录后缀 = 3 位开关向量：`b0_000`(c1) `only_001`(c2,仅 DCCA) `only_010`(c3,仅 EAPS) `ad_011`(c4,D+E) `b1_100`(c5,仅 CASP) `ae_101`(c6,E+C) `b2_110`(c7,D+C) `b3_111`(c8,全开)。注意目录位序 = (d,e,c) 即 DCCA,EAPS,CASP；论文口径 c2-c8 见 §7.1。

---

## 7. 消融实验体系深度审计

### 7.1 第一轮 v3 消融（e49-e51，已完成）[报告《实验报告_v3消融.md》+logs/ablation_v3_summary.json，已验证]

- **设计**：8 组合 × 3 训练 seeds × 180 配对单元（2 test 实例 × 30 MC seeds）；预算档 D（500 iters × 64 eps，patience 20）——档 D 由 σ 归一最坏臂外推锁定（A 档 152.4h 超 27.6h 墙钟上限，D 档 14.9h）；
- **臂映射**：c1=b0_000(MAPPO⁰) / c2=only_001(仅 DCCA) / c3=only_010(仅 EAPS) / c4=ad_011(D+E) / c5=b1_100(仅 CASP) / c6=ae_101(E+C) / c7=b2_110(D+C) / c8=b3_111(全开)；
- **主结果（test 泄漏率）**：c1=0.6384，c2=0.6215（DCCA −0.0169），c3=0.6931（EAPS **+0.0547 恶化**），c4=0.6265，c5=0.7386（CASP **+0.1002 恶化**），c6=0.6150，c7=0.6332，c8=0.6237（全开 −0.0147，Wilcoxon p=0.0168 显著）；
- **结构性问题**：c8 反而劣于 c6（+0.0086，p=3.7e-04）→ EAPS 在最优组合上仍是拖累；c5/c3 为学习最慢臂（24 臂中 3 例未收敛全部集中于此）。

### 7.2 v5 消融（e46-e47，已完成）[报告+logs/ablation_v5_summary.json，已验证]

档 A（8 组合 × 1 seed）：b0_000=0.4571 / b1_100=0.4468 / b2_110=0.4577 / only_001=0.5070 / ad_011=0.4582 / only_010=0.4257 / ae_101=0.4610 / b3_111=0.4496。
配对边际：**DCCA −0.0314/−0.0232（一致改善）**；EAPS +0.0499/+0.0345（一致恶化）；CASP +0.0103/+0.0119（恶化）。
跨族结论：DCCA 边际随预算增大单调改善（档 D 下 c5 全场最差 → 档 A 下持平无害）；EAPS 在两族方向一致负贡献。

### 7.3 第二轮重标定消融（e52-e55，**改造完成、未运行**）[需求文档+源码+Git，已验证]

**根因诊断**（需求文档 §0，基于第一轮实证）：
- **R-A 预算不足**：档 D vs e20 档 A 截断模块增益约 0.027（P1 主因）；
- **R-B EAPS 塑形 1:1 满幅失配**：势差项量级压过稀疏事件奖励，无可调尺度参数（结构性）；
- **R-C DCCA 信用三通道 1:1:1 满幅**：credit 单笔 ≈ w_j/total 通常远大于逐步 GAE 量级（结构性）。

**管线改造（已实施进工作区）**：
- 新 CLI：`--phi-scale`（λ）/ `--credit-alpha`（α）/ `--cf-beta`（β），缺省全 1.0（位级等价改造）；
- 公式落地：`R_shaped = R_team + λ·phi_sign·(γΦ′−Φ)`；`adv_i = GAE + α·credit + β·cf`；
- checkpoint 新增 `reshaping` 元数据 + 训练首行 `[reshaping]` 日志 + 评估器一致性校验；
- 等价性验收产物已存在：`output/_pre_ablation_ref/r2_e1_before|after`、`r2_pre_mod_md5.txt`；
- `tests/test_ablation_switches.py` 已扩展覆盖 r2 参数（λ 仅在 use_eaps 分支、α/β 仅在 use_dcca 分支、reshaping 元数据校验）。

**预注册网格**（`experiments/e52_select.py::PREREG/ARMS`，冻结）：
- λ ∈ {0.2, 0.5}（P1 扩展 0.1）；(α,β) ∈ {(0.5,1),(1,0.5),(0.5,0.5)}（P2 扩展 (0.25,0.5),(0.5,0.25)）；E-ref/D-ref/F-full/F-pick 对照共 10 臂；档 T=800×128 patience 30，仅 val 选择；
- e53 正式轮：档 A 系（3000×128 pat 60；超 60h 降 A-1/A-2）× 24 臂，CPU；
- e54 终评：test 400 eps × 3 seeds + 泛化 + repro（seed 7, 50 eps）+ **PPA OOD**（平台 50/100 × 目标 30/50 变体，`--variant v<t>t<v>`）；e55 汇总脚本**尚不存在**（`run_e54_batch.sh` 引用了 `experiments/e55_summary.py`，属待写项）。

**验收目标**：T1 = c8−c1 ≤ −0.030 且显著（底线 −0.020）；T2 = 三个单开臂 vs c1 全部正提升（底线无一显著恶化）；禁止作弊条款 R11（不得单臂降预算/用 test 反馈/篡改 MAPPO⁰ 定义）。

### 7.4 消融方法论资产（可复用协议）[产物，已验证]

- 预算锁定链：smoke 实测 s/iter → σ 归一最坏臂外推 → 档位表 → `logs/ablation_v3*_budget.json`；
- CPLEX 参考缓存：`output/_cplex_ref_cache/`（md5(实例字节+求解配置) 键控，跨臂复用安全——MIP 文本完全决定最优解）；
- 等价性对照：`output/_pre_ablation_ref/`（改造前后逐位一致验证 + switch_audit.json）；
- 180 配对单元 + 双侧 Wilcoxon + 方向一致性投票（3 seeds × 2 指标）。

---

## 8. 关键事实表（主表数字，均为 test split）

| 维度 | 事实 | 出处 |
|---|---|---|
| v5 最优求解器 | cplex 0.2283±0.0112 | v5 报告主表 |
| v5 最优学习 | ecmappo 0.3485±0.0155（gap 4.5%） | v5 报告主表 |
| v5 学习次序 | ecmappo < mappo(0.4226) < qmix(0.5904) < maddpg(0.6628) | v5 报告主表 |
| v3 学习 | EC-MAPPO 0.5963 < MAPPO⁰ 0.6362；CPLEX 0.4280 | e20/v3 报告 |
| 第一轮 v3 消融 | c8−c1=−0.0147（p=0.0168）；c3/c5 单开显著恶化 | v3 消融报告 |
| v5 消融边际 | DCCA −0.0314/−0.0232 改善；EAPS +0.0499/+0.0345 恶化；CASP +0.0103/+0.0119 恶化 | e47+汇总 JSON |
| 硬不变量 | shots_total≤18（v3 池上限）、ammo_end≥0、零非法动作、零 NaN、参数量∈[1e3,1e5] | 需求文档 §2+e51 |
| 训练缺省超参 | clip 0.2 / GAE(0.95,0.99) / Adam 3e-4 / 熵 0.01 / 档 A 3000×128 | marl/train.py |
| 奖励常量 | C_INVALID=0.01 / GAMMA_SHAPE=0.99 / phi_sign=−1 | marl/reward.py |
| 第二轮状态 | 改造完成（λ/α/β 入库+测试+等价性产物），e52-e55 未运行，e55_summary.py 待写 | Git+源码+产物 |

---

## 9. 已验证 / 不可验证 / 假设分层

### 9.1 [已验证]（可直接引用）

§1-§8 全部主事实：环境动力学公式、三模块代码实现与公式、三版数据集形状与划分、v5/v3 主表数字、第一轮与 v5 消融数字、第二轮改造的代码落地状态、评估协议与指标定义。

### 9.2 [部分验证]

- BC 预训练（`marl/bc_pretrain.py`）与 init-blend 链路在 e15-e25 后的主表/消融中未再使用（代码在、引用弱）；
- `main.py`/`dwta/simulator.py` 的静态 WTA 时代细节（仅确认其 DN 时代不被调用）；
- e14 首版 MARL 的具体数字（报告提及，未复核原始产物）；
- e26（v5 探针）、e30-e35（v4）逐项数字（有产物与日志，未逐表复核）。

### 9.3 [推测·待验证] / [失败实验] / [已废弃]

- [推测·待验证] 第二轮三参数能修复 EAPS/CASP 负边际（需求文档的机制假说 R-A/R-B/R-C，**e52-e55 尚无数据**）；
- [推测·待验证] PPA OOD（平台/目标规模变化）下 EC-MAPPO 的泛化行为（e54 变体实验未运行）；
- [失败实验·已归档] 第一轮档 D 消融的 c3/c5 恶化结果——作为第二轮根因诊断的实证输入保留；
- [已废弃] `marl/train_mappo.py`（v4 时代独立 MAPPO 入口，已被统一训练器开关取代并删除）；`output/e24_mappo/`（对应产物）；`项目总结.md`（v2 口径）；`output/REPORT.md`（早期版报告）；`marl/bc_pretrain.py`（主流程弃用）；`main.py` 静态入口。

---

## 10. 关键文件与事实映射表

| 想核验什么 | 去哪里 |
|---|---|
| 环境动力学/弹药池/可观测性 | `dwta/dn_env.py`、`dwta/dn_instance.py` |
| 策略族实现与注册 | `dwta/dn_policies.py::build_policy` |
| GA 求解器 | `dwta/ga_solver.py`（档位：主 40×50 / 敏感 20×25、80×100） |
| CPLEX per-step MIP | `cplex/wta_cplex.py`（子进程调用链见 `dwta/dn_policies.py::CplexPolicy`） |
| MAPPO⁰/PPO 超参 | `marl/train.py`（模块级常量 PPO_CLIP/GAE_LAMBDA/GAMMA/LR/ENT_COEF） |
| DCCA/EAPS/CASP 公式 | §5.3-5.5 + `marl/reward.py`、`marl/network.py`、`marl/train.py::Trainer.process_batch` |
| 消融开关语义 | `marl/train.py` CLI（--use-dcca/--use-eaps/--use-casp）+ `tests/test_ablation_switches.py` |
| 第二轮 λ/α/β | `marl/train.py` CLI（--phi-scale/--credit-alpha/--cf-beta）+ `experiments/e52_select.py::PREREG` |
| 数据划分 | `marl/data_split.py::discover_split` |
| 评估指标 | `experiments/dn_family_eval.py::FAMILY_KEYS` |
| v5 主表 | `实验报告_v5全算法总览.md` + `output/e44_*`/`e4x_*` 产物 |
| 消融数字 | `logs/ablation_v3_summary.json`、`logs/ablation_v5_summary.json` |
| 消融预算锁定 | `logs/ablation_v3_budget.json`、`experiments/e53_lock_budget.py` |
| 等价性验收 | `output/_pre_ablation_ref/`（含 r2_e1_before/after） |
| 模块语义权威 | `EC-MAPPO三模块界定.md` |
| 第二轮设计 | `需求文档_v3消融实验_第二轮.md` |

---

## 11. 潜在问题与观察（审计者视角，非结论）

1. **`experiments/e55_summary.py` 不存在**而 `scripts/run_e54_batch.sh` 尾部调用它——第二轮启动前必须补写（[已验证] 缺失）。
2. **第二轮改造未提交 Git**：HEAD 停在改造前存档点，改造只存在于工作区——审计可追溯（有 `_pre_ablation_ref/r2_pre_mod_md5.txt`），但版本管理上脆弱，建议尽快 commit。
3. **报告与产物的数字一致性**：抽查的 v3/v5 消融主数字在报告与 `logs/ablation_v3/v5_summary.json` 间一致；未做全量逐数复核（[部分验证]）。
4. **MARL-MILP 鸿沟（R3，界定文档红线）**：学得策略的连续输出分布与 MILP 组合解不可直接比较——报告口径统一用"泄漏率+gap_mean"，引用时不得混用。
5. **EC-MAPPO 在 v3/v5 的模块边际符号不一致**（v5 下 DCCA 正、v3 档 D 下负）——这不是矛盾而是预算敏感（R-A 证据链），论文表述需绑定预算档位。
6. **e20（v3 主表）与 e49（消融 c1）的 MAPPO⁰ 数字不同**（0.6362 vs 0.6384 附近量级但档位不同）——前者档 A 后者档 D，跨实验引用必须带预算档。
7. `output/` 下存在 `_rerun_backup_0919` 备份目录——重跑史证据，引用数字时注意以报告汇总 JSON 为准。

---

## 12. 使用指南（常见问题路由）

- **"EC-MAPPO 是什么？"** → §1.2 + §5 + 《EC-MAPPO三模块界定.md》。
- **"现在效果最好的策略/数字？"** → §6.2（v5 主表）、§8。
- **"消融结论支持哪个模块？"** → §7.1-7.2（第一轮：DCCA 两族一致正或中性、EAPS 一致负、CASP 混合）+ §7.3（第二轮修复假说，**尚无数据**）。
- **"我要跑/复现实验？"** → §3.1 入口矩阵 + `scripts/` 驱动 + §2.5 环境；训练必带 `--data-dir` 显式声明。
- **"我要写论文/报告？"** → §5 公式（源码级）+ §8 数字表 + §11.4-11.6 的口径警告。
- **"第二轮进行到哪了？"** → §7.3：改造入库+测试扩展+等价性产物完成；e52-e55 未运行；e55 汇总脚本待写。

---

## 13. 术语表

| 术语 | 定义 | 出处 |
|---|---|---|
| DN-WTA | 动态网络化武器目标分配（本文问题域） | §1.1 |
| 泄漏率 leak_rate | Σ w_j·p_surv(j,K)/Σ w_j（主指标，越低越好） | §1.1 |
| MAPPO⁰ | 纯骨架：共享演员 MAPPO+团队 V(s)，消融臂 (0,0,0) | §1.2 |
| DCCA/EAPS/CASP | 三机制模块（定义见 §5.3-5.5） | §1.2 |
| c1-c8 | 消融组合记号（c1=全关 … c8=全开），与目录位序映射见 §6.4/§7.1 | 界定文档 |
| 档 A/B/C/D | 训练预算档（A=3000×128 pat60 … D=500×64 pat20） | 需求文档 |
| 档 T | 第二轮调参专用档（800×128 pat30） | r2 需求 §4.1 |
| λ/α/β | 第二轮重标定参数 phi_scale/credit_alpha/cf_beta | §7.3 |
| PPA OOD | 平台-目标规模超出分布泛化实验（e54 变体） | §7.3 |
| gap_mean | vs per-step CPLEX 参考的相对差（学习策略专属指标） | §4.4 |
| 180 配对单元 | 2 test 实例 × 30 MC seeds × 3 训练 seeds 的配对统计单元 | e51 |
| worst-case 聚合 | 跨实例族指标聚合取最坏方向 | §4.4 |

---

## 14. 变更日志

| 日期 | 变更 | 作者 |
|---|---|---|
| 2026-09-21 | 初版：全仓库审计（源码/数据/产物/报告/Git），生成 14 节事实底稿 | AI 代码助手（提示词驱动审计） |

---

*本底稿在仓库演进后会过时。使用前请优先核对：`git log --oneline -5`、`ls output/ | tail`、`logs/*.json` 的时间戳与本底稿基准时点（2026-09-21）的关系。*
