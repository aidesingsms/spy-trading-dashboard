#!/bin/bash
# Market Monitor Cron Job
# Runs every 5 minutes during market hours

# Set environment
export PATH="/usr/local/bin:/usr/bin:/bin:$PATH"
export TELEGRAM_BOT_TOKEN="8419473578:AAFg5yU35ZrgO5JlJDCq5H-UUH6eX_OAGqA"

# Log file
LOG_FILE="/tmp/market_monitor.log"
PID_FILE="/tmp/market_monitor.pid"

# Check if already running
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE")
    if ps -p "$OLD_PID" > /dev/null 2>&1; then
        echo "$(date): Monitor already running (PID: $OLD_PID)" >> "$LOG_FILE"
        exit 0
    fi
fi

# Save PID
echo $$ > "$PID_FILE"

# Log start
echo "$(date): Starting market monitor cycle" >> "$LOG_FILE"

# Run Python monitor
cd /root/.openclaw/workspace
python3 market_monitor.py >> "$LOG_FILE" 2>&1

# Log completion
echo "$(date): Monitor cycle complete" >> "$LOG_FILE"
echo "---" >> "$LOG_FILE"

# Remove PID file
rm -f "$PID_FILE"
