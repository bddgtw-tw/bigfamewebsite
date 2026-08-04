"""Normalize Big Fame public page links to the clean-URL contract.

This is intentionally limited to known page routes and does not touch asset
paths, query strings, or external URLs.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PAGE_NAMES = {"index", "about", "products", "services", "applications", "contact"}


def normalize_absolute_urls(text: str) -> str:
    return re.sub(
        r"(https://www\.bigfame\.co/(?:tw|en|jp)/(?:index|about|products|services|applications|contact))\.html",
        r"\1",
        text,
        flags=re.IGNORECASE,
    )


def normalize_relative_page_links(text: str) -> str:
    for prefix in ("", "../"):
        for language in ("tw", "en", "jp"):
            for page in PAGE_NAMES:
                text = text.replace(f'href="{prefix}{language}/{page}.html"', f'href="{prefix}{language}/{page if page != "index" else ""}"')

    for page in PAGE_NAMES:
        replacement = "./" if page == "index" else page
        text = text.replace(f'href="{page}.html"', f'href="{replacement}"')
        text = text.replace(f'href="./{page}.html"', f'href="{replacement}"')

    def clean_link(match: re.Match[str]) -> str:
        prefix, page, suffix = match.groups()
        prefix = prefix or ""
        replacement = "./" if page == "index" else page
        return f'href="{prefix}{replacement}{suffix}"'

    text = re.sub(
        r'href="(\.{0,2}/)?(index|about|products|services|applications|contact)\.html([^\"]*)"',
        clean_link,
        text,
        flags=re.IGNORECASE,
    )

    text = text.replace('href="../jp/index.html"', 'href="../jp/"')
    text = text.replace('href="../en/index.html"', 'href="../en/"')
    text = text.replace('href="../tw/index.html"', 'href="../tw/"')
    text = text.replace('href="./jp/index.html"', 'href="./jp/"')
    text = text.replace('href="./en/index.html"', 'href="./en/"')
    text = text.replace('href="./tw/index.html"', 'href="./tw/"')
    return text


def main() -> None:
    for page in ROOT.rglob("*.html"):
        if page.name == "style-tiles.html":
            continue
        original = page.read_text(encoding="utf-8")
        updated = normalize_relative_page_links(normalize_absolute_urls(original))
        if updated != original:
            page.write_text(updated, encoding="utf-8", newline="")

    sitemap = ROOT / "sitemap.xml"
    original = sitemap.read_text(encoding="utf-8")
    updated = normalize_absolute_urls(original)
    if updated != original:
        sitemap.write_text(updated, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
