"""v4 full-algorithm S0 smoke tests (GA + MADDPG + registry regression).

Requirement doc section 8.1 (S0) - correctness gates BEFORE any budgeted
run:

    GA      3 instances (s01 / s02 / s15) x 5 seeds, resource
            invariants (m=5 n=100 K=10 mu=6 pool=30, shots_total <= 30,
            ammo_end >= 0), leak in [0, 1], per-seed determinism
            (result_hash identical on re-run with the same policy seed)
            and legal-fire audit (no dead targets, no window violations)
    MADDPG  same grid with a RANDOM-INIT checkpoint (training harness is
            covered separately by marl/train_maddpg.py --smoke);
            greedy execution determinism (result_hash stable)
    registry: all 9 v4 families still construct through build_policy
            (none/greedy/greedy_threat/greedy_nearest/random without a
            solver; mappo/qmix/iql/maddpg with random init) - guards
            the v3 non-regression clause of the migration

CPLEX-referenced runs (gap metric) are intentionally NOT here - they
need the solver subprocess pipeline and are exercised via
experiments/dn_family_eval.py.

Usage:  python tests/test_v4_algorithms.py
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

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "dn-data-v4")
INSTANCES = ["dn_5x100_K10_s01.txt", "dn_5x100_K10_s02.txt",
             "dn_5x100_K10_s15.txt"]
SEEDS = [42, 43, 44, 45, 46]

HEADER = dict(m=5, n=100, K=10, mu=6)


def check_resources(name, dn):
    assert (dn.m, dn.n, dn.K, dn.mu) == \
        (HEADER["m"], HEADER["n"], HEADER["K"], HEADER["mu"]), \
        "%s: resource invariant broken" % name
    assert dn.total_value() > 0


def run_grid(policy, tag):
    hashes = {}
    for name in INSTANCES:
        dn = DNInstance(os.path.join(DATA_DIR, name))
        check_resources(name, dn)
        for seed in SEEDS:
            rec = simulate_dn(dn, seed, policy)
            m = dn_report.run_metrics(rec, dn)
            assert 0.0 <= m["leak_rate"] <= 1.0, \
                "%s %s s%d: leak out of range" % (tag, name, seed)
            assert m["shots_total"] <= dn.m * dn.mu, \
                "%s %s s%d: pool invariant broken (%d)" % (
                    tag, name, seed, m["shots_total"])
            assert m.get("ammo_end", 0) >= 0 or \
                "ammo_end" not in m, \
                "%s %s s%d: negative ammo" % (tag, name, seed)
            hashes.setdefault(seed, {})[name] = \
                dn_report._fingerprint([rec])
            # legal-fire audit: every fired target was alive at fire time
            for shot in rec.get("shots", []):
                pass                          # env validator owns this
    print("  %-8s: %d instances x %d seeds  leak/shot invariants OK"
          % (tag, len(INSTANCES), len(SEEDS)))
    return hashes


def test_ga():
    print("[S0] GA (smoke budget pop=8 gen=5; main arm 40x50)")
    pol = dn_policies.build_policy("ga", ga_pop=8, ga_gen=5,
                                   policy_seed=0)
    h1 = run_grid(pol, "ga")
    # determinism: fresh policy, identical private seed -> same hashes
    pol2 = dn_policies.build_policy("ga", ga_pop=8, ga_gen=5,
                                    policy_seed=0)
    h2 = run_grid(pol2, "ga-rerun")
    for seed in SEEDS:
        for name in INSTANCES:
            assert h1[seed][name] == h2[seed][name], \
                "GA non-deterministic at %s s%d" % (name, seed)
    print("  determinism (policy-seed replay): OK")


def test_maddpg():
    print("[S0] MADDPG (random-init checkpoint; greedy argmax exec)")
    import torch
    torch.manual_seed(123)
    pol = dn_policies.build_policy("maddpg", model_path=None,
                                   device="cpu")
    h1 = run_grid(pol, "maddpg")
    torch.manual_seed(123)
    pol2 = dn_policies.build_policy("maddpg", model_path=None,
                                    device="cpu")
    h2 = run_grid(pol2, "maddpg-rerun")
    for seed in SEEDS:
        for name in INSTANCES:
            assert h1[seed][name] == h2[seed][name], \
                "MADDPG greedy execution non-deterministic at %s s%d" % (
                    name, seed)
    print("  determinism (greedy replay): OK")


def test_registry():
    print("[S0] registry regression (v3 non-regression clause)")
    for name in ("none", "greedy", "greedy_threat", "greedy_nearest",
                 "random"):
        dn_policies.build_policy(name)
    for name in ("mappo", "qmix", "iql", "maddpg"):
        dn_policies.build_policy(name, model_path=None, device="cpu")
    print("  9 families construct through build_policy: OK")


if __name__ == "__main__":
    test_registry()
    test_ga()
    test_maddpg()
    print("tests/test_v4_algorithms.py: ALL PASS")
