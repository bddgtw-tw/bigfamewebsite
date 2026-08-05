from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
TARGETS = []
for language in ("tw", "en", "jp"):
    folder = ROOT / language
    TARGETS += [folder / "applications.html", *folder.glob("case-*.html"), *folder.glob("case-*/index.html")]


def original(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    return subprocess.check_output(["git", "show", f"HEAD:{rel}"], cwd=ROOT, text=True, encoding="utf-8")


def first(pattern: str, text: str) -> str | None:
    match = re.search(pattern, text, re.I)
    return match.group(1) if match else None


for path in sorted(set(TARGETS)):
    current = path.read_text(encoding="utf-8")
    old = original(path)
    old_canonical = first(r'<link\s+rel="canonical"\s+href="([^"]+)"', old)
    old_og_url = first(r'<meta\s+property="og:url"\s+content="([^"]+)"', old)
    old_lang = first(r'<html\s+lang="([^"]+)"', old)
    if old_og_url:
        current = re.sub(r'(<meta\s+property="og:url"\s+content=")[^"]+("[^>]*>)', rf'\g<1>{old_og_url}\g<2>', current, flags=re.I)
    if old_canonical:
        current = re.sub(r'(<link\s+rel="canonical"\s+href=")[^"]+("[^>]*>)', rf'\g<1>{old_canonical}\g<2>', current, flags=re.I)
        current = re.sub(r'("url"\s*:\s*")[^"]+("\s*[,}])', rf'\g<1>{old_canonical}\g<2>', current, flags=re.I)
    old_image = first(r'"image"\s*:\s*"([^"]+)"', old)
    if old_image:
        current = re.sub(r'("image"\s*:\s*")[^"]+("\s*[,}])', rf'\g<1>{old_image}\g<2>', current, flags=re.I)
    old_case_urls = set(re.findall(r'https://www\.bigfame\.co/[^" ]*case-[^" ]+', old, flags=re.I))
    for url in old_case_urls:
        stripped = re.sub(r'(?:19|20)\d{2}', '', url)
        current = current.replace(stripped, url)
    if old_lang:
        current = re.sub(r'(<html\s+lang=")[^"]*("[^>]*>)', rf'\g<1>{old_lang}\g<2>', current, count=1, flags=re.I)
    current = re.sub(r"(<(?:title|h[1-3])[^>]*>)\s+", r"\1", current, flags=re.I)
    current = current.replace("  ", " ")
    current = re.sub(r"(?m)^[ \t]+$", "", current)
    path.write_text(current, encoding="utf-8")
