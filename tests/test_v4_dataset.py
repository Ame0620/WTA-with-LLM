"""DN-WTA v4 dataset acceptance tests (V1'-V5' + resource invariants).

Covers the data-level acceptance of data/dn-data-v4 (m=5, n=100, K=10,
mu=6, quota 2,2,6, 30 instances, spec: DN-WTA_v4_数据集说明.md):

    V1' format & parse      30 instances via DNInstance + line count
                            1+n+2mn + shared header fields
    V2' determinism         per-file md5 against the MANIFEST baseline
                            table + byte-identical regeneration of two
                            seeds through the generator's main()
    V3' arrival balance     exactly 10 arrivals per window, 30/30
    V4' value trend         merged per-window mean(w): window 9 / window 0
                            >= 2 and monotonic non-decreasing
    V5' no-defense histogram data-level breakthrough histogram
                            0,2,4,10x7 + end 24 identical across the whole
                            family; env-level NonePolicy over test/train/
                            val pick: leaked_ids identical across 5 seeds,
                            leak_rate == 1.0, shots_total == 0

Resource invariants (post v2.0 pool-race fix): shots_total <= m*mu and
ammo_end >= 0 on every run produced here.

V6' (foresight dividend via cplex) is NOT here: it needs the CPLEX
subprocess pipeline and is run through experiments/dn_family_eval.py
(see DN-WTA_v4_数据集说明.md section on acceptance records).

Usage:  python tests/test_v4_dataset.py     (or pytest tests/test_v4_dataset.py)
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

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "dn-data-v4")

# shared header of the whole v4 family
HEADER = dict(m=5, n=100, K=10, mu=6, dt=10.0, delta_d=3.0, v_m=1.0, pcap=95)

# quota (2,2,6) -> 1x 1-window, 2x 2-window, 6x 3-window per wave of 10:
# per-window no-defense leak 0,2,4,10x7 + end settlement 24 (appendix A')
EXPECTED_HIST = (0, 2, 4, 10, 10, 10, 10, 10, 10, 10, 24)

# md5 baseline (V2'), generated 2026-09-08 by experiments/gen_dn_data.py
MD5_BASELINE = {
    1: "6d8c1802aa8df115770621ee32075f44",
    2: "d1e823f31fb01b15a6cccb1d4fd578ac",
    3: "3ef9f4bc2f956d5f6c9870faa1ea7596",
    4: "60b4abc66ad3273d0743bf336d376b4d",
    5: "cf2897e4391a95177172a05af3f10f41",
    6: "917017003a9ee23743114d4f76a55135",
    7: "32c918a10535b478120261618c265ca1",
    8: "731355c3a4f25aee3936c422950ee181",
    9: "da3050c47c950cf36ffcc165754b9162",
    10: "b15dd68a7edf15c4602c3212171ef03e",
    11: "02afa2167ebe35bf2cf52c474fc78126",
    12: "20c77570cc6307e507c246a18a8974c1",
    13: "80b56e49bca1ddb5b6166d2312ba143d",
    14: "493932a5908683a3e33684d1527c1b96",
    15: "bc698c7ff9839147ff19f399aa79349b",
    16: "1b42e55ab8cf49fb3ded980050394960",
    17: "0d324def5558a7137ab0fc9bd725c57b",
    18: "ba6d47886339301ab7719848891e77ee",
    19: "2ca8dae9d47e577baf31444ed30d534f",
    20: "a25a165420c8e53041250366876dcc1e",
    21: "44c20aed53edead820d53427655ffd64",
    22: "9073ea4acdce0d2553737526c4ed65b4",
    23: "d5a920f5fcaf1f7650025b173b0a8229",
    24: "9903fb5dd4ed4a66749f0ed5548f424b",
    25: "74e6e45882092795ea03e1f7f2b0131b",
    26: "db1fe47f187ad1b8ef26ca8a3746f657",
    27: "94406186b8407b26e8ce06abdac2214e",
    28: "5d1942c6d5e5e0fde50dfdbca9eed52e",
    29: "185005c5b901438697e45358f35c1ad3",
    30: "2f2a7ddc09d8fd265cba4e8640b861ff",
}


def _path(s):
    return os.path.join(DATA_DIR, "dn_5x100_K10_s%02d.txt" % s)


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
    tmp = tempfile.mkdtemp(prefix="v4_regen_")
    try:
        for s in (1, 15):   # one test-family seed, one train-family seed
            gen_dn_data.main([
                "--seeds", str(s), "--m", "5", "--n", "100", "--K", "10",
                "--mu", "6", "--w-trend", "1.5", "--quota", "2,2,6",
                "--outdir", tmp, "--pad", "2"])
            a = open(os.path.join(tmp, "dn_5x100_K10_s%02d.txt" % s), "rb").read()
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
                (s, seed)


def test_v5_end_settlement_split():
    # end bucket 24 = wave 9 (10) + wave 8 2/3-window (2+6=8) + wave 7
    # 3-window (6);  per-wave quota 2,2,6 (appendix A')
    for p in (_path(1), _path(15), _path(29)):
        dn = DNInstance(p)
        end_ids = [j for j in dn.T
                   if min(dn.breakthrough_step(j), dn.K) == dn.K]
        assert len(end_ids) == 24, p
        from collections import Counter
        by_wave = Counter(dn.k_arr[j] for j in end_ids)
        assert by_wave == {9: 10, 8: 8, 7: 6}, (p, by_wave)


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items())
           if k.startswith("test_") and callable(v)]
    for fn in fns:
        fn()
        print("PASS %s" % fn.__name__)
    print("all %d acceptance tests passed" % len(fns))
