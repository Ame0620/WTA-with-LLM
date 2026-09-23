#!/bin/zsh
# Overnight chain: wait for the running e53 driver (PID passed as $1) to
# finish cleanly, then launch e54 (final eval + generalization + repro),
# whose tail runs e55_summary.py automatically. If the e53 driver dies
# without "ALL E53 ARMS DONE" (e.g. checkpoint sanity halt), do NOT
# proceed - surface the failure for manual inspection instead.
cd /Users/fgod/Desktop/FGOD/Projects/UAS/WTA-Dn-branch01
E53PID=$1
while kill -0 $E53PID 2>/dev/null; do
  sleep 300
done
if ! grep -q "ALL E53 ARMS DONE" logs/e53_driver.log; then
  echo "CHAIN ABORTED: e53 driver exited without completion $(date '+%F %T')"
  tail -20 logs/e53_driver.log
  exit 1
fi
echo "e53 finished cleanly -> starting e54 $(date '+%F %T')"
zsh scripts/run_e54_batch.sh
echo "CHAIN COMPLETE (e53+e54+e55) $(date '+%F %T')"
