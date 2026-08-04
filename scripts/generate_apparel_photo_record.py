"""Generate an evidence-controlled apparel retail photo record."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
SLUG = "case-apparel-2016"

DATA = {
    "tw": {
        "lang": "zh-Hant-TW",
        "title": "2016 服飾品牌門市照片紀錄",
        "description": "2016 服飾品牌門市照片紀錄：中島展示、壁面陳列、吊掛系統與配件展示；客戶、交付與承擔範圍仍待核准。",
        "nav": ("首頁", "產品", "應用案例", "討論服飾店型"),
        "kicker": "EVIDENCE-CONTROLLED PHOTO RECORD",
        "lead": "從可辨識的門市場景開始，確認服飾展示設備的需求方向；這不是已核准的完整客戶交付案例。",
        "record": "來源資料夾中的 3 張成組照片，檔名含「CASE-01, 2016, clothing brand」。照片可辨識服飾門市的中島展示、壁面陳列、吊掛系統、桌面配件與鞋類展示情境。",
        "cards": [
            ("可由照片辨識", "服飾商品以吊掛、壁面層架、中島桌架與獨立展示架分區陳列；照片也可見包款、鞋類與桌面配件展示。"),
            ("可支援的需求討論", "店型、動線、展示密度、吊掛高度、中島尺寸、壁面系統、配件展示與多店複製條件。"),
            ("目前不能由照片推定", "客戶名稱、Big Fame 實際承擔範圍、正式材質牌號、尺寸、數量、MOQ、交期、交付地與成果數據。"),
            ("證據狀態", "這是匿名照片紀錄；照片對外授權、專案角色與可公開文字仍需逐案確認。")
        ],
        "faq": [
            ("這是完整的服飾品牌案例嗎？", "不是。目前來源只有 3 張檔名可辨識年份與產業的照片，足以支撐匿名店型與展示情境，不足以證明客戶名稱、交付範圍或成果。"),
            ("要討論類似服飾店展示，應提供什麼？", "請提供平面或現場照片、商品尺寸、展示數量、吊掛與壁面系統、中島尺寸、材質方向、目標時程與交貨地；如有圖面，也可一併提供。")
        ],
        "cta": "討論服飾店展示條件",
        "related": (("服飾店展示設備入口", "apparel-store-fixtures"), ("模組化展示架", "modular-fixtures"), ("展示掛勾", "display-hooks"))
    },
    "en": {
        "lang": "en",
        "title": "2016 Apparel Brand Retail Photo Record",
        "description": "Evidence-controlled 2016 apparel retail photo record showing island displays, wall merchandising, hanging systems and accessory presentation; client and delivery scope remain unconfirmed.",
        "nav": ("Home", "Products", "Applications", "Discuss apparel retail"),
        "kicker": "EVIDENCE-CONTROLLED PHOTO RECORD",
        "lead": "Start with a visible apparel-store setting and define the fixture need; this is not an approved complete client delivery case.",
        "record": "The source folder contains 3 grouped photos whose filenames include “CASE-01, 2016, clothing brand”. The images visibly show apparel retail with island displays, wall merchandising, hanging systems, tabletop accessories and footwear presentation.",
        "cards": [
            ("What the photos show", "Apparel is arranged across hanging rails, wall shelving, island tables and freestanding fixtures; bags, footwear and tabletop accessories are also visible."),
            ("What this can support", "A discussion of store type, customer flow, display density, hanging height, island dimensions, wall systems, accessory presentation and repeatable store conditions."),
            ("What the photos cannot prove", "Client identity, Big Fame scope, formal material grades, dimensions, quantity, MOQ, lead time, destination or performance results."),
            ("Evidence status", "This is an anonymous photo record; photo authorization, project role and publishable wording still require case-by-case confirmation.")
        ],
        "faq": [
            ("Is this a complete apparel brand case study?", "No. The source currently contains 3 photos with a filename indicating year and industry. They support an anonymous store-type and fixture-context description, not client identity, delivery scope or outcomes."),
            ("What should we share for a similar apparel-store project?", "Share a plan or site photos, merchandise dimensions, display quantity, hanging and wall systems, island dimensions, material direction, target timing and destination. Include drawings if available.")
        ],
        "cta": "Discuss apparel-store fixture conditions",
        "related": (("Apparel fixture planning entry", "apparel-store-fixtures"), ("Modular Fixtures", "modular-fixtures"), ("Display Hooks", "display-hooks"))
    },
    "jp": {
        "lang": "ja",
        "title": "2016 アパレルブランド店舗 写真記録",
        "description": "証拠管理された2016年アパレル店舗写真記録。島什器、壁面陳列、ハンギングシステム、アクセサリー展示を確認できます。",
        "nav": ("ホーム", "製品", "用途事例", "アパレル店舗を相談"),
        "kicker": "EVIDENCE-CONTROLLED PHOTO RECORD",
        "lead": "確認できる店舗風景からアパレル什器の条件を整理します。承認済みの完全な納品事例ではありません。",
        "record": "出典フォルダーには、ファイル名に「CASE-01, 2016, clothing brand」を含む3枚の写真があります。島什器、壁面陳列、ハンギングシステム、卓上アクセサリー、靴の展示が確認できます。",
        "cards": [
            ("写真で確認できること", "衣料品をハンガーレール、壁面棚、島什器、独立什器で分けて展示しています。バッグ、靴、卓上アクセサリーも確認できます。"),
            ("相談に使える方向", "業態、動線、展示密度、ハンギング高さ、島什器寸法、壁面システム、アクセサリー展示、多店舗展開の条件。"),
            ("写真だけでは確認できないこと", "顧客名、Big Fameの担当範囲、正式な材料、寸法、数量、MOQ、納期、納品地、成果データ。"),
            ("証拠の状態", "匿名の写真記録です。写真の公開許諾、担当範囲、公開可能な文章は案件ごとに確認が必要です。")
        ],
        "faq": [
            ("完全なアパレルブランド事例ですか？", "いいえ。現時点の出典は、年と業種を示すファイル名を持つ3枚の写真です。匿名の店舗・什器の状況は示せますが、顧客名、納品範囲、成果は証明しません。"),
            ("類似のアパレル店舗を相談するには？", "平面または現場写真、商品の寸法、数量、ハンギング・壁面システム、島什器寸法、材料方向、希望時期、納品地を共有してください。図面があれば添付してください。")
        ],
        "cta": "アパレル店舗什器の条件を相談する",
        "related": (("アパレル什器の計画入口", "apparel-store-fixtures"), ("モジュール什器", "modular-fixtures"), ("ディスプレイフック", "display-hooks"))
    }
}


def make_page(folder: str, d: dict) -> str:
    base = f"https://www.bigfame.co/{folder}/{SLUG}"
    alts = "".join(f'<link rel="alternate" hreflang="{code}" href="https://www.bigfame.co/{loc}/{SLUG}">' for code, loc in (("zh-TW", "tw"), ("en", "en"), ("ja", "jp")))
    article = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": d["title"], "description": d["description"], "image": "https://www.bigfame.co/images/case-2016-apparel.jpg", "url": base}, ensure_ascii=False)
    breadcrumb = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"https://www.bigfame.co/{folder}/"}, {"@type": "ListItem", "position": 2, "name": d["nav"][2], "item": f"https://www.bigfame.co/{folder}/applications"}, {"@type": "ListItem", "position": 3, "name": d["title"], "item": base}]}, ensure_ascii=False)
    faq = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}, ensure_ascii=False)
    cards = "".join(f'<article class="location-card reveal"><h3>{html.escape(h)}</h3><p>{html.escape(b)}</p></article>' for h, b in d["cards"])
    faqs = "".join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in d["faq"])
    related = " · ".join(f'<a href="{slug}">{html.escape(name)}</a>' for name, slug in d["related"])
    contact = "contact?category=system_fixtures&role=brand"
    return f'''<!DOCTYPE html><html lang="{d["lang"]}><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(d["description"], quote=True)}"><title>{html.escape(d["title"])} | Big Fame</title><link rel="canonical" href="{base}">{alts}<link rel="stylesheet" href="../css/style.css"><script type="application/ld+json">{article}</script><script type="application/ld+json">{breadcrumb}</script><script type="application/ld+json">{faq}</script></head><body><header class="header"><div class="container header-inner"><a href="./" class="logo">BIG FAME</a><nav class="nav-menu"><a href="./" class="nav-link">{d["nav"][0]}</a><a href="products" class="nav-link">{d["nav"][1]}</a><a href="applications" class="nav-link active">{d["nav"][2]}</a><a href="{contact}" class="nav-link nav-cta">{d["nav"][3]}</a></nav></div></header><main><section class="hero"><div class="container hero-content reveal"><p class="hero-kicker">{d["kicker"]}</p><h1>{html.escape(d["title"])}</h1><p class="hero-description">{html.escape(d["lead"])}</p><a class="btn btn-primary" href="{contact}">{html.escape(d["cta"])}</a></div></section><section class="section section-light"><div class="container grid-2"><div class="reveal"><img class="hero-image-main" src="../images/case-2016-apparel.jpg" alt="{html.escape(d["title"], quote=True)}" loading="eager"></div><div class="location-card reveal"><span class="section-subtitle">SOURCE RECORD</span><h2>{html.escape(d["title"])}</h2><p>{html.escape(d["record"])}</p></div></div></section><section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">EVIDENCE BOUNDARY</span><h2 class="section-title">What this record can and cannot establish</h2></div><div class="grid-2">{cards}</div><p class="section-note reveal">This page is an anonymous, evidence-controlled photo record. It is not a named client case, delivery claim or proof of Big Fame’s contractual scope.</p></div></section><section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">FAQ</h2></div><div class="grid-2">{faqs}</div></div></section><section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{html.escape(d["cta"])}</h2><p>{related}</p><a class="btn btn-primary" href="{contact}">{html.escape(d["nav"][3])}</a></div></div></section></main><footer class="footer"><div class="container footer-bottom"><p>© Big Fame IND. CORP.</p><a href="applications">{d["nav"][2]}</a></div></footer><script src="../js/main.js"></script></body></html>'''


for folder, data in DATA.items():
    (ROOT / folder / f"{SLUG}.html").write_text(make_page(folder, data), encoding="utf-8")

for folder, link_text in {
    "tw": "查看 2016 服飾照片紀錄",
    "en": "View 2016 apparel photo record",
    "jp": "2016年アパレル写真記録を見る",
}.items():
    path = ROOT / folder / "applications.html"
    text = path.read_text(encoding="utf-8")
    if f"{SLUG}" not in text:
        marker = f'<a href="apparel-store-fixtures">'
        idx = text.find(marker, text.find('id="apparel"'))
        if idx < 0:
            raise SystemExit(f"Apparel entry link not found: {folder}")
        text = text[:idx] + f'<a href="{SLUG}">{link_text}</a> · ' + text[idx:]
        path.write_text(text, encoding="utf-8")

sitemap = ROOT / "sitemap.xml"
text = sitemap.read_text(encoding="utf-8")
for folder in DATA:
    line = f"  <url><loc>https://www.bigfame.co/{folder}/{SLUG}</loc></url>"
    if line not in text:
        text = text.replace("</urlset>", line + "\n</urlset>")
sitemap.write_text(text, encoding="utf-8")
print(f"Generated {SLUG} in tw/en/jp, linked apparel application cards, and updated sitemap.")
