#!/usr/bin/env python3
"""
seed-compliance-data.py — Cardinal Six Cyber compliance data seeder.

Generates the CMMC ↔ NIST 800-171 mapping data used by the compliance tracker.
Maps all 110 NIST SP 800-171 Rev 2 security requirements to their corresponding
CMMC Model v2.0 practice metadata.

Usage:
    python scripts/seed-compliance-data.py
"""

import json
import os
import urllib.request

# ---------------------------------------------------------------------------
# CMMC Domain definitions
# ---------------------------------------------------------------------------
DOMAINS = {
    "AC": "Access Control",
    "AT": "Awareness & Training",
    "AU": "Audit & Accountability",
    "CM": "Configuration Management",
    "IA": "Identification & Authentication",
    "IR": "Incident Response",
    "MA": "Maintenance",
    "MP": "Media Protection",
    "PS": "Personnel Security",
    "PE": "Physical Protection",
    "RA": "Risk Assessment",
    "CA": "Security Assessment",
    "SC": "System & Communications Protection",
    "SI": "System & Information Integrity",
}

# NIST 800-171 family prefix → CMMC domain code
FAMILY_TO_DOMAIN = {
    "3.1":  "AC",
    "3.2":  "AT",
    "3.3":  "AU",
    "3.4":  "CM",
    "3.5":  "IA",
    "3.6":  "IR",
    "3.7":  "MA",
    "3.8":  "MP",
    "3.9":  "PS",
    "3.10": "PE",
    "3.11": "RA",
    "3.12": "CA",
    "3.13": "SC",
    "3.14": "SI",
}

# The 17 Level 1 (FCI) practices — these map to CMMC L1
LEVEL_1_REQUIREMENTS = frozenset([
    "3.1.1", "3.1.2", "3.1.20", "3.1.22",
    "3.3.5",
    "3.4.1", "3.4.2",
    "3.5.1", "3.5.2", "3.5.7",
    "3.8.3",
    "3.10.1", "3.10.3", "3.10.4", "3.10.5",
    "3.13.1",
    "3.14.1",
])


def _family(req_id: str) -> str:
    """Return the NIST 800-171 family prefix from a requirement ID."""
    parts = req_id.split(".")
    return f"{parts[0]}.{parts[1]}"


def _build_entry(req_id: str) -> dict:
    """Build a single CMMC mapping entry for a given 800-171 requirement ID."""
    level = 1 if req_id in LEVEL_1_REQUIREMENTS else 2
    domain_code = FAMILY_TO_DOMAIN[_family(req_id)]
    practice_id = f"{domain_code}.L{level}-{req_id}"
    return {
        "practiceId": practice_id,
        "domain": DOMAINS[domain_code],
        "domainCode": domain_code,
        "level": level,
    }


# ---------------------------------------------------------------------------
# Complete mapping: all 110 NIST SP 800-171 Rev 2 requirements
# ---------------------------------------------------------------------------
# fmt: off
ALL_REQUIREMENT_IDS = [
    # 3.1.x — Access Control (22 requirements)
    "3.1.1",  "3.1.2",  "3.1.3",  "3.1.4",  "3.1.5",
    "3.1.6",  "3.1.7",  "3.1.8",  "3.1.9",  "3.1.10",
    "3.1.11", "3.1.12", "3.1.13", "3.1.14", "3.1.15",
    "3.1.16", "3.1.17", "3.1.18", "3.1.19", "3.1.20",
    "3.1.21", "3.1.22",
    # 3.2.x — Awareness & Training (3 requirements)
    "3.2.1",  "3.2.2",  "3.2.3",
    # 3.3.x — Audit & Accountability (9 requirements)
    "3.3.1",  "3.3.2",  "3.3.3",  "3.3.4",  "3.3.5",
    "3.3.6",  "3.3.7",  "3.3.8",  "3.3.9",
    # 3.4.x — Configuration Management (9 requirements)
    "3.4.1",  "3.4.2",  "3.4.3",  "3.4.4",  "3.4.5",
    "3.4.6",  "3.4.7",  "3.4.8",  "3.4.9",
    # 3.5.x — Identification & Authentication (11 requirements)
    "3.5.1",  "3.5.2",  "3.5.3",  "3.5.4",  "3.5.5",
    "3.5.6",  "3.5.7",  "3.5.8",  "3.5.9",  "3.5.10",
    "3.5.11",
    # 3.6.x — Incident Response (3 requirements)
    "3.6.1",  "3.6.2",  "3.6.3",
    # 3.7.x — Maintenance (6 requirements)
    "3.7.1",  "3.7.2",  "3.7.3",  "3.7.4",  "3.7.5",
    "3.7.6",
    # 3.8.x — Media Protection (9 requirements)
    "3.8.1",  "3.8.2",  "3.8.3",  "3.8.4",  "3.8.5",
    "3.8.6",  "3.8.7",  "3.8.8",  "3.8.9",
    # 3.9.x — Personnel Security (2 requirements)
    "3.9.1",  "3.9.2",
    # 3.10.x — Physical Protection (6 requirements)
    "3.10.1", "3.10.2", "3.10.3", "3.10.4", "3.10.5",
    "3.10.6",
    # 3.11.x — Risk Assessment (3 requirements)
    "3.11.1", "3.11.2", "3.11.3",
    # 3.12.x — Security Assessment (4 requirements)
    "3.12.1", "3.12.2", "3.12.3", "3.12.4",
    # 3.13.x — System & Communications Protection (16 requirements)
    "3.13.1",  "3.13.2",  "3.13.3",  "3.13.4",  "3.13.5",
    "3.13.6",  "3.13.7",  "3.13.8",  "3.13.9",  "3.13.10",
    "3.13.11", "3.13.12", "3.13.13", "3.13.14", "3.13.15",
    "3.13.16",
    # 3.14.x — System & Information Integrity (7 requirements)
    "3.14.1", "3.14.2", "3.14.3", "3.14.4", "3.14.5",
    "3.14.6", "3.14.7",
]
# fmt: on

CMMC_MAPPING = {req_id: _build_entry(req_id) for req_id in ALL_REQUIREMENT_IDS}


# ---------------------------------------------------------------------------
# NIST SP 800-171 Rev 2 fallback data for controls absent/withdrawn in Rev 3
# Source: NIST SP 800-171 Rev 2 (February 2020)
# ---------------------------------------------------------------------------
REV2_FALLBACK: dict[str, dict] = {
    "3.1.13": {"title": "Employ Cryptographic Mechanisms to Protect the Confidentiality of Remote Access Sessions", "description": "Employ cryptographic mechanisms to protect the confidentiality of remote access sessions."},
    "3.1.14": {"title": "Route Remote Access via Managed Access Control Points", "description": "Route remote access via managed access control points."},
    "3.1.15": {"title": "Authorize Remote Execution of Privileged Commands and Remote Access to Security-Relevant Information", "description": "Authorize remote execution of privileged commands and remote access to security-relevant information."},
    "3.1.17": {"title": "Protect Wireless Access Using Authentication and Encryption", "description": "Protect wireless access using authentication and encryption."},
    "3.1.19": {"title": "Encrypt CUI on Mobile Devices and Mobile Computing Platforms", "description": "Encrypt CUI on mobile devices and mobile computing platforms."},
    "3.1.21": {"title": "Limit Use of Portable Storage Devices on External Systems", "description": "Limit use of organizational portable storage devices on external systems."},
    "3.2.3":  {"title": "Provide Security Awareness Training on Recognizing and Reporting Potential Indicators of Insider Threat", "description": "Provide security awareness training on recognizing and reporting potential indicators of insider threat."},
    "3.3.9":  {"title": "Provide a System Capability That Compares and Synchronizes Internal System Clocks", "description": "Provide a system capability that compares and synchronizes internal system clocks with an authoritative source to generate time stamps for audit records."},
    "3.4.7":  {"title": "Restrict, Disable, or Prevent the Use of Nonessential Programs, Functions, Ports, Protocols, and Services", "description": "Restrict, disable, or prevent the use of nonessential programs, functions, ports, protocols, and services."},
    "3.4.9":  {"title": "Control and Monitor User-Installed Software", "description": "Control and monitor user-installed software."},
    "3.5.6":  {"title": "Disable Identifier After a Defined Period of Inactivity", "description": "Disable identifiers after a defined period of inactivity."},
    "3.5.8":  {"title": "Implement Replay-Resistant Authentication Mechanisms for Network Access to Non-Privileged Accounts", "description": "Implement replay-resistant authentication mechanisms for network access to non-privileged accounts."},
    "3.5.9":  {"title": "Allow Temporary Password Use for System Logons with an Immediate Change to a Permanent Password", "description": "Allow temporary password use for system logons with an immediate change to a permanent password."},
    "3.5.10": {"title": "Store and Transmit Only Cryptographically-Protected Passwords", "description": "Store and transmit only cryptographically-protected passwords."},
    "3.7.1":  {"title": "Perform Maintenance on Organizational Systems", "description": "Perform maintenance on organizational systems."},
    "3.7.2":  {"title": "Provide Controls on the Tools, Techniques, Mechanisms, and Personnel Used to Conduct System Maintenance", "description": "Provide controls on the tools, techniques, mechanisms, and personnel used to conduct system maintenance."},
    "3.7.3":  {"title": "Ensure Equipment Removed for Off-Site Maintenance Is Sanitized of Any CUI", "description": "Ensure equipment removed for off-site maintenance is sanitized of any CUI."},
    "3.8.6":  {"title": "Implement Cryptographic Mechanisms to Protect the Confidentiality of CUI Stored on Digital Media During Transport", "description": "Implement cryptographic mechanisms to protect the confidentiality of CUI stored on digital media during transport unless otherwise protected by alternative physical safeguards."},
    "3.8.8":  {"title": "Prohibit the Use of Portable Storage Devices When Such Devices Have No Identifiable Owner", "description": "Prohibit the use of portable storage devices when such devices have no identifiable owner."},
    "3.10.3": {"title": "Escort Visitors and Monitor Visitor Activity", "description": "Escort visitors and monitor visitor activity."},
    "3.10.4": {"title": "Maintain Audit Logs of Physical Access", "description": "Maintain audit logs of physical access."},
    "3.10.5": {"title": "Control and Manage Physical Access Devices", "description": "Control and manage physical access devices."},
    "3.11.3": {"title": "Remediate Vulnerabilities in Accordance with Risk Assessments", "description": "Remediate vulnerabilities in accordance with risk assessments."},
    "3.12.4": {"title": "Develop, Document, and Periodically Update System Security Plans", "description": "Develop, document, and periodically update system security plans that describe system boundaries, system environments of operation, how security requirements are implemented, and the relationships with or connections to other systems."},
    "3.13.2": {"title": "Employ Architectural Designs, Software Development Techniques, and Systems Engineering Principles That Promote Effective Information Security", "description": "Employ architectural designs, software development techniques, and systems engineering principles that promote effective information security within organizational systems."},
    "3.13.3": {"title": "Separate User Functionality from System Management Functionality", "description": "Separate user functionality from system management functionality."},
    "3.13.5": {"title": "Implement Subnetworks for Publicly Accessible System Components That Are Physically or Logically Separated from Internal Networks", "description": "Implement subnetworks for publicly accessible system components that are physically or logically separated from internal networks."},
    "3.13.7": {"title": "Prevent Remote Devices from Simultaneously Establishing Non-Remote Connections with Organizational Systems and Communicating via Some Other Connection to Resources in External Networks (Split Tunneling)", "description": "Prevent remote devices from simultaneously establishing non-remote connections with organizational systems and communicating via some other connection to resources in external networks (i.e., split tunneling)."},
    "3.13.14": {"title": "Control and Monitor the Use of Voice over Internet Protocol (VoIP) Technologies", "description": "Control and monitor the use of Voice over Internet Protocol (VoIP) technologies."},
    "3.13.16": {"title": "Protect the Confidentiality of CUI at Rest", "description": "Protect the confidentiality of CUI at rest."},
    "3.14.4": {"title": "Update Malicious Code Protection Mechanisms When New Releases Are Available", "description": "Update malicious code protection mechanisms when new releases are available."},
    "3.14.5": {"title": "Perform Periodic Scans of Organizational Systems and Real-Time Scans of Files from External Sources", "description": "Perform periodic scans of organizational systems and real-time scans of files from external sources as files are downloaded, opened, or executed."},
    "3.14.7": {"title": "Identify Unauthorized Use of Organizational Systems", "description": "Identify unauthorized use of organizational systems."},
}


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------
def _validate():
    """Verify the mapping is correct and complete."""
    assert len(CMMC_MAPPING) == 110, f"Expected 110 entries, got {len(CMMC_MAPPING)}"

    l1_count = sum(1 for v in CMMC_MAPPING.values() if v["level"] == 1)
    assert l1_count == 17, f"Expected 17 Level 1 practices, got {l1_count}"

    l2_count = sum(1 for v in CMMC_MAPPING.values() if v["level"] == 2)
    assert l2_count == 93, f"Expected 93 Level 2 practices, got {l2_count}"

    # Verify all 14 domains are represented
    domains_seen = {v["domainCode"] for v in CMMC_MAPPING.values()}
    assert len(domains_seen) == 14, f"Expected 14 domains, got {len(domains_seen)}"

    # Verify practice ID format
    for req_id, entry in CMMC_MAPPING.items():
        expected_level = 1 if req_id in LEVEL_1_REQUIREMENTS else 2
        expected_pid = f"{entry['domainCode']}.L{expected_level}-{req_id}"
        assert entry["practiceId"] == expected_pid, (
            f"Practice ID mismatch for {req_id}: {entry['practiceId']} != {expected_pid}"
        )

    print(f"Validation passed: {len(CMMC_MAPPING)} requirements mapped")
    print(f"  Level 1: {l1_count} practices")
    print(f"  Level 2: {l2_count} practices")
    print(f"  Domains: {len(domains_seen)}")


# ---------------------------------------------------------------------------
# NIST 800-171 → 800-53 Cross-Reference (from SP 800-171 Rev 2, Appendix D)
# ---------------------------------------------------------------------------
NIST_800_53_MAP: dict[str, list[str]] = {
    "3.1.1":  ["AC-2", "AC-3", "AC-17"],
    "3.1.2":  ["AC-3", "AC-4", "SC-7"],
    "3.1.3":  ["AC-4"],
    "3.1.4":  ["AC-5"],
    "3.1.5":  ["AC-6", "AC-6(1)", "AC-6(5)"],
    "3.1.6":  ["AC-6(2)"],
    "3.1.7":  ["AC-6(9)", "AC-6(10)"],
    "3.1.8":  ["AC-7"],
    "3.1.9":  ["AC-8"],
    "3.1.10": ["AC-11", "AC-11(1)"],
    "3.1.11": ["AC-12"],
    "3.1.12": ["AC-17(1)", "AC-17(2)"],
    "3.1.13": ["AC-17(3)"],
    "3.1.14": ["AC-17(4)"],
    "3.1.15": ["AC-18"],
    "3.1.16": ["AC-18(1)"],
    "3.1.17": ["AC-18(3)"],
    "3.1.18": ["AC-19"],
    "3.1.19": ["AC-19(5)"],
    "3.1.20": ["AC-20", "AC-20(1)"],
    "3.1.21": ["AC-20(2)"],
    "3.1.22": ["AC-22"],
    "3.2.1":  ["AT-2"],
    "3.2.2":  ["AT-2(2)"],
    "3.2.3":  ["AT-3"],
    "3.3.1":  ["AU-2", "AU-3", "AU-3(1)", "AU-12"],
    "3.3.2":  ["AU-6"],
    "3.3.3":  ["AU-6(3)"],
    "3.3.4":  ["AU-7"],
    "3.3.5":  ["AU-8"],
    "3.3.6":  ["AU-9"],
    "3.3.7":  ["AU-9(4)"],
    "3.3.8":  ["AU-11"],
    "3.3.9":  ["AU-12(3)"],
    "3.4.1":  ["CM-2", "CM-6", "CM-8", "CM-8(1)"],
    "3.4.2":  ["CM-2", "CM-6", "CM-8", "CM-8(1)"],
    "3.4.3":  ["CM-3"],
    "3.4.4":  ["CM-3(2)"],
    "3.4.5":  ["CM-5"],
    "3.4.6":  ["CM-7"],
    "3.4.7":  ["CM-7(1)", "CM-7(2)"],
    "3.4.8":  ["CM-7(4)", "CM-7(5)"],
    "3.4.9":  ["CM-11"],
    "3.5.1":  ["IA-2", "IA-5"],
    "3.5.2":  ["IA-2", "IA-5"],
    "3.5.3":  ["IA-2(1)", "IA-2(2)"],
    "3.5.4":  ["IA-2(8)", "IA-2(9)"],
    "3.5.5":  ["IA-4"],
    "3.5.6":  ["IA-4"],
    "3.5.7":  ["IA-5(1)"],
    "3.5.8":  ["IA-5(1)"],
    "3.5.9":  ["IA-5(2)"],
    "3.5.10": ["IA-6"],
    "3.5.11": ["IA-8"],
    "3.6.1":  ["IR-2", "IR-4", "IR-5", "IR-6", "IR-7"],
    "3.6.2":  ["IR-6"],
    "3.6.3":  ["IR-3"],
    "3.7.1":  ["MA-2"],
    "3.7.2":  ["MA-3", "MA-3(1)", "MA-3(2)"],
    "3.7.3":  ["MA-4"],
    "3.7.4":  ["MA-4(2)"],
    "3.7.5":  ["MA-5"],
    "3.7.6":  ["MA-6"],
    "3.8.1":  ["MP-2", "MP-4", "MP-6"],
    "3.8.2":  ["MP-2"],
    "3.8.3":  ["MP-4"],
    "3.8.4":  ["MP-5"],
    "3.8.5":  ["MP-5(4)"],
    "3.8.6":  ["MP-6"],
    "3.8.7":  ["MP-7"],
    "3.8.8":  ["MP-7(1)"],
    "3.8.9":  ["SC-28"],
    "3.9.1":  ["PS-3", "PS-4", "PS-5"],
    "3.9.2":  ["PS-4", "PS-5"],
    "3.10.1": ["PE-2", "PE-6"],
    "3.10.2": ["PE-2"],
    "3.10.3": ["PE-3"],
    "3.10.4": ["PE-5"],
    "3.10.5": ["PE-6"],
    "3.10.6": ["PE-17"],
    "3.11.1": ["RA-3"],
    "3.11.2": ["RA-5", "RA-5(5)"],
    "3.11.3": ["RA-5"],
    "3.12.1": ["CA-2", "CA-5", "CA-7"],
    "3.12.2": ["CA-2"],
    "3.12.3": ["CA-7"],
    "3.12.4": ["CA-9", "PL-2"],
    "3.13.1": ["SC-7"],
    "3.13.2": ["SA-8"],
    "3.13.3": ["AC-4", "SC-7(5)"],
    "3.13.4": ["SC-2"],
    "3.13.5": ["SC-4"],
    "3.13.6": ["SC-7(7)"],
    "3.13.7": ["SC-7(5)"],
    "3.13.8": ["SC-8", "SC-8(1)"],
    "3.13.9": ["SC-10"],
    "3.13.10": ["SC-12"],
    "3.13.11": ["SC-13"],
    "3.13.12": ["SC-15"],
    "3.13.13": ["SC-18"],
    "3.13.14": ["SC-23"],
    "3.13.15": ["SC-28"],
    "3.13.16": ["SC-39"],
    "3.14.1": ["SI-2", "SI-3", "SI-5"],
    "3.14.2": ["SI-2"],
    "3.14.3": ["SI-3"],
    "3.14.4": ["SI-4"],
    "3.14.5": ["SI-4(4)"],
    "3.14.6": ["SI-5"],
    "3.14.7": ["SI-7"],
}


# ---------------------------------------------------------------------------
# OSCAL Fetch & Parse
# ---------------------------------------------------------------------------
# We fetch the NIST SP 800-171 Rev 3 OSCAL catalog (Rev 2 was removed from
# the OSCAL-content repo). Controls 03.01–03.14 map 1:1 to Rev 2's 3.1–3.14
# families, so we convert IDs (03.01.01 → 3.1.1) and extract content only
# for the 110 requirements in our CMMC mapping.
OSCAL_URL = (
    "https://raw.githubusercontent.com/usnistgov/oscal-content/main/"
    "nist.gov/SP800-171/rev3/json/NIST_SP800-171_rev3_catalog.json"
)


def _rev3_to_rev2(sort_id: str) -> str:
    """Convert Rev 3 sort-id (03.01.01) to Rev 2 format (3.1.1)."""
    parts = sort_id.split(".")
    return ".".join(str(int(p)) for p in parts)


def _extract_description(control: dict) -> str:
    """Extract the description/statement text from an OSCAL control.

    Tries the statement part first, then falls back to guidance.
    """
    for part in control.get("parts", []):
        if part.get("name") == "statement":
            items = []
            if part.get("prose"):
                items.append(part["prose"])
            for sub in part.get("parts", []):
                if sub.get("prose"):
                    items.append(sub["prose"].strip())
                for subsub in sub.get("parts", []):
                    if subsub.get("prose"):
                        items.append(subsub["prose"].strip())
            if items:
                return " ".join(items)

    # Fallback: use guidance prose
    for part in control.get("parts", []):
        if part.get("name") == "guidance" and part.get("prose"):
            return part["prose"].strip()

    return ""


def _extract_assessment_objectives(control: dict) -> list[str]:
    """Extract assessment objective prose strings from an OSCAL control."""
    objectives = []
    for part in control.get("parts", []):
        if part.get("name") == "assessment-objective" and part.get("prose"):
            objectives.append(part["prose"].strip())
    return objectives


def _fetch_oscal_catalog() -> dict[str, dict]:
    """Fetch the OSCAL catalog and return a dict keyed by Rev 2 ID.

    Each value has keys: title, family, familyCode, description,
    assessmentObjectives.
    """
    print(f"Fetching OSCAL catalog from {OSCAL_URL} ...")
    resp = urllib.request.urlopen(OSCAL_URL)
    data = json.loads(resp.read())
    catalog = data["catalog"]

    result: dict[str, dict] = {}
    rev2_set = set(ALL_REQUIREMENT_IDS)

    for group in catalog.get("groups", []):
        group_title = group.get("title", "")
        # familyCode in Rev 3: "SP_800_171_03.01" → extract "03.01"
        group_sort_prefix = group.get("id", "").replace("SP_800_171_", "")

        for control in group.get("controls", []):
            # Get sort-id from props
            sort_id = None
            for prop in control.get("props", []):
                if prop["name"] == "sort-id":
                    sort_id = prop["value"]
                    break
            if not sort_id:
                continue

            rev2_id = _rev3_to_rev2(sort_id)
            if rev2_id not in rev2_set:
                continue

            title = control.get("title", "")
            description = _extract_description(control)
            objectives = _extract_assessment_objectives(control)

            # Apply Rev 2 fallback for controls withdrawn/empty in Rev 3
            fallback = REV2_FALLBACK.get(rev2_id)
            if fallback:
                if not description or title == sort_id:
                    title = fallback.get("title", title)
                    description = fallback.get("description", description)
            elif title == sort_id:
                # Title is just the sort-id — not a real title
                title = ""

            result[rev2_id] = {
                "title": title,
                "family": group_title,
                "familyCode": _rev3_to_rev2(
                    group_sort_prefix.replace("SP_800_171_", "")
                ) if "." in group_sort_prefix else group_sort_prefix,
                "description": description,
                "assessmentObjectives": objectives,
            }

    print(f"  Parsed {len(result)} controls from OSCAL catalog")
    return result


# ---------------------------------------------------------------------------
# Slug helpers
# ---------------------------------------------------------------------------
def _slug_171(req_id: str) -> str:
    """3.1.1 → '3-1-1'"""
    return req_id.replace(".", "-")


def _slug_cmmc(practice_id: str) -> str:
    """AC.L2-3.1.1 → 'ac-l2-3-1-1'"""
    return practice_id.lower().replace(".", "-")


# ---------------------------------------------------------------------------
# JSON generation
# ---------------------------------------------------------------------------
def _generate_nist_json(oscal: dict[str, dict]) -> list[dict]:
    """Build the nist-800-171.json requirements list."""
    requirements = []
    for req_id in ALL_REQUIREMENT_IDS:
        info = oscal.get(req_id, {})
        cmmc = CMMC_MAPPING[req_id]
        practice_slug = _slug_cmmc(cmmc["practiceId"])

        requirements.append({
            "id": _slug_171(req_id),
            "displayId": req_id,
            "title": info.get("title", ""),
            "family": info.get("family", cmmc["domain"]),
            "familyCode": _family(req_id),
            "description": info.get("description", ""),
            "assessmentObjectives": info.get("assessmentObjectives", []),
            "nist80053": NIST_800_53_MAP.get(req_id, []),
            "cmmcPractices": [practice_slug],
            "notes": None,
        })
    return requirements


def _generate_cmmc_json(oscal: dict[str, dict]) -> list[dict]:
    """Build the cmmc-practices.json practices list."""
    practices = []
    for req_id in ALL_REQUIREMENT_IDS:
        info = oscal.get(req_id, {})
        cmmc = CMMC_MAPPING[req_id]
        practice_id = cmmc["practiceId"]

        practices.append({
            "id": _slug_cmmc(practice_id),
            "displayId": practice_id,
            "title": info.get("title", ""),
            "domain": cmmc["domain"],
            "domainCode": cmmc["domainCode"],
            "level": cmmc["level"],
            "description": info.get("description", ""),
            "assessmentObjectives": info.get("assessmentObjectives", []),
            "nist800171": [_slug_171(req_id)],
            "nist80053": NIST_800_53_MAP.get(req_id, []),
            "notes": None,
        })
    return practices


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    _validate()

    # Fetch OSCAL data
    oscal_data = _fetch_oscal_catalog()

    # Ensure data/ directory exists
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(data_dir, exist_ok=True)

    # Generate NIST 800-171 JSON
    nist_reqs = _generate_nist_json(oscal_data)
    nist_path = os.path.join(data_dir, "nist-800-171.json")
    with open(nist_path, "w", encoding="utf-8") as f:
        json.dump({"requirements": nist_reqs}, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(nist_reqs)} requirements to {nist_path}")

    # Generate CMMC practices JSON
    cmmc_practices = _generate_cmmc_json(oscal_data)
    cmmc_path = os.path.join(data_dir, "cmmc-practices.json")
    with open(cmmc_path, "w", encoding="utf-8") as f:
        json.dump({"practices": cmmc_practices}, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(cmmc_practices)} practices to {cmmc_path}")

    # Post-generation validation
    l1 = sum(1 for p in cmmc_practices if p["level"] == 1)
    l2 = sum(1 for p in cmmc_practices if p["level"] == 2)
    print(f"\nPost-generation validation:")
    print(f"  CMMC practices: {len(cmmc_practices)} (L1: {l1}, L2: {l2})")
    print(f"  NIST requirements: {len(nist_reqs)}")

    # Verify cross-references
    cmmc_slugs = {p["id"] for p in cmmc_practices}
    nist_slugs = {r["id"] for r in nist_reqs}
    for r in nist_reqs:
        for cs in r["cmmcPractices"]:
            assert cs in cmmc_slugs, f"Broken xref: NIST {r['id']} → CMMC {cs}"
    for p in cmmc_practices:
        for ns in p["nist800171"]:
            assert ns in nist_slugs, f"Broken xref: CMMC {p['id']} → NIST {ns}"
    print("  Cross-references: all valid")

    # Verify titles populated from OSCAL
    titled = sum(1 for p in cmmc_practices if p["title"])
    print(f"  Titles populated: {titled}/{len(cmmc_practices)}")

    print("\nDone.")
