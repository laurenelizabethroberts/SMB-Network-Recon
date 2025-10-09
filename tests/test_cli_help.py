import subprocess, sys, os

def test_cli_help_runs():
    # Ensure we can call the script and it returns help/usage without error
    cmd = [sys.executable, "src/smb_report.py", "-h"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    # Accept 0 (OK) or 2 (argparse shows help with error code when no args)
    assert proc.returncode in (0, 2)
    assert "help" in (proc.stdout + proc.stderr).lower()
