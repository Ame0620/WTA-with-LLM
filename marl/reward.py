"""M5: per-step team reward, potential shaping and kill credit.

All events are read from the post-run DNEnv object and run_rec (zero env
changes). Normalisation base = dyn.total_value().

    R(t) = sum_{breakthrough/end leak @t} (-w_j/total)
         + sum_{kills settled @t}        (+w_j/total)
         - c_invalid * |{invalid settlements @t}|

    R'(t) = R(t) + 0.99 * Phi(s_{t+1}) - Phi(s_t)
    Phi(s) = -sum_{j alive} w_j * pbar_j / total,  Phi(terminal) = 0
    pbar_j(t) = 1 - prod(1 - p_shot) over in-flight interceptors on j
    (in-flight set = shots with t_fire <= t < t_hit, i.e. including this
    step's launches - training-side global information, critic-scope).

Credit attribution - E15-A3 (proportional p_shot split, replaces the e14
killer-takes-all booking):
    For each kill event (t_kill, j) the +w_j/total credit is split over
    the interceptors still in flight toward j at settlement time (the
    killer included, i.e. t_fire <= t_kill <= t_hit), EXCLUDING shots
    whose own outcome is 'invalid' (a duplicate-kill or dead-target shot
    never contributed a live probability, so it receives no share - this
    is what the A3 spec assertions pin down). Each interceptor's share

        kill_credit_k = (w_j / total) * p_shot_k / sum_{k' in pool} p_shot_k

    is booked at ITS OWN firing slot (t_fire_k, i_k) - the e14 credit
    key semantics are unchanged, so downstream credit.get((t, i))
    matching in process_batch needs no edits. A lone killer therefore
    receives the full w_j/total exactly as e14 did; misses/invalid
    settlements produce no credit events of their own.

Reconciliation (selftest-asserted):
    * sum_t R_team == (destroyed_value - leak_value) / total   < 1e-9
    * kill-shot count == len(env.destroyed_at)
    * credit keys subset of env.shots (t_fire, i) keys
    * sum(credit) == destroyed_value / total   (A3 split conserves mass)
    * no 'invalid' shot is ever credited by any kill pool        (A3)
"""

import torch

C_INVALID = 0.01        # per invalid settlement (locked, 0.005-0.05)
GAMMA_SHAPE = 0.99


def build_rewards(env, run_rec: dict, dyn,
                  c_invalid: float = C_INVALID,
                  credit_mode: str = "credit_kill",
                  phi_sign: float = -1.0,
                  use_eaps: bool = True,
                  phi_scale: float = 1.0) -> dict:
    """phi_sign: -1 (default, historical) gives Phi = -sum w*pbar (launch
    steps receive a negative kick); +1 flips the potential sign (E15-A3
    alternative 1: launch steps get an immediate positive kick) - used
    only as the A0-triggered pos control arm after e16 picks c*.

    use_eaps (v5 ablation switch): True (default, bit-identical to the
    historical path) applies the potential shaping term; False skips the
    Phi construction entirely and sets R_shaped = R_team (the base event
    sequence is fully preserved; closing EAPS by flipping/zeroing
    phi_sign is FORBIDDEN per the ablation spec R7).

    phi_scale (r2 recalibration lambda): multiplies the shaping term
    R_shaped = R_team + phi_scale * phi_sign * (gamma*Phi' - Phi)
    strictly INSIDE the use_eaps branch; phi_scale with use_eaps=0 is a
    no-op (E2 gate) and phi_scale=1.0 keeps the pre-r2 path
    bit-identical (x*1.0 == x exactly in IEEE754)."""
    total = float(dyn.total_value())
    K = dyn.K
    steps = K + 1                                  # t = 0..K

    # ---- raw event streams from the post-run env ----------------------
    kills_at = {}                                  # t -> value sum
    for j, t in env.destroyed_at.items():
        kills_at[t] = kills_at.get(t, 0.0) + dyn.w[j]
    leak_at = {}                                   # t -> value sum
    for j, (t, _cause) in env.leaked_at.items():
        leak_at[t] = leak_at.get(t, 0.0) + dyn.w[j]
    invalid_at = {}                                # t -> count
    for ev in env.shots:
        if ev.get("outcome") == "invalid":
            t = ev["t_hit"]
            invalid_at[t] = invalid_at.get(t, 0) + 1

    R_team = torch.zeros(steps, dtype=torch.float64)
    R_pure = torch.zeros(steps, dtype=torch.float64)   # no invalid penalty
    for t in range(steps):
        r = 0.0
        r -= leak_at.get(t, 0.0) / total
        r += kills_at.get(t, 0.0) / total
        R_pure[t] = r
        R_team[t] = r - c_invalid * invalid_at.get(t, 0)

    # ---- potential Phi(t): state AFTER step t's events ----------------
    # replay alive set + in-flight set from the recorded outcomes.
    # EAPS off: the Phi construction itself is REMOVED from the training
    # signal (audit A-2) - it is not computed at all and R_shaped equals
    # the base event sequence below.
    Phi = torch.zeros(steps + 1, dtype=torch.float64)   # Phi[steps] = terminal = 0
    if use_eaps:
        alive = set()
        fired = sorted(env.shots, key=lambda e: (e["t_fire"], e["i"]))
        for t in range(steps):
            for j in dyn.targets_arriving(t):
                alive.add(j)
            alive.discard(None)
            # remove destroyed / leaked at t
            for j, td in env.destroyed_at.items():
                if td == t:
                    alive.discard(j)
            for j, (tl, _c) in env.leaked_at.items():
                if tl == t:
                    alive.discard(j)
            # in-flight including this step's launches (t_fire <= t < t_hit)
            phi = 0.0
            for j in list(alive):
                p_surv = 1.0
                for ev in fired:
                    if ev["j"] == j and ev["t_fire"] <= t < ev["t_hit"]:
                        p_surv *= (1.0 - ev["p_shot"])
                pbar = 1.0 - p_surv
                if pbar > 0.0:
                    phi -= dyn.w[j] * pbar / total
            Phi[t] = phi

        R_shaped = torch.zeros(steps, dtype=torch.float64)
        for t in range(steps):
            nxt = Phi[t + 1] if t + 1 <= steps else 0.0
            R_shaped[t] = R_team[t] \
                + phi_scale * phi_sign * (GAMMA_SHAPE * nxt - Phi[t])
    else:
        # EAPS off: no potential-difference term at all (R_shaped IS the
        # base event sequence; Phi stays identically zero)
        R_shaped = R_team.clone()

    # ---- credit attribution (E15-A3) -----------------------------------
    # Proportional p_shot split over the in-flight pool at kill time;
    # 'credit_kill_cf' is an accepted alias (dummy compatibility mode -
    # identical semantics). See module docstring for the exact pool rule.
    credit = {}
    for ev in env.shots:
        if ev.get("outcome") != "kill":
            continue
        j, t_kill = ev["j"], ev["t_hit"]
        val = dyn.w[j] / total
        pool = [e for e in env.shots
                if e["j"] == j and e["t_fire"] <= t_kill
                and e["t_hit"] >= t_kill
                and e.get("outcome") != "invalid"]
        psum = sum(e["p_shot"] for e in pool)
        if psum <= 0.0:                              # degenerate guard
            key = (ev["t_fire"], ev["i"])
            credit[key] = credit.get(key, 0.0) + val
            continue
        for e in pool:
            key = (e["t_fire"], e["i"])
            credit[key] = credit.get(key, 0.0) + val * e["p_shot"] / psum

    shots_detail = [dict(ev) for ev in env.shots]

    return {
        "R_team": R_team,
        "R_pure": R_pure,
        "R_shaped": R_shaped,
        "credit": credit,
        "shots_detail": shots_detail,
    }


# ----------------------------------------------------------------------
# selftest: offline replay reconciliation on real episodes
# ----------------------------------------------------------------------

def _selftest(instances):
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from dwta.dn_instance import DNInstance
    from dwta.dn_env import DNEnv
    from dwta.dn_policies import build_policy

    total_checks = 0
    for path in instances:
        dn = DNInstance(path)
        for seed in (42, 43):
            env = DNEnv(dn, seed)
            pol = build_policy("greedy")
            run_rec = env.run(pol)
            out = build_rewards(env, run_rec, dn)
            total_val = float(dn.total_value())
            lhs = float(out["R_pure"].sum())
            rhs = (run_rec["destroyed_value"] - run_rec["leak_value"]) \
                / total_val
            err = abs(lhs - rhs)
            assert err < 1e-9, "reconciliation error %g on %s seed %d" \
                % (err, path, seed)
            n_kills = sum(1 for s in out["shots_detail"]
                          if s.get("outcome") == "kill")
            assert n_kills == len(env.destroyed_at), "kill count mismatch"
            valid_keys = {(s["t_fire"], s["i"]) for s in env.shots}
            assert set(out["credit"]).issubset(valid_keys), "credit leak"
            # ---- A3 assertions --------------------------------------
            # (a) mass conservation: split pools still book exactly the
            #     killed value (a lone killer gets the full w_j/total)
            cred_sum = sum(out["credit"].values())
            kills_val = sum(dn.w[j] for j in env.destroyed_at) / total_val
            assert abs(cred_sum - kills_val) < 1e-9, \
                "A3 credit mass off by %g" % abs(cred_sum - kills_val)
            # (b) full replay cross-check: proportional p_shot split over
            #     the in-flight pool, invalid shots excluded -> implies
            #     duplicate-kill / dead-target shots earn zero credit
            replay = {}
            for ev in env.shots:
                if ev.get("outcome") != "kill":
                    continue
                pool = [e for e in env.shots
                        if e["j"] == ev["j"]
                        and e["t_fire"] <= ev["t_hit"]
                        and e["t_hit"] >= ev["t_hit"]
                        and e.get("outcome") != "invalid"]
                psum = sum(e["p_shot"] for e in pool)
                val = dn.w[ev["j"]] / total_val
                if psum <= 0:
                    k0 = (ev["t_fire"], ev["i"])
                    replay[k0] = replay.get(k0, 0.0) + val
                    continue
                for e in pool:
                    k0 = (e["t_fire"], e["i"])
                    replay[k0] = replay.get(k0, 0.0) \
                        + val * e["p_shot"] / psum
            assert set(replay) == set(out["credit"]), "A3 key mismatch"
            for k0 in replay:
                assert abs(replay[k0] - out["credit"][k0]) < 1e-9, \
                    "A3 share mismatch at %s" % (k0,)
            total_checks += 1
            print("  %s seed %d: R_team sum=%.6f reconciled (err %.2e), "
                  "kills=%d, credit slots=%d"
                  % (os.path.basename(path), seed, lhs, err, n_kills,
                     len(out["credit"])))
    print("marl/reward.py selftest: ALL PASS (%d episodes)" % total_checks)


if __name__ == "__main__":
    import argparse
    import os
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--instances", default=None)
    args = ap.parse_args()
    if args.selftest:
        insts = [p.strip() for p in args.instances.split(",")] \
            if args.instances else []
        if not insts:
            raise SystemExit("--selftest requires --instances")
        _selftest(insts)
    else:
        print("use --selftest --instances <files>")
