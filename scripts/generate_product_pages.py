"""Generate evidence-controlled product entry pages for the three locales."""

from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = [
    ("display-hooks", "Display Hooks", "展示掛鉤", "ディスプレイフック", "店面展示掛鉤、背板掛鉤與展示配件的採購入口。"),
    ("optical-hooks", "Optical Display Hooks", "眼鏡展示掛鉤", "メガネディスプレイフック", "適用於眼鏡與小型商品展示的掛鉤方向，依商品尺寸與展示方式確認。"),
    ("anti-theft-hooks", "Anti-theft Display Hooks", "防盜展示掛鉤", "防犯ディスプレイフック", "針對商品安全展示與取放管理的掛鉤需求，依店型與防盜條件確認。"),
    ("slatwall-pegboard-accessories", "Slatwall and Pegboard Accessories", "槽板／洞洞板配件", "スラットウォール・有孔ボード用金具", "槽板、洞洞板、方管與模組化展示系統配件的採購入口。"),
    ("price-tag-holders", "Price Tag Holders and Signage Accessories", "價格條與標示配件", "プライスレール・表示金具", "價格牌、標示、吊牌與展示連接件的採購與開發入口。"),
    ("pos-displays", "POS Displays", "POS 展示架", "POSディスプレイ", "桌上型展示架、品牌促銷展示與零售 POS 情境的整合入口。"),
    ("modular-fixtures", "Modular Retail Display Fixtures", "模組化展示架", "モジュール什器", "可依店型、商品流線與展示系統討論的模組化展示設備。"),
    ("custom-metal-parts", "Custom Metal Parts for Retail Display", "客製金屬零件", "店舗什器向けカスタム金属部品", "依圖面開發的展示設備金屬零件、支架與連接件。"),
]

LABELS = {
    "tw": {"lang":"zh-Hant-TW", "home":"首頁", "products":"產品", "cases":"應用案例", "contact":"開始詢問", "role":"buyer", "cta":"提交產品與數量", "category":"display_hardware", "h2":"採購前先確認這些條件", "fields":[("適用店型","服飾、眼鏡／精品、化妝品、便利商店、超市、家居、3C 與其他零售情境；以實際店型確認。"),("適用系統","槽板、洞洞板、方管、桌面或客製展示結構；相容性依圖面與樣品確認。"),("材質／尺寸／表面處理","依產品、SKU、圖面與樣品確認，不在未有證據時預設規格。"),("MOQ／交期","客製五金通常 500 pcs 起；整體展示專案通常 50 sets 起。打樣約 2–3 週，首批約 6–8 週，重複訂單約 4–6 週，仍以專案確認為準。"),("客製範圍","可從照片、PDF、DWG、DXF、STEP 或概念需求開始討論。"),("圖片／圖面","本頁先作需求入口；可在詢問表附上照片、圖面與數量。")], "notice":"上述為目前可公開的通用採購框架；實際尺寸、材料、表面處理與報價必須依 SKU 或圖面確認。"},
    "en": {"lang":"en", "home":"Home", "products":"Products", "cases":"Applications", "contact":"Start an inquiry", "role":"buyer", "cta":"Submit product and quantity", "category":"display_hardware", "h2":"Confirm these conditions before sourcing", "fields":[("Suitable store types","Apparel, eyewear, cosmetics, convenience, supermarket, home, 3C and other retail situations; confirm against the actual store format."),("Compatible systems","Slatwall, pegboard, square tubing, countertop or custom display structures; confirm compatibility with drawings and samples."),("Material / dimensions / finish","Confirm by product, SKU, drawing and sample. Do not assume specifications without evidence."),("MOQ / lead time","Custom hardware is usually discussed from 500 pcs; a full fixture project is usually discussed from 50 sets. Sampling is about 2–3 weeks, first batch about 6–8 weeks and repeat orders about 4–6 weeks, subject to project confirmation."),("Customization","Start with a photo, PDF, DWG, DXF, STEP file or a concept brief."),("Images / drawings","Use this page as the sourcing entry and attach photos, drawings and quantity in the inquiry form.")], "notice":"This is the current public general sourcing framework. Actual dimensions, materials, finishes and quotation require SKU or drawing confirmation."},
    "jp": {"lang":"ja", "home":"ホーム", "products":"製品", "cases":"導入事例", "contact":"お問い合わせ", "role":"buyer", "cta":"製品・数量を送る", "category":"display_hardware", "h2":"調達前に確認する条件", "fields":[("適用店舗","アパレル、メガネ、コスメ、コンビニ、スーパー、ホーム、3Cなど。実際の店舗形態で確認します。"),("対応システム","スラットウォール、有孔ボード、角パイプ、卓上またはカスタム什器。図面とサンプルで確認します。"),("材質・寸法・仕上げ","製品、SKU、図面、サンプルにより確認します。根拠のない規格は掲載しません。"),("MOQ・納期","カスタム金具は通常500個から、什器プロジェクトは通常50セットから相談。試作約2–3週間、初回約6–8週間、リピート約4–6週間を目安とし、案件ごとに確認します。"),("カスタム範囲","写真、PDF、DWG、DXF、STEPまたは概念資料から相談できます。"),("画像・図面","写真、図面、数量を問い合わせフォームに添付してください。")], "notice":"公開しているのは一般的な調達フレームです。寸法、材質、仕上げ、見積はSKUまたは図面で確認します。"},
}


def render(folder: str, slug: str, names: tuple, description: str, cfg: dict) -> str:
    zh, en, ja, _ = names
    title_name = {"tw": zh, "en": en, "jp": ja}[folder]
    base = f"https://www.bigfame.co/{folder}/{slug}"
    alternates = ''.join(f'<link rel="alternate" hreflang="{hreflang}" href="https://www.bigfame.co/{target}/{slug}">' for hreflang, target in (("zh-TW","tw"),("en","en"),("ja","jp")))
    fields = ''.join(f'<article class="location-card reveal"><h3>{html.escape(h)}</h3><p>{html.escape(v)}</p></article>' for h, v in cfg["fields"])
    contact = f'contact?category={cfg["category"]}&role={cfg["role"]}'
    schema = json.dumps({"@context":"https://schema.org", "@type":"CollectionPage", "name":title_name, "description":description, "url":base}, ensure_ascii=False)
    return f'''<!DOCTYPE html><html lang="{cfg["lang"]}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(description, quote=True)}"><title>{html.escape(title_name)} | Big Fame</title><link rel="canonical" href="{base}">{alternates}<link rel="stylesheet" href="../css/style.css"><script type="application/ld+json">{schema}</script></head><body><header class="header"><div class="container header-inner"><a href="./" class="logo">BIG FAME</a><nav class="nav-menu"><a href="./" class="nav-link">{cfg["home"]}</a><a href="products" class="nav-link active">{cfg["products"]}</a><a href="applications" class="nav-link">{cfg["cases"]}</a><a href="{contact}" class="nav-link nav-cta">{cfg["contact"]}</a></nav></div></header><main><section class="hero"><div class="container hero-content reveal"><p class="hero-kicker">B2B RETAIL DISPLAY HARDWARE</p><h1>{html.escape(title_name)}</h1><p class="hero-description">{html.escape(description)}</p><a class="btn btn-primary" href="{contact}">{cfg["cta"]}</a></div></section><section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SPECIFICATION CHECKLIST</span><h2 class="section-title">{cfg["h2"]}</h2></div><div class="grid-3">{fields}</div><p class="section-note reveal">{html.escape(cfg["notice"])}</p><p class="reveal"><a href="applications">{cfg["cases"]}</a> · <a href="display-hooks">Display hardware overview</a></p></div></section><section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{cfg["cta"]}</h2><a class="btn btn-primary" href="{contact}">{cfg["contact"]}</a></div></div></section></main><footer class="footer"><div class="container footer-bottom"><p>© 1988-2026 Big Fame IND. CORP.</p><a href="{contact}">{cfg["contact"]}</a></div></footer><script src="../js/main.js"></script></body></html>'''


for folder, cfg in LABELS.items():
    for slug, en, zh, ja, description in PRODUCTS:
        (ROOT / folder / f"{slug}.html").write_text(render(folder, slug, (zh, en, ja, slug), description, cfg), encoding="utf-8")
