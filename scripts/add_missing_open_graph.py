"""Add conservative Open Graph metadata from existing page metadata."""
from html import escape, unescape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def value(pattern: str, text: str) -> str | None:
    match = re.search(pattern, text, re.S)
    return unescape(match.group(1).strip()) if match else None


def main() -> None:
    changed = 0
    for language in ("tw", "en", "jp"):
        for path in sorted((ROOT / language).rglob("*.html")):
            text = path.read_text(encoding="utf-8")
            if '<meta property="og:url"' in text:
                continue
            canonical = value(r'<link rel="canonical" href="([^"]+)"', text)
            description = value(r'<meta name="description" content="([^"]+)"', text)
            title = value(r'<title>(.*?)</title>', text)
            if not (canonical and description and title):
                continue
            og_type = "article" if "case-" in path.stem or path.parent.name.startswith("case-") else "website"
            tags = (
                f'<meta property="og:type" content="{og_type}">'
                f'<meta property="og:title" content="{escape(title, quote=True)}">'
                f'<meta property="og:description" content="{escape(description, quote=True)}">'
                f'<meta property="og:url" content="{escape(canonical, quote=True)}">'
                '<meta property="og:site_name" content="Big Fame IND. CORP.">'
            )
            marker = re.search(r'<meta name="description" content="[^"]+">', text)
            if not marker:
                continue
            text = text[:marker.end()] + tags + text[marker.end():]
            path.write_text(text, encoding="utf-8")
            changed += 1
            print(f"UPDATED {path.relative_to(ROOT)}")
    print(f"OPEN_GRAPH_PAGES={changed}")


if __name__ == "__main__":
    main()
