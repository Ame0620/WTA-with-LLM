"""E18 信息边界单测：POCplexPolicy 只读共享/own obs。

方法：BoundaryProxy 只暴露 dn / pool / get_observation 三个合法表面，
其它任何属性访问（env.rng、env.shots、env.inflight、env.destroyed_at
等深层数组）都会抛 AssertionError。DNEnv.run(GuardedPolicy(...)) 全程
驱动，若 POCplexPolicy 触碰任何越界属性，代理立即引爆。

自检部分先验证代理本身确实拦得住（故意越界必须抛错），再跑真实
episode。跑法（约 1 分钟）：

    /opt/anaconda3/envs/wta/bin/python tests/test_pocplex_boundary.py
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from dwta.dn_instance import DNInstance                    # noqa: E402
from dwta.dn_env import DNEnv                             # noqa: E402
from dwta.dn_policies import build_policy                 # noqa: E402

ALLOWED = {"dn", "pool", "get_observation"}


class BoundaryProxy(object):
    """Forwards ONLY the legal observation surface; everything else is a
    boundary violation."""

    def __init__(self, env):
        object.__setattr__(self, "_env", env)

    def __getattr__(self, name):
        if name in ALLOWED:
            return getattr(object.__getattribute__(self, "_env"), name)
        raise AssertionError(
            "boundary violation: POCplexPolicy accessed env.%s" % name)


class GuardedPolicy(object):
    """Feeds the policy a BoundaryProxy instead of the raw env."""

    def __init__(self, pol):
        self.pol = pol

    def act(self, env, t):
        return self.pol.act(BoundaryProxy(env), t)


def main():
    inst = os.path.join(ROOT, "data", "dn-data-v3",
                        "dn_3x50_K10_s27.txt")
    dn = DNInstance(inst)

    # ---- self-check: the proxy must catch violations ------------------
    proxy = BoundaryProxy(DNEnv(dn, 42))
    try:
        _ = proxy.rng                                   # noqa: F841
        print("FAIL: proxy did not block env.rng")
        return 1
    except AssertionError:
        pass
    try:
        _ = proxy.shots                                 # noqa: F841
        print("FAIL: proxy did not block env.shots")
        return 1
    except AssertionError:
        pass
    try:
        _ = proxy.destroyed_at                          # noqa: F841
        print("FAIL: proxy did not block env.destroyed_at")
        return 1
    except AssertionError:
        pass
    _ = proxy.pool                                       # legal
    _ = proxy.get_observation(0, 0)                      # legal
    print("proxy self-check: violations blocked, legal surface reachable")

    # ---- real run under the guarded surface ---------------------------
    pol = build_policy("pocplex")
    env = DNEnv(dn, 42)
    rec = env.run(GuardedPolicy(pol))
    leak = rec["leak_rate"]
    shots = rec["shots_total"]
    print("guarded episode finished: leak=%.4f shots=%d kills=%d"
          % (leak, shots, len(rec.get("destroyed_ids", []))))
    assert 0.0 <= leak <= 1.0 and shots >= 0
    print("test_pocplex_boundary: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
