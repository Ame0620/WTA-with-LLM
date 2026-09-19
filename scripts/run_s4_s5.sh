#!/bin/zsh
# v4 full-algorithm experiment: S4 (learning-family evals) + S5 (summary)
# Waits for the S3 driver (scripts/run_s3.sh) to finish, then runs:
#   e34: per-algo formal test eval (30 seeds, per-step CPLEX reference)
#   e35: generalisation over {train, val, test} (30 seeds, leak tier,
#        --no-ref to keep the 30-instance sweep tractable; metric-x
#        generalisation gap only needs leak means)
#   e36: consolidated report via scripts/make_v4_report.py
set -e
PY=/opt/anaconda3/envs/wta/bin/python
cd "$(dirname "$0")/.."
mkdir -p logs

echo "[watch] waiting for S3 driver to finish ..."
while pgrep -f "zsh scripts/run_s3.sh" > /dev/null 2>&1; do
    sleep 120
done
echo "[watch] S3 done at $(date)"

for f in output/e33_v4_maddpg/best.pt output/e33_v4_qmix/best.pt \
         output/e33_v4_mappo/best.pt output/e33_v4_ecmappo/best.pt; do
    if [ ! -f "$f" ]; then
        echo "[watch] FATAL: missing checkpoint $f"; exit 1
    fi
done

echo "[S4] formal test evals (with CPLEX reference)"
$PY experiments/dn_family_eval.py --split test --policy maddpg \
    --model output/e33_v4_maddpg/best.pt --seeds 30 \
    --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
    --output output/e34_v4_maddpg_eval --log logs/e34_v4_maddpg_eval.log
$PY experiments/dn_family_eval.py --split test --policy qmix \
    --model output/e33_v4_qmix/best.pt --seeds 30 \
    --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
    --output output/e34_v4_qmix_eval --log logs/e34_v4_qmix_eval.log
$PY experiments/dn_family_eval.py --split test --policy mappo \
    --model output/e33_v4_mappo/best.pt --seeds 30 \
    --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
    --output output/e34_v4_mappo_eval --log logs/e34_v4_mappo_eval.log
$PY experiments/dn_family_eval.py --split test --policy marl \
    --model output/e33_v4_ecmappo/best.pt --seeds 30 \
    --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
    --output output/e34_v4_ecmappo_eval --log logs/e34_v4_ecmappo_eval.log

echo "[S4] generalisation sweeps (train/val/test, --no-ref)"
for algo in maddpg qmix mappo ecmappo; do
    case $algo in
        ecmappo) pol="marl";;
        *) pol="$algo";;
    esac
    model="output/e33_v4_${algo}/best.pt"
    for split in train val test; do
        $PY experiments/dn_family_eval.py --split $split --policy $pol \
            --model $model --seeds 30 --no-ref \
            --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
            --output output/e35_v4_${algo}_gen/$split \
            --log logs/e35_v4_${algo}_gen_${split}.log
    done
done

echo "[S5] consolidated report"
$PY scripts/make_v4_report.py

echo "[S4+S5] ALL DONE at $(date)"
