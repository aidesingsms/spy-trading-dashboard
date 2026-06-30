#!/bin/bash
# Enhanced Market Monitor - Runs every 5 minutes
# Analyzes technical indicators and sends alerts

# Environment
export PATH="/usr/local/bin:/usr/bin:/bin:$PATH"
export TELEGRAM_BOT_TOKEN="8419473578:AAFg5yU35ZrgO5JlJDCq5H-UUH6eX_OAGqA"

# Paths
SCRIPT_DIR="/root/.openclaw/workspace"
LOG_FILE="/tmp/enhanced_monitor.log"
PID_FILE="/tmp/enhanced_monitor.pid"

# Check if already running
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE")
    if ps -p "$OLD_PID" > /dev/null 2>&1; then
        echo "$(date '+%Y-%m-%d %H:%M:%S'): Monitor already running (PID: $OLD_PID)" >> "$LOG_FILE"
        exit 0
    fi
fi

# Save PID
echo $$ > "$PID_FILE"

# Log start
echo "$(date '+%Y-%m-%d %H:%M:%S'): ======================================== " >> "$LOG_FILE"
echo "$(date '+%Y-%m-%d %H:%M:%S'): Starting Enhanced Market Monitor" >> "$LOG_FILE"
echo "$(date '+%Y-%m-%d %H:%M:%S'): ======================================== " >> "$LOG_FILE"

# Run monitor
cd "$SCRIPT_DIR"
python3 enhanced_monitor.py >> "$LOG_FILE" 2>&1
EXIT_CODE=$?

# Log completion
echo "$(date '+%Y-%m-%d %H:%M:%S'): Monitor exited with code $EXIT_CODE" >> "$LOG_FILE"
echo "$(date '+%Y-%m-%d %H:%M:%S'): ----------------------------------------" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# Cleanup
rm -f "$PID_FILE"

exit $EXIT_CODE
