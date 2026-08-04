"""Generate localized optical display hook pages from the verified drawing/photo evidence."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = {
    "tw": {
        "lang": "zh-Hant-TW", "name": "眼鏡展示掛勾", "alt": "眼鏡展示掛勾的黑、白與鍍鉻版本",
        "desc": "具 25 mm pitch 與 Ø6 mm 孔位圖面依據的眼鏡展示掛勾，適合眼鏡品牌門市、槽板與洞洞板展示。",
        "home": "首頁", "products": "產品與能力", "apps": "應用案例", "contact": "開始詢問",
        "cta": "詢問眼鏡掛勾規格", "h2": "圖面已確認的規格", "role": "buyer",
        "fields": [("孔位 pitch", "25 mm"), ("孔徑", "Ø6 mm"), ("展示方式", "圖面展示壁面、槽板／洞洞板相容方向；實際相容性依背板與樣品確認。"), ("外觀版本", "圖面／照片可見黑、白與鍍鉻外觀；正式表面處理依 SKU 確認。"), ("材質", "金屬線材與安裝片的產品形態可由圖面與照片核對；正式材質牌號依 SKU／圖面確認。"), ("MOQ／交期", "通用專案討論基準：客製五金通常 500 pcs 起、打樣約 2–3 週；正式數量與交期需按 SKU 確認。")],
        "faq": [("這個掛勾適合槽板或洞洞板嗎？", "圖面呈現壁面展示與多種背板／掛件方向；請提供背板孔位、厚度與照片，我們會按實際系統確認。"), ("可以從 CAD 或照片開始嗎？", "可以。請提供產品尺寸、背板系統、預估數量、目標交期與 PDF、DWG、DXF、STEP 或照片。"), ("25 mm 是什麼規格？", "來源圖面標示 25 mm pitch 與 Ø6 mm 孔位；其他長度、線徑與表面處理不應由此頁推定。")],
    },
    "en": {
        "lang": "en", "name": "Optical Display Hooks", "alt": "Optical display hooks in black, white and chrome finishes",
        "desc": "Optical display hooks with drawing evidence for a 25 mm pitch and Ø6 mm holes, for eyewear retail, slatwall and pegboard display projects.",
        "home": "Home", "products": "Products", "apps": "Applications", "contact": "Start an inquiry", "cta": "Ask about optical hooks", "h2": "Drawing-backed specification", "role": "buyer",
        "fields": [("Hole pitch", "25 mm"), ("Hole diameter", "Ø6 mm"), ("Display systems", "The drawing shows wall, slatwall and pegboard-oriented configurations; confirm the actual backing system and sample."), ("Appearance", "Black, white and chrome variants are visible in the drawing/photo set; final finish is SKU-specific."), ("Material", "The drawing/photo set shows wire and mounting-plate construction; confirm the formal material grade by SKU/drawing."), ("MOQ / lead time", "General project baseline: custom hardware is commonly discussed from 500 pcs and sampling from about 2–3 weeks; confirm the actual SKU.")],
        "faq": [("Can these hooks work with slatwall or pegboard?", "The drawing shows wall and multiple backing/display directions. Share the backing pitch, thickness and a photo so we can confirm compatibility."), ("Can I start with a CAD file or photo?", "Yes. Share product dimensions, backing system, estimated quantity, target date and a PDF, DWG, DXF, STEP file or photo."), ("What does 25 mm refer to?", "The source drawing marks a 25 mm pitch and Ø6 mm holes. Do not infer other lengths, wire diameters or finishes from this page.")],
    },
    "jp": {
        "lang": "ja", "name": "眼鏡展示フック", "alt": "ブラック、ホワイト、クロームの眼鏡展示フック", "desc": "25 mm pitch と Ø6 mm 孔の図面根拠がある眼鏡展示フック。眼鏡店、スラットウォール、有孔ボードの展示に対応します。", "home": "ホーム", "products": "製品", "apps": "用途・事例", "contact": "お問い合わせ", "cta": "眼鏡フックを相談する", "h2": "図面で確認できる仕様", "role": "buyer",
        "fields": [("孔ピッチ", "25 mm"), ("孔径", "Ø6 mm"), ("展示システム", "図面には壁面、スラットウォール、有孔ボード向けの方向を記録。実際の互換性は背板とサンプルで確認します。"), ("外観", "図面・写真にはブラック、ホワイト、クロームのバリエーション。正式仕上げは SKU ごとに確認します。"), ("材質", "図面・写真から線材と取付プレートの構成を確認できます。正式な材質グレードは SKU／図面で確認します。"), ("MOQ／納期", "一般的な相談基準はカスタム金具 500 pcs から、サンプル約 2–3 週間。実際の SKU で確認します。" )],
        "faq": [("スラットウォールや有孔ボードに使えますか？", "図面には壁面と複数の背板方向を記録しています。背板のピッチ、厚み、写真をお送りください。"), ("CAD や写真から相談できますか？", "可能です。寸法、背板システム、数量、希望納期、PDF、DWG、DXF、STEP または写真をご用意ください。"), ("25 mm とは何ですか？", "元図面に 25 mm pitch と Ø6 mm の孔が記載されています。その他の長さ、線径、仕上げは推測しません。")],
    },
}


def render(lang: str, cfg: dict) -> str:
    slug = "optical-hooks"
    base = f"https://www.bigfame.co/{lang}/{slug}"
    alts = ''.join(f'<link rel="alternate" hreflang="{h}" href="https://www.bigfame.co/{l}/{slug}">' for h, l in (("zh-TW", "tw"), ("en", "en"), ("ja", "jp")))
    fields = ''.join(f'<article class="location-card reveal"><h3>{html.escape(k)}</h3><p>{html.escape(v)}</p></article>' for k, v in cfg["fields"])
    faq_json = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in cfg["faq"]]}, ensure_ascii=False)
    product_json = json.dumps({"@context":"https://schema.org","@type":"Product","name":cfg["name"],"image":["https://www.bigfame.co/images/product-optical-hooks.png"],"category":"Eyewear retail display hardware","material":"Confirm by SKU and drawing","additionalProperty":[{"@type":"PropertyValue","name":"Drawing pitch","value":"25 mm"},{"@type":"PropertyValue","name":"Drawing hole diameter","value":"6 mm"}],"manufacturer":{"@type":"Organization","name":"Big Fame IND. CORP."},"url":base}, ensure_ascii=False)
    crumb_json = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Big Fame","item":f"https://www.bigfame.co/{lang}/"},{"@type":"ListItem","position":2,"name":cfg["products"],"item":f"https://www.bigfame.co/{lang}/products"},{"@type":"ListItem","position":3,"name":cfg["name"],"item":base}]}, ensure_ascii=False)
    faq_visible = ''.join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q,a in cfg["faq"])
    contact = f'contact?category=display_hardware&role={cfg["role"]}'
    return f'''<!DOCTYPE html><html lang="{cfg["lang"]}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(cfg["desc"], quote=True)}"><title>{html.escape(cfg["name"])} | Big Fame</title><link rel="canonical" href="{base}">{alts}<link rel="stylesheet" href="../css/style.css"><script type="application/ld+json">{product_json}</script><script type="application/ld+json">{crumb_json}</script><script type="application/ld+json">{faq_json}</script></head><body><header class="header"><div class="container header-inner"><a href="./" class="logo">BIG FAME</a><nav class="nav-menu"><a href="./" class="nav-link">{cfg["home"]}</a><a href="products" class="nav-link active">{cfg["products"]}</a><a href="applications" class="nav-link">{cfg["apps"]}</a><a href="{contact}" class="nav-link nav-cta">{cfg["contact"]}</a></nav></div></header><main><section class="hero"><div class="container hero-content reveal"><p class="hero-kicker">EYEWEAR RETAIL DISPLAY HARDWARE</p><h1>{html.escape(cfg["name"])}</h1><p class="hero-description">{html.escape(cfg["desc"])}</p><a class="btn btn-primary" href="{contact}">{cfg["cta"]}</a></div></section><section class="section section-light"><div class="container grid-2"><div class="reveal"><img class="hero-image-main" src="../images/product-optical-hooks.png" alt="{html.escape(cfg["alt"], quote=True)}"></div><div class="location-card reveal"><span class="section-subtitle">DRAWING + PHOTO EVIDENCE</span><h2>{cfg["h2"]}</h2><p>{html.escape(cfg["desc"])}</p><p>Source evidence: Eyewear Display Hook drawing set; the visible drawing marks 25 mm pitch and Ø6 mm holes.</p></div></div></section><section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SPECIFICATION</span><h2 class="section-title">{cfg["h2"]}</h2></div><div class="grid-3">{fields}</div><p class="section-note reveal">Dimensions above are limited to the visible drawing evidence. Formal SKU material, wire diameter, finish, MOQ and delivery schedule require confirmation against the current drawing and sample.</p><p class="reveal"><a href="case-eyewear-2016">Related eyewear retail case</a> · <a href="case-modular-3c-store">Related modular retail case</a></p></div></section><section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">FAQ</h2></div><div class="grid-3">{faq_visible}</div></div></section><section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{cfg["cta"]}</h2><a class="btn btn-primary" href="{contact}">{cfg["contact"]}</a></div></div></section></main><footer class="footer"><div class="container footer-bottom"><p>© Big Fame IND. CORP.</p><a href="products">{cfg["products"]}</a></div></footer><script src="../js/main.js"></script></body></html>'''


for lang, cfg in DATA.items():
    (ROOT / lang / "optical-hooks.html").write_text(render(lang, cfg), encoding="utf-8", newline="")
