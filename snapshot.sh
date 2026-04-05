#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
[ -f "$SCRIPT_DIR/.env" ] && set -a && source "$SCRIPT_DIR/.env" && set +a

CAMERA_HOST="${TAPO_CAMERA_HOST:-192.168.68.60}"
CAMERA_USER="${TAPO_CAMERA_USER:?Set TAPO_CAMERA_USER}"
CAMERA_PASS="${TAPO_CAMERA_PASS:?Set TAPO_CAMERA_PASS}"
OUTPUT="${1:-/tmp/led-panel-snapshot.jpg}"

/opt/homebrew/bin/ffmpeg -rtsp_transport tcp \
  -i "rtsp://${CAMERA_USER}:${CAMERA_PASS}@${CAMERA_HOST}/stream1" \
  -frames:v 1 -update 1 -y "$OUTPUT" 2>/dev/null

echo "Snapshot saved to $OUTPUT"
