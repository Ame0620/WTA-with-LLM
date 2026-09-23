# Related Work

**Static and dynamic WTA as combinatorial optimization.**

Research on weapon-target assignment (WTA) traces back to early missile-allocation studies that established mathematical-programming and dynamic-programming formulations for allocating finite weapons against targets with heterogeneous values and kill probabilities [@matlin1970review]. Hosein and Athans formalized the distinction between static WTA (SWTA), in which all assignments are made simultaneously under perfect state information, and dynamic WTA (DWTA), in which decisions unfold across engagement stages with evolving target states and weapon arrivals [@hosein1990dynamic]. Murphey further provided a target-based formulation that remains a reference for subsequent algorithmic work [@murphey2000target]. For SWTA, exact methods include branch-and-bound procedures with network-flow lower bounds and constructive heuristics [@ahuja2007exact], Lagrangian relaxation that decomposes the relaxed model into tractable subproblems [@ni2011lagrange], and bounded-approximation schemes [@andersen2022weapontarget]. When the scale or nonlinear coupling of the assignment precludes exhaustive optimization, heuristic and metaheuristic search remains important; representative examples include iterative heuristic and metaheuristic methods for SWTA [@kline2020heuristic] and adaptive large-neighborhood search for multi-stage WTA [@chang2023adaptive]. For DWTA, evolutionary decision methods have incorporated capability, strategy, resource, and engagement-feasibility constraints [@chen2009evolutionary], while adaptive dynamic programming combines simulation and mathematical programming to estimate future-stage value [@ahner2014optimal]. These approaches provide explicit constraint handling and strong optimization baselines, but they typically assume centralized full-state observability and their repeated online solution becomes expensive when the operational state changes rapidly. Crucially, none of these formulations address a setting in which platforms cannot communicate directly, kill outcomes are observed only after stochastic delay, and the target set itself varies over time.

**Reinforcement learning for WTA.**

Reinforcement learning (RL) recasts DWTA as sequential decision making, allowing an assignment policy to optimize cumulative mission return rather than solve each stage independently. Time-driven DWTA models use RL to respond to evolving target threats at sampled decision epochs [@liu2023timedriven]. Deep value-based methods have also been used to learn assignment policies directly from interaction, including a DQN formulation for DWTA [@li2023dynamic]; in joint-combat settings, multi-head deep RL constructs a multi-constraint WTA Markov decision process and learns assignments through attention-oriented policy representations [@li2023weapontarget]. For maritime soft-kill engagements, value-iteration-based RL has been coupled with static binary optimization and simulation-optimization components to address sequential allocation [@tashakori2024dynamic]. Compared with repeated mixed-integer or metaheuristic optimization, these methods shift computational effort to offline training and can support rapid inference during execution. However, existing RL–WTA studies predominantly assume full observability or centralized execution, and they rarely confront the credit-assignment difficulty that arises when kill outcomes follow a delayed Bernoulli settlement process: a single episode contains few decision steps, and a successful interception may be credited only several steps after the firing decision. The general multi-agent RL (MARL) literature has developed counterfactual baselines [@foerster2018coma] and potential-based reward shaping with provable policy-invariance guarantees [@ng1999policy], but these mechanisms have not been systematically adapted to the structured credit-assignment problem of delayed WTA.

**Decentralized and partially observable WTA.**

A separate line of research recognizes that WTA decisions may be made by geographically distributed platforms with local information and imperfect communication. Decentralized WTA has been formulated through distributed optimization, where weapons optimize disjoint variable subsets and primal–dual updates retain convergence guarantees under asynchronous computation and communication [@hendrickson2022decentralized]. Unreliable peer-to-peer architectures explicitly model packet loss and employ decentralized artificial-bee-colony optimization [@liu2021weapontarget]; communication-range limits have also motivated grouped distributed-auction mechanisms for online WTA [@si2023online]. Dynamic distributed constraint optimization with multi-agent RL further treats cooperative DWTA as a time-varying distributed decision problem [@shokoohi2022dynamic]. More generally, cooperative MARL provides a decentralized-execution framework for agents acting under partial observations, commonly formalized through decentralized partially observable Markov decision processes (Dec-POMDPs) [@oliehoek2016concise]. These studies address isolated aspects of distributed decision making—asynchronous updates, packet loss, or cooperative learning—but they uniformly assume at least some form of inter-platform information exchange, even when degraded. None considers the stricter regime of zero direct communication coupled with globally shared but locally invisible ammo resources, where coordination must rely entirely on implicit signals inferred from observable side effects.

**Scalable coordination and set-structured policies.**

Beyond WTA-specific work, the broader MARL literature offers building blocks that are relevant but not yet integrated for this problem. The centralized-training-and-decentralized-execution (CTDE) paradigm, exemplified by MADDPG [@lowe2017maddpg] and surveyed by Amato [@amato2024introduction], allows global information to shape training while preserving deployment-time autonomy. Mean-field MARL approximates interactions among many agents using an aggregate effect of neighboring policies, reducing the complexity of explicitly representing joint actions [@yang2018meanfield]. For problems with variable-size input sets, permutation-invariant neural architectures such as Deep Sets [@zaheer2017deep] and Set Transformer [@lee2019set] provide natural invariance to set cardinality and element ordering, which is essential when the number of tracked targets changes during an engagement. However, these techniques have been developed and validated in generic cooperative-navigation or particle-world benchmarks; their combination with hard action-masking, delayed Bernoulli feedback, and resource-coupling constraints in a WTA setting remains unexplored.

**Positioning of this work.**

This paper studies a strictly partially observable DWTA in which platforms cannot communicate directly, ammo resources are globally coupled, kill outcomes follow a delayed Bernoulli settlement process, and the target set varies over time—a regime that none of the methods reviewed above jointly addresses. To this end, we develop a centralized-training-and-decentralized-execution (CTDE) learning policy that operates within a verifiable information boundary, and show empirically that it outperforms distributed greedy baselines on leakage rate, ammo efficiency, and decision latency.

<!-- ================================================================
     旧版草稿（原 LaTeX \iffalse ... \fi 注释块，仅存档备查）
     ================================================================ -->

<!--
Research on WTA has progressed from static mathematical formulations to
dynamic and learning-based decision models. Traditional approaches
include integer and mixed-integer programming, constructive heuristics,
evolutionary algorithms, and other combinatorial optimization methods.
These methods remain valuable because they provide strong optimization
baselines and, for moderate problem sizes, can produce high-quality or
provably optimal solutions. However, DWTA introduces temporal state
transitions and repeated resource allocation, making repeated exact
optimization increasingly expensive. Existing surveys distinguish
static WTA from multi-stage and fully dynamic formulations and emphasize
that time-varying weapon availability, target state, engagement timing,
and resource consumption substantially increase the difficulty of the
problem [@li2024survey].

Learning-based WTA methods seek to amortize part of this computational
cost by learning a policy offline and applying it through fast neural
inference online. Recent work has introduced Q-learning, actor–critic
architectures, pointer networks, recurrent networks, and attention
mechanisms for weapon allocation. Na et al. formulate constrained WTA
with heterogeneous launchers as a decentralized multi-agent decision
problem and introduce a hierarchical MARL structure that sequentially
selects agents and targets [@na2026priority]. Other recent work on
multi-stage DWTA incorporates weapon availability, cooldown intervals,
and target engagement windows and uses an improved actor–critic model
with attention and dynamic masking to handle variable-size assignment
spaces [@zou2026multistage]. These studies demonstrate the value of
learning temporal assignment strategies, but their primary emphasis is
on assignment quality, constraint handling, or scalable policy
representation.

The broader MARL literature has also investigated coordination when the
number of interacting agents becomes large. Mean-field MARL, for
example, approximates interactions among many agents using an aggregate
effect of neighboring policies, reducing the complexity of explicitly
representing joint actions [@yang2018meanfield]. Such approaches
illustrate that useful coordination information does not always require
complete access to every other agent's action. Related decentralized WTA
research has additionally considered imperfect or asynchronous
communications, highlighting the practical importance of distributed
decision making [@hendrickson2023decentralized].

Our work focuses on a different information bottleneck. The missing
variable is not merely another agent's current action, but the
*temporally persistent consequence* of a previous action: an
interceptor that has already been launched but has not yet produced an
observable damage outcome. We therefore treat pending engagement
coverage as a latent state to be reconstructed rather than as an
explicit communication message. This perspective connects delayed
feedback, partial observability, and multi-agent coordination within a
single DWTA formulation.
-->

## References

<!-- ===== 早期草稿中引用的文献 ===== -->

- **li2024survey** — Jinrui Li, Guohua Wu, and Ling Wang. "A Comprehensive Survey of Weapon Target Assignment Problem: Model, Algorithm, and Application." *Engineering Applications of Artificial Intelligence*, 137:109212, 2024. <https://doi.org/10.1016/j.engappai.2024.109212>
- **yang2018meanfield** — Yaodong Yang, Rui Luo, Minne Li, Ming Zhou, Weinan Zhang, and Jun Wang. "Mean Field Multi-Agent Reinforcement Learning." In *Proceedings of the 35th International Conference on Machine Learning*, volume 80 of *Proceedings of Machine Learning Research*, pages 5571–5580, 2018.
- **na2026priority** — Hyungho Na, Jaemyung Ahn, and Il-Chul Moon. "Multi-Agent Reinforcement Learning Considering Agent Priority for Weapon–Target Assignment." *Journal of Aerospace Information Systems*, 23(6), 2026. <https://doi.org/10.2514/1.I011676>
- **zou2026multistage** — Yao Zou, Tianjiao Liu, Xu Lyu, Yanling Zhang, and Wenda Guo. "Multi-stage Dynamic Weapon-target Assignment Based on Improved Reinforcement Learning." *Information and Control*, 55(2):292–305, 2026. <https://doi.org/10.13976/j.cnki.xk.2025.3302>
- **hendrickson2023decentralized** — K. Hendrickson, P. Ganesh, K. Volle, P. Buzaud, K. Brink, and M. Hale. "Decentralized Weapon–Target Assignment under Asynchronous Communications." *Journal of Guidance, Control, and Dynamics*, 46:312–324, 2023.

<!-- ===== related work 2026.9.10 更新的文献 ===== -->

- **matlin1970review** — Samuel Matlin. "A Review of the Literature on the Missile-Allocation Problem." *Operations Research*, 18(3):374–380, 1970. <https://doi.org/10.1287/opre.18.3.374>
- **hosein1990dynamic** — Patrick A. Hosein and Michael Athans. "The Dynamic Weapon-Target Allocation Problem." Technical Report LIDS-P-1946, MIT Laboratory for Information and Decision Systems, Cambridge, MA, 1990.
- **murphey2000target** — Robert A. Murphey. "Target-Based Weapon Target Assignment Problems." In Panos M. Pardalos and Leonidas S. Pitsoulis, editors, *Nonlinear Assignment Problems: Algorithms and Applications*, pages 39–53. Springer, Boston, MA, 2000. <https://doi.org/10.1007/978-1-4757-6663-9_3>
- **ahuja2007exact** — Ravindra K. Ahuja, Arvind Kumar, Krishna C. Jha, and James B. Orlin. "Exact and Heuristic Algorithms for the Weapon-Target Assignment Problem." *Operations Research*, 55(6):1136–1146, 2007. <https://doi.org/10.1287/opre.1070.0440>
- **ni2011lagrange** — Mingfang Ni, Zhanke Yu, Feng Ma, and Xinrong Wu. "A Lagrange Relaxation Method for Solving Weapon-Target Assignment Problem." *Mathematical Problems in Engineering*, 2011:873292, 2011. <https://doi.org/10.1155/2011/873292>
- **kline2020heuristic** — Alexander R. Kline, Darryl K. Ahner, and Brian J. Lunday. "A Heuristic and Metaheuristic Approach to the Static Weapon Target Assignment Problem." *Journal of Heuristics*, 26(3):379–403, 2020. <https://doi.org/10.1007/s10732-019-09419-2>
- **andersen2022weapontarget** — Alexandre Colaers Andersen, Konstantin Pavlikov, and Túlio A. M. Toffolo. "Weapon-Target Assignment Problem: Exact and Approximate Solution Algorithms." *Annals of Operations Research*, 2022. <https://doi.org/10.1007/s10479-022-04525-6>
- **chang2023adaptive** — Xuening Chang, Jianmai Shi, Zhihao Luo, and Yao Liu. "Adaptive Large Neighborhood Search Algorithm for Multi-Stage Weapon Target Assignment Problem." *Computers & Industrial Engineering*, 181:109303, 2023. <https://doi.org/10.1016/j.cie.2023.109303>
- **chen2009evolutionary** — Jie Chen, Bin Xin, Zhihong Peng, Lihua Dou, and Juan Zhang. "Evolutionary Decision-Makings for the Dynamic Weapon-Target Assignment Problem." *Science China Information Sciences*, 52(11):2126–2137, 2009. <https://doi.org/10.1007/s11432-009-0190-x>
- **ahner2014optimal** — Darryl K. Ahner and Carl R. Parsons. "Optimal Multi-Stage Allocation of Weapons to Targets Using Adaptive Dynamic Programming." *Optimization Letters*, 8(5):1625–1637, 2014. <https://doi.org/10.1007/s11590-014-0823-x>
- **liu2023timedriven** — Chang Liu, Jiang Li, Ye Wang, Yang Yu, Lihong Guo, Yuan Gao, Yang Chen, and Feng Zhang. "A Time-Driven Dynamic Weapon Target Assignment Method." *IEEE Access*, 11:133325–133339, 2023. <https://doi.org/10.1109/ACCESS.2023.3332513>
- **li2023dynamic** — Chong Li, Bin Xin, Yingmei He, Danjing Wang, and Yang Li. "Dynamic Weapon Target Assignment Based on Deep Q Network." In *2023 42nd Chinese Control Conference (CCC)*, pages 1–6, 2023. <https://doi.org/10.23919/CCC58697.2023.10240428>
- **li2023weapontarget** — Shuai Li, Xiaoyuan He, Xiao Xu, Tan Zhao, Chenye Song, and Jiabao Li. "Weapon-Target Assignment Strategy in Joint Combat Decision-Making Based on Multi-Head Deep Reinforcement Learning." *IEEE Access*, 11:33241–33251, 2023. <https://doi.org/10.1109/ACCESS.2023.3324193>
- **tashakori2024dynamic** — Sadegh Tashakori, Mohammad Ranjbar, Saeed Balochian, Javad Sharif-Razavian, and Mahboobeh Peymankar. "Dynamic Soft-Kill Weapon-Target Assignment in Naval Environments." *Computers & Industrial Engineering*, 187:110606, 2024. <https://doi.org/10.1016/j.cie.2024.110606>
- **hendrickson2022decentralized** — Katherine Hendrickson, Prashant Ganesh, Kyle Volle, Paul Buzaud, Kevin Brink, and Matthew Hale. "Decentralized Weapon–Target Assignment Under Asynchronous Communications." *Journal of Guidance, Control, and Dynamics*, 45(8):1456–1468, 2022. <https://doi.org/10.2514/1.G006532>
- **liu2021weapontarget** — Xiaolong Liu, Jinchao Liang, De-Yu Liu, Riqing Chen, and Shyan-Ming Yuan. "Weapon-Target Assignment in Unreliable Peer-to-Peer Architecture Based on Adapted Artificial Bee Colony Algorithm." *Frontiers of Computer Science*, 15(6):156315, 2021. <https://doi.org/10.1007/s11704-021-0395-8>
- **si2023online** — Jiashuai Si and Mingrui Hao. "Online Weapon-Target Assignment Based on Distributed Auction Mechanism." *Journal of Physics: Conference Series*, 2456(1):012044, 2023. <https://doi.org/10.1088/1742-6596/2456/1/012044>
- **shokoohi2022dynamic** — Maryam Shokoohi, Mohsen Afsharchi, and Hamed Shah-Hosseini. "Dynamic Distributed Constraint Optimization Using Multi-Agent Reinforcement Learning." *Soft Computing*, 26(24):14132–14149, 2022. <https://doi.org/10.1007/s00500-022-06820-7>
- **oliehoek2016concise** — Frans A. Oliehoek and Christopher Amato. *A Concise Introduction to Decentralized POMDPs*. SpringerBriefs in Intelligent Systems. Springer, Cham, Switzerland, 2016. <https://doi.org/10.1007/978-3-319-28929-8>
- **amato2024introduction** — Christopher Amato. "An Introduction to Centralized Training for Decentralized Execution in Cooperative Multi-Agent Reinforcement Learning." *arXiv preprint arXiv:2409.03052*, 2024. <https://doi.org/10.48550/arXiv.2409.03052>
- **foerster2018coma** — Jakob N. Foerster, Gregory Farquhar, Triantafyllos Afouras, Nantas Nardelli, and Shimon Whiteson. "Counterfactual Multi-Agent Policy Gradients." In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 32, pages 2974–2982. AAAI Press, 2018.
- **ng1999policy** — Andrew Y. Ng, Daishi Harada, and Stuart Russell. "Policy Invariance under Reward Transformations: Theory and Application to Reward Shaping." In *Proceedings of the 16th International Conference on Machine Learning (ICML)*, pages 278–287. Morgan Kaufmann, 1999.
- **lowe2017maddpg** — Ryan Lowe, Yi Wu, Aviv Tamar, Jean Harb, Pieter Abbeel, and Igor Mordatch. "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments." In *Advances in Neural Information Processing Systems*, volume 30, pages 6379–6390. Curran Associates, 2017.
- **zaheer2017deep** — Manzil Zaheer, Satwik Kottur, Siamak Ravanbakhsh, Barnabas Poczos, Ruslan R. Salakhutdinov, and Alexander J. Smola. "Deep Sets." In *Advances in Neural Information Processing Systems*, volume 30, pages 3391–3401. Curran Associates, 2017.
- **lee2019set** — Juho Lee, Yoonho Lee, Jungtaek Kim, Adam R. Kosiorek, Seungjin Choi, and Yee Whye Teh. "Set Transformer: A Framework for Attention-Based Permutation-Invariant Neural Networks." In *Proceedings of the 36th International Conference on Machine Learning*, pages 3744–3753. PMLR, 2019.
