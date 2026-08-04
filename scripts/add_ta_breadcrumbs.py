"""Add BreadcrumbList schema to the procurement and design-support TA entries."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
NAMES = {
    "tw": {"procurement": "台灣店面展示設備採購", "design-support": "零售空間展示系統與設計支援", "products": "產品與能力", "applications": "應用案例"},
    "en": {"procurement": "Taiwan Retail Display Hardware Procurement", "design-support": "Retail Display Systems and Design Support", "products": "Products", "applications": "Applications"},
    "jp": {"procurement": "台湾の店舗什器・ディスプレイ金具の購買", "design-support": "店舗什器・ディスプレイシステム設計支援", "products": "製品", "applications": "用途事例"},
}

for lang in ("tw", "en", "jp"):
    for slug in ("procurement", "design-support"):
        path = ROOT / lang / f"{slug}.html"
        text = path.read_text(encoding="utf-8")
        if '"@type":"BreadcrumbList"' in text or '"@type": "BreadcrumbList"' in text:
            continue
        canonical = re.search(r'<link rel="canonical" href="([^"]+)"', text).group(1)
        schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"https://www.bigfame.co/{lang}/"},
            {"@type": "ListItem", "position": 2, "name": NAMES[lang]["applications"], "item": f"https://www.bigfame.co/{lang}/applications"},
            {"@type": "ListItem", "position": 3, "name": NAMES[lang][slug], "item": canonical},
        ]}
        text = text.replace("</head>", f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script></head>', 1)
        path.write_text(text, encoding="utf-8")

print("Added BreadcrumbList schema to six localized TA entry pages.")
