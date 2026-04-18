#!/usr/bin/env python3
"""Inject practitioner notes into NIST 800-53 JSON data file."""
import json
import sys
sys.path.insert(0, 'scripts')

from notes_800_53_batch_1 import NOTES as B1
from notes_800_53_batch_2 import NOTES as B2
from notes_800_53_batch_3 import NOTES as B3
from notes_800_53_batch_4 import NOTES as B4
from notes_800_53_batch_5 import NOTES as B5

ALL_NOTES = {}
ALL_NOTES.update(B1)
ALL_NOTES.update(B2)
ALL_NOTES.update(B3)
ALL_NOTES.update(B4)
ALL_NOTES.update(B5)
print(f"Total notes: {len(ALL_NOTES)}")

with open("data/nist-800-53.json", "r", encoding="utf-8") as f:
    data = json.load(f)

updated = 0
missing = []
for ctrl in data["controls"]:
    if ctrl["id"] in ALL_NOTES:
        ctrl["notes"] = ALL_NOTES[ctrl["id"]]
        updated += 1
    else:
        missing.append(ctrl["id"])

print(f"Updated: {updated}/{len(data['controls'])}")
if missing:
    print(f"Missing: {missing}")

with open("data/nist-800-53.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Done!")
