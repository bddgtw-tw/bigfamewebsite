"""Mark visible FAQ sections on multilingual TA and resource pages."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = ("procurement", "design-support", "display-hooks", "technical-resources")

for language in ("tw", "en", "jp"):
    for slug in PAGES:
        path = ROOT / language / f"{slug}.html"
        source = path.read_text(encoding="utf-8")
        if 'data-bf-faq="1"' in source:
            continue
        matches = list(re.finditer(r"<section\b[^>]*>.*?</section>", source, re.S | re.I))
        candidates = [m for m in matches if re.search(r"FAQ|常見問題|よくある質問", m.group(0), re.I)]
        if len(candidates) != 1:
            raise SystemExit(f"Expected one visible FAQ section in {path}, found {len(candidates)}")
        match = candidates[0]
        opening_end = source.find(">", match.start())
        source = source[:opening_end] + ' data-bf-faq="1"' + source[opening_end:]
        path.write_text(source, encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}")
