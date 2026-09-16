"""基线算法扩展（E22-E25）三合一单测：

[1] 信息边界单测（e18 BoundaryProxy 模式，需求 §3 单测 ①）：
    greedy_threat / greedy_nearest / random / rh-cplex / mappo / qmix /
    iql 在只暴露 dn / pool / get_observation 的代理下完整跑 episode，
    任何越界属性访问（env.rng / env.shots / env.inflight /
    env.destroyed_at 等）立即引爆。

[2] RH-CPLEX 最优性自检（§3 单测 ②）：
    a) 虚拟平台展开 MIP（m'=m*H, mu=1）经真实求解器输出的目标值与
       暴力枚举最优解 gap < 1e-6（合成小规模 belief，7^6 枚举）；
    b) 公开动力学外推公式逐项复算（_rebuild_horizon 的 s=t+1 槽位）；
    c) 池尽边际修剪确定性（同输入两次调用逐位一致，且 <= pool）。

[3] 资源不变量冒烟（§3 单测 ③）：
    新策略 3 seeds x s01：发射总数 <= total_mu 且与 shots_total 一致、
    每平台每步至多 1 发、illegal_actions == 0。

跑法（约 2-4 分钟，需要 CPLEX 求解器可用）：

    /opt/anaconda3/envs/wta/bin/python tests/test_baseline_extension.py
"""

import itertools
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from dwta.dn_instance import DNInstance                    # noqa: E402
from dwta.dn_env import DNEnv                              # noqa: E402
from dwta.dn_policies import build_policy, RHCplexPolicy, \
    GreedyVariantPolicy, RandomPolicy                      # noqa: E402
from dwta import wave_runner                               # noqa: E402
from marl.baseline_policy import PoolMLPPolicy             # noqa: E402

DATA = os.path.join(ROOT, "data", "dn-data-v3")

ALLOWED = {"dn", "pool", "get_observation"}


class BoundaryProxy(object):
    """Forwards ONLY the legal observation surface; everything else is a
    boundary violation (identical to tests/test_pocplex_boundary.py)."""

    def __init__(self, env):
        object.__setattr__(self, "_env", env)

    def __getattr__(self, name):
        if name in ALLOWED:
            return getattr(object.__getattribute__(self, "_env"), name)
        raise AssertionError(
            "boundary violation: policy accessed env.%s" % name)


class GuardedPolicy(object):
    def __init__(self, pol):
        self.pol = pol

    def act(self, env, t):
        return self.pol.act(BoundaryProxy(env), t)


# ======================================================================
# [1] information boundary
# ======================================================================

def test_boundary():
    dn = DNInstance(os.path.join(DATA, "dn_3x50_K10_s27.txt"))

    # self-check: the proxy must block violations
    proxy = BoundaryProxy(DNEnv(dn, 42))
    for bad in ("rng", "shots", "inflight", "destroyed_at"):
        try:
            getattr(proxy, bad)
            raise SystemExit("FAIL: proxy did not block env.%s" % bad)
        except AssertionError:
            pass
    _ = proxy.pool
    _ = proxy.get_observation(0, 0)
    print("[boundary] proxy self-check ok")

    cases = [
        ("greedy_threat", build_policy("greedy_threat")),
        ("greedy_nearest", build_policy("greedy_nearest")),
        ("random p=0.3", build_policy("random", p_hold=0.3,
                                      policy_seed=0)),
        ("rh-cplex", build_policy("rh-cplex")),
        ("mappo(rand-init)", PoolMLPPolicy("mappo", device="cpu")),
        ("qmix(rand-init)", PoolMLPPolicy("qmix", device="cpu")),
        ("iql(rand-init)", PoolMLPPolicy("iql", device="cpu")),
    ]
    for label, pol in cases:
        env = DNEnv(dn, 42)
        rec = env.run(GuardedPolicy(pol))
        assert 0.0 <= rec["leak_rate"] <= 1.0
        print("[boundary] %-18s leak=%.4f shots=%d  PASS"
              % (label, rec["leak_rate"], rec["shots_total"]))
    print("[1] information boundary: ALL PASS")


# ======================================================================
# [2] RH-CPLEX optimality self-checks
# ======================================================================

def _brute_force_optimum(w, p2, m, H, L):
    """Enumerate every assignment of the m*H virtual platforms (each
    picks one of L targets or holds) -> min expected surviving value."""
    n = m * H
    options = [range(-1, L) for _ in range(n)]      # -1 = hold
    best = float("inf")
    for combo in itertools.product(*options):
        surv = 1.0
        total = 0.0
        hit = [1.0] * L
        for ip, j in enumerate(combo):
            if j >= 0:
                hit[j] *= (1.0 - p2[(ip // H, ip % H, j)])
        for j in range(L):
            total += w[j] * hit[j]
        del surv
        if total < best - 1e-12:
            best = total
    return best


def test_rhcplex_optimality():
    pol = RHCplexPolicy(solver=None, tmp_dir="/tmp/rh_opt_check")
    m, H = 3, 2
    ids = [101, 102, 103]
    w = {101: 9, 102: 6, 103: 3}      # solver parses integer values
    raw = {
        (0, 0): [0.50, 0.10, 0.00],
        (1, 0): [0.30, 0.40, 0.20],
        (2, 0): [0.00, 0.25, 0.60],
        (0, 1): [0.45, 0.05, 0.10],
        (1, 1): [0.25, 0.35, 0.15],
        (2, 1): [0.10, 0.20, 0.55],
    }
    p2 = {(i, s, j): raw[(i, s)][jj]
          for (i, s), row in raw.items()
          for jj, j in enumerate(ids)}

    inst = os.path.join(pol.tmp_dir, "opt_inst.txt")
    sol = os.path.join(pol.tmp_dir, "opt.sol")
    os.makedirs(pol.tmp_dir, exist_ok=True)
    if os.path.exists(sol):
        os.remove(sol)
    pol._write_horizon_instance(inst, ids, w, p2, m)
    rc, _out, _wall = wave_runner.run_solver(
        inst, sol, delta=0.001, timelimit=30, threads=1)
    parsed = wave_runner.parse_wave_solution(inst, sol, ids)
    assert parsed is not None, "solver run failed (rc=%s)" % rc
    brute = _brute_force_optimum(
        [w[j] for j in ids],
        {(i, s, jj): raw[(i, s)][jj]
         for (i, s), row in raw.items() for jj in range(len(ids))},
        m, H, len(ids))
    gap = abs(parsed["objective"] - brute)
    print("[rh-opt] solver=%.9f brute=%.9f gap=%.2e"
          % (parsed["objective"], brute, gap))
    assert gap < 1e-6, "MIP optimum deviates from brute force"
    print("[2a] virtual-platform MIP optimality: PASS")


def test_rhcplex_extrapolation():
    """Re-derive p2[(i, 1, j)] by hand from get_observation (snapshots
    taken along a real no-fire trajectory)."""
    dn = DNInstance(os.path.join(DATA, "dn_3x50_K10_s27.txt"))
    env = DNEnv(dn, 42)
    pol = RHCplexPolicy(solver=None, tmp_dir="/tmp/rh_extrap_check")
    records = []

    class Recorder(object):
        def act(self, e, t):
            ids, w, p2, pool = pol._rebuild_horizon(e, t)
            obs = [e.get_observation(i, t) for i in range(dn.m)]
            records.append((t, ids, w, p2, pool, obs))
            return {i: None for i in range(dn.m)}, {"solved": True}

    env.run(Recorder())
    rec_t = next((r for r in records if r[1]), None)
    assert rec_t is not None, "no live target found in any decision step"
    t, ids, w, p2, pool, obs_list = rec_t
    obs0 = obs_list[0]
    pub = obs0["public"]
    by_id = {tr["id"]: tr for tr in obs0["targets"]}
    checked = 0
    for i in range(dn.m):
        own = obs_list[i]["own"]
        for j in ids[:5]:
            p_slot0 = p2[(i, 0, j)]
            assert 0.0 <= p_slot0 <= pub["pcap"] + 1e-9
            tr = by_id[j]
            d = own["d"][j]
            d0 = d + pub["delta_d"] * tr["age"]
            d1 = max(0.0, d - pub["delta_d"])
            r1 = max(0.0, tr["r"] - pub["delta_d"])
            windows1 = math.ceil(r1 / pub["delta_d"] - 1e-9)
            if t + 1 > dn.K - 2 or pool <= 0 or windows1 < 1:
                expect = 0.0
            elif d1 <= 0.0:
                expect = pub["pcap"]
            else:
                p = min(pub["pcap"], own["p"][j] * d0 / d1)
                h1 = max(1, int(math.ceil(
                    d1 / pub["v_m"] / pub["dt"] - 1e-9)))
                expect = 0.0 if h1 > windows1 else max(0.0, p)
            got = p2[(i, 1, j)]
            assert abs(got - expect) < 1e-12, \
                "extrapolation mismatch (%d,%d): %.12f vs %.12f" \
                % (i, j, got, expect)
            checked += 1
    print("[2b] public-dynamics extrapolation: %d pairs re-derived PASS"
          % checked)


def test_rhcplex_trim_determinism():
    """Pool-starved trimming: <= pool shots, deterministic bit-for-bit."""
    dn = DNInstance(os.path.join(DATA, "dn_3x50_K10_s27.txt"))
    pol = RHCplexPolicy(solver=None, tmp_dir="/tmp/rh_trim_check")

    class _Fixed:
        """Stub _solve_horizon to a pre-fixed plan (6 virtual shots)."""
        pass

    def fake_solve(t, m, ids, w, p2):
        plan = {}
        L = len(ids)
        for ip in range(m * pol.H):
            plan[ip] = ids[ip % L]
        return plan, 1.0, True

    orig = pol._solve_horizon
    pol._solve_horizon = fake_solve
    try:
        outs = []
        for _ in range(2):
            env = DNEnv(dn, 42)
            actions, _info = pol.act(env, 0)
            fired = [j for j in actions.values() if j is not None]
            assert len(fired) <= env.pool, "trim exceeded pool"
            outs.append(tuple(sorted(actions.items())))
        assert outs[0] == outs[1], "trimming not deterministic"
    finally:
        pol._solve_horizon = orig
    print("[2c] pool trimming determinism: PASS")


# ======================================================================
# [3] resource invariants smoke
# ======================================================================

def test_resource_invariants():
    dn = DNInstance(os.path.join(DATA, "dn_3x50_K10_s01.txt"))
    cases = [
        ("greedy_threat", lambda: build_policy("greedy_threat")),
        ("greedy_nearest", lambda: build_policy("greedy_nearest")),
        ("random", lambda: build_policy("random", p_hold=0.3,
                                        policy_seed=0)),
        ("mappo", lambda: PoolMLPPolicy("mappo", device="cpu")),
        ("qmix", lambda: PoolMLPPolicy("qmix", device="cpu")),
    ]
    for label, make in cases:
        total_mu = dn.m * dn.mu
        for seed in (42, 43, 44):
            pol = make()
            env = DNEnv(dn, seed)
            rec = env.run(pol)
            steps = rec["steps"]
            total_shots = sum(s["shots"] for s in steps)
            assert total_shots == rec["shots_total"] <= total_mu, \
                "%s seed %d: ammo invariant broken (%d vs %d)" \
                % (label, seed, total_shots, total_mu)
            for s in steps:
                assert s["shots"] <= dn.m, \
                    "%s seed %d t=%d: >1 shot per platform" \
                    % (label, seed, s["t"])
                assert s["illegal_actions"] == 0, \
                    "%s seed %d: illegal engagement" % (label, seed)
        print("[invariants] %-16s 3 seeds PASS" % label)
    print("[3] resource invariants: ALL PASS")


def main():
    test_boundary()
    test_rhcplex_optimality()
    test_rhcplex_extrapolation()
    test_rhcplex_trim_determinism()
    test_resource_invariants()
    print("test_baseline_extension: ALL PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
