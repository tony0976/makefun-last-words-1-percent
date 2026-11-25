"""Writes a phone's funniest last words at 1 percent battery to /output/entry.txt."""
import os

TEXT = "I die as I lived — one percent left, 47 tabs open, and not a single one of them the page you actually needed."

# Rule: the last words must be a single line of 1 to 200 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, f"entry must be one line, 1-200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
