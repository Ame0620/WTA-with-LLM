# v3 范围复验报告（S1–S2 门禁）

日期：2026-09-20　解释器：`/opt/anaconda3/envs/wta/bin/python`（torch 2.13.0）
依据：《需求文档_v3消融实验.md》§4–§5　结论：**S1–S2 全部 PASS（见 S3 定档后统一放行）**

---

## S1 只读核查

### S1.1 管线状态（相对 v5 验收基线）

- git HEAD = `39e24a7`（S0 改造前基线快照）；`marl/train.py`、`marl/reward.py`、`marl/policy.py`、`dwta/dn_policies.py` 相对 HEAD 的 diff 即消融改造本体，且：
  - `marl/train.py` md5 `ac2e9fa4…` = e47 运行时 `source_md5` 记录，**逐字节一致**
  - `dwta/dn_policies.py` md5 `1bf99929…` = e47 运行时记录，**逐字节一致**
  - `marl/reward.py`（mtime 09-19 21:42）、`marl/policy.py`（09-19 21:52）自 v5 改造后未再修改
- 今日 15:04 有四处配套改动，全部为 **R1 隔离清理的必要适配**（发生于 v5 e47/e48 完成后、本需求定稿时）：
  - 删除 `marl/train_mappo.py` 与 `output/e24_mappo*`（R1：「不引用 train_mappo.py（不存在）」的预期状态）
  - `marl/train_maddpg.py`：`from marl.train_mappo import GAMMA` → `from marl.train import GAMMA`（删除后唯一正确 import）
  - `experiments/dn_family_eval.py`：删除 `source_md5` 中 `train_mappo.py` 一行（功能零变化）
  - `marl/baseline_net.py`：仅 docstring/注释措辞更新（e47 运行时 md5 `fcd500a9…` = `pre_mod_md5.txt` 改造前记录，证明网络结构/前向自 v5 轮以来零变化）

**判定：核心训练与评估管线相对 v5 验收基线无未预期改动。**

### S1.2 数据完整性

- 30 实例文件齐全，md5 全部唯一（30/30）。
- 口径抽查（项目加载器）：`s01 m=3 n=50 K=10 mu=6 total=3942`、`s02 … total=3819`，与 MANIFEST/需求锚点一致；test 划分 s01–s02 / val s03–s06 / train s07–s30 确认。
- 已知历史差异（不阻塞，如实记录）：生成器 `experiments/gen_dn_data.py` 当前 md5 `1bda6548…` ≠ MANIFEST 记录 `3fe8c817…`；git 显示该文件相对 HEAD 无改动（HEAD 提交时已是此值），属 MANIFEST 写就（08-28）之后、S0 快照之前的生成器迭代，非本轮引入。v2 回归参照 `data/dn_3x50_K10_s1.txt` 已不存在（历史清理），30 实例本身的口径/总价值/唯一性核查全部通过。

### S1.3 缺省路径

- `marl/train.py` 缺省 `DATA_DIR='data/dn-data-v3'` ✓；`experiments/dn_family_eval.py` 缺省 `--manifest='data/dn-data-v3/MANIFEST.md'` ✓。

### S1.4 命名冲突

- `output/`、`logs/`、`scripts/` 均无 e49/e50/e51 前缀条目 ✓（`output/_rerun_backup_0919` 为 v4 历史备份，无冲突）。

---

## S2 v3 范围复验

### S2.1 静态审计（35 项）

```
$PY tests/test_ablation_switches.py
35 checks, 0 failed, ALL PASS
```
日志：`logs/s2_static_audit.log`。

### S2.2 确定性双跑（(1,1,1)，seed 0，--iters 25 --eval-every 5，其余缺省 128 eps）

两次独立运行（`v3_det_a` / `v3_det_b`）：

- `train_log.jsonl`：剔除 elapsed/wall/time 类字段后 **5/5 行逐位一致**（含 loss、adv 统计、reward 密度、非法计数）。
- `best.pt`：全部张量 `torch.equal` **逐位相等**；非张量元数据**零差异**（ablation/actor_type/best_val/budget/feature_spec/iter/params_count/train_seed/versions 完全一致）。
- 两遍终值：train 0.7366 / val 0.7751±0.0652。速率参考：8.1 s/iter（(1,1,1)@128eps，MPS）。

### S2.3 (0,0,0) MAPPO⁰ 运行时审计（200 iters，--eval-every 25，train 实例）

```
$PY marl/train.py --data-dir data/dn-data-v3 --seed 0 --iters 200 \
  --eval-every 25 --use-dcca 0 --use-eaps 0 --use-casp 0 \
  --output output/_pre_ablation_ref/v3_b0_audit
```

| 审计项 | 结果 |
|---|---|
| 全程 `adv_indiv_over_team_std` == 1.000（DCCA-off 语义） | PASS（8/8 eval 点） |
| 塑形/基础 `reward_nonzero_ratio` 逐点相等（EAPS-off 语义） | PASS（8/8，如 0.907955==0.907955） |
| checkpoint 元数据（best 与 last） | `ablation=(0,0,0)`、`actor_type=pool_mlp`、`critic_type=state_value`、`feature_spec.drop_m1=True` ✓ |
| 零 NaN（全部日志字段 finite） | PASS |
| 零非法（训练期 `illegal_actions`） | PASS（全程 0） |
| shots ≤ 18 / ammo_end ≥ 0（72 rollouts，24 train 实例 × 3 MC seeds 贪心评估） | PASS（0 越界 / 0 负弹药） |
| val 泄漏率明显下降 | 1.0000 → 0.6975（iter 200，best），远优于 ≤0.85 健康判据 |
| n_agents=3、参数量 | 3 ✓；总参 10242（actor 5313 + critic 4929） |

说明：`invalid_shots`（对已死亡/泄漏目标的结算弹）在 69/72 rollouts 中非零——该口径是**战术无效交战率**（e50 主表指标之一），非环境非法动作；MAPPO⁰ 消融 CASP 后无效交战偏高正是待测消融效应，与 v5 B4 同口径。

### S2.4 评估器元数据链路

- 正常路径：上述 (0,0,0) `best.pt` 经 `--policy ecmappo` 在 v3 train split（24 实例 × 3 seeds）完成 72 rollouts，family 泄漏率 0.6770±0.0395（与训练 val 0.6975 同量级），`[mech] repeat_targeting/run=0.00 policy_latency=1603.9us` 机制统计正常输出。
- 运行时结构还原断言：`MarlPolicy(model_path=best.pt)` → `actor_type='pool_mlp'`、`net` 为 `PoolMLPNet` 实例、`params_count=10242`（与 checkpoint 一致）。
- 冲突 raise 三路径运行时可达：
  - 结构冲突：请求 `set_attention` → ValueError（requested structure … conflicts with checkpoint metadata）
  - 特征冲突：请求 `drop_m1=False` → ValueError
  - 缺失元数据：剔除 `ablation` 字段 → ValueError（lacks the 'ablation' metadata field）
- 注：评估器 stdout 不打印结构字段（v5 e47 日志同口径），还原信息以 checkpoint 元数据 + 运行时断言 + 冲突检测链共同背书；`family_report.json` 记录 `params.model` 与 `source_md5`。

---

## 判定

S1 四项、S2 四项全部通过；S3 定档冒烟另见 `logs/ablation_v3_budget.json` 与批注。管线可承载 e49–e51。
