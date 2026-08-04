"""Preserve the technical-resource intent when users open the inquiry form."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
for language in ("tw", "en", "jp"):
    path = ROOT / language / "technical-resources.html"
    text = path.read_text(encoding="utf-8")
    old = "contact?category=display_hardware&role=buyer"
    new = old + "&requested_files=technical_pack"
    if new not in text:
        text = text.replace(old, new)
        path.write_text(text, encoding="utf-8", newline="")
print("Updated technical-resource inquiry links.")
