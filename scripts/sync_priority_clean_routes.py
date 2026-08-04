"""Keep canonical clean routes aligned with the reviewed flat page content.

The site is deployed with URLs such as /tw/display-hooks while the repository
also keeps a legacy flat HTML file.  The flat file is the reviewed content
source for this static site; this script copies it to the clean route and
rewrites known local page links to language-rooted clean URLs so that the same
content works without relying on a trailing slash.
"""

from pathlib import Path
import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
TA_SLUGS = {"procurement", "design-support", "display-hooks"}
PRODUCT_SLUGS = {
    "display-hooks",
    "optical-hooks",
    "anti-theft-hooks",
    "slatwall-pegboard-accessories",
    "price-tag-holders",
    "pos-displays",
    "modular-fixtures",
    "custom-metal-parts",
}
KNOWN_ROUTES = TA_SLUGS | PRODUCT_SLUGS | {
    "applications",
    "contact",
    "design-support",
    "display-hooks",
    "products",
    "procurement",
    "services",
    "technical-resources",
}


def rewrite_href(match: re.Match[str], lang: str) -> str:
    prefix, value, suffix = match.groups()
    if value.startswith(("http://", "https://", "//", "#", "mailto:", "tel:", "javascript:")):
        return match.group(0)

    path, query = (value.split("?", 1) + [""])[:2] if "?" in value else (value, "")
    path = path.split("#", 1)[0]
    if path.endswith((".css", ".js", ".png", ".jpg", ".jpeg", ".webp", ".svg", ".pdf", ".doc", ".docx", ".xls", ".xlsx")):
        return match.group(0)

    while path.startswith("../"):
        path = path[3:]
    if path.startswith("./"):
        path = path[2:]

    if not path:
        target = f"/{lang}/"
    elif path == "css" or path.startswith("css/"):
        target = f"/{path}"
    elif path in KNOWN_ROUTES:
        target = f"/{lang}/{path}"
    else:
        return match.group(0)

    if query:
        target += "?" + query
    return f'href={prefix}{target}{suffix}'


def repair_malformed_href_attributes(html: str) -> str:
    # Repair only the malformed tags produced by the first run of this script;
    # proper href attributes do not match this pattern.
    return re.sub(
        r'(<(?:a|link)\b[^>]*?)(\s+)(["\'])(/(?:tw|en|jp|css)/[^"\']*)(["\'])',
        lambda m: f"{m.group(1)}{m.group(2)}href={m.group(3)}{m.group(4)}{m.group(5)}",
        html,
        flags=re.IGNORECASE,
    )


def normalize(html: str, lang: str) -> str:
    html = repair_malformed_href_attributes(html)
    return re.sub(r'href=(["\'])([^"\']+)(["\'])', lambda m: rewrite_href(m, lang), html, flags=re.IGNORECASE)


def add_product_context(html: str, lang: str, slug: str) -> str:
    """Make product context available before JavaScript enhancement runs."""
    def add_query(match: re.Match[str]) -> str:
        quote, value, closing = match.groups()
        try:
            parts = urlsplit(value)
            if parts.path != f"/{lang}/contact":
                return match.group(0)
            query = dict(parse_qsl(parts.query, keep_blank_values=True))
            query.setdefault("product", slug)
            updated = urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))
            return f"href={quote}{updated}{closing}"
        except ValueError:
            return match.group(0)

    return re.sub(r'href=(["\'])([^"\']+)(["\'])', add_query, html, flags=re.IGNORECASE)


def sync(lang: str, slug: str) -> None:
    flat_path = ROOT / lang / f"{slug}.html"
    clean_path = ROOT / lang / slug / "index.html"
    if not flat_path.exists() or not clean_path.exists():
        return

    content = normalize(flat_path.read_text(encoding="utf-8"), lang)
    if slug in PRODUCT_SLUGS:
        content = add_product_context(content, lang, slug)
    flat_path.write_text(content, encoding="utf-8", newline="\n")
    clean_path.write_text(content, encoding="utf-8", newline="\n")


for lang in ("tw", "en", "jp"):
    slugs = TA_SLUGS | PRODUCT_SLUGS
    slugs |= {p.stem for p in (ROOT / lang).glob("case-*.html")}
    for slug in sorted(slugs):
        sync(lang, slug)

print("Synchronized priority TA, product and case clean routes for tw/en/jp")
