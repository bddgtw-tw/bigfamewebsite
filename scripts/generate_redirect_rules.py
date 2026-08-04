"""Generate explicit clean-route rewrites for static-host compatibility."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
lines = [
    "/overview /en/about 301",
    "/overview/ /en/about 301",
    "/contact-us /en/contact 301",
    "/contact-us/ /en/contact 301",
]
slugs = [
    "procurement", "design-support", "display-hooks", "case-eyewear-2016",
    "optical-hooks", "anti-theft-hooks", "slatwall-pegboard-accessories",
    "price-tag-holders", "pos-displays", "modular-fixtures", "custom-metal-parts",
]
for language in ("tw", "en", "jp"):
    for slug in slugs:
        lines.append(f"/{language}/{slug} /{language}/{slug}.html 200")

(ROOT / "_redirects").write_text("\n".join(lines) + "\n", encoding="utf-8")
