"""
Parse DISA STIG XCCDF XML files from zip archives into JSON for the site.
Usage: python scripts/parse_stigs.py
Outputs: data/stigs/<slug>.json + data/stig-index.json
"""

import json
import os
import re
import zipfile
from xml.etree import ElementTree as ET

NS = {"x": "http://checklists.nist.gov/xccdf/1.1"}

STIG_TARGETS = [
    {
        "zip": "U_MS_Windows_Server_2022_V2R7_STIG.zip",
        "slug": "windows-server-2022",
        "label": "Windows Server 2022",
        "category": "Operating System",
        "icon": "windows",
    },
    {
        "zip": "U_MS_Windows_Server_2019_V3R7_STIG.zip",
        "slug": "windows-server-2019",
        "label": "Windows Server 2019",
        "category": "Operating System",
        "icon": "windows",
    },
    {
        "zip": "U_MS_Windows_11_V2R6_STIG.zip",
        "slug": "windows-11",
        "label": "Windows 11",
        "category": "Operating System",
        "icon": "windows",
    },
    {
        "zip": "U_Active_Directory_Domain_V3R6_STIG.zip",
        "slug": "active-directory-domain",
        "label": "Active Directory Domain",
        "category": "Directory Services",
        "icon": "directory",
    },
    {
        "zip": "U_MS_Defender_Antivirus_V2R7_STIG.zip",
        "slug": "ms-defender-antivirus",
        "label": "Microsoft Defender Antivirus",
        "category": "Endpoint Security",
        "icon": "shield",
    },
    {
        "zip": "U_Google_Chrome_V2R11_STIG.zip",
        "slug": "google-chrome",
        "label": "Google Chrome",
        "category": "Browser",
        "icon": "browser",
    },
    {
        "zip": "U_RHEL_9_V2R7_STIG.zip",
        "slug": "rhel-9",
        "label": "Red Hat Enterprise Linux 9",
        "category": "Operating System",
        "icon": "linux",
    },
    {
        "zip": "U_MS_IIS_10-0_Y26M01_STIG.zip",
        "slug": "iis-10",
        "label": "Microsoft IIS 10.0",
        "category": "Web Server",
        "icon": "server",
    },
]


def parse_description_xml(raw: str) -> dict:
    """Parse the STIG description field which is XML-in-text."""
    try:
        wrapped = f"<root>{raw}</root>"
        elem = ET.fromstring(wrapped)
        def text(tag):
            el = elem.find(tag)
            return (el.text or "").strip() if el is not None else ""
        return {
            "discussion": text("VulnDiscussion"),
            "falsePositives": text("FalsePositives"),
            "falseNegatives": text("FalseNegatives"),
            "documentable": text("Documentable").lower() == "true",
            "mitigations": text("Mitigations"),
            "severityOverrideGuidance": text("SeverityOverrideGuidance"),
            "potentialImpact": text("PotentialImpacts"),
            "thirdPartyTools": text("ThirdPartyTools"),
            "mitigationControl": text("MitigationControl"),
            "responsibility": text("Responsibility"),
            "iaControls": text("IAControls"),
        }
    except ET.ParseError:
        return {"discussion": raw.strip()}


SEVERITY_MAP = {"high": "CAT I", "medium": "CAT II", "low": "CAT III"}
CAT_ORDER = {"high": 1, "medium": 2, "low": 3}


def find_xccdf(zf: zipfile.ZipFile) -> str | None:
    for name in zf.namelist():
        if name.endswith("-xccdf.xml") or name.endswith("_Manual-xccdf.xml"):
            return name
    # fallback: any xml
    for name in zf.namelist():
        if name.endswith(".xml") and "xccdf" in name.lower():
            return name
    return None


def parse_stig(zip_path: str, meta: dict) -> dict:
    with zipfile.ZipFile(zip_path) as zf:
        xccdf_path = find_xccdf(zf)
        if not xccdf_path:
            raise FileNotFoundError(f"No XCCDF found in {zip_path}")
        xml_bytes = zf.read(xccdf_path)

    root = ET.fromstring(xml_bytes)

    benchmark_title = (root.find("x:title", NS) or root).text or meta["label"]
    version_el = root.find(".//x:version", NS)
    plain_version = version_el.text.strip() if version_el is not None else ""
    release_el = root.find(".//x:plain-text[@id='release-info']", NS)
    release_info = release_el.text.strip() if release_el is not None else ""

    rules = []
    groups = root.findall("x:Group", NS)

    for group in groups:
        vuln_id = group.get("id", "")  # e.g. V-254238
        rule_el = group.find("x:Rule", NS)
        if rule_el is None:
            continue

        rule_id = rule_el.get("id", "")
        severity = rule_el.get("severity", "medium")
        stig_id_el = rule_el.find("x:version", NS)
        stig_id = stig_id_el.text.strip() if stig_id_el is not None else ""

        title_el = rule_el.find("x:title", NS)
        title = title_el.text.strip() if title_el is not None else ""

        desc_el = rule_el.find("x:description", NS)
        desc_raw = desc_el.text or "" if desc_el is not None else ""
        desc = parse_description_xml(desc_raw)

        fix_el = rule_el.find("x:fixtext", NS)
        fix_text = fix_el.text.strip() if fix_el is not None and fix_el.text else ""

        check_content_el = rule_el.find(".//x:check-content", NS)
        check_text = check_content_el.text.strip() if check_content_el is not None and check_content_el.text else ""

        # CCI refs → NIST 800-53 mapping
        cci_refs = []
        for ident in rule_el.findall("x:ident", NS):
            val = (ident.text or "").strip()
            if val.startswith("CCI-"):
                cci_refs.append(val)

        rules.append({
            "vulnId": vuln_id,
            "ruleId": rule_id,
            "stigId": stig_id,
            "severity": severity,
            "cat": SEVERITY_MAP.get(severity, "CAT II"),
            "title": title,
            "discussion": desc.get("discussion", ""),
            "checkText": check_text,
            "fixText": fix_text,
            "cciRefs": cci_refs,
            "documentable": desc.get("documentable", False),
            "responsibility": desc.get("responsibility", ""),
            "mitigations": desc.get("mitigations", ""),
            "falsePositives": desc.get("falsePositives", ""),
            "falseNegatives": desc.get("falseNegatives", ""),
        })

    # Sort CAT I → II → III
    rules.sort(key=lambda r: (CAT_ORDER.get(r["severity"], 99), r["stigId"]))

    counts = {"high": 0, "medium": 0, "low": 0}
    for r in rules:
        counts[r["severity"]] = counts.get(r["severity"], 0) + 1

    return {
        "slug": meta["slug"],
        "label": meta["label"],
        "benchmarkTitle": benchmark_title,
        "version": plain_version,
        "releaseInfo": release_info,
        "category": meta["category"],
        "icon": meta["icon"],
        "totalRules": len(rules),
        "catI": counts["high"],
        "catII": counts["medium"],
        "catIII": counts["low"],
        "rules": rules,
    }


def main():
    lib_dir = os.path.join("temp", "CUI_SRG-STIG_Library")
    out_dir = os.path.join("data", "stigs")
    os.makedirs(out_dir, exist_ok=True)

    index = []

    for meta in STIG_TARGETS:
        zip_path = os.path.join(lib_dir, meta["zip"])
        if not os.path.exists(zip_path):
            print(f"SKIP (not found): {meta['zip']}")
            continue

        print(f"Parsing {meta['label']}...", end=" ", flush=True)
        try:
            data = parse_stig(zip_path, meta)
        except Exception as e:
            print(f"ERROR: {e}")
            continue

        out_path = os.path.join(out_dir, f"{meta['slug']}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        index.append({
            "slug": data["slug"],
            "label": data["label"],
            "benchmarkTitle": data["benchmarkTitle"],
            "version": data["version"],
            "releaseInfo": data["releaseInfo"],
            "category": data["category"],
            "icon": data["icon"],
            "totalRules": data["totalRules"],
            "catI": data["catI"],
            "catII": data["catII"],
            "catIII": data["catIII"],
        })

        print(f"{data['totalRules']} rules (CAT I: {data['catI']}, II: {data['catII']}, III: {data['catIII']})")

    with open(os.path.join("data", "stig-index.json"), "w", encoding="utf-8") as f:
        json.dump({"benchmarks": index}, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Index written with {len(index)} benchmarks.")


if __name__ == "__main__":
    main()
