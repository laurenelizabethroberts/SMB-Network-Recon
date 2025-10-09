#!/usr/bin/env bash
# Fail on error, undefined vars, and pipe errors
set -euo pipefail

# --- Resolve project root (script can be called from anywhere) ---
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
cd "$REPO_ROOT"

# --- Choose Python (prefer venv if present) ---
PY=python
if [[ -d ".venv" ]]; then
  if [[ -f ".venv/bin/python" ]]; then
    PY=".venv/bin/python"
  elif [[ -f ".venv/Scripts/python.exe" ]]; then  # Windows venv
    PY=".venv/Scripts/python.exe"
  fi
fi

# --- Inputs/outputs with sensible defaults ---
IN="${1:-data/scans/smb_recon_example.xml}"
OUT="${2:-analysis/SMB_Recon_Report.csv}"

# --- Ensure input exists ---
if [[ ! -f "$IN" ]]; then
  echo "ERROR: input file not found: $IN"
  echo "Hint: put a demo XML in data/scans/smb_recon_example.xml or pass a path:"
  echo "  scripts/generate_report.sh path/to/scan.xml analysis/out.csv"
  exit 1
fi

# --- Ensure output directory exists ---
OUT_DIR="$(dirname "$OUT")"
mkdir -p "$OUT_DIR"

# --- Run the parser (edit flags to match your script) ---
# If your script supports -i/-o flags:
if $PY src/smb_report.py -h >/dev/null 2>&1; then
  "$PY" src/smb_report.py -i "$IN" -o "$OUT"
else
  # Fallback: redirect stdout -> CSV (if your script prints CSV)
  "$PY" src/smb_report.py "$IN" > "$OUT"
fi

echo "Wrote $OUT"

# Make executable (on any OS; Git respects this bit)
git update-index --chmod=+x scripts/generate_report.sh

# If you see 'bash\r: No such file or directory', convert CRLF->LF:
# (Run from Git Bash or WSL)
sed -i 's/\r$//' scripts/generate_report.sh
