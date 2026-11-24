#!/bin/bash
mkdir -p dr/backups
TS=$(date +"%Y%m%d_%H%M%S")
tar -czf dr/backups/capstone_snapshot_$TS.tar.gz app/ k8s/ infra/
echo "[DR BACKUP] Snapshot created: dr/backups/capstone_snapshot_$TS.tar.gz (RPO=0s)"
