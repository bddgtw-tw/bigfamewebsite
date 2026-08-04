"""Audit the required product-page contract without changing website files."""
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
        names = re.search(r'<p class="product-names.*?</p>', text, re.S)
        print(f"{path.relative_to(ROOT)}: " + (names.group(0) if names else "MISSING").encode("unicode_escape").decode("ascii"))

        checks = {
            "h1": r"<h1\b",
            "description": r'<meta name="description"',
            "store_or_system": r"store|retail|店型|店面|店舗|商空|display system|展示系統|展示システム",
            "material": r"material|材質|材料|素材",
            "dimensions": r"dimension|尺寸|寸法|pitch|孔徑|孔径",
            "finish": r"finish|表面處理|表面处理|仕上げ",
            "moq": r"MOQ",
            "lead_time": r"lead time|交期|納期",
            "custom_scope": r"custom|客製|カスタム",
            "asset": r"<img\b|drawing|圖面|図面",
            "related_case": r"case-",
            "inquiry_cta": r"contact\?",
            "faq_schema": r"FAQPage",
        }
        missing = [name for name, pattern in checks.items() if not re.search(pattern, text, re.I)]
        if missing:
            print(f"  MISSING_CONTRACT: {','.join(missing)}")
