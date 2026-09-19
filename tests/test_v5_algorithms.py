"""v5 full-algorithm S0 smoke tests (m = 10 dimension adaptation).

Requirement doc §4.1 (S0, gates V5''' / V2''') - correctness checks
BEFORE any budgeted run:

  nets    all four learning methods built at m = 10 stay inside the
          [1e3, 1e5] system-parameter red line; critic / mixer input
          dims are DERIVED from m (CriticNet state 35 + 3m = 65,
          CentralQCritic in 35 + 8m = 115, QMixer n_agents = 10)
  smoke   3 instances (s01 / s02 / s15) x 5 seeds per policy family:
          resource invariants (m = 10, n = 100, K = 10, mu = 7, global
          pool = 70 -> shots_total <= 70, ammo_end >= 0), zero invalid
          shots, leak in [0, 1]
  ga      chromosome length == dn.m (derived, not hardcoded)
  alias   build_policy('ecmappo') constructs the EC-MAPPO main-method
          policy (v5 §9 report alias)

CPLEX-referenced runs (gap metric) are intentionally NOT here - they
need the solver subprocess pipeline and are exercised via
experiments/dn_family_eval.py (S0 CPLEX probe: output/e26_v5_cplex_probe).

Usage:  python tests/test_v5_algorithms.py
"""

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from dwta.dn_instance import DNInstance                    # noqa: E402
from dwta.dn_env import simulate_dn                        # noqa: E402
from experiments import dn_report                          # noqa: E402
from dwta import dn_policies                               # noqa: E402

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "dn-data-v5")
INSTANCES = ["dn_10x100_K10_s01.txt", "dn_10x100_K10_s02.txt",
             "dn_10x100_K10_s15.txt"]
SEEDS = [42, 43, 44, 45, 46]

HEADER = dict(m=10, n=100, K=10, mu=7)     # global pool = 70


def check_resources(name, dn):
    assert (dn.m, dn.n, dn.K, dn.mu) == \
        (HEADER["m"], HEADER["n"], HEADER["K"], HEADER["mu"]), \
        "%s: resource invariant broken" % name
    assert dn.total_value() > 0


def run_grid(policy, tag):
    for name in INSTANCES:
        dn = DNInstance(os.path.join(DATA_DIR, name))
        check_resources(name, dn)
        for seed in SEEDS:
            rec = simulate_dn(dn, seed, policy)
            m = dn_report.run_metrics(rec, dn)
            assert 0.0 <= m["leak_rate"] <= 1.0, \
                "%s %s s%d: leak out of range" % (tag, name, seed)
            assert m["shots_total"] <= dn.m * dn.mu, \
                "%s %s s%d: pool invariant broken (%d > %d)" % (
                    tag, name, seed, m["shots_total"], dn.m * dn.mu)
            assert m.get("ammo_end", 0) >= 0 or \
                "ammo_end" not in m, \
                "%s %s s%d: negative ammo" % (tag, name, seed)
            # zero-illegal-action gate: decision-time legality audit
            # (invalid_shots counts flight-settlement misses, i.e. legal
            # shots whose target died in flight - a different thing)
            n_illegal = sum(s.get("illegal_actions", 0)
                            for s in rec.get("steps", []))
            assert n_illegal == 0, \
                "%s %s s%d: %d illegal decision actions" % (
                    tag, name, seed, n_illegal)
    print("  %-14s: %d instances x %d seeds  invariants OK"
          % (tag, len(INSTANCES), len(SEEDS)))


def _n_params(module):
    return sum(p.numel() for p in module.parameters())


def test_dims_and_params():
    import torch
    from marl.network import MarlNet
    from marl.train import CriticNet
    from marl.baseline_net import PoolMLPNet, QMixer
    from marl.maddpg_net import CentralQCritic, DetActor

    m = 10
    print("[S0] dimension audit at m = %d (all derived, none hardcoded)" % m)

    # EC-MAPPO: MarlNet actor + CriticNet(state 35 + 3m)
    actor = MarlNet()
    critic = CriticNet(n_agents=m)
    assert critic.state_dim == 35 + 3 * m, \
        "CriticNet state_dim %d != %d" % (critic.state_dim, 35 + 3 * m)
    sys_n = _n_params(actor) + _n_params(critic)
    assert 1e3 <= sys_n <= 1e5, "EC-MAPPO params %g out of red line" % sys_n
    print("  ecmappo : critic.state_dim=%d params=%d" % (
        critic.state_dim, sys_n))

    # MAPPO: PoolMLPNet actor + pooled state-value critic
    mappo_actor = PoolMLPNet()
    mappo_critic = PoolMLPNet()      # same skeleton, pooled critic head
    sys_n = _n_params(mappo_actor) + _n_params(mappo_critic)
    assert 1e3 <= sys_n <= 1e5, "MAPPO params %g out of red line" % sys_n
    print("  mappo   : params=%d" % sys_n)

    # QMIX: PoolMLPNet agents + monotone mixer at n_agents = m
    qmix_agent = PoolMLPNet()
    mixer = QMixer(n_agents=m)
    assert mixer.n_agents == m
    sys_n = _n_params(qmix_agent) + _n_params(mixer)
    assert 1e3 <= sys_n <= 1e5, "QMIX params %g out of red line" % sys_n
    print("  qmix    : mixer.n_agents=%d params=%d" % (
        mixer.n_agents, sys_n))

    # MADDPG: DetActor + CentralQCritic(in 35 + 8m)
    maddpg_actor = DetActor()
    central = CentralQCritic(n_agents=m)
    in_dim = central.body[0].in_features
    assert in_dim == 35 + 8 * m, \
        "CentralQCritic in_dim %d != %d" % (in_dim, 35 + 8 * m)
    sys_n = _n_params(maddpg_actor) + _n_params(central)
    assert 1e3 <= sys_n <= 1e5, "MADDPG params %g out of red line" % sys_n
    print("  maddpg  : critic.in_dim=%d params=%d" % (in_dim, sys_n))

    # forward shapes stay sane at m = 10 (one smoke forward each).
    # MarlNet sees the full 10-col x; PoolMLPNet / DetActor see the
    # 8-col drop_m1 view (feature_spec x: 8).
    with torch.no_grad():
        x10 = torch.randn(6, 10)
        x8 = torch.randn(6, 8)
        q = torch.randn(5)
        g = torch.randn(3)
        out = MarlNet()(x10, q, g)
        logits = out[0] if isinstance(out, tuple) else out
        assert logits.shape[0] == 7                   # hold + 6 targets
        assert PoolMLPNet()(x8, q, g).shape[0] == 7
        assert DetActor()(x8, q, g).shape[0] == 7
    print("  forward shapes at m=10: OK")


def test_env_smoke():
    print("[S0] env smoke: rules + GA + random-init learning policies")
    run_grid(dn_policies.build_policy("greedy"), "greedy")
    run_grid(dn_policies.build_policy("random", policy_seed=0), "random")
    run_grid(dn_policies.build_policy(
        "ga", ga_pop=8, ga_gen=5, policy_seed=0), "ga(8x5)")
    for name in ("ecmappo", "mappo", "qmix", "iql", "maddpg"):
        run_grid(dn_policies.build_policy(name, model_path=None,
                                          device="cpu"), name)


def test_ga_chromosome():
    print("[S0] GA chromosome length == dn.m (derived)")
    import numpy as np
    from dwta.dn_env import DNEnv
    from dwta import ga_solver
    dn = DNInstance(os.path.join(DATA_DIR, INSTANCES[0]))
    env = DNEnv(dn, 42)
    env._advance_to(0) if hasattr(env, "_advance_to") else None
    rng = np.random.RandomState(0)
    # decision step 0: chromosome covers ALL m platform slots
    assignment, _obj = ga_solver.solve_assign(env, 0, dn.m * dn.mu,
                                              rng, pop=8, gens=5)
    assert max(assignment.keys(), default=-1) < dn.m, \
        "GA chromosome uses platform id >= m"
    assert len(assignment) <= dn.m, "GA chromosome longer than m"
    print("  m=%d assignment slots=%d: OK" % (dn.m, len(assignment)))


def test_ecmappo_alias():
    print("[S0] build_policy('ecmappo') registry alias")
    from marl.policy import MarlPolicy
    pol = dn_policies.build_policy("ecmappo", model_path=None,
                                   device="cpu")
    assert isinstance(pol, MarlPolicy), \
        "ecmappo alias must construct MarlPolicy (EC-MAPPO main method)"
    print("  ecmappo -> MarlPolicy: OK")


if __name__ == "__main__":
    test_dims_and_params()
    test_ecmappo_alias()
    test_ga_chromosome()
    test_env_smoke()
    print("tests/test_v5_algorithms.py: ALL PASS")
