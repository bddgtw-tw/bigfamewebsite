"""Mark the visible FAQ section so it can be audited against FAQPage JSON-LD."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SLUGS = (
    "display-hooks", "optical-hooks", "anti-theft-hooks",
    "slatwall-pegboard-accessories", "price-tag-holders", "pos-displays",
    "modular-fixtures", "custom-metal-parts",
)

for language in ("tw", "en", "jp"):
    for slug in SLUGS:
        path = ROOT / language / f"{slug}.html"
        text = path.read_text(encoding="utf-8")
        if 'data-bf-faq="1"' in text:
            continue
        sections = list(re.finditer(r"<section\b(?P<attrs>[^>]*)>(?P<body>.*?)</section>", text, re.S | re.I))
        candidates = [m for m in sections if re.search(r"FAQ|常見問題|よくある質問", m.group("body"), re.I)]
        if len(candidates) != 1:
            raise SystemExit(f"Expected one visible FAQ section in {path}, found {len(candidates)}")
        match = candidates[0]
        start = match.start()
        opening_end = text.index(">", start)
        opening = text[start:opening_end]
        text = text[:opening_end] + ' data-bf-faq="1"' + text[opening_end:]
        path.write_text(text, encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}")
