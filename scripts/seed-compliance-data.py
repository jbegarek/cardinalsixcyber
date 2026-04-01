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
# Main — Task 2 will add OSCAL fetch + JSON generation here
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    _validate()

    # TODO (Task 2): Fetch NIST OSCAL catalog data and generate JSON output
    # files for the compliance tracker frontend.
