"""e50 entry: dn_family_eval with a cross-arm CPLEX reference cache.

Thin wrapper around experiments/dn_family_eval.py (NOT modified): before
delegating to its main(), it monkey-patches
dwta.dn_policies.CplexPolicy._solve so that

  * the per-step MIP instance written to tmp (dn_t< t>_inst.txt) is hashed
    (md5 over file bytes + solver config) into a persistent cache dir
    output/_cplex_ref_cache/<key>.sol;
  * cache HIT  -> the cached .sol is copied into tmp (fresh mtime, so the
    freshness gate in the original logic passes) and NO subprocess solve;
  * cache MISS -> the original subprocess solve runs and any successful
    .sol is stored into the cache.

The cache is sound because the step MIP text fully determines the solve
(same instance bytes + same solver settings => same optimum); different
joint states (visible target set / p_eff) hash differently, so no cross-
policy contamination is possible. Reference solutions therefore only get
reused when an arm reaches the exact same state at the same kind of step.

Usage (identical CLI to dn_family_eval.py):
  /opt/anaconda3/envs/wta/bin/python experiments/e50_eval_entry.py <args...>
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from dwta import dn_policies, wave_runner  # noqa: E402

CACHE_DIR = os.path.join(HERE, "output", "_cplex_ref_cache")
STATS = {"hit": 0, "miss": 0, "store": 0}

_orig_solve = dn_policies.CplexPolicy._solve


def _cache_key(inst_path, solver):
    h = hashlib.md5()
    with open(inst_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    cfg = "delta=%s|tl=%s|thr=%s" % (solver.get("delta"),
                                     solver.get("timelimit"),
                                     solver.get("threads"))
    h.update(cfg.encode("utf-8"))
    return h.hexdigest()


def _cached_solve(self, env, t):
    os.makedirs(self.tmp_dir, exist_ok=True)
    inst = os.path.join(self.tmp_dir, "dn_t%d_inst.txt" % t)
    sol = os.path.join(self.tmp_dir, "dn_t%d.sol" % t)
    sol_was = dn_policies._mtime_ns(sol)   # freshness gate, original logic
    target_ids = self._write_step_instance(inst, env, t)

    key = _cache_key(inst, self.solver)
    csol = os.path.join(CACHE_DIR, key + ".sol")
    if os.path.exists(csol):
        STATS["hit"] += 1
        shutil.copyfile(csol, sol)         # fresh mtime -> gate passes
    else:
        STATS["miss"] += 1
        rc, output, _wall = wave_runner.run_solver(
            inst, sol,
            delta=self.solver["delta"], timelimit=self.solver["timelimit"],
            threads=self.solver["threads"], python_exe=self.solver["python"],
            extra_args=self.solver.get("extra_args"))
        if os.path.exists(sol) and dn_policies._mtime_ns(sol) != sol_was:
            try:
                os.makedirs(CACHE_DIR, exist_ok=True)
                shutil.copyfile(sol, csol)
                STATS["store"] += 1
            except OSError:
                pass                        # cache write failure is benign

    # freshness gate + parsing identical to the original _solve
    if not os.path.exists(sol) or dn_policies._mtime_ns(sol) == sol_was:
        return {}, None, False, ("no solution file (cached lookup failed; "
                                 "hold fire this step")
    parsed = wave_runner.parse_wave_solution(inst, sol, target_ids)
    if parsed is None:
        return {}, None, False, "unparseable solution - hold fire this step"
    assignment = {}
    for j, per_i in parsed["assignment"].items():
        for i in per_i:
            assignment[i] = j              # mu = 1 -> at most one shot/(i,j)
    return assignment, parsed["objective"], True, None


def main():
    dn_policies.CplexPolicy._solve = _cached_solve
    import experiments.dn_family_eval as fe  # AFTER patch (it binds at call)
    rc = fe.main(sys.argv[1:])
    print("[refcache] hit=%d miss=%d store=%d dir=%s"
          % (STATS["hit"], STATS["miss"], STATS["store"], CACHE_DIR))
    return rc


if __name__ == "__main__":
    sys.exit(main())
