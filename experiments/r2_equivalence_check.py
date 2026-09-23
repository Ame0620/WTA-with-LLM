"""r2 E1/E2 bit-level equivalence checks (r2 spec §E1/E2; 口径 mirrors
the round-1 S2.2 acceptance).

E1  r2_equivalence_check.py E1 <before_dir> <after_dir>
    pre-vs-post modification, all defaults, (1,1,1), seed 0, 50 iters:
    train_log with elapsed/wall/time fields stripped must match
    bit-for-bit; best.pt tensors must be torch.equal; non-tensor
    metadata must match except the r2-added 'reshaping'/'versions'
    keys (the after-run necessarily carries them).

E2  r2_equivalence_check.py E2 <dir_default> <dir_lo> <dir_hi>
    all-off (0,0,0) with the recalibration scalars at the extremes
    {0.2, 2.0} vs the 1.0 defaults, seed 0, 25 iters: the three runs
    must be bit-identical on the same tensor/log criteria (scalars
    must be provably inert when both modules are off).

Exit 0 = PASS; a nonzero exit prints the first mismatch.
"""
import json
import sys

import torch

STRIP_KEYS_SUBSTR = ("wall", "time", "elapsed")
# r2-added PURE-OBSERVATION log columns (spec §3.4): absent on the
# pre-modification side by construction; every other key must match
# bit-for-bit. They are instrumentation reads only - they never enter
# any loss/gradient/optimizer path (verified by audit E10 + E1 tensors).
STRIP_KEYS_EXACT = ("r_shape_share", "credit_adv_share")
META_KEYS = ("ablation", "actor_type", "critic_type", "feature_spec",
             "budget", "train_seed")


def _norm_row(r):
    return json.dumps({k: v for k, v in r.items()
                       if not any(s in k.lower() for s in STRIP_KEYS_SUBSTR)
                       and k not in STRIP_KEYS_EXACT},
                      sort_keys=True)


def _check_log(d):
    rows = [_norm_row(json.loads(l))
            for l in open("%s/train_log.jsonl" % d)]
    return rows


def _check_ckpt(d):
    ck = torch.load("%s/best.pt" % d, map_location="cpu",
                    weights_only=False)
    sd = ck["state_dict"]
    meta = {k: ck.get(k) for k in META_KEYS}
    return {k: v.clone() for k, v in sd.items()}, meta


def _cmp_ckpts(a, b, tag):
    ta, ma = a
    tb, mb = b
    assert set(ta) == set(tb), "%s: state_dict key sets differ" % tag
    for k in ta:
        if not torch.equal(ta[k], tb[k]):
            raise AssertionError(
                "%s: tensor %s differs (max|d|=%.3e)"
                % (tag, k, float((ta[k] - tb[k]).abs().max())))
    for k in ma:
        if ma[k] != mb[k]:
            raise AssertionError("%s: meta %s differs" % (tag, k))


def main(argv):
    mode = argv[1]
    if mode == "E1":
        before, after = argv[2], argv[3]
        ra, rb = _check_log(before), _check_log(after)
        assert len(ra) == len(rb), "row count differs"
        for i, (x, y) in enumerate(zip(ra, rb)):
            assert x == y, "log row %d differs:\n  %s\n  %s" % (i, x, y)
        _cmp_ckpts(_check_ckpt(before), _check_ckpt(after),
                   "best.pt before/after")
        print("E1 PASS: pre/post-modification bit-identical "
              "(train_log stripped of wall/time + best.pt tensors)")
        return 0
    if mode == "E2":
        dirs = argv[2:5]
        assert len(dirs) == 3
        base = _check_log(dirs[0])
        base_ck = _check_ckpt(dirs[0])
        for d in dirs[1:]:
            rows = _check_log(d)
            assert len(rows) == len(base), "row count differs (%s)" % d
            for i, (x, y) in enumerate(zip(base, rows)):
                assert x == y, "%s log row %d differs:\n  %s\n  %s" \
                    % (d, i, x, y)
            _cmp_ckpts(base_ck, _check_ckpt(d), "best.pt %s" % d)
        print("E2 PASS: all-off runs bit-identical across scalar "
              "extremes {default, 0.2, 2.0}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
