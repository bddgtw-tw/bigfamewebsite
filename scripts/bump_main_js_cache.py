from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.3.23"

main_js = ROOT / "js" / "main.js"
source = main_js.read_text(encoding="utf-8")
source = re.sub(r"(SITE_VERSION\s*=\s*')[^']+(')", rf"\g<1>{VERSION}\g<2>", source, count=1)
main_js.write_text(source, encoding="utf-8", newline="\n")

changed = 0
for page in ROOT.rglob("*.html"):
    if "node_modules" in page.parts:
        continue
    source = page.read_text(encoding="utf-8")
    updated = re.sub(
        r"(main\.js\?v=)[^\"']+",
        rf"\g<1>{VERSION}",
        source,
        flags=re.IGNORECASE,
    )
    if updated != source:
        page.write_text(updated, encoding="utf-8", newline="\n")
        changed += 1

print(f"Updated main.js cache version to {VERSION} in {changed} HTML files")
