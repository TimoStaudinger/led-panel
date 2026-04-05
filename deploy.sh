#!/bin/bash
set -e

HOST="ledmatrix.local"
REMOTE_PATH="~/rpi-rgb-led-matrix/dist/main.py"
LOCAL_PATH="$(dirname "$0")/dist/main.py"

# Kill any running instance
ssh "$HOST" 'sudo killall -9 python3 2>/dev/null' || true

# Copy and run
scp "$LOCAL_PATH" "$HOST:$REMOTE_PATH"
ssh "$HOST" "sudo python3 $REMOTE_PATH"
