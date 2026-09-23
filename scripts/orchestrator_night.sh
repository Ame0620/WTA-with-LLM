#!/bin/zsh
# Night orchestrator: wait for e49 batch -> 24-arm self-check -> e50 -> e51.
# Usage: nohup ./scripts/orchestrator_night.sh <e49_batch_pid> &
set -u
cd /Users/fgod/Desktop/FGOD/Projects/UAS/WTA-Dn-branch01
PY=/opt/anaconda3/envs/wta/bin/python
E49_PID=${1:?usage: orchestrator_night.sh <e49_batch_pid>}
MAX_WAIT_H=12

log() { echo "[$(date '+%F %T')] $*" }

log "orchestrator start; waiting for e49 batch pid=$E49_PID (max ${MAX_WAIT_H}h)"
waited=0
while kill -0 "$E49_PID" 2>/dev/null; do
  sleep 120
  waited=$((waited+2))
  if [ $waited -ge $((MAX_WAIT_H*3600)) ]; then
    log "TIMEOUT waiting e49 after ${MAX_WAIT_H}h - abort"
    exit 1
  fi
done
log "e49 batch process exited"

log "running 24-arm final self-check"
if ! $PY experiments/e49_final_selfcheck.py > logs/e49_final_selfcheck.log 2>&1; then
  log "E49 SELF-CHECK FAILED - e50 NOT started; see logs/e49_final_selfcheck.log"
  exit 1
fi
log "self-check PASS: $(tail -2 logs/e49_final_selfcheck.log | head -1)"

log "starting e50 batch (test evals + generalization + repro check)"
./scripts/run_e50_batch.sh > logs/e50_batch.log 2>&1
rc=$?
log "e50 batch exit=$rc"
if [ $rc -ne 0 ]; then
  log "E50 FAILED - e51 NOT run; see logs/e50_batch.log"
  exit 1
fi

log "running e51 summary"
$PY experiments/e51_summary.py > logs/e51_summary.log 2>&1
rc=$?
log "e51 exit=$rc"
if [ $rc -ne 0 ]; then
  log "E51 FAILED; see logs/e51_summary.log"
  exit 1
fi
log "ORCHESTRATOR ALL DONE (e49 -> e50 -> e51)"
