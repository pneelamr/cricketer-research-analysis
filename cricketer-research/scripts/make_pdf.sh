#!/usr/bin/env bash
# Render a cricketer-research Markdown dossier as a PDF.
# Usage: make_pdf.sh INPUT.md [OUTPUT.pdf] [--page-size letter|a4]
# Uses the system Python if reportlab is importable; otherwise creates a
# private virtual environment under ~/.cache/cricketer-research on first use
# and installs reportlab there, leaving the system Python untouched.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY=python3
if ! python3 -c "import reportlab" >/dev/null 2>&1; then
  VENV="${XDG_CACHE_HOME:-$HOME/.cache}/cricketer-research/venv"
  if ! "$VENV/bin/python" -c "import reportlab" >/dev/null 2>&1; then
    echo "First run: installing reportlab into $VENV" >&2
    python3 -m venv "$VENV"
    "$VENV/bin/python" -m pip install --quiet --disable-pip-version-check reportlab
  fi
  PY="$VENV/bin/python"
fi
exec "$PY" "$DIR/md_to_pdf.py" "$@"
