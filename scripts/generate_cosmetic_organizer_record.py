"""Generate a trilingual evidence-controlled PAGE cosmetic organizer record."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
SLUG = "case-page-cosmetic-organizer"
IMAGE = "https://www.bigfame.co/images/product-cosmetic-organizer.png"

DATA = {
    "tw": {
        "lang": "zh-Hant-TW",
        "title": "PAGE 桌上型化妝品收納展示器資料紀錄",
        "description": "PAGE 桌上型化妝品收納展示器的證據控制紀錄：尺寸、壓克力與實木材質、包裝與樣品／量產交期以 2020-03-30 ver.01 文件為準。",
        "nav": ("首頁", "產品", "應用案例", "提交需求"),
        "kicker": "DOCUMENTED PRODUCT DEVELOPMENT RECORD",
        "need_title": "把桌上型美妝展示需求整理成可確認的規格",
        "need": "PAGE Offer Form 將一款垂直式桌上型化妝品收納展示器整理成尺寸、材質、包裝與交期條件，適合作為美妝櫃位、桌上型陳列與品牌展示需求的規格討論起點。",
        "record_title": "2020-03-30 ver.01 文件可核對內容",
        "record": [
            ("產品方向", "文件標示 Project PAGE / Tabletop Cosmetic Organizer，並以透明展示結構與垂直收納作為產品方向。"),
            ("尺寸", "文件記錄 W250 × D120 × H240 mm。此尺寸限於文件所示版本，不外推至其他型號。"),
            ("材質與表面", "文件記錄 Clear Acrylic、Edge polished，以及 Solid wood；正式板厚、木種與其他加工條件仍需依圖面與樣品確認。"),
            ("包裝", "文件記錄 1 SET/CTN；外箱尺寸、保護方式與運輸條件未在本公開紀錄推定。"),
            ("文件交期", "文件記錄樣品約 15–25 天、量產在訂單確認後約 25–35 天；實際交期仍依數量、版本、排程與交付地確認。"),
            ("證據邊界", "本頁使用 Offer Form、尺寸圖與產品影像作為規格討論證據；客戶名稱、正式 MOQ、數量、交付地、授權與完成成果未由來源確認。"),
        ],
        "faq": [
            ("這是已完成的客戶案例嗎？", "不是。本頁是匿名的產品開發／報價文件紀錄，公開已核對的規格方向，不推定客戶、訂單或最終交付成果。"),
            ("如果要詢問類似產品，應提供什麼？", "請提供商品尺寸、展示數量、櫃位或桌面尺寸、目標日期、交貨地、圖面或照片，以及是否需要透明壓克力、木作或其他材質方向。"),
        ],
        "cta": "詢問桌上型化妝品展示需求",
        "boundary": "本頁為證據控制的產品開發紀錄，不代表已核准的客戶案例、通用 MOQ、固定交期或正式量產承諾。",
        "related": (("桌上型化妝品收納展示器", "cosmetic-organizers"), ("POS 展示架", "pos-displays")),
        "app_text": ("PAGE 化妝品展示紀錄", "查看透明壓克力與實木桌上型展示器的文件證據。", "查看證據紀錄"),
    },
    "en": {
        "lang": "en",
        "title": "PAGE Tabletop Cosmetic Organizer Record",
        "description": "An evidence-controlled PAGE tabletop cosmetic organizer record: dimensions, acrylic and solid wood materials, packing and sample or bulk lead-time notes from the 2020-03-30 ver.01 document.",
        "nav": ("Home", "Products", "Applications", "Submit inquiry"),
        "kicker": "DOCUMENTED PRODUCT DEVELOPMENT RECORD",
        "need_title": "Turn a tabletop beauty-display need into confirmable conditions",
        "need": "The PAGE Offer Form organizes a vertical tabletop cosmetic organizer around dimensions, materials, packing and lead-time conditions. It can start a specification discussion for beauty counters, tabletop merchandising and brand display projects.",
        "record_title": "What the 2020-03-30 ver.01 document confirms",
        "record": [
            ("Product direction", "The document identifies the project as PAGE / Tabletop Cosmetic Organizer and presents a clear display structure with vertical storage."),
            ("Dimensions", "The document records W250 × D120 × H240 mm. This is limited to the documented version and is not extended to other models."),
            ("Materials and finish", "The document records clear acrylic with polished edges and solid wood. Sheet thickness, wood species and other processing conditions require drawing and sample confirmation."),
            ("Packing", "The document records 1 SET/CTN; carton dimensions, protection method and freight conditions are not inferred here."),
            ("Documented lead time", "The document records approximately 15–25 days for samples and approximately 25–35 days for bulk order after order confirmation. Actual timing depends on quantity, revision, schedule and destination."),
            ("Evidence boundary", "This page uses the Offer Form, dimension material and product images as specification-discussion evidence. Client name, formal MOQ, quantity, delivery location, authorization and completed outcome are not confirmed by the source."),
        ],
        "faq": [
            ("Is this a completed client case?", "No. This is an anonymous product-development and offer-form record. It publishes confirmed specification directions without inferring a client, order or final delivery outcome."),
            ("What should I share for a similar inquiry?", "Share merchandise dimensions, display quantity, counter or tabletop size, target date, destination, drawings or photos, and whether the direction should use clear acrylic, wood or another material."),
        ],
        "cta": "Discuss a tabletop cosmetic display",
        "boundary": "This is an evidence-controlled product-development record. It is not an approved client case, universal MOQ, fixed lead-time promise or mass-production commitment.",
        "related": (("Tabletop Cosmetic Organizer", "cosmetic-organizers"), ("POS Displays", "pos-displays")),
        "app_text": ("PAGE Cosmetic Display Record", "Review the documented evidence for a clear-acrylic and solid-wood tabletop organizer.", "Open evidence record"),
    },
    "jp": {
        "lang": "ja",
        "title": "PAGE 卓上化粧品オーガナイザー資料記録",
        "description": "PAGE 卓上化粧品オーガナイザーの証拠管理記録。2020-03-30 ver.01 の資料に基づき、寸法、アクリルと無垢材、梱包、サンプルと量産の納期方向を整理します。",
        "nav": ("ホーム", "製品", "用途事例", "相談を送る"),
        "kicker": "DOCUMENTED PRODUCT DEVELOPMENT RECORD",
        "need_title": "卓上化粧品展示の要件を確認可能な条件へ",
        "need": "PAGE Offer Form は、縦型の卓上化粧品オーガナイザーを寸法、材料、梱包、納期条件として整理しています。化粧品カウンター、卓上陳列、ブランド展示の仕様相談を始める資料として使用できます。",
        "record_title": "2020-03-30 ver.01 資料で確認できる内容",
        "record": [
            ("製品方向", "資料には Project PAGE / Tabletop Cosmetic Organizer と記載され、透明な展示構造と縦型収納の方向が示されています。"),
            ("寸法", "資料には W250 × D120 × H240 mm と記録されています。この寸法は記載された仕様に限り、他モデルへ拡張しません。"),
            ("材料と仕上げ", "透明アクリル、エッジ研磨、無垢材が資料に記録されています。板厚、木種、その他の加工条件は図面とサンプルで確認します。"),
            ("梱包", "1 SET/CTN と記録されています。外箱寸法、保護方法、輸送条件は推測しません。"),
            ("資料上の納期", "サンプル約15–25日、注文確認後の量産約25–35日と記録されています。実際の納期は数量、改訂、工程、納品地で確認します。"),
            ("証拠の範囲", "Offer Form、寸法資料、製品画像を仕様相談の根拠として使用しています。顧客名、正式 MOQ、数量、納品地、公開許諾、完成成果は原資料で確認できません。"),
        ],
        "faq": [
            ("完成した顧客事例ですか？", "いいえ。匿名の製品開発・見積資料の記録です。確認できる仕様方向のみを掲載し、顧客、注文、最終納品成果は推測しません。"),
            ("同様の製品を相談するには何を共有しますか？", "商品の寸法、展示数量、カウンターや卓上のサイズ、希望時期、納品地、図面または写真、透明アクリル・木材などの材料方向を共有してください。"),
        ],
        "cta": "卓上化粧品展示を相談する",
        "boundary": "証拠管理された製品開発記録です。承認済み顧客事例、共通 MOQ、固定納期、量産の確約を意味しません。",
        "related": (("卓上化粧品オーガナイザー", "cosmetic-organizers"), ("POS什器", "pos-displays")),
        "app_text": ("PAGE 化粧品展示記録", "透明アクリルと無垢材の卓上オーガナイザー資料を確認します。", "根拠資料を見る"),
    },
}


def make_page(folder: str, d: dict) -> str:
    base = f"https://www.bigfame.co/{folder}/{SLUG}"
    alternates = "".join(f'<link rel="alternate" hreflang="{code}" href="https://www.bigfame.co/{loc}/{SLUG}">' for code, loc in (("zh-TW", "tw"), ("en", "en"), ("ja", "jp")))
    article = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": d["title"], "description": d["description"], "image": IMAGE, "url": base}, ensure_ascii=False)
    breadcrumb = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"https://www.bigfame.co/{folder}/"}, {"@type": "ListItem", "position": 2, "name": d["nav"][2], "item": f"https://www.bigfame.co/{folder}/applications"}, {"@type": "ListItem", "position": 3, "name": d["title"], "item": base}]}, ensure_ascii=False)
    faq = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}, ensure_ascii=False)
    cards = "".join(f'<article class="location-card reveal"><h3>{html.escape(h)}</h3><p>{html.escape(b)}</p></article>' for h, b in d["record"])
    faqs = "".join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in d["faq"])
    related = " · ".join(f'<a href="{slug}">{html.escape(name)}</a>' for name, slug in d["related"])
    contact = "contact?category=display_hardware&role=buyer"
    return f'''<!DOCTYPE html><html lang="{d["lang"]}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(d["description"], quote=True)}"><title>{html.escape(d["title"])} | Big Fame</title><link rel="canonical" href="{base}">{alternates}<link rel="stylesheet" href="../css/style.css"><script type="application/ld+json">{article}</script><script type="application/ld+json">{breadcrumb}</script><script type="application/ld+json">{faq}</script></head><body><header class="header"><div class="container header-inner"><a href="./" class="logo">BIG FAME</a><nav class="nav-menu"><a href="./" class="nav-link">{d["nav"][0]}</a><a href="products" class="nav-link">{d["nav"][1]}</a><a href="applications" class="nav-link active">{d["nav"][2]}</a><a href="{contact}" class="nav-link nav-cta">{d["nav"][3]}</a></nav></div></header><main><section class="hero"><div class="container hero-content reveal"><p class="hero-kicker">{d["kicker"]}</p><h1>{html.escape(d["title"])}</h1><p class="hero-description">{html.escape(d["description"])}</p><a class="btn btn-primary" href="{contact}">{html.escape(d["cta"])}</a></div></section><section class="section section-light"><div class="container grid-2"><div class="reveal"><img class="hero-image-main" src="../images/product-cosmetic-organizer.png" alt="{html.escape(d["title"], quote=True)}" loading="eager"></div><div class="location-card reveal"><span class="section-subtitle">DOCUMENTED NEED</span><h2>{html.escape(d["need_title"])}</h2><p>{html.escape(d["need"])}</p></div></div></section><section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE EVIDENCE</span><h2 class="section-title">{html.escape(d["record_title"])}</h2></div><div class="grid-3">{cards}</div><p class="section-note reveal">{html.escape(d["boundary"])}</p></div></section><section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">FAQ</h2></div><div class="grid-2">{faqs}</div></div></section><section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{html.escape(d["cta"])}</h2><p>{related}</p><a class="btn btn-primary" href="{contact}">{html.escape(d["nav"][3])}</a></div></div></section></main><footer class="footer"><div class="container footer-bottom"><p>© Big Fame IND. CORP.</p><a href="applications">{d["nav"][2]}</a></div></footer><script src="../js/main.js"></script></body></html>'''


for folder, data in DATA.items():
    (ROOT / folder / f"{SLUG}.html").write_text(make_page(folder, data), encoding="utf-8")

application_cards = {
    "tw": '<article class="location-card reveal"><h3>PAGE 化妝品展示紀錄</h3><p>查看透明壓克力與實木桌上型展示器的文件證據。</p><a class="btn btn-secondary" href="case-page-cosmetic-organizer">查看證據紀錄</a></article>',
    "en": '<article class="location-card reveal"><h3>PAGE Cosmetic Display Record</h3><p>Review the documented evidence for a clear-acrylic and solid-wood tabletop organizer.</p><a class="btn btn-secondary" href="case-page-cosmetic-organizer">Open evidence record</a></article>',
    "jp": '<article class="location-card reveal"><h3>PAGE 化粧品展示記録</h3><p>透明アクリルと無垢材の卓上オーガナイザー資料を確認します。</p><a class="btn btn-secondary" href="case-page-cosmetic-organizer">根拠資料を見る</a></article>',
}
markers = {
    "tw": '<article class="location-card reveal"><h3>相關產品入口</h3>',
    "en": '<article class="location-card reveal"><h3>Related product routes</h3>',
    "jp": '<article class="location-card reveal"><h3>関連製品ルート</h3>',
}
for folder, marker in markers.items():
    path = ROOT / folder / "applications.html"
    text = path.read_text(encoding="utf-8")
    if "case-page-cosmetic-organizer" not in text:
        if text.count(marker) != 1:
            raise SystemExit(f"Applications marker not found exactly once: {folder}")
        text = text.replace(marker, application_cards[folder] + marker, 1)
        path.write_text(text, encoding="utf-8")

sitemap = ROOT / "sitemap.xml"
text = sitemap.read_text(encoding="utf-8")
for folder in DATA:
    line = f"  <url><loc>https://www.bigfame.co/{folder}/{SLUG}</loc></url>"
    if line not in text:
        text = text.replace("</urlset>", line + "\n</urlset>")
sitemap.write_text(text, encoding="utf-8")
print(f"Generated {SLUG} in tw/en/jp, linked applications pages, and updated sitemap.")
