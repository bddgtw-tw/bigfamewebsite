"""Add missing BreadcrumbList schema to localized content and product pages."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
LABELS = {
    "tw": {
        "about": "關於 Big Fame",
        "applications": "應用案例",
        "products": "產品",
        "services": "服務",
        "anti-theft-hooks": "防盜展示掛勾",
        "custom-metal-parts": "客製金屬零件",
        "pos-displays": "POS 展示架",
    },
    "en": {
        "about": "About Big Fame",
        "applications": "Applications",
        "products": "Products",
        "services": "Services",
        "anti-theft-hooks": "Anti-theft Display Hooks",
        "custom-metal-parts": "Custom Metal Parts",
        "pos-displays": "POS Displays",
    },
    "jp": {
        "about": "Big Fameについて",
        "applications": "用途事例",
        "products": "製品",
        "services": "サービス",
        "anti-theft-hooks": "防犯ディスプレイフック",
        "custom-metal-parts": "カスタム金属部品",
        "pos-displays": "POSディスプレイ",
    },
}

PAGES = ("about", "applications", "products", "services", "anti-theft-hooks", "custom-metal-parts", "pos-displays")

for lang in ("tw", "en", "jp"):
    for slug in PAGES:
        for path in (ROOT / lang / f"{slug}.html", ROOT / lang / slug / "index.html"):
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            if '"@type":"BreadcrumbList"' in text or '"@type": "BreadcrumbList"' in text:
                continue
            match = re.search(r'<link rel="canonical" href="([^"]+)"', text)
            if not match:
                raise SystemExit(f"Missing canonical in {path}")
            parent = "products" if slug in {"anti-theft-hooks", "custom-metal-parts", "pos-displays"} else None
            items = [
                {"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"https://www.bigfame.co/{lang}/"},
            ]
            if parent:
                items.append({"@type": "ListItem", "position": 2, "name": LABELS[lang][parent], "item": f"https://www.bigfame.co/{lang}/{parent}"})
            items.append({"@type": "ListItem", "position": len(items) + 1, "name": LABELS[lang][slug], "item": match.group(1)})
            schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
            text = text.replace("</head>", f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(",", ":"))}</script></head>', 1)
            path.write_text(text, encoding="utf-8")
            print(f"UPDATED {path.relative_to(ROOT)}")
