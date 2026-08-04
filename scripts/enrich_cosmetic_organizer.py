"""Enrich the evidence-controlled tabletop cosmetic organizer entry."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = {
    "tw": {
        "label": "桌上型化妝品收納展示器",
        "alt": "PAGE 桌上型化妝品收納展示器",
        "intro": "以透明壓克力與實木組成的桌上型化妝品展示器，從已核對的尺寸、材質與交期資料開始詢問。",
        "faq": [("Offer Form 已確認哪些條件？", "2020-03-30 ver.01 資料記錄 W250 × D120 × H240 mm、透明壓克力邊緣拋光、實木、1 SET/CTN、樣品約 15–25 天與量產約 25–35 天。"), ("MOQ 是否已公開？", "目前來源 PDF 未記錄通用 MOQ；數量、包裝、交貨地與正式報價需依專案確認。"), ("可以客製或從圖面開始嗎？", "可以先提供照片、圖面、商品尺寸、數量與目標日期，再依版本與樣品確認客製範圍。" )],
        "gate": "MOQ、正式 SKU、包裝細節、客製範圍與交貨條件仍需依專案確認。",
        "related": "相關入口：POS／桌上型展示、價格條與標示配件、化妝品與藥妝店型。",
    },
    "en": {
        "label": "Tabletop Cosmetic Organizer",
        "alt": "PAGE tabletop cosmetic organizer",
        "intro": "A tabletop cosmetic organizer combining clear polished-edge acrylic and solid wood, starting from verified dimensions, materials and schedule records.",
        "faq": [("What does the Offer Form confirm?", "The 2020-03-30 ver.01 record identifies W250 × D120 × H240 mm, clear polished-edge acrylic, solid wood, 1 SET/CTN, about 15–25 days for a sample and about 25–35 days for bulk after order confirmation."), ("Is a universal MOQ published?", "The source PDF does not record a universal MOQ. Confirm quantity, packing, destination and quotation by project."), ("Can we start with a drawing or request customization?", "Share photos, drawings, product dimensions, quantity and target date first; confirm the revision and customization scope against the sample and project." )],
        "gate": "MOQ, formal SKU, packing details, customization scope and delivery conditions require project confirmation.",
        "related": "Related routes: POS / countertop displays, price-tag holders and beauty or drugstore store formats.",
    },
    "jp": {
        "label": "卓上化粧品オーガナイザー",
        "alt": "PAGE 卓上化粧品オーガナイザー",
        "intro": "エッジ研磨の透明アクリルと無垢材を組み合わせた卓上化粧品オーガナイザー。確認済みの寸法、材質、納期資料から相談を始めます。",
        "faq": [("Offer Form で確認できる条件は？", "2020-03-30 ver.01 の資料には W250 × D120 × H240 mm、エッジ研磨透明アクリル、無垢材、1 SET/CTN、サンプル約15–25日、量産約25–35日が記録されています。"), ("共通 MOQ は公開されていますか？", "原資料の PDF に共通 MOQ の記録はありません。数量、梱包、納品先、見積は案件ごとに確認します。"), ("図面から相談できますか？", "写真、図面、商品寸法、数量、希望時期を共有し、サンプルと案件条件で改訂範囲を確認します。" )],
        "gate": "MOQ、正式 SKU、梱包詳細、カスタム範囲、納品条件は案件ごとに確認します。",
        "related": "関連：POS／卓上ディスプレイ、値札・表示用アクセサリー、コスメ・ドラッグストア店舗。",
    },
}


def enrich(path: Path, lang: str) -> None:
    text = path.read_text(encoding="utf-8")
    if 'data-bf-faq="1"' in text:
        return
    d = DATA[lang]
    image = "../../images/product-cosmetic-organizer.png" if path.name == "index.html" else "../images/product-cosmetic-organizer.png"
    text = text.replace(
        '"category":"Retail display / tabletop cosmetic organizer","material"',
        '"category":"Retail display / tabletop cosmetic organizer","image":["https://www.bigfame.co/images/product-cosmetic-organizer.png"],"material"',
        1,
    )
    visual = f'<section class="section section-light" data-bf-cosmetic="1"><div class="container grid-2"><div class="reveal"><img class="hero-image-main" src="{image}" alt="{d["alt"]}" loading="eager"></div><div class="location-card reveal"><span class="section-subtitle">SOURCE IMAGE EVIDENCE</span><h2>{d["label"]}</h2><p>{d["intro"]}</p><p>Representative image: BF-TP-CH0001-03. Formal product identity and final commercial conditions remain subject to source and project confirmation.</p></div></div></section>'
    spec_marker = '<section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">CONFIRMED SPECIFICATION</span>'
    text = text.replace(spec_marker, visual + spec_marker, 1)
    faq_schema = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}, ensure_ascii=False)
    text = text.replace("</head>", f'<script type="application/ld+json">{faq_schema}</script></head>', 1)
    visible = "".join(f'<article class="location-card reveal"><h3>{q}</h3><p>{a}</p></article>' for q, a in d["faq"])
    buyer = f'<section class="section section-light" data-bf-cosmetic="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">BUYER CHECKLIST</span><h2 class="section-title">{d["label"]}</h2></div><div class="grid-3"><article class="location-card reveal"><h3>MOQ</h3><p>{d["gate"]}</p></article><article class="location-card reveal"><h3>Customization</h3><p>{d["faq"][2][1]}</p></article><article class="location-card reveal"><h3>Related use</h3><p>{d["related"]}</p></article></div></div></section>'
    faq = f'<section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">{d["label"]} FAQ</h2></div><div class="grid-3">{visible}</div></div></section>'
    if '<section class="section section-dark">' in text:
        text = text.replace('<section class="section section-dark">', buyer + faq + '<section class="section section-dark">', 1)
    else:
        text = text.replace('</main>', buyer + faq + '</main>', 1)
    path.write_text(text, encoding="utf-8")


for lang in DATA:
    for path in (ROOT / lang).glob("cosmetic-organizers.html"):
        enrich(path, lang)
    index = ROOT / lang / "cosmetic-organizers" / "index.html"
    if index.exists():
        enrich(index, lang)
