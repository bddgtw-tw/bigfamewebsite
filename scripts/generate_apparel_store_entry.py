"""Generate a trilingual apparel-store fixture search entry."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
SLUG = "apparel-store-fixtures"

DATA = {
    "tw": {"lang": "zh-Hant-TW", "title": "服飾店展示設備與店面規劃", "description": "服飾店展示設備與店面規劃入口：中島、壁面展示、掛勾、衣架、模組化展示架與木作／壓克力品牌什器。", "nav": ("首頁", "產品", "應用案例", "討論服飾店型"), "kicker": "APPAREL RETAIL ENTRY", "lead": "把服飾店的展示密度、動線與品牌材料整理成可確認的採購條件。", "intro": "服飾店通常同時需要中島展示、壁面陳列、吊掛系統、衣架、標示與補貨動線。先提供平面、照片、商品尺寸、展示數量與材質方向，再進入產品、圖面、打樣與交付條件確認。", "cards": [("店面問題", "展示密度、試穿動線、補貨方式、品牌視覺與多店複製條件需要一起被整理。"), ("可討論的產品", "模組化展示架、展示掛勾、槽板／洞洞板配件、價格條與標示配件、POS 展示與客製金屬零件。"), ("材料與規格", "木材、金屬、壓克力與複合材質可以作為討論方向；正式材質、尺寸、表面處理與承重依圖面／樣品確認。"), ("採購前資料", "提供店型、平面或照片、商品與數量、目標日期、交貨地、包裝與是否需要 CAD／打樣。")], "faq": [("服飾店展示設備可以從哪裡開始？", "可先從模組化展示架、展示掛勾、槽板配件、價格牌座與 POS 展示方向比對，再依商品尺寸與店面動線確認。"), ("可以從 CAD 或照片開始嗎？", "可以。PDF、DWG、DXF、STEP 或照片都能作為規格討論起點；正式打樣與報價條件依產品與專案確認。"), ("服飾店展示設備的 MOQ 與交期是多少？", "沒有所有產品共用的 MOQ 或交期；需依型號、材質、數量、版本、樣品與排程確認。")], "cta": "討論服飾店展示條件", "related": (("2016 服飾照片紀錄", "case-apparel-2016"), ("模組化展示架", "modular-fixtures"), ("展示掛勾", "display-hooks"), ("規格與 CAD 資料索取", "technical-resources"))},
    "en": {"lang": "en", "title": "Apparel Store Fixtures & Retail Planning", "description": "Apparel store fixture and retail-planning entry for island displays, wall merchandising, hooks, garment racks, modular fixtures and wood or acrylic brand fixtures.", "nav": ("Home", "Products", "Applications", "Discuss apparel retail"), "kicker": "APPAREL RETAIL ENTRY", "lead": "Turn apparel-store density, customer flow and material direction into confirmable sourcing conditions.", "intro": "Apparel stores often combine island displays, wall merchandising, hanging systems, garment racks, signage and replenishment flow. Start with a plan, photos, merchandise dimensions, display quantity and material direction before reviewing products, drawings, sampling and delivery conditions.", "cards": [("The store problem", "Display density, try-on flow, replenishment, brand language and multi-store replication often need to be considered together."), ("Products to compare", "Modular fixtures, display hooks, slatwall or pegboard accessories, price-tag and signage accessories, POS displays and custom metal parts."), ("Materials and specification", "Wood, metal, acrylic and composite materials can be discussed as directions; formal material, dimensions, finish and load require drawing or sample confirmation."), ("Prepare before sourcing", "Share the store type, plan or photos, merchandise and quantity, target date, destination, packing needs and whether CAD or sampling is required.")], "faq": [("Where should an apparel-store fixture inquiry start?", "Compare modular fixtures, display hooks, slatwall accessories, price-tag holders and POS directions first, then align them with merchandise dimensions and store flow."), ("Can we start with CAD or photos?", "Yes. PDF, DWG, DXF, STEP or photos can start a specification discussion; formal sampling and quotation conditions are confirmed by product and project."), ("What are the MOQ and lead time for apparel fixtures?", "There is no universal MOQ or lead time for every product. Confirm them by model, material, quantity, revision, sample and production schedule.")], "cta": "Discuss apparel-store fixture conditions", "related": (("2016 Apparel Photo Record", "case-apparel-2016"), ("Modular Fixtures", "modular-fixtures"), ("Display Hooks", "display-hooks"), ("Technical Resources & CAD Request", "technical-resources"))},
    "jp": {"lang": "ja", "title": "アパレル店舗什器と店舗計画", "description": "アパレル店舗の什器・店舗計画入口。島什器、壁面陳列、フック、ハンガーラック、モジュール什器、木材・アクリル什器を整理します。", "nav": ("ホーム", "製品", "用途事例", "アパレル店舗を相談"), "kicker": "APPAREL RETAIL ENTRY", "lead": "アパレル店舗の展示密度、動線、材料方向を確認可能な調達条件へ整理します。", "intro": "アパレル店舗では、島什器、壁面陳列、ハンギングシステム、ハンガーラック、表示、補充動線を組み合わせます。平面、写真、商品寸法、数量、材料方向を共有してから、製品、図面、試作、納品条件を確認します。", "cards": [("店舗の課題", "展示密度、試着動線、補充方法、ブランドの素材感、多店舗展開を一緒に整理します。"), ("比較できる製品", "モジュール什器、ディスプレイフック、スラットウォール・有孔ボード金具、値札・表示用アクセサリー、POS什器、カスタム金属部品。"), ("材料と仕様", "木材、金属、アクリル、複合材を方向として相談できます。正式な材料、寸法、仕上げ、荷重は図面・サンプルで確認します。"), ("調達前に準備するもの", "業態、平面または写真、商品と数量、希望時期、納品地、梱包条件、CAD・試作の要否を共有してください。")], "faq": [("アパレル店舗什器は何から相談しますか？", "モジュール什器、ディスプレイフック、スラットウォール金具、値札ホルダー、POS什器を比較し、商品寸法と店舗動線に合わせて確認します。"), ("CAD や写真から始められますか？", "はい。PDF、DWG、DXF、STEP、写真を仕様相談の起点にできます。正式な試作・見積条件は製品と案件で確認します。"), ("アパレル什器の MOQ と納期は？", "全製品共通の MOQ・納期はありません。型式、材料、数量、版、サンプル、工程で確認します。")], "cta": "アパレル店舗の什器条件を相談する", "related": (("2016年アパレル写真記録", "case-apparel-2016"), ("モジュール什器", "modular-fixtures"), ("ディスプレイフック", "display-hooks"), ("仕様・CAD資料", "technical-resources"))},
}


def make_page(folder: str, d: dict) -> str:
    base = f"https://www.bigfame.co/{folder}/{SLUG}"
    alts = "".join(f'<link rel="alternate" hreflang="{code}" href="https://www.bigfame.co/{loc}/{SLUG}">' for code, loc in (("zh-TW", "tw"), ("en", "en"), ("ja", "jp")))
    collection = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": d["title"], "description": d["description"], "url": base}, ensure_ascii=False)
    breadcrumb = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"https://www.bigfame.co/{folder}/"}, {"@type": "ListItem", "position": 2, "name": d["nav"][2], "item": f"https://www.bigfame.co/{folder}/applications"}, {"@type": "ListItem", "position": 3, "name": d["title"], "item": base}]}, ensure_ascii=False)
    faq = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}, ensure_ascii=False)
    cards = "".join(f'<article class="location-card reveal"><h3>{html.escape(h)}</h3><p>{html.escape(b)}</p></article>' for h, b in d["cards"])
    faqs = "".join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in d["faq"])
    related = " · ".join(f'<a href="{slug}">{html.escape(name)}</a>' for name, slug in d["related"])
    contact = "contact?category=system_fixtures&role=brand"
    return f'''<!DOCTYPE html><html lang="{d["lang"]}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(d["description"], quote=True)}"><title>{html.escape(d["title"])} | Big Fame</title><link rel="canonical" href="{base}">{alts}<link rel="stylesheet" href="../css/style.css"><script type="application/ld+json">{collection}</script><script type="application/ld+json">{breadcrumb}</script><script type="application/ld+json">{faq}</script></head><body><header class="header"><div class="container header-inner"><a href="./" class="logo">BIG FAME</a><nav class="nav-menu"><a href="./" class="nav-link">{d["nav"][0]}</a><a href="products" class="nav-link active">{d["nav"][1]}</a><a href="applications" class="nav-link">{d["nav"][2]}</a><a href="{contact}" class="nav-link nav-cta">{d["nav"][3]}</a></nav></div></header><main><section class="hero"><div class="container hero-content reveal"><p class="hero-kicker">{d["kicker"]}</p><h1>{html.escape(d["title"])}</h1><p class="hero-description">{html.escape(d["lead"])}</p><a class="btn btn-primary" href="{contact}">{html.escape(d["cta"])}</a></div></section><section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">STORE-TYPE REQUIREMENTS</span><h2 class="section-title">{html.escape(d["title"])}</h2><p class="section-note">{html.escape(d["intro"])}</p></div><div class="grid-2">{cards}</div></div></section><section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">FAQ</h2></div><div class="grid-3">{faqs}</div></div></section><section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{html.escape(d["cta"])}</h2><p>{related}</p><p class="section-note">This is a store-type planning entry, not a named client case. Formal products, quantities, lead times and delivery scope require project confirmation.</p><a class="btn btn-primary" href="{contact}">{html.escape(d["nav"][3])}</a></div></div></section></main><footer class="footer"><div class="container footer-bottom"><p>© Big Fame IND. CORP.</p><a href="applications">{d["nav"][2]}</a></div></footer><script src="../js/main.js"></script></body></html>'''


for folder, data in DATA.items():
    (ROOT / folder / f"{SLUG}.html").write_text(make_page(folder, data), encoding="utf-8")

markers = {
    "tw": ('<a href="contact?category=system_fixtures" class="btn btn-secondary"', '<a href="apparel-store-fixtures">查看服飾店展示規劃入口</a>'),
    "en": ('<a href="contact?category=system_fixtures" class="btn btn-secondary"', '<a href="apparel-store-fixtures">Open apparel fixture planning entry</a>'),
    "jp": ('<a href="contact?category=system_fixtures" class="btn btn-secondary"', '<a href="apparel-store-fixtures">アパレル什器の計画入口を見る</a>'),
}
for folder, (needle, link) in markers.items():
    path = ROOT / folder / "applications.html"
    text = path.read_text(encoding="utf-8")
    if "apparel-store-fixtures" not in text:
        idx = text.find(needle, text.find('id="apparel"'))
        if idx < 0:
            raise SystemExit(f"Apparel card CTA not found: {folder}")
        text = text[:idx] + link + " · " + text[idx:]
        path.write_text(text, encoding="utf-8")

sitemap = ROOT / "sitemap.xml"
text = sitemap.read_text(encoding="utf-8")
for folder in DATA:
    line = f"  <url><loc>https://www.bigfame.co/{folder}/{SLUG}</loc></url>"
    if line not in text:
        text = text.replace("</urlset>", line + "\n</urlset>")
sitemap.write_text(text, encoding="utf-8")
print(f"Generated {SLUG} in tw/en/jp, linked apparel application cards, and updated sitemap.")
