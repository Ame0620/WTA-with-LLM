"""Baseline decision policies for the DN-WTA v2 environment.

All policies implement the same interface consumed by DNEnv.run:

    policy.act(env, t) -> (actions, info)
        actions : {agent_i: target_j or None}   (<= 1 shot per agent/step)
        info    : dict(solved, failed_agents, wall_time, objective,
                       detail) - objective is the pool-feasible centralised
                       myopic CPLEX optimum on the same state (metric iii
                       gap reference; re-scored after global-pool trimming,
                       so the cplex policy's own gap is 0 by definition).

Policies:

  NonePolicy   ('none')   : never fire - sanity lower bound, reproduces the
                            no-defense leak histogram of the dataset spec;
  GreedyPolicy ('greedy') : DISTRIBUTED local greedy. Each agent uses only
                            get_observation(i, t) (spec §7): score =
                            w_j * p_eff_ij(t) / remaining_windows, filtered
                            to targets the interceptor can still reach before
                            breakthrough (t_hit <= breakthrough step). No
                            communication -> duplicate engagements possible
                            (shows up in metric xvii);
  GreedyVariantPolicy
                ('greedy_threat')  : same structure/filter, score =
                            w_j / windows_left (B1: value x urgency WITHOUT
                            the p_eff term);
                ('greedy_nearest') : score = -d_ij(t) (C2 optional);
  RandomPolicy ('random') : uniform random over the same legal target set,
                            private RandomState(seed), p_hold hold-fire
                            probability (B2);
  CplexPolicy  ('cplex')  : CENTRALISED myopic optimum. Full joint state
                            (violates §7 on purpose - it is the reference
                            upper bound): builds the per-step static
                            sub-instance (mu = 1 per platform, effective
                            probabilities) and calls the untouched
                            cplex/wta_cplex.py via subprocess, exactly like
                            the legacy wave_runner. Global-pool aware
                            marginal-value trimming when the pool cannot
                            cover the solver's plan.
  POCplexPolicy('pocplex'): centralised rolling myopic optimum UNDER the
                            spec §7 boundary - belief rebuilt from the union
                            of per-agent observations (E18).
  RHCplexPolicy('rh-cplex'): 2-step receding-horizon lookahead under the
                            same §7 boundary - (platform x slot) pairs
                            expanded into m*H virtual platforms, slot-t+1
                            p_eff extrapolated along the public dynamics,
                            solver untouched, only the s=t slice executed
                            (E23 B3).

The CPLEX subprocess machinery (run_solver / parse_wave_solution /
CplexLimitError) is re-used as-is from dwta/wave_runner.py; only the
sub-instance writer is DN-specific (effective p at time t).
"""

import math
import os

import numpy as np

from . import wave_runner


# ----------------------------------------------------------------------
# policy 1: no defense
# ----------------------------------------------------------------------

class NonePolicy(object):
    name = "none"
    needs_solver = False

    def act(self, env, t):
        return {i: None for i in range(env.dn.m)}, {
            "solved": True, "failed_agents": 0}


# ----------------------------------------------------------------------
# policy 2: distributed local greedy (observation-only)
# ----------------------------------------------------------------------

class GreedyPolicy(object):
    name = "greedy"
    needs_solver = False

    def __init__(self, with_reference=False, solver=None, tmp_dir=None):
        """with_reference: additionally solve the per-step CPLEX optimum on
        the SAME state to compute the gap (iii) of this policy's decisions.
        Needs solver config dict + tmp_dir (see main.py)."""
        self.with_reference = with_reference
        self._solver = solver
        self._tmp_dir = tmp_dir
        self._ref = CplexPolicy(solver, tmp_dir) if with_reference else None

    @staticmethod
    def _obs_lookup(obs, j, key):
        return next(tr[key] for tr in obs["targets"] if tr["id"] == j)

    def _score(self, obs, i, j, t):
        """w_j * p_eff_ij(t) / windows_left - observation-only (spec §7).

        p_eff needs d0_ij which is NOT in the observation; the agent
        reconstructs it from the public closing dynamics:
        d0_ij = d_ij(t) + delta_d * age_j(t). windows_left and the flight
        time h derive from the shared r_j(t) / own d_ij(t) respectively.
        """
        pub, own = obs["public"], obs["own"]
        d = own["d"][j]
        age = self._obs_lookup(obs, j, "age")
        d0 = d + pub["delta_d"] * age
        p_eff = min(pub["pcap"], own["p"][j] * d0 / max(d, 1e-9))
        r = self._obs_lookup(obs, j, "r")
        windows_left = max(1, int(math.ceil(r / pub["delta_d"] - 1e-9)))
        w = self._obs_lookup(obs, j, "w")
        return w * p_eff / windows_left

    def act(self, env, t):
        dn = env.dn
        actions = {}
        if env.pool <= 0 or t > dn.K - 2:
            return {i: None for i in range(dn.m)}, {
                "solved": True, "failed_agents": 0}

        for i in range(dn.m):
            obs = env.get_observation(i, t)
            pub, own = obs["public"], obs["own"]
            best_j, best_s = None, 0.0
            for tr in obs["targets"]:
                if not tr["alive"]:
                    continue
                j, r = tr["id"], tr["r"]
                windows_left = math.ceil(r / pub["delta_d"] - 1e-9)
                if windows_left < 1:
                    continue  # cannot be engaged any more
                # own interceptor must arrive before/at breakthrough
                d = own["d"][j]
                h = max(1, int(math.ceil(d / pub["v_m"] / pub["dt"] - 1e-9)))
                if t + h > t + windows_left:
                    continue
                s = self._score(obs, i, j, t)
                if s > best_s:
                    best_j, best_s = j, s
            actions[i] = best_j

        info = {"solved": True, "failed_agents": 0}
        if self._ref is not None:
            _, ref_info = self._ref.act(env, t)
            info["reference_cost"] = ref_info.get("objective")
            info["reference_solved"] = ref_info.get("solved", False)
            info["detail"] = ref_info.get("detail")
        return actions, info


# ----------------------------------------------------------------------
# policy 2b: greedy family variants (B1 value-urgency / C2 nearest)
# ----------------------------------------------------------------------

class GreedyVariantPolicy(GreedyPolicy):
    """Greedy with a parameterised scoring rule (E22 baselines).

    Structurally identical to GreedyPolicy (same reachability filter:
    windows_left >= 1 and h <= windows_left, observation-only inputs per
    spec §7); only _score is swapped via `score_mode`:

      'threat'  : w_j / windows_left_j - value x urgency WITHOUT the
                  hit-probability term p_eff (B1: isolates how much of
                  greedy's strength comes from p_eff)
      'nearest' : 1/(d_ij(t) + eps) - engage the closest reachable
                  target, ignore value/urgency/p_eff (C2 optional
                  rule-family extension)

    Registered as 'greedy_threat' (score_mode='threat', the B1 baseline)
    and 'greedy_nearest' (score_mode='nearest', optional C2).
    """

    name = "greedy_threat"
    needs_solver = False

    def __init__(self, score_mode="threat", with_reference=False,
                 solver=None, tmp_dir=None):
        GreedyPolicy.__init__(self, with_reference=with_reference,
                              solver=solver, tmp_dir=tmp_dir)
        if score_mode not in ("threat", "nearest"):
            raise ValueError("unknown score_mode: %r" % score_mode)
        self.score_mode = score_mode

    def _score(self, obs, i, j, t):
        pub, own = obs["public"], obs["own"]
        if self.score_mode == "threat":
            # value x urgency, no p_eff term
            r = self._obs_lookup(obs, j, "r")
            windows_left = max(1, int(math.ceil(r / pub["delta_d"] - 1e-9)))
            w = self._obs_lookup(obs, j, "w")
            return w / windows_left
        # 'nearest': closer is better; 1/(d + eps) keeps the score
        # POSITIVE so the strictly-greater-than-0 update rule of
        # GreedyPolicy.act accepts it (ordering identical to -d)
        return 1.0 / (own["d"][j] + 1e-9)


# ----------------------------------------------------------------------
# policy 2c: uniform random over legal actions (B2 lower bound)
# ----------------------------------------------------------------------

class RandomPolicy(object):
    """Uniform-random legal baseline (E22 B2).

    Legal action set per agent/step = the SAME reachability filter as
    GreedyPolicy (alive + windows_left >= 1 + h <= windows_left, from
    get_observation(i, t) only, spec §7). Each step each platform:

        * with probability p_hold (CLI --p-hold, default 0.3): hold fire;
        * otherwise: uniformly at random one target from the legal set
          (hold if the legal set is empty).

    Determinism: private numpy RandomState(seed) (CLI --policy-seed,
    default 0) - NEVER touches env.rng; the stream is reset at every
    episode start (t rewind detection, same trick MarlPolicy uses, since
    DNEnv.run does not call reset_episode explicitly).
    """

    name = "random"
    needs_solver = False

    def __init__(self, p_hold=0.3, seed=0, with_reference=False,
                 solver=None, tmp_dir=None):
        self.p_hold = float(p_hold)
        self.seed = int(seed)
        self._rng = None
        self._last_t = None

    def reset_episode(self):
        self._rng = np.random.RandomState(self.seed)
        self._last_t = None

    def act(self, env, t):
        dn = env.dn
        if self._rng is None or (self._last_t is not None and t <= self._last_t):
            self.reset_episode()          # new episode: rewind detected
        self._last_t = t
        actions = {}
        if env.pool <= 0 or t > dn.K - 2:
            return {i: None for i in range(dn.m)}, {
                "solved": True, "failed_agents": 0}
        pub = env.get_observation(0, t)["public"]
        for i in range(dn.m):
            obs = env.get_observation(i, t)
            own = obs["own"]
            legal = []
            for tr in obs["targets"]:
                if not tr["alive"]:
                    continue
                j, r = tr["id"], tr["r"]
                windows_left = math.ceil(r / pub["delta_d"] - 1e-9)
                if windows_left < 1:
                    continue
                d = own["d"][j]
                h = max(1, int(math.ceil(d / pub["v_m"] / pub["dt"] - 1e-9)))
                if h > windows_left:
                    continue
                legal.append(j)
            if legal and self._rng.random_sample() >= self.p_hold:
                actions[i] = legal[self._rng.randint(len(legal))]
            else:
                actions[i] = None
        return actions, {"solved": True, "failed_agents": 0}


# ----------------------------------------------------------------------
# policy 3: centralised myopic CPLEX (reference upper bound)
# ----------------------------------------------------------------------

class CplexPolicy(object):
    name = "cplex"
    needs_solver = True

    def __init__(self, solver=None, tmp_dir=None):
        """solver: dict(delta, timelimit, threads, python[, extra_args]).
        tmp_dir: directory for the per-step temp instance / solution files."""
        self.solver = solver or {"delta": 0.001, "timelimit": 60,
                                 "threads": 1,
                                 "python": wave_runner.DEFAULT_PYTHON}
        self.tmp_dir = tmp_dir or os.path.join("output", "tmp")

    def _write_step_instance(self, path, env, t):
        """Static sub-instance for the CURRENT joint state (mu = 1):

            m n 1 / w_j lines / p_eff(i, j, t) lines (local target ids)
        """
        dn = env.dn
        target_ids = env.visible_targets(t)
        out = ["%d %d %d" % (dn.m, len(target_ids), 1)]
        for j in target_ids:
            out.append(str(dn.w[j]))
        for i in range(dn.m):
            for local_j, j in enumerate(target_ids):
                out.append("%d %d %.12f" % (i, local_j, dn.p_eff(i, j, t)))
        with open(path, "w") as f:
            f.write("\n".join(out) + "\n")
        return target_ids

    def _solve(self, env, t):
        """One subprocess solve on the current state.

        Returns (assignment {i: j}, objective, solved, detail) where
        objective = optimal expected surviving value over visible targets
        (metric iii reference), assignment possibly {} when unsolved.
        """
        os.makedirs(self.tmp_dir, exist_ok=True)
        inst = os.path.join(self.tmp_dir, "dn_t%d_inst.txt" % t)
        sol = os.path.join(self.tmp_dir, "dn_t%d.sol" % t)
        if os.path.exists(sol):
            os.remove(sol)
        target_ids = self._write_step_instance(inst, env, t)

        rc, output, _wall = wave_runner.run_solver(
            inst, sol,
            delta=self.solver["delta"], timelimit=self.solver["timelimit"],
            threads=self.solver["threads"], python_exe=self.solver["python"],
            extra_args=self.solver.get("extra_args"))

        parsed = wave_runner.parse_wave_solution(inst, sol, target_ids)
        if parsed is None:
            return {}, None, False, ("no solution file (rc=%s) - hold fire "
                                     "this step" % rc)
        assignment = {}
        for j, per_i in parsed["assignment"].items():
            for i in per_i:
                assignment[i] = j  # mu = 1 -> at most one shot per (i, j)
        return assignment, parsed["objective"], True, None

    @staticmethod
    def _expected_surviving(env, t, assignment):
        """Expected surviving value over ALL visible targets under
        `assignment` ({i: j}) - same formula and inputs as env cost_all,
        so the reported objective matches what the environment scores
        (cplex policy gap == 0 by definition)."""
        dn = env.dn
        per_target = {}
        for i, j in assignment.items():
            per_target.setdefault(j, []).append(i)
        cost = 0.0
        for j in env.visible_targets(t):
            shooters = per_target.get(j)
            if shooters:
                surv = 1.0
                for i in shooters:
                    surv *= (1.0 - dn.p_eff(i, j, t))
                cost += dn.w[j] * surv
            else:
                cost += dn.w[j]
        return cost

    def act(self, env, t):
        dn = env.dn
        no_action = {i: None for i in range(dn.m)}
        if t > dn.K - 2:
            return no_action, {"solved": True, "failed_agents": 0}

        assignment, objective, solved, detail = self._solve(env, t)
        info = {"solved": solved, "detail": detail, "objective": objective}
        if not solved:
            info["failed_agents"] = dn.m
            return no_action, info
        info["failed_agents"] = 0

        # global-pool trimming: keep the best-shots the pool can still
        # cover, ranked by marginal expected destroyed value; re-score the
        # surviving plan so `objective` stays the pool-feasible optimum
        # (same resource budget any policy faces at this state)
        if len(assignment) > env.pool:
            per_target = {}
            for i, j in sorted(assignment.items()):
                per_target.setdefault(j, []).append(i)
            marginal = []
            for j, shooters in per_target.items():
                surv = 1.0
                for i in shooters:  # ascending platform id: deterministic
                    p = dn.p_eff(i, j, t)
                    marginal.append((dn.w[j] * surv * p, i, j))
                    surv *= (1.0 - p)
            marginal.sort(key=lambda x: (-x[0], x[1], x[2]))
            keep = set(i for _, i, _ in marginal[:max(env.pool, 0)])
            assignment = {i: j for i, j in assignment.items() if i in keep}
            objective = self._expected_surviving(env, t, assignment)
            info["objective"] = objective

        actions = {i: None for i in range(dn.m)}
        for i, j in assignment.items():
            actions[i] = j
        return actions, info


# ----------------------------------------------------------------------
# policy 4: partial-observation rolling CPLEX (E18 PO-CPLEX baseline)
# ----------------------------------------------------------------------

class POCplexPolicy(object):
    """PO-CPLEX: centralised rolling myopic optimum UNDER the spec §7
    information boundary (E18 baseline for the MARL gap analysis).

    Unlike CplexPolicy (which deliberately reads the full joint state via
    dn.p_eff / dn.w as the omniscient reference), POCplexPolicy rebuilds
    a BELIEF state from the union of the per-agent observations only:

        * alive targets / w / r / age  <- shared obs["targets"]
        * per-(i, j) base probability  <- own obs of platform i
        * per-(i, j) distance d_ij(t)  <- own obs of platform i
        * d0_ij  = d_ij(t) + delta_d * age_j(t)     (public closing
          dynamics, exactly the reconstruction GreedyPolicy uses)
        * p_eff_hat = min(pcap, p_ij * d0_ij / d_ij(t))
        * unreachable engagements (flight time h > windows left, or
          windows < 1, or t > K-2) carry p_eff_hat = 0

    It then solves the SAME single-wave MIP as CplexPolicy on the belief
    probabilities (untouched cplex/wta_cplex.py subprocess), applies the
    same global-pool marginal trimming, and executes the plan; the next
    step re-observes and re-solves (rolling / decision-time resolution).

    Information-boundary notes: reads only env.get_observation(i, t),
    env.dn static scenario constants (m/K/dt/delta_d/v_m/pcap mirrored
    in obs["public"]) and env.pool (the shared counter exposed as
    obs["pool"]); it NEVER touches env.rng, env.shots / env.inflight
    internals or env.destroyed_at (enforced by the e18 boundary unit
    test that runs it against a proxy env exposing only that surface).
    """

    name = "pocplex"
    needs_solver = True

    def __init__(self, solver=None, tmp_dir=None, with_reference=False):
        self.solver = solver or {"delta": 0.001, "timelimit": 60,
                                 "threads": 1,
                                 "python": wave_runner.DEFAULT_PYTHON}
        self.tmp_dir = tmp_dir or os.path.join("output", "tmp")
        self.with_reference = with_reference
        self._ref = CplexPolicy(solver, tmp_dir) if with_reference else None

    # ---- belief-state reconstruction (obs-only) -----------------------
    def _rebuild(self, env, t):
        """Returns (target_ids, w_by_id, p_hat[(i, j)]) from the union of
        per-agent observations; p_hat is 0 for infeasible pairs."""
        dn = env.dn
        obs0 = env.get_observation(0, t)
        pub = obs0["public"]
        targets = [tr for tr in obs0["targets"] if tr["alive"]]
        ids = [tr["id"] for tr in targets]
        by_id = {tr["id"]: tr for tr in targets}
        w = {j: by_id[j]["w"] for j in ids}
        pool = obs0["pool"]
        p_hat = {}
        for i in range(dn.m):
            obs_i = env.get_observation(i, t)
            own = obs_i["own"]
            for j in ids:
                d = own["d"][j]
                age = by_id[j]["age"]
                r = by_id[j]["r"]
                windows = math.ceil(r / pub["delta_d"] - 1e-9)
                if d <= 0.0:
                    p = pub["pcap"]                 # defensive guard
                else:
                    d0 = d + pub["delta_d"] * age
                    p = min(pub["pcap"], own["p"][j] * d0 / d)
                h = max(1, int(math.ceil(
                    d / pub["v_m"] / pub["dt"] - 1e-9)))
                if t > dn.K - 2 or windows < 1 or h > windows or pool <= 0:
                    p = 0.0
                p_hat[(i, j)] = max(0.0, p)
        return ids, w, p_hat, pool

    # ---- MIP on the belief state (untouched solver subprocess) --------
    def _write_belief_instance(self, path, env, t, ids, w, p_hat):
        dn = env.dn
        out = ["%d %d %d" % (dn.m, len(ids), 1)]
        for j in ids:
            out.append(str(w[j]))
        for i in range(dn.m):
            for local_j, j in enumerate(ids):
                out.append("%d %d %.12f" % (i, local_j, p_hat[(i, j)]))
        with open(path, "w") as f:
            f.write("\n".join(out) + "\n")

    def _solve_belief(self, env, t, ids, w, p_hat):
        os.makedirs(self.tmp_dir, exist_ok=True)
        inst = os.path.join(self.tmp_dir, "po_t%d_inst.txt" % t)
        sol = os.path.join(self.tmp_dir, "po_t%d.sol" % t)
        if os.path.exists(sol):
            os.remove(sol)
        self._write_belief_instance(inst, env, t, ids, w, p_hat)
        rc, output, _wall = wave_runner.run_solver(
            inst, sol,
            delta=self.solver["delta"], timelimit=self.solver["timelimit"],
            threads=self.solver["threads"],
            python_exe=self.solver["python"],
            extra_args=self.solver.get("extra_args"))
        parsed = wave_runner.parse_wave_solution(inst, sol, ids)
        if parsed is None:
            return {}, None, False
        assignment = {}
        for j, per_i in parsed["assignment"].items():
            for i in per_i:
                assignment[i] = j
        return assignment, parsed["objective"], True

    # ------------------------------------------------------------------
    def act(self, env, t):
        dn = env.dn
        no_action = {i: None for i in range(dn.m)}
        info = {"solved": True, "failed_agents": 0}
        if t > dn.K - 2:
            return no_action, info
        ids, w, p_hat, pool = self._rebuild(env, t)
        if not ids or pool <= 0:
            return no_action, info

        assignment, objective, solved = self._solve_belief(
            env, t, ids, w, p_hat)
        info["solved"] = solved
        info["objective"] = objective
        if not solved:
            info["failed_agents"] = dn.m
            return no_action, info

        # global-pool trimming on the BELIEF marginals (same recipe as
        # CplexPolicy, deterministic under ascending platform id)
        if len(assignment) > pool:
            per_target = {}
            for i, j in sorted(assignment.items()):
                per_target.setdefault(j, []).append(i)
            marginal = []
            for j, shooters in per_target.items():
                surv = 1.0
                for i in shooters:
                    p = p_hat[(i, j)]
                    marginal.append((w[j] * surv * p, i, j))
                    surv *= (1.0 - p)
            marginal.sort(key=lambda x: (-x[0], x[1], x[2]))
            keep = set(i for _, i, _ in marginal[:max(pool, 0)])
            assignment = {i: j for i, j in assignment.items()
                          if i in keep}

        actions = {i: None for i in range(dn.m)}
        for i, j in assignment.items():
            actions[i] = j
        if self._ref is not None:
            _, ref_info = self._ref.act(env, t)
            info["reference_cost"] = ref_info.get("objective")
            info["reference_solved"] = ref_info.get("solved", False)
            info["detail"] = ref_info.get("detail")
        return actions, info


# ----------------------------------------------------------------------
# policy 5: receding-horizon (H=2) rolling CPLEX (E23 RH-CPLEX baseline)
# ----------------------------------------------------------------------

class RHCplexPolicy(POCplexPolicy):
    """RH-CPLEX: 2-step receding-horizon lookahead under the spec §7
    information boundary (B3).

    Route (i) - virtual-platform expansion, solver untouched: at each
    decision step t the belief is rebuilt EXACTLY like POCplexPolicy
    (union of per-agent observations, public-dynamics d0 reconstruction);
    the H=2 planning MIP with decision variables x[i, j, s], s in
    {t, t+1} is encoded as a single-wave instance by expanding every
    (platform i, slot s) pair into a virtual platform

        i' = i * H + s        (m' = m * H virtual platforms, header
                               "m' L 1" i.e. mu = 1 shot per virtual
                               platform = at most one shot per
                               (platform, slot)),

    slot-t+1 quantities extrapolated deterministically along the public
    dynamics (d_ij(t+1) = max(0, d_ij(t) - delta_d),
    r_j(t+1) = max(0, r_j(t) - delta_d), age+1 -> SAME d0, p_eff(t+1)
    = min(pcap, p * d0 / d(t+1))); pairs unreachable at t+1 (windows<1,
    h > windows, slot beyond the decision horizon K-2) carry p = 0.

    The GLOBAL POOL constraint is NOT in the MIP (keeps the solver at
    zero changes); when the plan exceeds env.pool the same
    marginal-value deterministic trimming as POCplexPolicy applies,
    ranked on (platform i, slot s) lexicographic order (== ascending
    virtual-platform id). Only the s = t slice of the surviving plan is
    EXECUTED; the next step re-observes and re-plans (receding horizon).

    Information boundary: identical surface to POCplexPolicy (union of
    get_observation(i, t), env.pool, static scenario constants via
    obs["public"]); never touches env.rng / env.shots / env.inflight /
    env.destroyed_at (covered by the e18-style proxy-env boundary test).
    """

    name = "rh-cplex"
    needs_solver = True
    H = 2

    # ---- 2-slot belief (slot t rebuilt by POCplexPolicy._rebuild) ------
    def _rebuild_horizon(self, env, t):
        """Returns (ids, w, p2, pool); p2[(i, s, j)] = belief probability
        that platform i firing at target j in slot s (s = 0 -> now,
        s = 1 -> one step later) destroys it; 0 for infeasible pairs."""
        dn = env.dn
        ids, w, p_hat, pool = POCplexPolicy._rebuild(self, env, t)
        p2 = {}
        obs0 = env.get_observation(0, t)
        pub = obs0["public"]
        by_id = {tr["id"]: tr for tr in obs0["targets"] if tr["alive"]}
        for i in range(dn.m):
            own = env.get_observation(i, t)["own"]
            for j in ids:
                # ---- slot 0: rebuilt belief as-is ----------------------
                p2[(i, 0, j)] = p_hat[(i, j)]
                # ---- slot 1: deterministic public-dynamics projection --
                if t + 1 > dn.K - 2:
                    p2[(i, 1, j)] = 0.0
                    continue
                tr = by_id[j]
                d = own["d"][j]
                age = tr["age"]
                d0 = d + pub["delta_d"] * age      # same d0 as slot 0
                d1 = max(0.0, d - pub["delta_d"])
                r1 = max(0.0, tr["r"] - pub["delta_d"])
                windows1 = math.ceil(r1 / pub["delta_d"] - 1e-9)
                if windows1 < 1 or pool <= 0:
                    p2[(i, 1, j)] = 0.0
                    continue
                if d1 <= 0.0:
                    p = pub["pcap"]                 # defensive guard
                else:
                    p = min(pub["pcap"], own["p"][j] * d0 / d1)
                h1 = max(1, int(math.ceil(
                    d1 / pub["v_m"] / pub["dt"] - 1e-9)))
                if h1 > windows1:
                    p2[(i, 1, j)] = 0.0
                    continue
                p2[(i, 1, j)] = max(0.0, p)
        return ids, w, p2, pool

    # ---- expanded single-wave instance for the untouched solver --------
    def _write_horizon_instance(self, path, ids, w, p2, m):
        """m' = m*H virtual platforms (i' = i*H + s), L targets, mu = 1;
        p2[(i, s, j)] probabilities with 0 for infeasible pairs."""
        out = ["%d %d %d" % (m * self.H, len(ids), 1)]
        for j in ids:
            out.append(str(w[j]))
        for i in range(m):
            for s in range(self.H):
                for local_j, j in enumerate(ids):
                    out.append("%d %d %.12f" % (
                        i * self.H + s, local_j, p2[(i, s, j)]))
        with open(path, "w") as f:
            f.write("\n".join(out) + "\n")

    def _solve_horizon(self, t, m, ids, w, p2):
        os.makedirs(self.tmp_dir, exist_ok=True)
        inst = os.path.join(self.tmp_dir, "rh_t%d_inst.txt" % t)
        sol = os.path.join(self.tmp_dir, "rh_t%d.sol" % t)
        if os.path.exists(sol):
            os.remove(sol)
        self._write_horizon_instance(inst, ids, w, p2, m)
        rc, output, _wall = wave_runner.run_solver(
            inst, sol,
            delta=self.solver["delta"], timelimit=self.solver["timelimit"],
            threads=self.solver["threads"],
            python_exe=self.solver["python"],
            extra_args=self.solver.get("extra_args"))
        parsed = wave_runner.parse_wave_solution(inst, sol, ids)
        if parsed is None:
            return {}, None, False
        assignment = {}                      # {virtual i': j}
        for j, per_i in parsed["assignment"].items():
            for ip in per_i:
                assignment[ip] = j
        return assignment, parsed["objective"], True

    # ------------------------------------------------------------------
    def act(self, env, t):
        dn = env.dn
        no_action = {i: None for i in range(dn.m)}
        info = {"solved": True, "failed_agents": 0}
        if t > dn.K - 2:
            return no_action, info
        ids, w, p2, pool = self._rebuild_horizon(env, t)
        if not ids or pool <= 0:
            return no_action, info

        assignment, objective, solved = self._solve_horizon(
            t, dn.m, ids, w, p2)
        info["solved"] = solved
        info["objective"] = objective
        if not solved:
            info["failed_agents"] = dn.m
            return no_action, info

        # global-pool trimming on BELIEF marginals; ascending virtual id
        # == (platform i, slot s) lexicographic (deterministic)
        if len(assignment) > pool:
            per_target = {}
            for ip, j in sorted(assignment.items()):
                per_target.setdefault(j, []).append(ip)
            marginal = []
            for j, shooters in per_target.items():
                surv = 1.0
                for ip in shooters:
                    p = p2[(ip // self.H, ip % self.H, j)]
                    marginal.append((w[j] * surv * p, ip, j))
                    surv *= (1.0 - p)
            marginal.sort(key=lambda x: (-x[0], x[1], x[2]))
            keep = set(ip for _, ip, _ in marginal[:max(pool, 0)])
            assignment = {ip: j for ip, j in assignment.items()
                          if ip in keep}

        # execute only the s = t slice (even virtual ids)
        actions = {i: None for i in range(dn.m)}
        for ip, j in assignment.items():
            if ip % self.H == 0:
                actions[ip // self.H] = j
        if self._ref is not None:
            _, ref_info = self._ref.act(env, t)
            info["reference_cost"] = ref_info.get("objective")
            info["reference_solved"] = ref_info.get("solved", False)
            info["detail"] = ref_info.get("detail")
        return actions, info


# ----------------------------------------------------------------------
# registry
# ----------------------------------------------------------------------

def build_policy(name, solver=None, tmp_dir=None, with_reference=False,
                 model_path=None, device="auto", p_hold=None,
                 policy_seed=0):
    if name == "none":
        return NonePolicy()
    if name == "greedy":
        return GreedyPolicy(with_reference=with_reference, solver=solver,
                            tmp_dir=tmp_dir)
    if name == "greedy_threat":
        return GreedyVariantPolicy(
            score_mode="threat", with_reference=with_reference,
            solver=solver, tmp_dir=tmp_dir)
    if name == "greedy_nearest":
        return GreedyVariantPolicy(
            score_mode="nearest", with_reference=with_reference,
            solver=solver, tmp_dir=tmp_dir)
    if name == "random":
        return RandomPolicy(
            p_hold=0.3 if p_hold is None else p_hold, seed=policy_seed,
            with_reference=with_reference, solver=solver, tmp_dir=tmp_dir)
    if name == "cplex":
        return CplexPolicy(solver, tmp_dir)
    if name == "pocplex":
        return POCplexPolicy(solver, tmp_dir,
                             with_reference=with_reference)
    if name == "rh-cplex":
        return RHCplexPolicy(solver, tmp_dir,
                             with_reference=with_reference)
    if name == "marl":
        from marl.policy import MarlPolicy
        return MarlPolicy(model_path=model_path, device=device,
                          greedy=True, seed=0, with_reference=with_reference,
                          solver=solver, tmp_dir=tmp_dir)
    if name in ("mappo", "qmix", "iql"):
        from marl.baseline_policy import PoolMLPPolicy
        return PoolMLPPolicy(policy_kind=name, model_path=model_path,
                             device=device, with_reference=with_reference,
                             solver=solver, tmp_dir=tmp_dir)
    raise ValueError("unknown DN policy: %r (expected none/greedy/"
                     "greedy_threat/greedy_nearest/random/cplex/pocplex/"
                     "rh-cplex/marl/mappo/qmix/iql)" % name)
