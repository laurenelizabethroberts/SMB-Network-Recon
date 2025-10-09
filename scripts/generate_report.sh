#!/usr/bin/env bash
set -euo pipefail
IN="${1:-data/scans/smb_recon_example.xml}"
OUT="${2:-analysis/SMB_Recon_Report.csv}"
python src/smb_report.py "$IN" > "$OUT"
echo "Wrote $OUT"
