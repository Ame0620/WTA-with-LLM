"""Networks for the v4 MADDPG baseline (off-policy CTDE, D1).

DetActor: the deterministic policy - EXACTLY the PoolMLPNet skeleton
(marl/baseline_net.py: x in R^8 / q in R^5 / g in R^3, pooling + per-
target scoring, hold-first [1+L] logits). Sharing the architecture with
the MAPPO actor isolates the training-paradigm axis (off-policy
deterministic PG + centralised Q critic vs on-policy stochastic PG +
centralised V critic); no problem-specific modules (red line 3.1.1).

CentralQCritic: one Q_i(s, a_1..a_m) per platform, SHARED body +
per-agent heads (parameter budget: the red line [1e3, 1e5] applies to
the whole learnable system).

    state  = the SAME 35-dim row as StateCritic (masked-mean pooled
             TRUE target features 5->32 + global row 3, from
             train.critic_inputs minus the act block)          -> [B,35]
    action = PERMUTATION-INVARIANT joint-action embedding: platform i's
             action a_i is encoded by the chosen target's obs feature
             x_j in R^8 (hold -> zero vector); the m 8-dim vectors are
             concatenated                                     -> [B,8m]
    input  = 35 + 8*m (75 for v4 m=5; NO target-id one-hot - n=100 and
             permutation-sensitive, forbidden by the spec)
    output = [B, m]  (column i = Q_i for platform i's critic)

Target networks (actor + critic) are plain deepcopies managed by the
trainer with soft updates (tau = 0.005).
"""

import os
import sys

import torch
import torch.nn as nn

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from marl.baseline_net import PoolMLPNet, X_DIM             # noqa: E402,F401
from marl.baseline_net import assert_params                 # noqa: E402,F401


class DetActor(PoolMLPNet):
    """Deterministic actor - identical skeleton/forward to PoolMLPNet
    (subclass exists only to pin the role in checkpoints/reports)."""

    pass


class CentralQCritic(nn.Module):
    """Centralised per-agent Q_i(s, a) with a permutation-invariant
    joint-action embedding. n_agents is DERIVED from the constructor
    argument (never hardcoded 3)."""

    def __init__(self, n_agents: int, x_dim: int = X_DIM,
                 state_dim: int = 32 + 3, hidden: int = 128):
        super().__init__()
        self.n_agents = n_agents
        self.x_dim = x_dim
        self.state_dim = state_dim
        in_dim = state_dim + n_agents * x_dim
        self.tgt_proj = nn.Linear(5, 32)
        self.body = nn.Sequential(nn.Linear(in_dim, hidden), nn.ReLU(),
                                  nn.Linear(hidden, hidden), nn.ReLU())
        self.heads = nn.ModuleList(
            [nn.Linear(hidden, 1) for _ in range(n_agents)])

    def embed_actions(self, act_x):
        """act_x: [B, m, x_dim] per-platform chosen-target features
        (hold = zero row). Kept explicit for symmetry/documentation."""
        return act_x.reshape(act_x.shape[0], -1)          # [B, m*x_dim]

    def forward(self, tgt, glob, act_x, tgt_mask=None):
        """tgt: [B, L, 5] padded true rows, glob: [B, 3],
        act_x: [B, m, x_dim] -> Q values [B, m] (col i = Q_i)."""
        e = torch.tanh(self.tgt_proj(tgt))                # [B,L,32]
        if tgt_mask is not None:
            msk = tgt_mask.unsqueeze(-1).to(e.dtype)
            pooled = (e * msk).sum(dim=1) / msk.sum(dim=1).clamp(min=1.0)
        else:
            pooled = e.mean(dim=1)
        z = torch.cat([pooled, glob, self.embed_actions(act_x)], dim=-1)
        h = self.body(z)
        return torch.cat([hd(h) for hd in self.heads], dim=-1)   # [B,m]

    def params_count(self) -> int:
        return sum(p.numel() for p in self.parameters()
                   if p.requires_grad)


def assert_system_params(actor, critics, lo: float = 1e3, hi: float = 1e5):
    """Red-line check on the WHOLE learnable system (actor + critic)."""
    n = actor.params_count() + critics.params_count()
    assert lo <= n <= hi, \
        "trainable params %d outside red-line [%g, %g]" % (n, lo, hi)
    return n


# ----------------------------------------------------------------------
# selftest
# ----------------------------------------------------------------------

def _selftest():
    torch.manual_seed(0)
    for m in (3, 5):                       # dimension derived, no const 3
        actor = DetActor()
        critic = CentralQCritic(n_agents=m)
        n = assert_system_params(actor, critic)
        B, L = 6, 9
        x = torch.randn(B, L, X_DIM)
        tgt = torch.randn(B, L, 5)
        glob = torch.randn(B, 3)
        act_x = torch.zeros(B, m, X_DIM)
        act_x[:, 0, :] = x[:, 0, :]                       # fire / hold mix
        tmask = torch.ones(B, L, dtype=torch.bool)
        tmask[0, 4:] = False
        logits = actor.forward_batch(x, torch.randn(B, 5),
                                     torch.randn(B, 3), tmask)
        assert logits.shape == (B, 1 + L)
        q = critic(tgt, glob, act_x, tmask)
        assert q.shape == (B, m)
        # hold rows contribute exactly zero to the action embedding
        q2 = critic(tgt, glob, torch.zeros_like(act_x), tmask)
        d = (critic(tgt, glob, act_x, tmask) - q2).abs().max()
        assert d > 0, "action embedding has no effect on Q"
        print("m=%d: system params=%d, Q%s OK" % (m, n, tuple(q.shape)))
    print("marl/maddpg_net.py selftest: ALL PASS")


if __name__ == "__main__":
    _selftest()
