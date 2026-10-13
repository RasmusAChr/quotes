#!/usr/bin/env python3
"""Add a quote to quotes.json.

Usage:
    ./add.py "The quote text" "Source"
    ./add.py            # prompts interactively
"""
import datetime
import json
import pathlib
import sys

FILE = pathlib.Path(__file__).with_name("quotes.json")


def main():
    if len(sys.argv) >= 2:
        text = sys.argv[1]
        source = sys.argv[2] if len(sys.argv) >= 3 else ""
    else:
        text = input("Quote: ").strip()
        source = input("Source: ").strip()

    if not text:
        sys.exit("No quote given.")

    quotes = json.loads(FILE.read_text(encoding="utf-8")) if FILE.exists() else []
    quotes.append({
        "text": text,
        "source": source,
        "added": datetime.date.today().isoformat(),
    })
    FILE.write_text(json.dumps(quotes, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added. {len(quotes)} quotes total.")


if __name__ == "__main__":
    main()
