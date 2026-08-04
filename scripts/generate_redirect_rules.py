"""Generate explicit clean-route rewrites for static-host compatibility."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
lines = [
    "/overview /en/about 301",
    "/overview/ /en/about 301",
    "/contact-us /en/contact 301",
    "/contact-us/ /en/contact 301",
]
(ROOT / "_redirects").write_text("\n".join(lines) + "\n", encoding="utf-8")
