#!/usr/bin/env python3
"""Inject practitioner notes into compliance JSON data files."""
import json
import sys

# Import all note batches
from notes_batch_1 import NOTES as BATCH_1
from notes_batch_2 import NOTES as BATCH_2
from notes_batch_3 import NOTES as BATCH_3
from notes_batch_4 import NOTES as BATCH_4

# Merge all notes
ALL_NOTES = {}
ALL_NOTES.update(BATCH_1)
ALL_NOTES.update(BATCH_2)
ALL_NOTES.update(BATCH_3)
ALL_NOTES.update(BATCH_4)

print(f"Total notes: {len(ALL_NOTES)}")

# Update CMMC practices
with open("data/cmmc-practices.json", "r", encoding="utf-8") as f:
    cmmc = json.load(f)

updated = 0
missing = []
for practice in cmmc["practices"]:
    if practice["id"] in ALL_NOTES:
        practice["notes"] = ALL_NOTES[practice["id"]]
        updated += 1
    else:
        missing.append(practice["id"])

print(f"CMMC practices updated: {updated}/{len(cmmc['practices'])}")
if missing:
    print(f"Missing notes for: {missing}")

with open("data/cmmc-practices.json", "w", encoding="utf-8") as f:
    json.dump(cmmc, f, indent=2, ensure_ascii=False)

# Update NIST 800-171 requirements with matching notes
with open("data/nist-800-171.json", "r", encoding="utf-8") as f:
    nist = json.load(f)

nist_updated = 0
for req in nist["requirements"]:
    # Find the matching CMMC practice note via cmmcPractices reference
    for cmmc_id in req.get("cmmcPractices", []):
        if cmmc_id in ALL_NOTES:
            req["notes"] = ALL_NOTES[cmmc_id]
            nist_updated += 1
            break

print(f"NIST requirements updated: {nist_updated}/{len(nist['requirements'])}")

with open("data/nist-800-171.json", "w", encoding="utf-8") as f:
    json.dump(nist, f, indent=2, ensure_ascii=False)

print("Done!")
