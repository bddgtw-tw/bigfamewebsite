"""Add localized FAQ and breadcrumb evidence to the two case pages missing it."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "case-eyewear-2016": {
        "tw": {
            "label": "應用案例",
            "questions": [
                ("這是完整交付案例嗎？", "這是匿名專案影像與需求討論入口。頁面只公開可核對的眼鏡零售展示方向，不推論客戶名稱、數量、成本、交期或正式 SKU。"),
                ("要如何用這個案例開始詢問？", "請提供店型、商品、展示密度、背板或安裝系統、預估數量與目標日期，我們再回到展示掛勾或眼鏡展示掛勾頁確認規格。"),
            ],
        },
        "en": {
            "label": "Applications",
            "questions": [
                ("Is this a complete delivery case?", "This is an anonymous project image and requirement discussion entry. It publishes only the confirmed eyewear retail display direction; client name, quantity, cost, schedule and formal SKU are not inferred."),
                ("How should we use this case for a new inquiry?", "Share the store format, products, display density, backing or mounting system, estimated quantity and target date. We can then return to the display-hook or optical-hook page for specification review."),
            ],
        },
        "jp": {
            "label": "用途事例",
            "questions": [
                ("これは正式な納品事例ですか？", "匿名プロジェクトの画像と要件整理の入口です。確認できるメガネ小売の展示方向だけを掲載し、顧客名、数量、費用、納期、正式 SKU は推定していません。"),
                ("新しい相談にはどのように使えますか？", "店舗形態、商品、展示密度、背板または取付システム、予定数量、希望時期を共有してください。展示フックまたはメガネ展示フックの仕様確認につなげます。"),
            ],
        },
    },
    "case-modular-3c-store": {
        "tw": {
            "label": "應用案例",
            "questions": [
                ("這個 3C 案例記錄了什麼？", "來源文件記錄二手 3C 店面的模組化需求，包括壁面展示、玻璃展示櫃、落地展示櫃與可替換功能上蓋；正式合約分工與數量未公開。"),
                ("可以直接複製到其他店面嗎？", "來源需求包含易運輸、易組裝與跨店複製方向，但新店仍需依平面、商品、數量、包裝與交付地重新確認。"),
            ],
        },
        "en": {
            "label": "Applications",
            "questions": [
                ("What does the 3C case record?", "The source brief records a modular second-hand 3C store direction covering wall displays, glass showcases, floor-standing showcases and replaceable functional tops; formal contract scope and quantity are not public."),
                ("Can the system be copied to another store?", "The brief includes shipping, assembly and repeatability requirements, but each new store still requires confirmation against the plan, products, quantity, packaging and destination."),
            ],
        },
        "jp": {
            "label": "用途事例",
            "questions": [
                ("3C事例では何を記録していますか？", "資料には中古3C店舗向けのモジュール方向として、壁面展示、ガラスショーケース、床置きケース、交換可能な機能天板が記録されています。正式な契約範囲と数量は公開していません。"),
                ("別店舗にもそのまま展開できますか？", "資料には輸送、組立、複数店舗への展開を考えた方向がありますが、新しい店舗では平面、商品、数量、梱包、納品先を再確認します。"),
            ],
        },
    },
}


def enrich(path: Path, cfg: dict, slug: str, lang: str) -> None:
    text = path.read_text(encoding="utf-8")
    if 'data-bf-faq="1"' in text:
        return
    canonical = f"https://www.bigfame.co/{lang}/{slug}"
    crumb = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"https://www.bigfame.co/{lang}/"},
            {"@type": "ListItem", "position": 2, "name": cfg["label"], "item": f"https://www.bigfame.co/{lang}/applications"},
            {"@type": "ListItem", "position": 3, "name": slug, "item": canonical},
        ],
    }, ensure_ascii=False)
    faq = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in cfg["questions"]
        ],
    }, ensure_ascii=False)
    visible = "".join(f'<article class="location-card reveal"><h3>{q}</h3><p>{a}</p></article>' for q, a in cfg["questions"])
    section = f'<section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">{cfg["label"]} FAQ</h2></div><div class="grid-2">{visible}</div></div></section>'
    text = text.replace("</head>", f'<script type="application/ld+json">{crumb}</script><script type="application/ld+json">{faq}</script></head>', 1)
    text = text.replace('<section class="section section-dark">', section + '<section class="section section-dark">', 1)
    path.write_text(text, encoding="utf-8")


for slug, locales in CASES.items():
    for lang, cfg in locales.items():
        enrich(ROOT / lang / f"{slug}.html", cfg, slug, lang)
