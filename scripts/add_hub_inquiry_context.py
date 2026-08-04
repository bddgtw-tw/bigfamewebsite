"""Add a safe default inquiry category to generic hub-page contact links."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    "about.html",
    "applications.html",
    "index.html",
    "products.html",
    "services.html",
]

changed = 0
for locale in ("tw", "en", "jp"):
    for filename in PAGES:
        path = ROOT / locale / filename
        text = path.read_text(encoding="utf-8")
        before = text
        text = text.replace('href="contact"', 'href="contact?category=integration"')
        text = text.replace('href="contact.html"', 'href="contact.html?category=integration"')
        if text != before:
            path.write_text(text, encoding="utf-8", newline="")
            changed += 1

print(f"Updated generic contact context on {changed} hub pages.")
