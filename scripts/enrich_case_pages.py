"""Add consistent BreadcrumbList and FAQPage data to evidence-controlled case pages."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "tw": {
        "label": "應用案例",
        "faq": [
            ("這些案例是否代表已完成的客戶安裝？", "頁面會依資料狀態標示為匿名專案、系統開發或樣品圖面紀錄；未核准的安裝、數量、成果與交付資訊不會推論。"),
            ("開始詢問時需要準備什麼？", "請提供店型或空間用途、產品尺寸、預估數量、目標交期、交貨地與圖面或照片，我們再確認規格與可行流程。"),
        ],
    },
    "en": {
        "label": "Applications",
        "faq": [
            ("Do these pages claim completed client installations?", "Each page states whether it is an anonymous project, system development record or sample-drawing record. Unapproved installation, quantity, outcome and delivery details are not inferred."),
            ("What should I prepare for an inquiry?", "Share the store type or space use, product dimensions, estimated quantity, target date, delivery location and any drawings or photos so we can review the specification and route."),
        ],
    },
    "jp": {
        "label": "用途・事例",
        "faq": [
            ("完成した顧客施工を示すページですか？", "各ページで匿名案件、システム開発、サンプル図面の記録かを明示しています。未承認の施工、数量、成果、納入情報は推測していません。"),
            ("相談時に何を準備すればよいですか？", "店舗タイプ、用途、商品寸法、数量、希望納期、納入地、図面または写真をお送りください。仕様と進め方を確認します。"),
        ],
    },
}
SLUGS = ("case-ivy-modular-system", "case-boutique-hotel-furniture", "case-modular-3c-store")


def enrich(language: str, slug: str) -> None:
    path = ROOT / language / f"{slug}.html"
    text = path.read_text(encoding="utf-8")
    canonical = f"https://www.bigfame.co/{language}/{slug}"
    cfg = PAGES[language]
    if '"@type":"BreadcrumbList"' not in text:
        crumb = json.dumps({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"https://www.bigfame.co/{language}/"},
                {"@type": "ListItem", "position": 2, "name": cfg["label"], "item": f"https://www.bigfame.co/{language}/applications"},
                {"@type": "ListItem", "position": 3, "name": slug, "item": canonical},
            ],
        }, ensure_ascii=False)
        text = text.replace("</head>", f'<script type="application/ld+json">{crumb}</script></head>', 1)
    if '"@type":"FAQPage"' not in text:
        faq = json.dumps({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in cfg["faq"]
            ],
        }, ensure_ascii=False)
        visible = ''.join(f'<article class="location-card reveal"><h3>{q}</h3><p>{a}</p></article>' for q, a in cfg["faq"])
        section = f'<section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">{cfg["label"]} FAQ</h2></div><div class="grid-2">{visible}</div></div></section>'
        text = text.replace("</head>", f'<script type="application/ld+json">{faq}</script></head>', 1)
        text = text.replace('<section class="section section-dark">', section + '<section class="section section-dark">', 1)
    path.write_text(text, encoding="utf-8", newline="")


for lang in PAGES:
    for slug in SLUGS:
        enrich(lang, slug)
