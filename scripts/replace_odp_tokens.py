"""
Replace {{ insert: param, ODP_ID }} tokens in cmmc-practices.json
with human-readable labels and CMMC/STIG constraint notes.
"""

import json
import re

ODP_MAP = {
    # A.03.01.01 — Account Management
    "A.03.01.01.ODP.01": {
        "label": "35 days",
        "note": "DISA STIG upper limit: accounts inactive >35 days must be disabled (V-220740)"
    },
    "A.03.01.01.ODP.02": {
        "label": "within 24 hours",
        "note": "DoD practice standard: same business day notification required"
    },
    "A.03.01.01.ODP.03": {
        "label": "within 8 business hours (same day)",
        "note": "CMMC CAG: notification upon termination; immediate action is expected by assessors"
    },
    "A.03.01.01.ODP.04": {
        "label": "within 24 hours",
        "note": "CMMC CAG: timely notification required; 24 hours is the accepted DoD practitioner standard"
    },
    "A.03.01.01.ODP.05": {
        "label": "15 minutes",
        "note": "DISA STIG upper limit: session must lock after no more than 15 minutes of inactivity (V-220726)"
    },
    "A.03.01.01.ODP.06": {
        "label": "the user leaves the workstation unattended or the session ends",
        "note": "Organization-defined condition; common values include end of work session or transitioning to a different security domain"
    },

    # A.03.01.05 — Least Privilege / Privileged Accounts
    "A.03.01.05.ODP.01": {
        "label": "quarterly (every 90 days)",
        "note": "CMMC CAG: regular review required; quarterly is the widely-accepted assessor expectation"
    },
    "A.03.01.05.ODP.02": {
        "label": "the System Owner or Information System Security Manager (ISSM)",
        "note": "Organization-defined role; must be documented in the SSP"
    },
    "A.03.01.05.ODP.03": {
        "label": "system administration, security administration, audit log access, account management, and configuration management functions",
        "note": "Organization-defined list; must align with what privileged accounts can do in your environment"
    },

    # A.03.01.06 — Non-Privileged Account Use
    "A.03.01.06.ODP.01": {
        "label": "all administrative functions including system configuration changes, user account management, audit log access, software installation, and security tool management",
        "note": "DISA STIG: administrative accounts must not be used for non-administrative functions (V-220729)"
    },

    # A.03.01.08 — Unsuccessful Login Attempts
    "A.03.01.08.ODP.01": {
        "label": "3 consecutive invalid attempts",
        "note": "DISA STIG hard upper limit: lockout threshold must be 3 or fewer invalid attempts (V-220741)"
    },
    "A.03.01.08.ODP.02": {
        "label": "15 minutes",
        "note": "DISA STIG: reset account lockout counter after 15 minutes (V-220742)"
    },
    "A.03.01.08.ODP.03": {
        "label": "15 minutes (or until unlocked by an administrator)",
        "note": "DISA STIG hard lower limit: lockout duration must be at least 15 minutes or require administrator unlock (V-220741)"
    },

    # A.03.01.10 — Session Lock
    "A.03.01.10.ODP.01": {
        "label": "15 minutes",
        "note": "DISA STIG hard upper limit: screen saver/session lock must activate after no more than 15 minutes of inactivity (V-220726)"
    },

    # A.03.01.11 — Session Termination
    "A.03.01.11.ODP.01": {
        "label": "session time limit expiration, detection of anomalous activity, explicit user logoff, or end of a defined work period",
        "note": "Organization-defined conditions; must be enumerated in the SSP"
    },

    # A.03.01.20 — External Connections
    "A.03.01.20.ODP.01": {
        "label": "all systems that store, process, or transmit CUI and all remote access connections used to access CUI",
        "note": "Organization-defined scope; DFARS 252.204-7012 defines the broader CUI boundary"
    },

    # A.03.02.01 — Policy and Procedures
    "A.03.02.01.ODP.01": {
        "label": "annually (every 12 months) or following significant changes",
        "note": "CMMC CAG: policies reviewed at least annually; 'or following significant changes' is standard DoD language"
    },
    "A.03.02.01.ODP.02": {
        "label": "annually (every 12 months) or following significant changes",
        "note": "CMMC CAG: procedures reviewed at least annually"
    },
    "A.03.02.01.ODP.03": {
        "label": "the Authorizing Official (AO) or Information System Security Manager (ISSM)",
        "note": "Organization-defined role; must be named in the SSP"
    },
    "A.03.02.01.ODP.04": {
        "label": "the Information System Security Officer (ISSO) or designated System Administrator under ISSM oversight",
        "note": "Organization-defined role; must be named in the SSP"
    },

    # A.03.02.02 — System Use Notification
    "A.03.02.02.ODP.01": {
        "label": "the DoD-approved system use notification banner",
        "note": "DISA STIG hard requirement: exact DoD warning banner text must be displayed verbatim (required on all platforms)"
    },
    "A.03.02.02.ODP.02": {
        "label": "before authentication is completed (at every login prompt)",
        "note": "DISA STIG hard requirement: banner must appear before access is granted; pre-logon display is mandatory"
    },
    "A.03.02.02.ODP.03": {
        "label": "each login session",
        "note": "DISA STIG hard requirement: user must acknowledge the banner before every session"
    },
    "A.03.02.02.ODP.04": {
        "label": "all users accessing systems that store, process, or transmit CUI",
        "note": "CMMC CAG: no exceptions — all users must acknowledge"
    },

    # A.03.03.01 — Audit Logging
    "A.03.03.01.ODP.01": {
        "label": "account logon/logoff, account management, object access to CUI, policy changes, privilege use, process tracking, system events, failed access attempts, and use of privileged functions",
        "note": "CMMC CAG AU.L2-3.3.1 and DISA Audit Policy STIG: these 9 categories are the minimum baseline; all must be enabled"
    },
    "A.03.03.01.ODP.02": {
        "label": "date/time, event type, user/process identity, source (IP or device), outcome (success/failure), and affected object",
        "note": "CMMC CAG AU.L2-3.3.1 and NIST SP 800-171 Rev 3: these fields are required in every audit record"
    },

    # A.03.03.04 — Audit Log Review
    "A.03.03.04.ODP.01": {
        "label": "weekly for routine review, with automated daily alerting for security-relevant events",
        "note": "CMMC CAG: 'regularly' required; weekly manual review plus automated alerting is the safe DoD standard"
    },
    "A.03.03.04.ODP.02": {
        "label": "the ISSO or designated Security Operations Center (SOC) personnel",
        "note": "Organization-defined role; must be documented in the SSP"
    },

    # A.03.03.05 — Audit Log Retention
    "A.03.03.05.ODP.01": {
        "label": "minimum 1 year total, with at least 90 days immediately accessible online",
        "note": "DoD policy (DoDI 8500.01) and CMMC CAG: 1 year total retention; 90-day hot storage is the DoD practitioner standard"
    },

    # A.03.03.07 — Timestamps
    "A.03.03.07.ODP.01": {
        "label": "1-second granularity, synchronized to an authoritative time source (NTP from a DoD-approved Stratum 2 server)",
        "note": "DISA STIG hard requirement: systems must sync to an authoritative time source (V-220772); 1-second granularity is the minimum for forensic utility"
    },

    # A.03.04.01 — Configuration Baselines
    "A.03.04.01.ODP.01": {
        "label": "annually or following significant system changes, security incidents, or new vulnerability disclosures",
        "note": "CMMC CAG CM.L2: baselines reviewed regularly; annual plus event-driven is the safe standard"
    },

    # A.03.04.02 — Configuration Change Control
    "A.03.04.02.ODP.01": {
        "label": "the Change Control Board (CCB) or designated Configuration Manager with ISSM concurrence",
        "note": "CMMC CAG CM.L2: designated personnel required; DoD RMF standard is CCB with security review role in the approval chain"
    },

    # A.03.04.06 — Least Functionality
    "A.03.04.06.ODP.01": {
        "label": "peer-to-peer file sharing, unauthorized remote access tools, cryptocurrency mining software, unapproved cloud sync clients",
        "note": "Organization-defined prohibited software list; must be documented in the SSP and enforced technically"
    },
    "A.03.04.06.ODP.02": {
        "label": "Telnet, FTP (plaintext), SNMPv1/v2, rsh/rlogin, and TFTP (unless operationally required)",
        "note": "DISA STIG: insecure protocols must be disabled; only explicitly required and documented services are permitted"
    },
    "A.03.04.06.ODP.03": {
        "label": "all ports and protocols not explicitly required and documented in the SSP (default-deny with allow-list)",
        "note": "Organization-defined; default-deny posture is required for CMMC compliance"
    },
    "A.03.04.06.ODP.04": {
        "label": "USB storage auto-run, Bluetooth (if not required for operations), and direct memory access from external interfaces",
        "note": "Organization-defined restricted capabilities; must be technically enforced and documented"
    },
    "A.03.04.06.ODP.05": {
        "label": "personal email clients, social media applications, and other applications not required for mission functions",
        "note": "Organization-defined based on mission; must be documented in the SSP"
    },
    "A.03.04.06.ODP.06": {
        "label": "annually or following significant system changes",
        "note": "CMMC CAG: least functionality posture reviewed regularly; annual plus event-driven is the standard"
    },

    # A.03.04.08 — Application Execution Policy
    "A.03.04.08.ODP.01": {
        "label": "organization-approved applications defined in the application allowlist",
        "note": "CMMC CAG CM.L2: org-defined allowlist required; implemented via Windows Defender Application Control (WDAC) or AppLocker per DISA STIG"
    },

    # A.03.05.01 — Identification
    "A.03.05.01.ODP.01": {
        "label": "unique username per individual user; device identifiers (hostname, MAC address, or certificate); service accounts identified by function with no shared credentials",
        "note": "CMMC CAG IA.L1 and DISA STIG: shared accounts are prohibited for CUI access"
    },

    # A.03.05.02 — Authentication
    "A.03.05.02.ODP.01": {
        "label": "multi-factor authentication (MFA) for all users; PIV/CAC preferred; MFA mandatory for privileged users and all remote access",
        "note": "CMMC CAG IA.L2-3.5.3 hard requirement: MFA required for network access and privileged accounts; DISA STIG mandates MFA for all privileged access"
    },

    # A.03.05.05 — Authenticator Management
    "A.03.05.05.ODP.01": {
        "label": "temporary passwords must meet complexity requirements, be unique per user, expire on first use, and never be transmitted in cleartext",
        "note": "DISA STIG: default/shared initial passwords must be changed immediately at first login"
    },
    "A.03.05.05.ODP.02": {
        "label": "1 day minimum password age",
        "note": "DISA STIG hard lower limit: minimum password age must be at least 1 day to prevent cycling through password history (V-220748)"
    },

    # A.03.05.07 — Password Complexity
    "A.03.05.07.ODP.01": {
        "label": "15 characters minimum",
        "note": "DISA STIG hard lower limit: minimum 14 characters (V-220749); DoD practice standard is 15 characters per current NSA/OMB M-22-09 guidance"
    },
    "A.03.05.07.ODP.02": {
        "label": "characters from at least 3 of 4 categories (uppercase, lowercase, numbers, special characters); no dictionary words; 24-password history enforced; maximum 60-day password age",
        "note": "DISA STIG hard values: complexity enabled (V-220750), history of 24 (V-220752), max age 60 days (V-220751)"
    },

    # A.03.06.02 — Contingency Plan
    "A.03.06.02.ODP.01": {
        "label": "annually (tabletop exercise minimum; full operational test where feasible)",
        "note": "CMMC CAG: annual testing is the expected floor; FedRAMP and DoD RMF both reference annual CP testing"
    },
    "A.03.06.02.ODP.02": {
        "label": "the ISSO/ISSM and designated IT recovery personnel (roles named in the Contingency Plan)",
        "note": "Organization-defined; roles must be named in both the SSP and the Contingency Plan document"
    },

    # A.03.06.03 — Contingency Plan Update
    "A.03.06.03.ODP.01": {
        "label": "annually or following significant system changes, personnel changes, or actual activation of the plan",
        "note": "CMMC CAG: 'regularly' required; annual plus event-driven is the standard"
    },

    # A.03.08.07 — Media Sanitization
    "A.03.08.07.ODP.01": {
        "label": "organization-approved and asset-tagged encrypted USB storage devices only; all personal or unapproved portable storage is prohibited",
        "note": "CMMC CAG MP.L2 and DISA STIG: removable media must be controlled and approved; unapproved devices should be technically blocked via USB port control"
    },

    # A.03.09.01 — Personnel Screening
    "A.03.09.01.ODP.01": {
        "label": "every 5 years for all personnel with CUI access, and immediately upon: credible derogatory information, significant change in duties, arrest or criminal charge, or adverse financial change indicating insider threat risk",
        "note": "DoD personnel security standard (DoDM 5200.02): 5-year reinvestigation cycle; event-driven triggers are required"
    },

    # A.03.09.02 — Personnel Termination
    "A.03.09.02.ODP.01": {
        "label": "exit interview covering CUI obligations and NDA; retrieval of all credentials and property at separation; acknowledgment that CUI confidentiality obligations survive employment (minimum 2 years post-employment)",
        "note": "CMMC CAG PS.L2 and DFARS 252.204-7012: continuing CUI obligations apply post-employment; 2 years is the safe legal/contractual standard"
    },

    # A.03.10.01 — Physical Access Log Review
    "A.03.10.01.ODP.01": {
        "label": "monthly at minimum, and immediately following any security incident or anomaly",
        "note": "CMMC CAG PE.L2: 'regularly' required; monthly is the accepted floor"
    },

    # A.03.10.02 — Physical Access Records
    "A.03.10.02.ODP.01": {
        "label": "minimum 3 years",
        "note": "NARA federal contractor records retention guidance; CMMC CAG PE.L2: org-defined; 3 years aligns with federal records requirements"
    },
    "A.03.10.02.ODP.02": {
        "label": "visitor logs, access badge issuance/termination records, PACS logs, maintenance and delivery personnel records, and key/combination issuance records",
        "note": "CMMC CAG PE.L2: types of records must be enumerated in the SSP and Physical Security Policy"
    },

    # A.03.10.06 — Alternate Work Site
    "A.03.10.06.ODP.01": {
        "label": "VPN with MFA for all CUI access; encrypted storage for CUI at rest; approved/government-furnished device only; physical privacy measures; no CUI printing at home; and incident reporting capability",
        "note": "CMMC CAG PE.L2-3.10.6 and DISA telework guidance: controls must be documented in a Telework/Remote Work Policy in the SSP"
    },

    # A.03.11.01 — Risk Assessment
    "A.03.11.01.ODP.01": {
        "label": "annually or following significant changes to the system, threat environment, or organizational mission",
        "note": "CMMC CAG RA.L2-3.11.1: annual assessment is the DoD RMF standard; event-driven reassessment is also required"
    },

    # A.03.11.02 — Vulnerability Monitoring
    "A.03.11.02.ODP.01": {
        "label": "at least monthly (weekly where tooling permits)",
        "note": "CISA BOD 19-02 and DoD ACAS policy hard lower limit: network-accessible systems must be scanned at least monthly"
    },
    "A.03.11.02.ODP.02": {
        "label": "within 72 hours of a new critical CVE being publicly disclosed or when directed by CISA/USCYBERCOM",
        "note": "CISA BOD 19-02 and DoD ACAS policy: 72-hour response to new critical disclosures is the DoD practitioner standard"
    },
    "A.03.11.02.ODP.03": {
        "label": "within 15 days of discovery for critical vulnerabilities (CVSS 9.0–10.0)",
        "note": "CISA BOD 19-02 hard upper limit: critical vulnerabilities on internet-facing systems must be remediated within 15 calendar days"
    },
    "A.03.11.02.ODP.04": {
        "label": "within 30 days of discovery for high vulnerabilities (CVSS 7.0–8.9)",
        "note": "CISA BOD 19-02 hard upper limit: high vulnerabilities must be remediated within 30 calendar days"
    },

    # A.03.12.01 — Security Assessment
    "A.03.12.01.ODP.01": {
        "label": "annually for internal assessments; every 3 years for formal C3PAO assessment (CMMC Level 2 certification cycle)",
        "note": "CMMC model: C3PAO assessment every 3 years; annual internal reviews satisfy ongoing assessment requirements per CMMC CAG CA.L2-3.12.1"
    },

    # A.03.13.09 — Transmission Confidentiality
    "A.03.13.09.ODP.01": {
        "label": "NSA/CNSSI 7003-compliant Protected Distribution Systems (PDS) or dedicated physically secured conduit with access controls equivalent to the data classification",
        "note": "CMMC CAG SC.L2-3.13.8: cryptography (TLS 1.2+ or FIPS 140-2/3 validated) is strongly preferred; physical alternative is rare and expensive — document why crypto is not feasible"
    },

    # A.03.13.10 — Network Disconnect
    "A.03.13.10.ODP.01": {
        "label": "15 minutes",
        "note": "DISA Network Infrastructure and Application STIG: network sessions must terminate after 15 minutes of inactivity; consistent with session lock requirement"
    },

    # A.03.13.11 — Cryptographic Key Management
    "A.03.13.11.ODP.01": {
        "label": "FIPS 140-2 or 140-3 validated cryptographic modules; RSA 2048-bit minimum; AES-128 minimum (AES-256 preferred); key lifecycle managed per NIST SP 800-57 Part 1; documented key custodian roles required",
        "note": "CMMC CAG SC.L2-3.13.10 hard requirement: FIPS 140-2/3 validation is mandatory for CMMC; non-FIPS cryptography is a finding"
    },

    # A.03.13.12 — Collaborative Computing
    "A.03.13.12.ODP.01": {
        "label": "all systems in CUI environments including video conferencing endpoints, webcams, microphones, smartboard systems, and screen sharing tools",
        "note": "CMMC CAG SC.L2-3.13.12: physical indicator (hardware privacy light or cover) plus software controls required; document all in-scope systems in the SSP"
    },

    # A.03.14.01 — Flaw Remediation
    "A.03.14.01.ODP.01": {
        "label": "within 72 hours of discovery or vendor notification",
        "note": "CISA BOD 19-02 and CMMC CAG SI.L1-3.14.1: 72 hours is the DoD practitioner standard for initial identification and reporting"
    },
    "A.03.14.01.ODP.02": {
        "label": "critical (CVSS 9.0–10.0): 15 days; high (CVSS 7.0–8.9): 30 days; moderate (CVSS 4.0–6.9): 60 days; low: 90 days",
        "note": "CISA BOD 19-02 hard upper limits: these tiered timelines satisfy both CMMC CAG SI.L1-3.14.1 and DISA STIG requirements"
    },

    # A.03.14.02 — Malicious Code Protection
    "A.03.14.02.ODP.01": {
        "label": "real-time/on-access scanning: continuous; scheduled full scans: weekly; signature/definition updates: daily (automatic, no older than 7 days)",
        "note": "DISA Antivirus STIG hard requirement: real-time scanning must be enabled and definitions must be no more than 7 days old"
    },
}


def replace_odp(text: str) -> str:
    """Replace {{ insert: param, ODP_ID }} tokens with labeled values and constraint notes."""
    def replacer(match):
        odp_id = match.group(1).strip()
        if odp_id in ODP_MAP:
            entry = ODP_MAP[odp_id]
            label = entry["label"]
            note = entry["note"]
            return (
                f'{label}'
                f'<mark class="stig-note" title="{note}">'
                f'CMMC/STIG'
                f'</mark>'
            )
        # Fallback: keep the ODP ID but make it readable
        return f'<mark class="stig-note" title="Organization-defined value">{odp_id}</mark>'

    return re.sub(r'\{\{\s*insert:\s*param,\s*([^}]+?)\s*\}\}', replacer, text)


def process_json(input_path: str, output_path: str):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    def walk(obj):
        if isinstance(obj, str):
            return replace_odp(obj)
        elif isinstance(obj, list):
            return [walk(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: walk(v) for k, v in obj.items()}
        return obj

    processed = walk(data)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(processed, f, indent=2, ensure_ascii=False)

    print(f"Done. Written to {output_path}")

    # Report any remaining unresolved tokens
    remaining = re.findall(r'\{\{[^}]+\}\}', json.dumps(processed))
    if remaining:
        print(f"\nUnresolved tokens ({len(remaining)}):")
        for t in sorted(set(remaining)):
            print(f"  {t}")
    else:
        print("All tokens resolved.")


if __name__ == "__main__":
    import os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    process_json(
        os.path.join(base, "data", "cmmc-practices.json"),
        os.path.join(base, "data", "cmmc-practices.json"),
    )
