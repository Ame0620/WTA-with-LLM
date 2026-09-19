# output/ 产物索引

按《项目整理规范》：扁平实验产物目录，本文件为唯一入口。

| 目录 | 内容 | 关键结果 | 上游 |
|------|------|----------|------|
| `regress_e11_none/` | e11 none 基线回归（test×30 seeds） | leak 1.0000；s01 指纹 `9134a16f`、s02 `e717a4c1` 与 MANIFEST 一致 | `experiments/dn_family_eval.py --policy none` |
| `regress_e12_greedy/` | e12 greedy 基线回归（test×30 seeds） | leak 0.7913±0.0095（与 LOGS_SUMMARY 一致） | `--policy greedy`（含逐步参考解） |
| `regress_e13_cplex/` | e13 cplex 基线回归（test×30 seeds） | leak 0.7085±0.0343 worst 0.7428；gap≈1e-14（参考解自洽） | `--policy cplex` |
| `e14_marl_train/` | 学习策略训练（M6） | `best.pt` / `train_log.jsonl` / `train_summary.json`：460 iters 早停，墙钟 5918s，best val 0.8943（iter 60），28482 参数，MPS | `marl/train.py --output output/e14_marl_train` |
| `e14_dn3_marl/` | e14 终评（test×30 seeds，含参考解） | leak 0.9009±0.0295 worst 0.9304；gap 0.7032；invalid 0.1130；纯策略 act p50 4ms | `--policy marl --model e14_marl_train/best.pt` |
| `e14_generalization/` | 泛化性快照（train/val split×30 seeds，`--no-ref`） | train 0.9166±0.0247 / val 0.8902±0.0134 —— 与 test 0.9009 一致，无过拟合 | `--policy marl --split train/val --no-ref` |

## E15–E25 实验索引（2026-09-07 ~ 09-09，最新进展）

| 目录 | 内容 | 关键结果 | 上游 |
|------|------|----------|------|
| `e15_diag/` | A0 只读诊断：e14 曲线判 PLATEAU → A3 为主攻 | `diag_report.md` | `experiments/e15_diag.py` |
| `e15_smoke/` | A1 PPO 批化等价性冒烟 | policy_loss 相对误差 1.77e-07；加速 ~170×（`bench.md`，含两处非显然修复） | `marl/network.py forward_batch` |
| `e15_train/` | e15 = A1+A2（批化 + 预算 4×）训练 | test leak 0.6194（−31.3%） | `marl/train.py` |
| `e16_scan/` | A3 击杀信用 p_shot 摊派 c_invalid 四档扫描 | 主臂 c\*=0.01：test leak 0.5546（再 −10.5%） | `marl/reward.py` |
| `e16_pos/` | Φ 符号翻转对照（pos-ctrl） | 0.6302，备选被数据否决 | — |
| `e17_bc/` `e17_bc01/` `e17_bc10/` | A4 BC 热启动（greedy 教师） | 在线复现比 1.000 门禁 PASS；blend 优于全量 | `marl/bc_pretrain.py` |
| `e18_eval/` | E18 PO-CPLEX 同信息中心化基线 | leak 0.7085、gap≡0（信息边界无实质约束） | `dwta/dn_policies.py POCplexPolicy` |
| `e19_eval/` | E19 终评大表（test×30 seeds） | `e19_summary.md`：e16_c010 0.5546，超 myopic CPLEX 21.7% | `bash experiments/e19_eval.sh` |
| `e19_generalization/` | 泛化性快照（train/val×30，`--no-ref`） | c010 val 0.6144，无过拟合 | `experiments/dn_family_eval.py` |
| `fix_marl/` `fix_regress/` | 全局池同拍竞态修复后全臂重评 + 基线锁定 | 修复后 c005 0.5993 / c010 0.6149；基线 result_hash 与锁定值逐位一致 | 见《实验报告_MARL核心框架.md》§4 |
| `e20_retrain/` `e20_eval/` `e20_gen/` | E20 修复后环境干净重训（c005/c010）+ 终评 + 泛化 | c010 test 0.5963 / c005 0.6032；val 0.6120 | `marl/train.py`（resume-from） |
| `e21_v4_cplex_probe/` | V4 规模（5×100）CPLEX 探针 | leak 0.6981、gap≡0；弹药 t=5 耗尽与 v3 节奏一致 | `data/dn-data-v4/` |
| `e22_baselines/` | 基线扩展：greedy_nearest / greedy_threat / random 两档 | 0.8922 / 0.8594 / 0.8724 / 0.8466 | `dwta/dn_policies.py` |
| `e26_v5_{none,cplex,greedy}_probe/` | V5 数据集（10×100，池 80）基线探针（test×5 seeds） | none 1.0000；greedy 0.6843±0.0415；**cplex 0.2938±0.0260**（弹药 t=7 耗尽、晚窗占比 0.81–0.93） | `data/dn-data-v5/`（见 `DN-WTA_v5_数据集说明.md`） |
| `e23_rhcplex/` | 滚动时域（receding horizon）CPLEX 基线 | leak 0.6808（优于 myopic 0.7085） | `dwta/dn_policies.py` |
| `e24_mappo*` | E24 MAPPO 基线（训练+终评+泛化） | test leak 0.6014；3.46M env steps / 3000 iters | `marl/train_mappo.py` |
| `e25_qmix*` | E25 QMIX 基线（训练+终评+泛化） | test leak 0.8262；1.81M steps 早停 | `marl/train_qmix.py` |
| `regress_check_e22to26.md` | E22–E26 改动后回归核查 | 6/6 result_hash 逐位一致 ALL PASS | — |

## 回归门结论（需求文档阶段 0）

三基线在 test split 上与 LOGS_SUMMARY e11–e13 记录**逐字段复现**（均值/方差/worst/gap/invalid/ammo/latency），核心求解与环境链路可用，允许进入 marl 开发。

## E14 结论速览

```
none    1.0000                    （下界）
marl    0.9009 ± 0.0295          （学习策略，第一版：显著优于 none，未追平 greedy）
greedy  0.7913 ± 0.0095          （启发式）
cplex   0.7085 ± 0.0343          （短视最优上界）
```

详见《实验报告_DN学习策略.md》。

## E15–E25 结论速览（详见《实验报告_MARL核心框架.md》终版 v2）

```
none      1.0000                    （下界）
qmix      0.8262                    （E25 基线扩展）
greedy    0.7913 ± 0.010            （启发式）
cplex     0.7085 ± 0.0343           （全知/同信息 myopic 最优，PO-CPLEX gap≡0 等价）
rhcplex   0.6808                    （E23 滚动时域）
mappo     0.6014                    （E24 基线扩展）
e20 c010  0.5963 ± 0.0168           （竞态修复后干净重训）
e19 c010  0.5546 ± 0.062            （改进主臂，修复前口径：超 myopic CPLEX 21.7%）
```

> 运维注：CPLEX 参考解长跑（每步删 2 个临时文件）曾受工作区安全删除阈值
> （500 文件/turn）影响中断，规避方式为 `--output /tmp/<dir>` 跑完后拷回
> （/tmp 删除不计入工作区 scope）。
