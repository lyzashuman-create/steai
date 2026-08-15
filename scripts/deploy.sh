#!/usr/bin/env bash
# One-click deploy: let an AI come play STEAI.
# Usage:  ./scripts/deploy.sh  <command-that-runs-an-AI> [optional args...]
#
# It hands the AI the play instruction and lets it generate its own seed and
# play to completion. No reproduction — every AI plays its own round.
#
# Examples:
#   ./scripts/deploy.sh "hermes chat -q"
#   ./scripts/deploy.sh "claude -p"
#   ./scripts/deploy.sh "codex exec"
set -euo pipefail

INSTRUCTION_FILE="$(dirname "$0")/../protocols/play_instruction.md"
[ -f "$INSTRUCTION_FILE" ] || { echo "play_instruction.md not found"; exit 1; }

if [ $# -lt 1 ]; then
  echo "Usage: $0 <command-that-runs-an-AI> [args...]"
  echo "Examples: $0 \"hermes chat -q\"   $0 \"claude -p\""
  exit 1
fi

AI_CMD="$*"
PLAY="$(sed -n '/## 指令原文/,/^## /p' "$INSTRUCTION_FILE" | tail -n +2 | head -n -1)"

echo ">>> Handing the play instruction to: $AI_CMD"
$AI_CMD "$PLAY"
