#!/bin/bash
# OMEGA System Launch Script
# Starts the Workspace Hub Daemon and monitors health

cd /home/q/TravelKing.Live
source venv/bin/activate

echo "🚀 Launching OMEGA Workspace Hub..."
nohup python3 core/enterprise/workspace_hub.py --daemon > logs/hub.log 2>&1 &
echo "✅ Hub running in background (PID: $!). Logs: logs/hub.log"

echo "🛡️  Running Guardian Health Check..."
python3 core/maintenance/guardian.py
