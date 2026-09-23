"""Structural reference networks for the learning baselines and the v5
ablation arms (QMIX / IQL agent nets; the CASP-off / DCCA-off ablation
actor & critic driven by the marl/train.py switches).

All agent-side networks consume the SAME §7 observation features as the
self-developed marl policy, minus the two M1-memory columns (see
perceive.build_inputs(drop_m1=True)): x in R^8, q in R^5, g in R^3.

PoolMLPNet (MLP + target mean/max pooling - the CASP-off ablation
actor in marl/train.py --use-casp 0, the agent network for QMIX/IQL):
    pooled  = [mean(x), max(x)] in R^16                (0-safe at L=0)
    z_i     = MLP_enc([pooled, q, g])        24 -> 64 -> 64
    s_j     = MLP_score([z_i, x_j])          72 -> 32 -> 1   per target
    s_hold  = MLP_hold([z_i])                64 -> 32 -> 1
    logits/Q = [s_hold, s_1..s_L]   (hold FIRST, same layout as MarlNet)

StateCritic (the DCCA-off ablation critic in marl/train.py --use-dcca 0):
    state value V(s) WITHOUT joint-action conditioning: masked-mean pooled
    true target features (5->32) + global row (3) -> 35 -> 128 -> 1.
    Inputs come from train.critic_inputs minus the act block.

QMixer (standard QMIX monotonic hypernetwork mixing, weights forced
non-negative through abs()): state in R^35 (same state vector as
StateCritic), embed 32, Q_tot monotone in every per-agent Q_i.

Parameter budget ~1.0e4 for PoolMLPNet (red line < 1e5, same as marl).
"""

import torch
import torch.nn as nn

X_DIM = 8          # build_inputs(drop_m1=True): 10 - 2 M1 columns
Q_DIM, G_DIM = 5, 3
STATE_DIM = 32 + 3     # pooled true targets + global row (mixer / critic)
# v5 (dn-data-v5, m = 10): all nets are parameterised by dn.m at
# construction time (see train.py ablation switches / train_qmix /
# train_maddpg). The N_AGENTS constant below is ONLY a legacy default /
# selftest convenience and must NOT be used as a training-time dimension
# source.
N_AGENTS = 3           # legacy default (dn-data-v3); v5 uses m = 10


class PoolMLPNet(nn.Module):
    """MLP agent network with target mean/max pooling (CASP-off
    ablation actor / QMIX + IQL agent net). Interface mirrors MarlNet:
    forward returns logits [1+L] hold-first; forward_batch is the A1
    batched twin."""

    def __init__(self, x_dim: int = X_DIM, d: int = 64):
        super().__init__()
        self.x_dim = x_dim
        self.d = d
        self.enc = nn.Sequential(
            nn.Linear(2 * x_dim + Q_DIM + G_DIM, d), nn.ReLU(),
            nn.Linear(d, d), nn.ReLU())
        self.score = nn.Sequential(nn.Linear(d + x_dim, 32), nn.ReLU(),
                                   nn.Linear(32, 1))
        self.hold = nn.Sequential(nn.Linear(d, 32), nn.ReLU(),
                                  nn.Linear(32, 1))

    # ------------------------------------------------------------------
    def _pool(self, x):
        """x: [L, x_dim] -> [2*x_dim] (mean, max); 0-safe at L=0."""
        L = x.shape[0]
        if L == 0:
            return torch.zeros(2 * self.x_dim)
        return torch.cat([x.mean(dim=0), x.max(dim=0).values])

    def forward(self, x, q, g):
        """x: [L, x_dim], q: [5], g: [3] -> logits [1+L] (hold first)."""
        z = self.enc(torch.cat([self._pool(x), q, g]))
        if x.shape[0] == 0:
            return self.hold(z)                      # [1]
        s_j = self.score(torch.cat(
            [z.unsqueeze(0).expand(x.shape[0], -1), x], dim=-1)
        ).squeeze(-1)
        s_p = self.hold(z)                           # [1]
        return torch.cat([s_p, s_j])

    # ------------------------------------------------------------------
    def forward_batch(self, x, q, g, pad_mask=None):
        """A1 batched twin: x [B, L, x_dim], q [B,5], g [B,3], pad_mask
        [B,L] bool (True = real row). Padded target slots get -inf so
        downstream softmax/gather are unaffected; pooling is masked so
        real rows see EXACTLY the per-sample forward (selftest)."""
        B, L, _ = x.shape
        m = pad_mask if pad_mask is not None \
            else torch.ones(B, L, dtype=torch.bool, device=x.device)
        mm = m.unsqueeze(-1).to(x.dtype)                  # [B,L,1]
        cnt = mm.sum(dim=1).clamp(min=1.0)                # [B,1]
        mean = (x * mm).sum(dim=1) / cnt                  # [B,x_dim]
        neg = torch.finfo(x.dtype).min
        xmax = x.masked_fill(~m.unsqueeze(-1), neg).max(dim=1).values
        empty = (m.sum(dim=1) == 0)                       # [B]
        xmax = torch.where(empty.unsqueeze(-1),
                           torch.zeros_like(xmax), xmax)
        z = self.enc(torch.cat([mean, xmax, q, g], dim=-1))   # [B,d]
        s_j = self.score(torch.cat(
            [z.unsqueeze(1).expand(B, L, self.d), x], dim=-1)
        ).squeeze(-1)                                     # [B,L]
        s_p = self.hold(z).squeeze(-1)                    # [B]
        logits = torch.cat([s_p.unsqueeze(1), s_j], dim=1)
        if pad_mask is not None:
            out_pad = torch.cat(
                [torch.zeros(B, 1, dtype=torch.bool, device=x.device),
                 ~pad_mask], dim=1)
            logits = logits.masked_fill(out_pad, -float("inf"))
        return logits

    def params_count(self) -> int:
        return sum(p.numel() for p in self.parameters()
                   if p.requires_grad)


def assert_params(model, lo: float = 1e3, hi: float = 1e5):
    n = model.params_count()
    assert lo <= n <= hi, \
        "trainable params %d outside red-line [%g, %g]" % (n, lo, hi)
    return n


class StateCritic(nn.Module):
    """State-value critic V(s): NO joint-action conditioning (the
    DCCA-off ablation arm - plain team GAE, no COMA counterfactuals)."""

    def __init__(self):
        super().__init__()
        self.tgt_proj = nn.Linear(5, 32)
        self.head = nn.Sequential(nn.Linear(STATE_DIM, 128), nn.Tanh(),
                                  nn.Linear(128, 1))

    def forward(self, tgt, glob, tgt_mask=None):
        """tgt: [B, L, 5] (padded true rows), glob: [B, 3] -> [B]."""
        e = torch.tanh(self.tgt_proj(tgt))                # [B,L,32]
        if tgt_mask is not None:
            m = tgt_mask.unsqueeze(-1).to(e.dtype)
            pooled = (e * m).sum(dim=1) / m.sum(dim=1).clamp(min=1.0)
        else:
            pooled = e.mean(dim=1)                        # 0-safe
        z = torch.cat([pooled, glob], dim=-1)
        return self.head(z).squeeze(-1)


class QMixer(nn.Module):
    """Standard QMIX monotonic mixing network (hypernetwork, abs()
    weights). state: [B, STATE_DIM]; agent_qs: [B, n_agents]."""

    def __init__(self, state_dim: int = STATE_DIM,
                 n_agents: int = N_AGENTS, embed: int = 32):
        super().__init__()
        self.n_agents = n_agents
        self.embed = embed
        self.hyper_w1 = nn.Sequential(nn.Linear(state_dim, 64), nn.ReLU(),
                                      nn.Linear(64, n_agents * embed))
        self.hyper_b1 = nn.Linear(state_dim, embed)
        self.hyper_w2 = nn.Sequential(nn.Linear(state_dim, 64), nn.ReLU(),
                                      nn.Linear(64, embed))
        self.hyper_b2 = nn.Sequential(nn.Linear(state_dim, 32), nn.ReLU(),
                                      nn.Linear(32, 1))

    def forward(self, agent_qs, state):
        """agent_qs: [B, n_agents], state: [B, state_dim] -> Q_tot [B].
        Monotone in every Q_i: all mixing weights pass through abs()."""
        B = agent_qs.shape[0]
        w1 = torch.abs(self.hyper_w1(state)).view(B, self.n_agents,
                                                   self.embed)
        b1 = self.hyper_b1(state).view(B, 1, self.embed)
        hidden = torch.nn.functional.elu(
            torch.bmm(agent_qs.view(B, 1, self.n_agents), w1) + b1)
        w2 = torch.abs(self.hyper_w2(state)).view(B, self.embed, 1)
        b2 = self.hyper_b2(state).view(B, 1, 1)
        return torch.bmm(hidden, w2).squeeze(1).squeeze(-1)


# ----------------------------------------------------------------------
# selftest: forward/forward_batch equivalence, pooling 0-safety,
# mixer monotonicity, parameter budget
# ----------------------------------------------------------------------

def _selftest():
    torch.manual_seed(0)
    net = PoolMLPNet()
    n = assert_params(net)
    L = 6
    x = torch.randn(L, X_DIM)
    q, g = torch.randn(Q_DIM), torch.randn(G_DIM)
    logits1 = net(x, q, g)
    assert logits1.shape == (1 + L,)

    # permutation invariance of per-target logits
    perm = torch.randperm(L)
    logits2 = net(x[perm], q, g)
    assert torch.allclose(logits1[1:], logits2[1:][perm.argsort()],
                          atol=1e-5), "permutation inconsistency"

    # empty target set
    logits0 = net(torch.zeros(0, X_DIM), q, g)
    assert logits0.shape == (1,)

    # forward_batch == per-sample forward (ragged padding)
    Bs, Lmax = 5, 8
    lens = [0, 3, 8, 1, 5]
    xb = torch.zeros(Bs, Lmax, X_DIM)
    qb = torch.randn(Bs, Q_DIM)
    gb = torch.randn(Bs, G_DIM)
    pm = torch.zeros(Bs, Lmax, dtype=torch.bool)
    for b, Lb in enumerate(lens):
        xb[b, :Lb] = torch.randn(Lb, X_DIM)
        pm[b, :Lb] = True
    lb = net.forward_batch(xb, qb, gb, pm)
    for b, Lb in enumerate(lens):
        ref = net(xb[b, :Lb], qb[b], gb[b])
        got = lb[b, :1 + Lb]
        assert torch.allclose(got, ref, atol=1e-5), \
            "forward_batch mismatch on row %d" % b
        assert torch.isfinite(lb[b, 1 + Lb:]).sum() == 0, "pad not -inf"
    # empty-set row keeps a finite hold logit
    assert torch.isfinite(lb[0, 0])

    # critic forward
    crit = StateCritic()
    v = crit(torch.randn(4, 7, 5), torch.randn(4, 3),
             torch.ones(4, 7, dtype=torch.bool))
    assert v.shape == (4,)

    # mixer monotonicity: d Q_tot / d Q_i >= 0 over a random batch
    mix = QMixer()
    st = torch.randn(16, STATE_DIM)
    qs = torch.randn(16, N_AGENTS)
    qtot = mix(qs, st)
    for i in range(N_AGENTS):
        qs2 = qs.clone()
        qs2[:, i] += 0.5
        assert (mix(qs2, st) >= qtot - 1e-6).all(), \
            "mixer not monotone in Q_%d" % i

    print("marl/baseline_net.py selftest: ALL PASS (agent params=%d)"
          % n)


if __name__ == "__main__":
    _selftest()
