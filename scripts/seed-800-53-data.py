#!/usr/bin/env python3
"""
Fetch NIST SP 800-53 Rev 5 controls from the OSCAL catalog and generate
data/nist-800-53.json with cross-references to CMMC practices and 800-171.
"""

import json
import os
import re
import urllib.request

OSCAL_URL = (
    "https://raw.githubusercontent.com/usnistgov/oscal-content/"
    "main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json"
)

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def oscal_id_to_display(oscal_id: str) -> str:
    """Convert OSCAL id like 'ac-2.1' to display id like 'AC-2(1)'."""
    # Base controls: ac-2 -> AC-2
    # Enhancements: ac-2.1 -> AC-2(1)
    if "." in oscal_id:
        base, enh = oscal_id.rsplit(".", 1)
        return f"{base.upper()}({enh})"
    return oscal_id.upper()


def display_to_slug(display_id: str) -> str:
    """Convert display id like 'AC-2(1)' to slug like 'ac-2-1'."""
    s = display_id.lower()
    s = s.replace("(", "-").replace(")", "")
    return s


def oscal_id_to_slug(oscal_id: str) -> str:
    """Convert OSCAL id like 'ac-2.1' to slug like 'ac-2-1'."""
    return display_to_slug(oscal_id_to_display(oscal_id))


def extract_prose(parts, name):
    """Recursively extract prose from parts with a given name."""
    if not parts:
        return ""
    for part in parts:
        if part.get("name") == name:
            prose = part.get("prose", "")
            # Also collect sub-part prose
            if "parts" in part:
                sub_texts = []
                for sp in part["parts"]:
                    sp_prose = sp.get("prose", "")
                    if sp_prose:
                        sub_texts.append(sp_prose)
                    # Go one more level deep
                    if "parts" in sp:
                        for ssp in sp["parts"]:
                            ssp_prose = ssp.get("prose", "")
                            if ssp_prose:
                                sub_texts.append(ssp_prose)
                if sub_texts:
                    if prose:
                        prose += "\n" + "\n".join(sub_texts)
                    else:
                        prose = "\n".join(sub_texts)
            return prose.strip()
    return ""


def extract_related_controls(control):
    """Extract related control slugs from links with rel='related'."""
    related = []
    for link in control.get("links", []):
        if link.get("rel") == "related":
            href = link["href"].lstrip("#")
            # href is an OSCAL id like 'ac-3' or 'ac-2.1'
            slug = oscal_id_to_slug(href)
            related.append(slug)
    return sorted(set(related))


def parse_control(control, family_title, family_code):
    """Parse a single control (base or enhancement) into our schema."""
    oscal_id = control["id"]
    display_id = oscal_id_to_display(oscal_id)
    slug = oscal_id_to_slug(oscal_id)

    description = extract_prose(control.get("parts"), "statement")
    guidance = extract_prose(control.get("parts"), "guidance")
    related = extract_related_controls(control)

    return {
        "id": slug,
        "displayId": display_id,
        "title": control["title"],
        "family": family_title,
        "familyCode": family_code,
        "description": description,
        "supplementalGuidance": guidance,
        "relatedControls": related,
        "nist800171": [],
        "cmmcPractices": [],
        "notes": None,
    }


def build_reverse_map(items, source_key, nist_field="nist80053"):
    """
    Build a map from 800-53 display ID -> list of source slugs.
    e.g. {"AC-2": ["3-1-1"], "AC-3": ["3-1-1", "3-1-2"]}
    """
    mapping = {}
    for item in items:
        for ref in item.get(nist_field, []):
            mapping.setdefault(ref, []).append(item["id"])
    return mapping


def main():
    print("Fetching OSCAL 800-53 Rev 5 catalog...")
    resp = urllib.request.urlopen(OSCAL_URL)
    oscal_data = json.loads(resp.read().decode("utf-8"))
    catalog = oscal_data["catalog"]

    # Load cross-reference data
    cmmc_path = os.path.join(DATA_DIR, "cmmc-practices.json")
    nist171_path = os.path.join(DATA_DIR, "nist-800-171.json")

    cmmc_map = {}
    nist171_map = {}

    if os.path.exists(cmmc_path):
        with open(cmmc_path, "r", encoding="utf-8") as f:
            cmmc_data = json.load(f)
        cmmc_map = build_reverse_map(cmmc_data.get("practices", []), "id")
        print(f"  Loaded {len(cmmc_data.get('practices', []))} CMMC practices")

    if os.path.exists(nist171_path):
        with open(nist171_path, "r", encoding="utf-8") as f:
            nist171_data = json.load(f)
        nist171_map = build_reverse_map(nist171_data.get("requirements", []), "id")
        print(f"  Loaded {len(nist171_data.get('requirements', []))} NIST 800-171 requirements")

    # Parse all controls
    controls = []
    families = set()

    for group in catalog.get("groups", []):
        family_title = group["title"]
        family_code = group["id"].upper()
        families.add(family_code)

        for control in group.get("controls", []):
            # Base control
            ctrl = parse_control(control, family_title, family_code)
            controls.append(ctrl)

            # Enhancements (nested controls)
            for enhancement in control.get("controls", []):
                enh = parse_control(enhancement, family_title, family_code)
                controls.append(enh)

    # Apply cross-references
    cmmc_count = 0
    nist171_count = 0

    for ctrl in controls:
        display_id = ctrl["displayId"]
        if display_id in cmmc_map:
            ctrl["cmmcPractices"] = sorted(cmmc_map[display_id])
            cmmc_count += 1
        if display_id in nist171_map:
            ctrl["nist800171"] = sorted(nist171_map[display_id])
            nist171_count += 1

    # Write output
    os.makedirs(DATA_DIR, exist_ok=True)
    output_path = os.path.join(DATA_DIR, "nist-800-53.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"controls": controls}, f, indent=2, ensure_ascii=False)

    print(f"\nResults:")
    print(f"  Total controls (base + enhancements): {len(controls)}")
    print(f"  Families: {len(families)} — {', '.join(sorted(families))}")
    print(f"  Controls with CMMC cross-refs: {cmmc_count}")
    print(f"  Controls with 800-171 cross-refs: {nist171_count}")
    print(f"  Output: {output_path}")


if __name__ == "__main__":
    main()
