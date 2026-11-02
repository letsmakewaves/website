#!/bin/bash
# Installs the graphify CLI (PyPI: graphifyy) in Claude Code cloud sessions.
set -euo pipefail

# Only run in Claude Code cloud sessions
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

export PATH="$HOME/.local/bin:$PATH"

# Install uv if missing (it is normally pre-installed)
if ! command -v uv >/dev/null 2>&1; then
  python3 -m pip install --quiet --user uv
fi

# Install graphify only if it is not already on PATH
if ! command -v graphify >/dev/null 2>&1; then
  uv tool install --quiet graphifyy
fi

# Make sure the uv tool bin dir is on PATH for the rest of the session
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export PATH=\"$(uv tool dir --bin):\$PATH\"" >> "$CLAUDE_ENV_FILE"
fi
