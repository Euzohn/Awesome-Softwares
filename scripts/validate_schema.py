#!/usr/bin/env python3
"""
Validate data/software.json against a basic schema:
- Required fields for each software
- Valid platforms and categories
- GitHub format owner/repo if present
- URLs basic format
"""

import json
import re
from pathlib import Path
import sys

DATA_FILE = Path(__file__).parent.parent / "data" / "software.json"

VALID_PLATFORMS = {"macOS", "Windows", "Linux", "Android", "iOS", "Web"}
# Allow broader URL characters including @, :, ~ and others commonly seen
URL_RE = re.compile(r"^https?://[^\s]+$", re.IGNORECASE)
GITHUB_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")

REQUIRED_FIELDS = [
    "name",
    "description",
    "website",
    "platforms",
    "category",
    "open_source",
    "free",
]


def fail(msg: str):
    print(f"❌ {msg}")
    sys.exit(1)


def validate():
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"Failed to read JSON: {e}")

    categories = {c["id"] for c in data.get("categories", [])}
    if not categories:
        fail("categories list is empty or missing")

    sw_list = data.get("software_list", [])
    if not isinstance(sw_list, list) or not sw_list:
        fail("software_list must be a non-empty list")

    for idx, sw in enumerate(sw_list, start=1):
        # Required fields
        for f in REQUIRED_FIELDS:
            if f not in sw:
                fail(f"Item {idx} ('{sw.get('name','<unknown>')}') missing required field: {f}")

        # Website URL
        website = sw["website"]
        if not isinstance(website, str) or not URL_RE.match(website):
            fail(f"Item {idx} invalid website: {website}")

        # Platforms
        platforms = sw["platforms"]
        if not isinstance(platforms, list) or not platforms:
            fail(f"Item {idx} platforms must be a non-empty list")
        if any(p not in VALID_PLATFORMS for p in platforms):
            invalid = [p for p in platforms if p not in VALID_PLATFORMS]
            fail(f"Item {idx} has invalid platforms: {invalid}")

        # Category must exist in categories list
        cat = sw["category"]
        if cat not in categories:
            fail(f"Item {idx} category '{cat}' not found in categories")

        # GitHub owner/repo if present
        gh = sw.get("github")
        if gh and not GITHUB_RE.match(gh):
            fail(f"Item {idx} invalid github format (owner/repo): {gh}")

        # Optional logo URL or relative path
        logo = sw.get("logo")
        if logo:
            if logo.startswith("http"):
                if not URL_RE.match(logo):
                    fail(f"Item {idx} invalid logo URL: {logo}")
            else:
                # allow relative like ./images/foo.png
                if not (logo.startswith("./") or logo.startswith("images/")):
                    fail(f"Item {idx} invalid logo path (must be URL or relative to images/): {logo}")

    print(f"✅ Schema validation passed: {len(sw_list)} items, {len(categories)} categories")


if __name__ == "__main__":
    validate()
