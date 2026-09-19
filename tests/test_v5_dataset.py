"""DN-WTA v5 dataset acceptance tests (V1''-V6'' + resource invariants).

Covers the data-level acceptance of data/dn-data-v5 (m=10, n=100, K=10,
mu=7, quota 2,2,6, 30 instances, spec: DN-WTA_v5_数据集说明.md):

    V1'' format & parse      30 instances via DNInstance + line count
                             1+n+2mn + shared header fields
    V2'' determinism         per-file md5 against the MANIFEST baseline
                             table + byte-identical regeneration of two
                             seeds through the generator's main()
    V3'' arrival balance     exactly 10 arrivals per window, 30/30
    V4'' value trend         merged per-window mean(w): window 9 / window 0
                             >= 2 and monotonic non-decreasing
    V5'' no-defense histogram data-level breakthrough histogram
                             0,2,4,10x7 + end 24 identical across the whole
                             family; env-level NonePolicy over test/train/
                             val pick: leaked_ids identical across 5 seeds,
                             leak_rate == 1.0, shots_total == 0
    V6'' v4 inheritance      same-seed instances share the target block
                             (k_arr/r0/w -> identical total_value) and the
                             first-5-platform p/d0 blocks with v4

Resource invariants: shots_total <= m*mu (=70) and ammo_end >= 0 on every
run produced here (V8'' none-policy part).

V7'' (foresight dividend via cplex) is NOT here: it needs the CPLEX
subprocess pipeline and is run through experiments/dn_family_eval.py
(see DN-WTA_v5_数据集说明.md section on acceptance records).

Usage:  python tests/test_v5_dataset.py     (or pytest tests/test_v5_dataset.py)
"""

import hashlib
import os
import shutil
import sys
import tempfile

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from dwta.dn_instance import DNInstance          # noqa: E402
from dwta.dn_env import simulate_dn              # noqa: E402
from dwta.dn_policies import NonePolicy          # noqa: E402

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "dn-data-v5")
V4_DIR = os.path.join(PROJECT_ROOT, "data", "dn-data-v4")

# shared header of the whole v5 family
HEADER = dict(m=10, n=100, K=10, mu=7, dt=10.0, delta_d=3.0, v_m=1.0, pcap=95)

# quota (2,2,6) -> same target flow as v4: per-window no-defense leak
# 0,2,4,10x7 + end settlement 24 (v5 spec appendix A'')
EXPECTED_HIST = (0, 2, 4, 10, 10, 10, 10, 10, 10, 10, 24)

# md5 baseline (V2''), generated 2026-09-18 by experiments/gen_dn_data.py
MD5_BASELINE = {
    1: "8d29337da4bc0fce0b8e58b9f6fee850",
    2: "0183a40e326833ac5b99a1fbb1da1049",
    3: "d77baddb574ce1686b0f7d273f843344",
    4: "9b62d799ac914174f7cb107d0160099e",
    5: "277fa099fd78e043ef35db175dd379c2",
    6: "6e304a653d4b066b7e904ba176397335",
    7: "d39ffabddb16384132e3fc7ac87d604a",
    8: "cbb774c4efef7dcb6993461b36f9dd13",
    9: "2c71f21eae8c25d46d454f4486303153",
    10: "bdcdf91048f622f19c627d1413875248",
    11: "3afafd662b84f870abb4d133c4af9062",
    12: "b6f4d75c546efa0fed19bdbd9db8f3ed",
    13: "2addabda27495135492e28562fb99f65",
    14: "e78f5ed60d7a8fcffa199df9079d461b",
    15: "9c723d2909be29df5ece6b10b15e8625",
    16: "03382a1eeee74f830e1542efe67f116f",
    17: "0f8040d40b3300d4ac6613269f034214",
    18: "523c02eddf0dd3f64868a3cd14b369f3",
    19: "b84b36133f92f78bac705cc8b456afc8",
    20: "dce3e227298e2d40eaee7606b54041e2",
    21: "2693d5819fe611eab6840cabf9c41ee7",
    22: "dc6b6434fb7d97dbc9c1ad68bfbe86bc",
    23: "39287a81334617427da92bf0b77a64a1",
    24: "144269afc14e73e7ac83532875750eea",
    25: "f000ef6dded3f5a599a3558df0cacea6",
    26: "8d2203ccc8414451c7979211b067e359",
    27: "8b7286c3615e67d9b65049c59bc5871f",
    28: "3bc2c8ad3e68f5126a78918653279cec",
    29: "fecb9da3d752629cc0e5d04d3e257a26",
    30: "7f8924dc63af1fbb71572122725d162d",
}


def _path(s):
    return os.path.join(DATA_DIR, "dn_10x100_K10_s%02d.txt" % s)


def _v4_path(s):
    return os.path.join(V4_DIR, "dn_5x100_K10_s%02d.txt" % s)


def _load_all():
    return [_path(s) for s in range(1, 31)]


def test_v1_format_and_parse():
    for p in _load_all():
        dn = DNInstance(p)
        assert (dn.m, dn.n, dn.K, dn.mu) == \
            (HEADER["m"], HEADER["n"], HEADER["K"], HEADER["mu"]), p
        assert (dn.dt, dn.delta_d, dn.v_m, dn.pcap_pct) == \
            (HEADER["dt"], HEADER["delta_d"], HEADER["v_m"], HEADER["pcap"]), p
        n_lines = sum(1 for _ in open(p))
        assert n_lines == 1 + dn.n + 2 * dn.m * dn.n, p
        assert all(d0 >= r0 for (_, _), d0, r0 in
                   [(k, dn.d0[k], dn.r0[k[1]]) for k in dn.d0]), p
        assert all(0.0 < p_ij < 1.0 for p_ij in dn.p.values()), p


def test_v2_determinism_md5():
    for s, md5 in MD5_BASELINE.items():
        got = hashlib.md5(open(_path(s), "rb").read()).hexdigest()
        assert got == md5, (s, got, md5)


def test_v2_regeneration_byte_identical():
    from experiments import gen_dn_data
    tmp = tempfile.mkdtemp(prefix="v5_regen_")
    try:
        for s in (1, 15):   # one test-family seed, one train-family seed
            gen_dn_data.main([
                "--seeds", str(s), "--m", "10", "--n", "100", "--K", "10",
                "--mu", "7", "--w-trend", "1.5", "--quota", "2,2,6",
                "--outdir", tmp, "--pad", "2"])
            a = open(os.path.join(tmp, "dn_10x100_K10_s%02d.txt" % s), "rb").read()
            b = open(_path(s), "rb").read()
            assert a == b, s
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_v3_arrival_balance():
    for p in _load_all():
        dn = DNInstance(p)
        per = [sum(1 for x in dn.k_arr if x == k) for k in range(dn.K)]
        assert per == [dn.n // dn.K] * dn.K == [10] * 10, p


def test_v4_value_trend():
    ws = [[] for _ in range(10)]
    for p in _load_all():
        dn = DNInstance(p)
        for k in range(10):
            ws[k].extend(dn.w[j] for j in dn.T if dn.k_arr[j] == k)
    mw = [sum(v) / len(v) for v in ws]
    assert mw[9] / mw[0] >= 2.0, mw
    assert all(mw[i] <= mw[i + 1] for i in range(9)), mw


def _data_histogram(dn):
    bt = [min(dn.breakthrough_step(j), dn.K) for j in dn.T]
    return tuple(sum(1 for x in bt if x == k) for k in range(dn.K + 1))


def test_v5_histogram_data_level():
    for p in _load_all():
        dn = DNInstance(p)
        assert _data_histogram(dn) == EXPECTED_HIST, p


def test_v5_none_env_level():
    for s in (1, 15, 29):          # test / train / val pick, one each
        dn = DNInstance(_path(s))
        base = None
        for seed in (42, 43, 44, 45, 46):
            rec = simulate_dn(dn, seed, NonePolicy())
            # deterministic data -> identical leak set across seeds
            if base is None:
                base = rec
            else:
                assert rec["leaked_ids"] == base["leaked_ids"], (s, seed)
            # no defense: everything leaks, nothing fired
            assert rec["leak_count"] == dn.n and rec["leak_rate"] == 1.0, (s, seed)
            assert rec["leak_value"] == dn.total_value(), (s, seed)
            assert rec["shots_total"] == 0 and rec["ammo_end"] == dn.m * dn.mu, \
                (s, seed)      # ammo_end == 70 (V8'' none-policy part)


def test_v5_end_settlement_split():
    # end bucket 24 = wave 9 (10) + wave 8 2/3-window (2+6=8) + wave 7
    # 3-window (6);  per-wave quota 2,2,6 (appendix A'')
    for p in (_path(1), _path(15), _path(29)):
        dn = DNInstance(p)
        end_ids = [j for j in dn.T
                   if min(dn.breakthrough_step(j), dn.K) == dn.K]
        assert len(end_ids) == 24, p
        from collections import Counter
        by_wave = Counter(dn.k_arr[j] for j in end_ids)
        assert by_wave == {9: 10, 8: 8, 7: 6}, (p, by_wave)


def test_v6_inheritance_from_v4():
    # v5 spec section 10: same-seed v5 = v4 target block + first-5-platform
    # p/d0 blocks + new platforms 5..9 drawn from the same RandomState
    # streams -> cross-version deltas are attributable to resource scaling
    for s in range(1, 31):
        a, b = DNInstance(_path(s)), DNInstance(_v4_path(s))
        assert a.k_arr == b.k_arr, s
        assert a.r0 == b.r0, s
        assert a.w == b.w, s
        assert a.total_value() == b.total_value(), s
        assert all(a.p[(i, j)] == b.p[(i, j)]
                   for i in range(5) for j in range(100)), s
        assert all(a.d0[(i, j)] == b.d0[(i, j)]
                   for i in range(5) for j in range(100)), s


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items())
           if k.startswith("test_") and callable(v)]
    for fn in fns:
        fn()
        print("PASS %s" % fn.__name__)
    print("all %d acceptance tests passed" % len(fns))
