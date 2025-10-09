# SMB / Network Recon Demo — 198.51.100.100
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![CI](https://github.com/laurenelizabethroberts/SMB-Network-Recon/actions/workflows/python-ci.yml/badge.svg)

<p align="center">
  <img src="https://img.shields.io/badge/Nmap-SMB%20Recon-informational" alt="Nmap SMB Recon">
  <img src="https://img.shields.io/badge/Python-3.11-success" alt="Python 3.11">
  <img src="https://img.shields.io/badge/Shell-Scripts-lightgrey" alt="Shell">
  <a href="#license"><img src="https://img.shields.io/badge/License-MIT-blue" alt="License"></a>
</p>



 

## Objective 

Demonstrate safe, methodical network reconnaissance and SMB enumeration used in vulnerability assessment and cyber research. This repo documents step-by-step commands, raw outputs, and interpretations to showcase skills relevant to roles such as Cybersecurity Researcher at Idaho National Laboratory (INL). 

 

> **Ethics & scope:** All scans were performed on lab-controlled infrastructure with explicit permission. Never scan systems you do not own or have written permission to test. 

 

--- 

 

## Repo layout 

- `scans/` — raw outputs (nmap, enum4linux, smbclient, rpcclient, nmblookup) 

- `analysis/` — human-readable interpretation of outputs and next steps 

- `scripts/` — optional small scripts used to run scans 

- `README.md` — this document



--- 

 

## Tools used 

- `nmap` (SYN scans, version detection, NSE scripts)   

- `enum4linux`, `smbclient`, `rpcclient`   

- `nmblookup` / `nbstat` (NetBIOS name lookups)   

 
---


## How to run (demo data)

1) Ensure Python 3.11+ is available.

2) Use the included demo XML:
python src/smb_report.py data/scans/smb_recon_example.xml > analysis/SMB_Recon_Report.csv

2) If your script supports flags, you can also do:
python src/smb_report.py -i data/scans/smb_recon_example.xml -o analysis/SMB_Recon_Report.csv

3) Review outputs:
- `analysis/SMB_Recon_Report.csv` — consolidated host/OS/SMB signing/shares
- `analysis/findings.md` — analyst interpretation & recommendations



---



## SMB Recon Data
- `data/scans/smb_recon_example.xml` — **simulated** Nmap XML output for two hosts (demo only).
- `src/smb_report.py` — parses Nmap hostscript fields (`smb-os-discovery`, `smb2-security-mode`, `smb-enum-shares`) into a summary CSV.
- `docs/SMB_Recon_Report.csv` — generated report (host, OS, SMB signing status, shares).

> ⚠️ Ethical use: run real scans only on systems you own or have explicit permission to test.



---
 

## Methodology (concise) 

1. Confirm host up: `ping -c 4 <TARGET_IP>`   

2. Fast TCP discovery (top 100 ports): `sudo nmap -sS -Pn --top-ports 100 -T4`   

3. Focused SMB/RPC enumeration (versions, dialects, capabilities, signing): `nmap -p 135,139,445 -sV --script=...`   

4. Anonymous/Null session attempts: `smbclient -L //IP -N`, `rpcclient -U "" IP`, `enum4linux -a IP`   

5. UDP NetBIOS checks: `nmblookup -A IP`, `nmap -sU -p 137 --script=nbstat`   

6. (Optional, authenticated) enumerate shares and users with test credentials. 

 

--- 

 

## How to use this repo 

1. Place raw scan outputs into `scans/` (replace placeholder files).   

2. Edit `analysis/findings.md` to add your interpretation and remediation recommendations.   

3. Commit and push to a private repo while you decide which outputs (if any) are safe to make public. 

 

--- 

 

## Next recommended (safe) steps — for lab use only 

- If you have test credentials for the VM, run authenticated enumeration:
-   smbclient -L //<TARGET_IP> -U *username*
-   rpcclient -U '<username>%<password>' <TARGET_IP>



---



## Contact / Author
- Author: Lauren Roberts
- Notes: This project demonstrates methodical reconnaissance and interpretation skills suitable for vulnerability assessment
