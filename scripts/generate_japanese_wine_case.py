"""Generate an evidence-controlled anonymous hospitality case in three locales."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
IMAGE = "https://www.bigfame.co/images/case-japanese-wine-bar.jpg"

DATA = {
    "tw": {
        "lang": "zh-Hant-TW", "title": "台北匿名酒吧酒類展示櫃專案紀錄",
        "description": "匿名台北酒吧的壁面酒類展示櫃與展示照明設計紀錄，整理酒品可視性、玻璃層板與柔光展示需求。",
        "kicker": "ANONYMOUS HOSPITALITY PROJECT / WINE BAR", "nav": ("首頁", "產品與能力", "應用案例", "提交需求"),
        "need_title": "讓酒品成為空間中的視覺主角", "need": "來源文件描述一間位於台北市中心的現代酒吧；在夜生活競爭激烈的環境中，業主希望讓酒類產品獲得清楚的展示視線，並以照明建立舒適的氛圍。",
        "record_title": "來源文件可確認的展示方向", "record": [("展示櫃", "大型壁面酒類展示櫃，搭配多層透明玻璃層板。"), ("展示照明", "文件記錄與 KANEKA OLED light panel 的合作方向，描述薄型、低操作溫度與柔和陰影的展示特性。"), ("材質與配置", "透明強化玻璃讓光線穿過層板，照亮酒瓶與包裝；其他板材、五金與表面處理未在公開頁面推定。"), ("Big Fame 公開範圍", "本頁使用匿名專案文件與現場照片說明展示櫃及照明需求；正式合約分工、數量、交期與授權狀態未公開。"), ("店型／地點", "現代酒吧；來源文件指向台北市中心的店面，但最終交付地未另行記錄。"), ("公開程度", "匿名專案紀錄；未公開客戶名稱、報價、數量、交期或成果數據。")],
        "faq": [("這個案例可以證明什麼？", "來源文件可確認壁面酒類展示櫃、透明玻璃層板與展示照明的設計方向；不從照片推定正式尺寸、數量或合約分工。"), ("如果我要做酒類或旅宿展示，應提供什麼？", "請提供店型、展示物尺寸、櫃體寬高深、玻璃與照明方向、數量、目標交期、交貨地與平面／立面圖。")],
        "cta": "討論酒類展示與店面圖面",
    },
    "en": {
        "lang": "en", "title": "Anonymous Taipei Wine Bar Display Cabinet Project",
        "description": "An anonymous Taipei wine-bar record covering a large wall wine display cabinet, glass shelves and soft display lighting.",
        "kicker": "ANONYMOUS HOSPITALITY PROJECT / WINE BAR", "nav": ("Home", "Products", "Applications", "Submit inquiry"),
        "need_title": "Make the wine collection the visual focus", "need": "The source document describes a modern bar in central Taipei, where competition for nightlife attention was strong. The owner wanted the alcoholic products to have a clear visual presence, making lighting a central design issue.",
        "record_title": "What the source record confirms", "record": [("Display cabinet", "A large wall-side wine display cabinet with multiple transparent glass shelves."), ("Display lighting", "The document records collaboration around a KANEKA OLED light panel and describes thin form, low operating temperature and soft shadow characteristics for display."), ("Materials and arrangement", "Transparent tempered glass lets light pass through each shelf to illuminate bottles and packaging; other panels, hardware and finishes are not inferred here."), ("Public Big Fame scope", "This page uses an anonymous project document and site photographs to explain the cabinet and lighting requirements; formal contract division, quantity, schedule and authorization are not published."), ("Store type / location", "Modern wine bar; the source points to a central Taipei store, but does not separately record a final delivery destination."), ("Publication level", "Anonymous project record; client name, quotation, quantity, schedule and performance data are not published.")],
        "faq": [("What does this case prove?", "The source confirms a wall wine display cabinet, transparent glass shelving and a display-lighting direction. Do not infer formal dimensions, quantity or contract division from the photographs."), ("What should I share for a wine or hospitality display project?", "Share the store type, display-product dimensions, cabinet width/height/depth, glass and lighting direction, quantity, target date, delivery location and plan/elevation drawings.")],
        "cta": "Discuss a wine display and store drawing",
    },
    "jp": {
        "lang": "ja", "title": "台北匿名ワインバー展示キャビネット事例",
        "description": "台北の匿名ワインバーについて、壁面の酒類展示キャビネット、ガラス棚、柔らかな展示照明の方向を整理した記録です。",
        "kicker": "ANONYMOUS HOSPITALITY PROJECT / WINE BAR", "nav": ("ホーム", "製品", "用途事例", "お問い合わせ"),
        "need_title": "酒類を空間の視覚的な主役にする", "need": "元資料は台北中心部のモダンバーを記録しています。夜の商業環境で酒類を見せることが課題となり、照明を重要な設計条件として整理しています。",
        "record_title": "資料で確認できる展示方向", "record": [("展示キャビネット", "複数の透明ガラス棚を備えた大型の壁面酒類展示キャビネット。"), ("展示照明", "KANEKA OLED light panel との協業方向を記録し、薄型、低い動作温度、柔らかな影の特性を説明しています。"), ("材質と配置", "透明強化ガラスを通して棚ごとに光を入れ、ボトルとパッケージを照らす方向です。その他の板材、金具、仕上げは推定しません。"), ("Big Fame の公開範囲", "匿名のプロジェクト文書と現場写真から展示キャビネットと照明要件を説明します。正式な契約範囲、数量、納期、公開許諾は記録されていません。"), ("業態・場所", "モダンバー。元資料は台北中心部の店舗を示しますが、最終納品先は別途記録されていません。"), ("公開レベル", "匿名プロジェクト記録。顧客名、見積、数量、納期、成果数値は公開していません。")],
        "faq": [("この事例で確認できることは何ですか？", "壁面酒類展示キャビネット、透明ガラス棚、展示照明の方向を確認できます。写真から正式寸法、数量、契約範囲を推定しません。"), ("酒類・宿泊施設向け展示の相談には何が必要ですか？", "業態、展示物の寸法、キャビネットの幅・高さ・奥行、ガラスと照明の方向、数量、希望納期、納品先、平面図・立面図をご用意ください。")],
        "cta": "酒類展示と図面を相談する",
    },
}

def page(folder, d):
    base = f"https://www.bigfame.co/{folder}/case-japanese-wine-bar"
    alt = ''.join(f'<link rel="alternate" hreflang="{h}" href="https://www.bigfame.co/{f}/case-japanese-wine-bar">' for h, f in (("zh-TW", "tw"), ("en", "en"), ("ja", "jp")))
    schema = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": d["title"], "description": d["description"], "image": IMAGE, "url": base}, ensure_ascii=False)
    crumb = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"https://www.bigfame.co/{folder}/"}, {"@type": "ListItem", "position": 2, "name": d["nav"][2], "item": f"https://www.bigfame.co/{folder}/applications"}, {"@type": "ListItem", "position": 3, "name": d["title"], "item": base}]}, ensure_ascii=False)
    faq = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}, ensure_ascii=False)
    cards = ''.join(f'<article class="location-card reveal"><h3>{html.escape(h)}</h3><p>{html.escape(b)}</p></article>' for h, b in d["record"])
    faqs = ''.join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in d["faq"])
    return f'''<!DOCTYPE html><html lang="{d["lang"]}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(d["description"], quote=True)}"><title>{html.escape(d["title"])} | Big Fame</title><link rel="canonical" href="{base}">{alt}<link rel="stylesheet" href="../css/style.css"><script type="application/ld+json">{schema}</script><script type="application/ld+json">{crumb}</script><script type="application/ld+json">{faq}</script></head><body><header class="header"><div class="container header-inner"><a href="./" class="logo">BIG FAME</a><nav class="nav-menu"><a href="./" class="nav-link">{d["nav"][0]}</a><a href="products" class="nav-link">{d["nav"][1]}</a><a href="applications" class="nav-link active">{d["nav"][2]}</a><a href="contact?category=system_fixtures&role=designer" class="nav-link nav-cta">{d["nav"][3]}</a></nav></div></header><main><section class="hero"><div class="container hero-content reveal"><p class="hero-kicker">{d["kicker"]}</p><h1>{html.escape(d["title"])}</h1><p class="hero-description">{html.escape(d["description"])}</p><a class="btn btn-primary" href="contact?category=system_fixtures&role=designer">{html.escape(d["cta"])}</a></div></section><section class="section section-light"><div class="container grid-2"><div class="reveal"><img class="hero-image-main" src="../images/case-japanese-wine-bar.jpg" alt="{html.escape(d["title"], quote=True)}" loading="eager"></div><div class="location-card reveal"><span class="section-subtitle">THE DESIGN NEED</span><h2>{html.escape(d["need_title"])}</h2><p>{html.escape(d["need"])}</p></div></div></section><section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">PROJECT EVIDENCE</span><h2 class="section-title">{html.escape(d["record_title"])}</h2></div><div class="grid-3">{cards}</div><p class="section-note reveal">{html.escape(d["description"])} {"本頁為匿名專案資料整理；正式規格、數量、交期、合約分工與公開授權需逐案確認。" if folder == "tw" else "This page is an anonymous project record; formal specifications, quantity, schedule, contract division and publication authorization require case-by-case confirmation." if folder == "en" else "本ページは匿名プロジェクト記録です。正式仕様、数量、納期、契約範囲、公開許諾は案件ごとに確認します。"}</p></div></section><section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">FAQ</h2></div><div class="grid-2">{faqs}</div></div></section><section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{html.escape(d["cta"])}</h2><p><a href="custom-metal-parts">{"相關客製金屬零件入口" if folder == "tw" else "Related custom metal parts entry" if folder == "en" else "関連するカスタム金属部品"}</a> · <a href="modular-fixtures">{"模組化展示架" if folder == "tw" else "Modular fixtures" if folder == "en" else "モジュール什器"}</a></p><a class="btn btn-primary" href="contact?category=system_fixtures&role=designer">{html.escape(d["nav"][3])}</a></div></div></section></main><footer class="footer"><div class="container footer-bottom"><p>© Big Fame IND. CORP.</p><a href="applications">{d["nav"][2]}</a></div></footer><script src="../js/main.js"></script></body></html>'''

for folder, data in DATA.items():
    (ROOT / folder / "case-japanese-wine-bar.html").write_text(page(folder, data), encoding="utf-8")
print("Generated three localized anonymous wine-bar case pages.")
