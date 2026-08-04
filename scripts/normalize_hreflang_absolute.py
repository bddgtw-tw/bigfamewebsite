"""Normalize alternate-language links to absolute clean public URLs."""

from html import unescape
from pathlib import Path
from urllib.parse import urljoin
import re


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_ORIGIN = "https://www.bigfame.co/"


def public_url_for_file(path: Path) -> str:
    relative = path.relative_to(ROOT).as_posix()
    if relative == "index.html":
        return PUBLIC_ORIGIN
    if relative.endswith("/index.html"):
        return urljoin(PUBLIC_ORIGIN, relative[:-len("index.html")])
    if relative.endswith(".html"):
        return urljoin(PUBLIC_ORIGIN, relative[:-len(".html")])
    return urljoin(PUBLIC_ORIGIN, relative)


def normalize_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    page_url = public_url_for_file(path)

    def replace_tag(match: re.Match[str]) -> str:
        tag = match.group(0)
        href_match = re.search(r'(href=["\'])([^"\']+)(["\'])', tag, re.IGNORECASE)
        if not href_match:
            return tag
        href = unescape(href_match.group(2))
        if href.startswith(("https://", "http://", "//", "#")):
            return tag
        absolute = urljoin(page_url, href)
        return tag[:href_match.start(2)] + absolute + tag[href_match.end(2):]

    updated = re.sub(
        r'<link\b(?=[^>]*\brel=["\']alternate["\'])(?=[^>]*\bhreflang=)[^>]*>',
        replace_tag,
        original,
        flags=re.IGNORECASE,
    )
    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="")
        return True
    return False


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*.html"):
        if "node_modules" in path.parts:
            continue
        changed += int(normalize_file(path))
    print(f"Updated alternate links in {changed} HTML files.")


if __name__ == "__main__":
    main()
