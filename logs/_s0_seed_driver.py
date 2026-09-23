"""S0 pre-ablation baseline driver (no source changes).

marl/train.py (pre-modification) does NOT seed torch's GLOBAL RNG; the
batched PPO update draws torch.randperm from it, so two processes with
identical CLI args would otherwise diverge. This driver seeds the global
RNG (torch.manual_seed(0), same value as --seed 0) and then runs the
UNMODIFIED marl/train.py main. The post-modification trainer seeds the
global RNG internally with args.seed at Trainer construction, so S0 and
the B.3 all-open rerun consume identical RNG streams (construction ->
sampling -> shuffles).

Usage (from the project root):
    /opt/anaconda3/envs/wta/bin/python logs/_s0_seed_driver.py \
        --data-dir data/dn-data-v5 --seed 0 --iters 50 \
        --episodes-per-iter 48 --eval-every 25 \
        --output output/_pre_ablation_ref/base_s0
"""
import os
import runpy
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import torch  # noqa: E402

SEED = 0  # == --seed 0 of the S0 run (fixed by the doc's section 4.2 command)
torch.manual_seed(SEED)

sys.argv = ["train.py"] + sys.argv[1:]
runpy.run_path(os.path.join(ROOT, "marl", "train.py"), run_name="__main__")
