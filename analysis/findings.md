# Findings & Recommendations

**Scope:** Lab demo (198.51.100.0/24)  
**Date:** 2025-10-09  
**Analyst:** Lauren Roberts

| ID | Host | Issue | Evidence | Risk | Recommendation |
|---|------|-------|----------|------|----------------|
| F-01 | 198.51.100.10 | SMB signing not required | `smb2-security-mode: signing enabled but not required` | High | Enforce `RequireSecuritySignature=1` on clients/servers; GPO hardening |
| F-02 | 198.51.100.10 | Public share exposed | `smb-enum-shares: Public (read-only)` | Medium | Limit to authenticated users; remove if not necessary |
| F-03 | 198.51.100.20 | Admin shares present | `ADMIN$`, `C$` | Low | Monitor access; ensure only admins via secure channels |

**Executive Summary:**  
- One host allows SMB without mandatory signing (MITM risk).  
- Shares exist that increase surface area.  
- Recommend immediate GPO to require SMB signing, review share ACLs, and add detection rules for unsigned SMB attempts.
