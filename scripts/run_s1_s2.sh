#!/bin/zsh
# v4 full-algorithm experiment: S1 (solvers) + S2 (rule baselines)
# Requirement doc v1.1 sections 6 / 9 - formal 30-seed test evaluations.
set -e
PY=/opt/anaconda3/envs/wta/bin/python
cd "$(dirname "$0")/.."
mkdir -p logs

echo "[S1] CPLEX 30-seed formal evaluation"
$PY experiments/dn_family_eval.py --split test --policy cplex --seeds 30 \
    --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
    --output output/e30_v4_cplex --log logs/e30_v4_cplex.log

echo "[S1] GA main arm p40 g50"
$PY experiments/dn_family_eval.py --split test --policy ga \
    --ga-pop 40 --ga-gen 50 --seeds 30 \
    --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
    --output output/e31_v4_ga/p40g50 --log logs/e31_v4_ga_p40g50.log

echo "[S1] GA sensitivity p20 g25"
$PY experiments/dn_family_eval.py --split test --policy ga \
    --ga-pop 20 --ga-gen 25 --seeds 30 \
    --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
    --output output/e31_v4_ga/p20g25 --log logs/e31_v4_ga_p20g25.log

echo "[S1] GA sensitivity p80 g100"
$PY experiments/dn_family_eval.py --split test --policy ga \
    --ga-pop 80 --ga-gen 100 --seeds 30 \
    --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
    --output output/e31_v4_ga/p80g100 --log logs/e31_v4_ga_p80g100.log

echo "[S2] Random 30 seeds"
$PY experiments/dn_family_eval.py --split test --policy random --seeds 30 \
    --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
    --output output/e32_v4_baselines/random --log logs/e32_v4_random.log

echo "[S2] Greedy-Nearest 30 seeds"
$PY experiments/dn_family_eval.py --split test --policy greedy_nearest \
    --seeds 30 \
    --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
    --output output/e32_v4_baselines/greedy_nearest \
    --log logs/e32_v4_greedy_nearest.log

echo "[S2] Greedy-Threat 30 seeds"
$PY experiments/dn_family_eval.py --split test --policy greedy_threat \
    --seeds 30 \
    --data-dir data/dn-data-v4 --manifest data/dn-data-v4/MANIFEST.md \
    --output output/e32_v4_baselines/greedy_threat \
    --log logs/e32_v4_greedy_threat.log

echo "[S1+S2] ALL DONE"
