#!/usr/bin/env python3
from pathlib import Path
import csv, re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
XML_IN = ROOT / "data" / "scans" / "smb_recon_example.xml"
OUT = ROOT / "docs" / "SMB_Recon_Report.csv"

def parse_smb(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    ns = {}  # nmap XML has no required namespace
    rows = []
    for host in root.findall("host", ns):
        status = host.find("status")
        if status is not None and status.get("state") != "up":
            continue
        addr = host.find("address").get("addr")
        hostname = host.find("hostnames/hostname")
        hostname = hostname.get("name") if hostname is not None else ""
        # pull hostscript results
        os_out = sec_out = shares_out = ""
        for hs in host.findall("hostscript/script"):
            sid = hs.get("id", "")
            out = hs.get("output", "")
            if sid == "smb-os-discovery":
                os_out = out
            elif sid == "smb2-security-mode":
                sec_out = out
            elif sid == "smb-enum-shares":
                shares_out = out
        # normalize signing
        signing = "unknown"
        m = re.search(r"Signing:\s*([^\s]+)", sec_out, re.I)
        if m:
            signing = m.group(1).lower()
        rows.append({
            "host": addr,
            "hostname": hostname,
            "os_discovery": os_out,
            "smb_signing": signing,           # e.g., required / disabled
            "shares": shares_out,             # semicolon-separated
            "note": "simulated dataset"
        })
    return rows

def main():
    rows = parse_smb(XML_IN)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["host","hostname","os_discovery","smb_signing","shares","note"])
        w.writeheader()
        w.writerows(rows)
    print(f"[OK] Wrote {OUT} ({len(rows)} hosts)")

if __name__ == "__main__":
    main()
