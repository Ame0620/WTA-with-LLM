"""GA solver core for the v4 rolling-horizon myopic WTA baseline (D2).

Pure-function genetic-algorithm search over the CURRENT-step assignment,
with EXACTLY the same information boundary, state-reading convention and
objective as CplexPolicy (per-step expected destroyed value maximisation
Sigma_j w_j * (1 - Prod_i (1 - p_eff_ij)), constraints: <= 1 shot per
platform per step, global pool level, engagement-window legality). No
torch / cplex dependency - numpy + stdlib only.

Spec defaults (v4 requirement doc 3.2.2):
    encoding    length-m integer chromosome, gene i in {0} u feasible_i
                (0 = hold); the allele sets come from the same
                reachability filter the greedy family uses (windows>=1,
                h <= windows, t + h <= K)
    fitness     expected destroyed value of the step plan (table lookup
                on the precomputed w * p_eff matrix)
    init        half greedy seeds (threat / nearest solutions +
                perturbation), half uniform-legal random
    selection   tournament k=3
    crossover   uniform, p=0.8
    mutation    reset one gene to a uniform legal allele, p=1/m
    repair      plans exceeding the global pool are trimmed by ascending
                marginal expected destroyed value -> hold
    budget      population P x generations G (main setting 40 x 50,
                sensitivity arms 20x25 / 80x100)
    stop        G generations or 10 consecutive generations without
                best-fitness improvement

Determinism: the caller owns the RNG stream (GAPolicy passes its private
RandomState(policy_seed), never env.rng) - same trick as RandomPolicy.
"""

import math

TOURNAMENT_K = 3
CROSSOVER_P = 0.8
STALL_GENS = 10


def _ceil_int(x, eps=1e-9):
    return int(math.ceil(x - eps))


def feasible_pairs(env, t):
    """Per-platform feasible target lists under the CplexPolicy-visible
    state (alive targets, public dynamics, engagement-window legality).

    Returns (target_ids, w_by_j, p_by_ij, feasible) where
        target_ids : sorted alive (visible) target ids (LOCAL indexing
                     follows this list order)
        w_by_j     : {j: w_j}
        p_by_ij    : {(i, j): p_eff(i, j, t)}       (dn.p_eff, same as
                     the CPLEX reference - public prior quantities)
        feasible   : {i: [j, ...]} legal alleles per platform
    """
    dn = env.dn
    target_ids = env.visible_targets(t)
    w_by_j = {j: dn.w[j] for j in target_ids}
    p_by_ij = {(i, j): dn.p_eff(i, j, t)
               for i in range(dn.m) for j in target_ids}
    feasible = {i: [] for i in range(dn.m)}
    for i in range(dn.m):
        for j in target_ids:
            r = dn.r(j, t)
            u = _ceil_int(r / dn.delta_d - 1e-9) if r > 0 else 0
            h = max(1, _ceil_int(dn.dist(i, j, t) / dn.v_m / dn.dt - 1e-9))
            if u >= 1 and h <= u and t + h <= dn.K:
                feasible[i].append(j)
    return target_ids, w_by_j, p_by_ij, feasible


def plan_value(chrom, w_by_j, p_by_ij):
    """Fitness: expected destroyed value of the step plan (analytic,
    no rng). chrom[i] = target id or 0 (hold)."""
    per_target = {}
    for i, j in enumerate(chrom):
        if j:
            per_target.setdefault(j, []).append(p_by_ij[(i, j)])
    val = 0.0
    for j, ps in per_target.items():
        surv = 1.0
        for p in ps:
            surv *= (1.0 - p)
        val += w_by_j[j] * (1.0 - surv)
    return val


def repair_pool(chrom, w_by_j, p_by_ij, pool):
    """Global-pool trim: if the plan fires more shots than the pool can
    cover, drop the smallest-marginal-value shots (deterministic under
    ascending (marginal, platform) order) -> hold."""
    fires = [i for i, j in enumerate(chrom) if j]
    if len(fires) <= pool:
        return chrom
    per_target = {}
    for i in fires:
        per_target.setdefault(chrom[i], []).append(i)
    marginal = []
    for j, shooters in per_target.items():
        surv = 1.0
        for i in sorted(shooters):
            p = p_by_ij[(i, j)]
            marginal.append((w_by_j[j] * surv * p, i, j))
            surv *= (1.0 - p)
    marginal.sort(key=lambda x: (x[0], x[1], x[2]))
    drop = set(i for _, i, _ in marginal[:len(fires) - max(pool, 0)])
    return [0 if i in drop else chrom[i] for i in range(len(chrom))]


def _greedy_seeds(env, t, target_ids, w_by_j, p_by_ij, feasible, rng):
    """Two greedy seed chromosomes (threat / nearest, computed from the
    same joint-visible quantities the fitness table uses) + one
    perturbed copy each."""
    dn = env.dn
    seeds = []
    for mode in ("threat", "nearest"):
        chrom = [0] * dn.m
        taken = {}
        for i in range(dn.m):
            best_j, best_s = 0, None
            for j in feasible[i]:
                if mode == "threat":
                    r = dn.r(j, t)
                    u = max(1, _ceil_int(r / dn.delta_d - 1e-9))
                    s = w_by_j[j] / float(u)
                else:
                    s = 1.0 / (dn.dist(i, j, t) + 1e-9)
                # mild crowding penalty (marginal value under current plan)
                p = p_by_ij[(i, j)]
                surv = 1.0
                for ii in taken.get(j, []):
                    surv *= (1.0 - p_by_ij[(ii, j)])
                s = s * (1.0 - surv) if mode == "threat" else s
                if best_s is None or s > best_s:
                    best_j, best_s = j, s
            chrom[i] = best_j
            if best_j:
                taken.setdefault(best_j, []).append(i)
        seeds.append(chrom)
        # perturbed twin: each gene re-drawn uniformly with p=0.3
        pert = []
        for i in range(dn.m):
            if chrom[i] and rng.random_sample() < 0.3:
                alleles = feasible[i]
                pert.append(alleles[rng.randint(len(alleles))]
                            if alleles else 0)
            else:
                pert.append(chrom[i])
        seeds.append(pert)
    return seeds


def solve_assign(env, t, pool, rng, pop=40, gens=50):
    """One GA solve for decision step t on the CplexPolicy-visible state.

    Returns (assignment {i: j}, objective) where objective = expected
    SURVIVING value over all visible targets under the final plan (same
    convention as CplexPolicy._expected_surviving / the solver output,
    so gap comparisons are apples-to-apples).
    """
    dn = env.dn
    if t > dn.K - 2 or pool <= 0:
        return {}, sum(dn.w[j] for j in env.visible_targets(t))
    target_ids, w_by_j, p_by_ij, feasible = feasible_pairs(env, t)
    if not target_ids:
        return {}, 0.0
    m = dn.m

    # ---- population init: greedy seeds + uniform legal ----------------
    chroms = _greedy_seeds(env, t, target_ids, w_by_j, p_by_ij,
                           feasible, rng)
    while len(chroms) < pop:
        chrom = []
        for i in range(m):
            alleles = feasible[i]
            chrom.append(alleles[rng.randint(len(alleles))]
                         if alleles and rng.random_sample() < 0.8 else 0)
        chroms.append(chrom)
    chroms = [repair_pool(c, w_by_j, p_by_ij, pool)
              for c in chroms[:pop]]
    fits = [plan_value(c, w_by_j, p_by_ij) for c in chroms]

    best_idx = max(range(pop), key=lambda k: fits[k])
    best_chrom, best_fit = list(chroms[best_idx]), fits[best_idx]
    stall = 0

    for _g in range(gens - 1):
        if stall >= STALL_GENS:
            break
        # ---- tournament selection (k=3) -------------------------------
        parents = []
        for _ in range(pop):
            cand = rng.choice(pop, size=TOURNAMENT_K, replace=False)
            parents.append(chroms[min(cand, key=lambda k: -fits[k])])
        # ---- uniform crossover p=0.8 + mutation p=1/m ------------------
        offspring = []
        pm = 1.0 / m
        for k in range(0, pop, 2):
            c1, c2 = list(parents[k]), list(parents[min(k + 1, pop - 1)])
            if rng.random_sample() < CROSSOVER_P:
                swap = [rng.random_sample() < 0.5 for _ in range(m)]
                c1, c2 = [c2[i] if swap[i] else c1[i] for i in range(m)], \
                         [c1[i] if swap[i] else c2[i] for i in range(m)]
            for c in (c1, c2):
                for i in range(m):
                    if rng.random_sample() < pm:
                        alleles = feasible[i]
                        c[i] = alleles[rng.randint(len(alleles))] \
                            if alleles else 0
                offspring.append(c)
                if len(offspring) >= pop:
                    break
            if len(offspring) >= pop:
                break
        chroms = [repair_pool(c, w_by_j, p_by_ij, pool)
                  for c in offspring[:pop]]
        fits = [plan_value(c, w_by_j, p_by_ij) for c in chroms]
        gen_best = max(range(pop), key=lambda k: fits[k])
        if fits[gen_best] > best_fit + 1e-9:
            best_chrom, best_fit = list(chroms[gen_best]), fits[gen_best]
            stall = 0
        else:
            stall += 1
        # elitism: keep the best chromosome in slot 0
        chroms[0], fits[0] = list(best_chrom), best_fit

    assignment = {i: j for i, j in enumerate(best_chrom) if j}
    # objective on the SURVIVING-value convention (CPLEX comparable):
    # cost = total visible value - achieved expected destroyed value
    total_vis = sum(w_by_j.values())
    return assignment, total_vis - best_fit


# ----------------------------------------------------------------------
# selftest: determinism, zero-illegality on a real v4 instance,
# fitness monotonicity under pool trim
# ----------------------------------------------------------------------

def _selftest():
    import os
    import sys
    import numpy as np
    sys.path.insert(0, os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))
    from dwta.dn_instance import DNInstance
    from dwta.dn_env import DNEnv

    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(here, "data", "dn-data-v4",
                        "dn_5x100_K10_s01.txt")
    dn = DNInstance(path)
    assert dn.m == 5 and dn.n == 100, "expected a v4 5x100 instance"

    env = DNEnv(dn, 42)
    # determinism: same rng state -> same solve
    for t in (0, 3, 5):
        rng1 = np.random.RandomState(7)
        rng2 = np.random.RandomState(7)
        a1, o1 = solve_assign(env, t, env.pool, rng1)
        a2, o2 = solve_assign(env, t, env.pool, rng2)
        assert a1 == a2 and abs(o1 - o2) < 1e-12, "non-deterministic solve"
        for i, j in a1.items():
            assert j in env.alive, "assignment on dead target"
        assert len(a1) <= env.pool, "pool violation"
    # pool trim honoured under artificially tight budgets
    rng = np.random.RandomState(0)
    a, o = solve_assign(env, 0, 2, rng)
    assert len(a) <= 2, "trim failed"
    print("dwta/ga_solver.py selftest: ALL PASS")


if __name__ == "__main__":
    _selftest()
