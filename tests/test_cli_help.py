import subprocess
import sys
from pathlib import Path

def test_cli_help_runs():
    # Resolve repo root so the test works no matter where pytest is called from
    repo_root = Path(__file__).resolve().parents[1]
    script = repo_root / "src" / "smb_report.py"

    assert script.exists(), f"Missing script: {script}"

    proc = subprocess.run(
        [sys.executable, str(script), "-h"],
        capture_output=True,
        text=True
    )

    # With -h, argparse should exit 0 and print a usage header
    assert proc.returncode == 0
    out = (proc.stdout + proc.stderr).lower()
    assert "usage:" in out or "optional arguments" in out or "options:" in out
