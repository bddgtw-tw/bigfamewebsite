"""Generate an anonymous evidence-controlled headphone display engineering record."""

from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
SLUG = "case-headphone-display-set"
BASE = "https://www.bigfame.co"

DATA = {
    "tw": {
        "lang": "zh-Hant-TW",
        "title": "三耳機展示組工程紀錄",
        "description": "匿名三耳機展示組工程紀錄，整理展示結構、客戶圖面、包裝保護、工廠組裝與多通路版本需求。",
        "kicker": "ANONYMOUS ENGINEERING RECORD",
        "lede": "當展示設備同時要處理產品固定、影音互動、通路版本與運輸保護，Big Fame 可從需求圖面延伸到組裝與包裝文件。",
        "alt": "電子產品展示架示意圖；非正式專案現場照片",
        "note": "此頁主視覺為示意素材；歷史原始照片與公開授權仍需另行確認。",
        "home": "首頁", "products": "產品與能力", "cases": "應用案例", "contact": "開始詢問",
        "sections": [
            ("客戶問題", "三個耳機的展示與互動需求", "來源文件描述三耳機展示組，並區分不同通路版本；差異包含展示耳機、掛鉤貼紙、底部圖像與影音播放器。"),
            ("Actual scope · 設計與工程範圍", "從零件到展示外殼", "專案資料包含客戶圖面、零件編號、真空成型外殼、金屬支撐件、背景圖像、按鈕、影音播放器與掛鉤組件。正式合約範圍不公開。"),
            ("包裝與運輸", "把展示設備納入裝箱邏輯", "Packout 文件列出上／下填充件、外箱、套管與保護流程，並說明展示架、電源線、金屬支架、螺絲包與說明文件在箱內的配置。"),
            ("工廠組裝", "讓現場能依文件完成組裝", "工廠組裝說明逐步列出鉚接、圖像貼合、按鈕與影音播放器安裝、電源線固定，以及展示外殼與支撐件的組合。"),
            ("可複製的能力", "展示、包裝與通路版本同步考量", "這類專案的價值不只在外觀，而在於把產品展示、零件清單、組裝步驟與運輸保護放進同一套工程溝通中。"),
        ],
        "faq": [
            ("這是已完成交付的客戶案例嗎？", "目前以匿名工程紀錄公開。來源支持客戶圖面、展示結構、包裝與組裝文件，但公開頁不宣稱客戶名稱、訂單數量、交期或正式交付結果。"),
            ("Big Fame 可以協助哪些部分？", "可從展示物、尺寸、固定方式與通路條件出發，協助評估結構、零件、樣品、組裝說明與包裝保護需求；正式承擔範圍需依專案確認。"),
            ("要如何詢問類似展示架？", "提供展示產品、尺寸、數量、使用通路、是否需要影音互動、包裝方式與預定時程，並附上現有圖面或照片。"),
        ],
        "boundary": "公開頁不揭露客戶名稱、品牌、正式訂單數量、交期、交貨地、現行 SKU、測試標準或未核准的所有權主張。歷史圖面與文件是專案證據，不等同於現行型錄規格。",
        "cta_title": "從你的展示需求開始",
        "cta": "提供展示產品、尺寸、通路版本、數量與時程，我們再判斷應先進行圖面、樣品、結構或包裝評估。",
        "cta_text": "提交展示設備需求",
    },
    "en": {
        "lang": "en",
        "title": "Three-Headphone Display Set Engineering Record",
        "description": "An anonymous engineering record covering a three-headphone display set, customer drawings, protective packing, plant assembly and channel versions.",
        "kicker": "ANONYMOUS ENGINEERING RECORD",
        "lede": "When a display fixture must address product retention, interactive media, channel variants and transport protection together, the engineering path has to connect the drawing, assembly and packout instructions.",
        "alt": "Illustrative electronics display fixture; not a formal project-site photograph",
        "note": "The hero visual is illustrative; historical project photographs and publication permission require separate confirmation.",
        "home": "Home", "products": "Products and capabilities", "cases": "Applications", "contact": "Start an inquiry",
        "sections": [
            ("Client problem", "A three-headphone display with interactive requirements", "The source record describes a three-headphone display set with multiple channel versions. The differences include headphones, hook decals, bottom graphics and an audio/video player."),
            ("Design scope", "From component list to display housing", "The project files include customer drawings, part numbers, a vacuum-formed housing, metal support plates, graphics, push buttons, an audio/video player and hook assemblies. Formal contract scope is not public."),
            ("Packing and transport", "Putting the fixture into a packout logic", "The packout documents list top and bottom fillers, an outer shipper, a flanged tube and protection steps for the display, power cord, metal bracket, screw pack and instruction sheet."),
            ("Plant assembly", "Making the build sequence understandable", "The in-plant assembly instructions cover riveting, graphic placement, button and player installation, power-cable retention and the connection of the display housing to its support components."),
            ("Reusable capability", "Connecting display, packing and channel variants", "The value of this type of project is not only the appearance. It is the engineering communication that connects the displayed product, component list, assembly sequence and transport protection."),
        ],
        "faq": [
            ("Is this a confirmed customer delivery case?", "It is published as an anonymous engineering record. The sources support customer drawings, display structure, packing and assembly documentation; the public page does not claim the customer name, order quantity, lead time or formal delivery result."),
            ("What can Big Fame help with?", "We can evaluate the display item, dimensions, retention method and channel conditions, then determine whether structure, parts, samples, assembly instructions or packing protection should come first. Final responsibility is project-specific."),
            ("What should I include in an inquiry?", "Share the displayed product, dimensions, quantity, channel context, interactive-media needs, packing conditions and target schedule, together with any drawings or photos."),
        ],
        "boundary": "The public page withholds the client name, brand, formal order quantity, lead time, destination, current SKU, test standard and unapproved ownership claims. Historical drawings and documents are project evidence, not current catalogue specifications.",
        "cta_title": "Start with the display requirement",
        "cta": "Share the displayed product, dimensions, channel versions, quantity and schedule so we can decide whether drawings, samples, structure or packing should come first.",
        "cta_text": "Submit a display-fixture inquiry",
    },
    "jp": {
        "lang": "ja",
        "title": "3ヘッドホン展示セットのエンジニアリング記録",
        "description": "3ヘッドホン展示セットについて、顧客図面、梱包保護、工場組立、販売チャネル別仕様を整理した匿名のエンジニアリング記録です。",
        "kicker": "ANONYMOUS ENGINEERING RECORD",
        "lede": "製品の固定、映像機器、販売チャネル別仕様、輸送保護を同時に考える展示什器では、図面・組立・梱包を一つの工程としてつなぐ必要があります。",
        "alt": "電子製品展示什器のイメージ画像。正式な現場写真ではありません",
        "note": "メインビジュアルはイメージ素材です。過去案件の写真と公開許可は別途確認が必要です。",
        "home": "ホーム", "products": "製品・対応力", "cases": "事例", "contact": "問い合わせを始める",
        "sections": [
            ("顧客課題", "3台のヘッドホン展示と操作性", "資料には3台のヘッドホン展示セットと複数の販売チャネル仕様が記録されています。ヘッドホン、フック用グラフィック、底部グラフィック、映像プレーヤーなどが仕様差分です。"),
            ("Actual scope · 設計範囲", "部品表から展示ハウジングまで", "顧客図面、部品番号、真空成形ハウジング、金属支持板、グラフィック、ボタン、映像プレーヤー、フック部品が記録されています。正式な契約範囲は公開していません。"),
            ("梱包・輸送", "展示什器を梱包設計に組み込む", "上下面の緩衝材、外箱、筒状部材、展示本体、電源コード、金属ブラケット、ねじ袋、説明書の梱包手順が整理されています。"),
            ("工場組立", "現場で再現できる組立手順", "リベット、グラフィック、ボタン、映像プレーヤー、電源コード、展示ハウジングと支持部品の組立手順が記録されています。"),
            ("応用できる力", "展示・梱包・チャネル仕様をつなぐ", "外観だけでなく、展示製品、部品表、組立手順、輸送保護を一つのエンジニアリングコミュニケーションにまとめることがこの種の案件の要点です。"),
        ],
        "faq": [
            ("納品済みの顧客事例ですか？", "匿名のエンジニアリング記録として公開しています。顧客図面、展示構造、梱包、組立資料は確認できますが、顧客名、数量、納期、正式な納品結果は公開していません。"),
            ("Big Fameは何を支援できますか？", "展示製品、寸法、固定方法、販売チャネルの条件から、構造、部品、サンプル、組立説明、梱包保護のどこから検討するかを整理できます。正式な担当範囲は案件ごとに確認します。"),
            ("問い合わせには何が必要ですか？", "展示製品、寸法、数量、販売チャネル、映像機器の有無、梱包条件、希望時期、図面または写真をご提供ください。"),
        ],
        "boundary": "顧客名、ブランド、正式な発注数量、納期、納品先、現行SKU、試験規格、未承認の権利主張は公開していません。過去の図面と資料は案件証拠であり、現行カタログ仕様ではありません。",
        "cta_title": "展示要件から始める",
        "cta": "展示製品、寸法、チャネル仕様、数量、希望時期をお知らせください。図面、サンプル、構造、梱包のどこから始めるかを整理します。",
        "cta_text": "展示什器の相談を送る",
    },
}


def link(path: str, clean: bool) -> str:
    return f"../{path}" if clean else path


def render(locale: str, clean: bool) -> str:
    d = DATA[locale]
    url = f"{BASE}/{locale}/{SLUG}"
    prefix = "../" if clean else ""
    contact = link("contact?role=buyer&category=system_fixtures&requested_files=dimension_drawing", clean)
    sections = "".join(f'<article class="location-card reveal"><span class="section-subtitle">{html.escape(k)}</span><h3>{html.escape(t)}</h3><p>{html.escape(b)}</p></article>' for k, t, b in d["sections"])
    faq = "".join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in d["faq"])
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}
    article_schema = {"@context": "https://schema.org", "@type": "Article", "name": d["title"], "description": d["description"], "url": url, "author": {"@type": "Organization", "name": "Big Fame IND. CORP."}, "about": "Retail display fixture engineering"}
    crumb_schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"{BASE}/{locale}/"}, {"@type": "ListItem", "position": 2, "name": d["cases"], "item": f"{BASE}/{locale}/applications"}, {"@type": "ListItem", "position": 3, "name": d["title"], "item": url}]}
    alternates = "".join(f'<link rel="alternate" hreflang="{h}" href="{BASE}/{l}/{SLUG}">' for h, l in [("zh-TW", "tw"), ("en", "en"), ("ja", "jp")])
    related = "<a href=\"{}\">{}</a> · <a href=\"{}\">{}</a> · <a href=\"{}\">{}</a>".format(link("display-hooks", clean), "展示掛勾" if locale == "tw" else "Display hooks" if locale == "en" else "展示フック", link("modular-fixtures", clean), "模組化展示架" if locale == "tw" else "Modular fixtures" if locale == "en" else "モジュール什器", link("applications", clean), d["cases"])
    return f'''<!DOCTYPE html>
<html lang="{d["lang"]}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(d["description"], quote=True)}"><meta property="og:type" content="article"><meta property="og:title" content="{html.escape(d["title"], quote=True)} | Big Fame"><meta property="og:description" content="{html.escape(d["description"], quote=True)}"><meta property="og:url" content="{url}"><meta property="og:site_name" content="Big Fame IND. CORP."><title>{html.escape(d["title"])} | Big Fame</title><link rel="canonical" href="{url}">{alternates}<link rel="stylesheet" href="{prefix}../css/style.css"><script type="application/ld+json">{json.dumps(article_schema, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(crumb_schema, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script></head>
<body><header class="header"><div class="container header-inner"><a href="{link('', clean)}" class="logo">BIG FAME</a><nav class="nav-menu"><a href="{link('', clean)}" class="nav-link">{d["home"]}</a><a href="{link('products', clean)}" class="nav-link">{d["products"]}</a><a href="{link('applications', clean)}" class="nav-link active">{d["cases"]}</a><a href="{contact}" class="nav-link nav-cta">{d["contact"]}</a></nav></div></header>
<main><section class="case-hero"><div class="container case-hero-grid"><div class="reveal"><div class="case-hero-kicker">{d["kicker"]}</div><h1>{html.escape(d["title"])}</h1><p class="case-hero-lede">{html.escape(d["lede"])}</p><div class="case-hero-actions"><a class="btn btn-primary" href="{contact}">{d["cta_text"]}</a><a class="btn btn-secondary" href="{link('applications', clean)}">{d["cases"]}</a></div></div><div class="case-hero-visual reveal"><img class="hero-image-main" src="{prefix}../images/case_h_electronics.jpg" alt="{html.escape(d["alt"], quote=True)}"><div class="case-hero-note"><strong>SOURCE RECORD</strong><span>{html.escape(d["note"])}</span></div></div></div></section>
<section class="section section-light"><div class="container"><div class="section-header reveal"><span class="section-subtitle">ENGINEERING EVIDENCE</span><h2 class="section-title">{html.escape(d["title"])}</h2></div><div class="grid-2">{sections}</div><p class="section-note reveal">{html.escape(d["boundary"])}</p></div></section>
<section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-header reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">FAQ</h2></div><div class="grid-3">{faq}</div></div></section>
<section class="section section-light"><div class="container"><div class="section-header reveal"><span class="section-subtitle">RELATED CAPABILITIES</span><h2 class="section-title">{d["products"]}</h2></div><p class="reveal">{related}</p></div></section>
<section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{html.escape(d["cta_title"])}</h2><p>{html.escape(d["cta"])}</p><a class="btn btn-primary" href="{contact}">{d["cta_text"]}</a></div></div></section></main>
<footer class="footer"><div class="container footer-bottom"><p>© Big Fame IND. CORP.</p><a href="{link('applications', clean)}">{d["cases"]}</a></div></footer><script src="{prefix}../js/main.js"></script></body></html>'''


for locale in DATA:
    (ROOT / locale / f"{SLUG}.html").write_text(render(locale, False), encoding="utf-8")
    folder = ROOT / locale / SLUG
    folder.mkdir(exist_ok=True)
    (folder / "index.html").write_text(render(locale, True), encoding="utf-8")
