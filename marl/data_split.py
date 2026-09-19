"""Shared dataset-split discovery for the v4 algorithm migration.

The split protocol is FIXED across layouts (v3 3x50 / v4 5x100):
    s01-s02 test / s03-s26 train / s27-s30 val
Instance files are matched by the dn_<m>x<n>_K<k>_s<nn>.txt pattern so
the SAME trainer code serves both datasets (v3 regression unaffected;
v4 = --data-dir data/dn-data-v4).
"""

import os
import re


def discover_split(data_dir):
    """-> (train_files, val_files) sorted by s-number."""
    if not os.path.isdir(data_dir):
        raise SystemExit("[ERROR] data dir not found: %s" % data_dir)
    files = [f for f in os.listdir(data_dir)
             if re.match(r"dn_\d+x\d+_K\d+_s\d+\.txt$", f)]
    files.sort(key=lambda f: int(re.search(r"_s(\d+)\.txt$", f).group(1)))
    s_of = lambda f: int(re.search(r"_s(\d+)", f).group(1))  # noqa: E731
    train = [f for f in files if 3 <= s_of(f) <= 26]
    val = [f for f in files if s_of(f) >= 27]
    if not train or not val:
        raise SystemExit("[ERROR] split discovery found nothing usable "
                         "in %s" % data_dir)
    return train, val


def load_instances(data_dir, files):
    from dwta.dn_instance import DNInstance
    return [DNInstance(os.path.join(data_dir, f)) for f in files]
