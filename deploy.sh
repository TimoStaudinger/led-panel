#!/bin/bash
set -e

HOST="ledmatrix.local"
REMOTE_DIR="~/rpi-rgb-led-matrix/dist"
LOCAL_DIR="$(dirname "$0")/dist"

# Kill any running instance
ssh "$HOST" 'sudo killall -9 python3 2>/dev/null' || true

# Copy and run
scp -r "$LOCAL_DIR" "$HOST:~/rpi-rgb-led-matrix/"
ssh "$HOST" "cd $REMOTE_DIR && sudo python3 main.py"
