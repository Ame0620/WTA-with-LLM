#!/bin/zsh
# v4 full-algorithm experiment: S3 (learning-family retraining)
# Budget layering (D6/4.3): QMIX/MADDPG 3h tier (defaults
# 1200 iters x 24 ep + 2.5h wall); EC-MAPPO full tier (2500 x 96,
# patience 60, --wall-limit 6h).
set -e
PY=/opt/anaconda3/envs/wta/bin/python
cd "$(dirname "$0")/.."
mkdir -p logs

echo "[S3] MADDPG (3h tier)"
$PY marl/train_maddpg.py --data-dir data/dn-data-v4 --device auto \
    --output output/e33_v4_maddpg 2>&1 | tee logs/e33_v4_maddpg_train.log

echo "[S3] QMIX (3h tier)"
$PY marl/train_qmix.py --algo qmix --data-dir data/dn-data-v4 --device auto \
    --output output/e33_v4_qmix 2>&1 | tee logs/e33_v4_qmix_train.log

echo "[S3] EC-MAPPO (full tier <=6h)"
$PY marl/train.py --data-dir data/dn-data-v4 --iters 2500 \
    --episodes-per-iter 96 --patience 60 --wall-limit 6 --device auto \
    --output output/e33_v4_ecmappo 2>&1 | tee logs/e33_v4_ecmappo_train.log

echo "[S3] ALL DONE"
