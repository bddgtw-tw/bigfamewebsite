"""Audit visible product-page content, not only generic keyword presence."""
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SLUGS = (
    "display-hooks", "optical-hooks", "anti-theft-hooks",
    "slatwall-pegboard-accessories", "price-tag-holders", "pos-displays",
    "modular-fixtures", "custom-metal-parts",
)


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.attrs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href"):
            self.attrs.append(attrs["href"])

    def handle_data(self, data):
        self.text.append(data)


def visible_text(source: str) -> str:
    parser = TextParser()
    parser.feed(source)
    return re.sub(r"\s+", " ", " ".join(parser.text)).strip()


checks = {
    "names": lambda s, t, a: 'class="product-names' in s and len(re.search(r'<p class="product-names.*?</p>', s, re.S).group(0)) > 50,
    "store_or_system": lambda s, t, a: bool(re.search(r"store|retail|店型|店面|店舗|商空|display system|展示系統|展示システム", t, re.I)),
    "material": lambda s, t, a: bool(re.search(r"material|材質|材料|素材", t, re.I)),
    "dimensions": lambda s, t, a: bool(re.search(r"dimension|尺寸|寸法|pitch|孔徑|孔径|\b\d+\s*mm", t, re.I)),
    "finish": lambda s, t, a: bool(re.search(r"finish|表面處理|表面处理|仕上げ", t, re.I)),
    "moq_and_lead_time": lambda s, t, a: bool(re.search(r"MOQ", t, re.I)) and bool(re.search(r"lead time|交期|納期", t, re.I)),
    "custom_scope": lambda s, t, a: bool(re.search(r"custom|客製|カスタム", t, re.I)),
    "asset": lambda s, t, a: bool(re.search(r"<img\b|drawing|圖面|図面", s, re.I)),
    "related_case": lambda s, t, a: any(re.match(r"(?:\.\./)?case-", href) for href in a),
    "inquiry_cta": lambda s, t, a: any("contact?category=" in href for href in a),
    "faq": lambda s, t, a: "FAQPage" in s and 'data-bf-faq="1"' in s,
}

failures = []
for language in ("tw", "en", "jp"):
    for slug in SLUGS:
        path = ROOT / language / f"{slug}.html"
        source = path.read_text(encoding="utf-8")
        parser = TextParser()
        parser.feed(source)
        text = visible_text(source)
        missing = [name for name, check in checks.items() if not check(source, text, parser.attrs)]
        if missing:
            failures.append((str(path.relative_to(ROOT)), missing))

print(f"PRODUCT_QUALITY_PAGES={len(SLUGS) * 3}")
print(f"PRODUCT_QUALITY_FAILURES={len(failures)}")
for path, missing in failures:
    print(f"{path}: {', '.join(missing)}")
if failures:
    raise SystemExit(1)
