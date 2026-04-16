"""
Post-process dumped JSON data.

Reads all JSON files in the json_dumps folder, applies cleanup
transformations, and writes them back. Currently applies:
- Strips trailing exclamation marks from all string values.

Usage:
    python process_data.py
"""

import json
import glob
from config import JSON_FOLDER


def strip_trailing_exclamation(obj):
    if isinstance(obj, str):
        return obj.rstrip("!")
    if isinstance(obj, list):
        return [strip_trailing_exclamation(item) for item in obj]
    if isinstance(obj, dict):
        return {k: strip_trailing_exclamation(v) for k, v in obj.items()}
    return obj


for path in glob.glob(f"{JSON_FOLDER}/*.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data = strip_trailing_exclamation(data)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Processed {path}")
