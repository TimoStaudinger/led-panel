#!/bin/bash
set -e

HOST="ledmatrix.local"
REMOTE_DIR="~/rpi-rgb-led-matrix/dist"
LOCAL_DIR="$(dirname "$0")/dist"

# Copy files to Pi
scp -r "$LOCAL_DIR" "$HOST:~/rpi-rgb-led-matrix/"

# Install and restart the systemd service
ssh "$HOST" "sudo cp $REMOTE_DIR/led-panel.service /etc/systemd/system/ && sudo systemctl daemon-reload && sudo systemctl enable led-panel && sudo systemctl restart led-panel"
