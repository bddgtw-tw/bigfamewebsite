"""Generate an anonymous evidence-controlled automotive parts display rack record."""

from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
SLUG = "case-automotive-parts-rack"
BASE = "https://www.bigfame.co"

PAGES = {
    "tw": {
        "lang": "zh-Hant-TW",
        "label": "繁中",
        "title": "汽車零件展示架工程紀錄",
        "description": "匿名汽車零件展示架工程紀錄：從洞洞板與旋轉架相容性、POP 掛牌、結構補強，到表面保護、組裝與包裝改善。",
        "kicker": "ANONYMOUS ENGINEERING RECORD",
        "lede": "當展示設備同時面對相容性、結構、運輸保護與組裝問題，Big Fame 以需求回覆、圖面迭代與改善紀錄，把問題整理成可討論的工程方案。",
        "breadcrumb_products": "產品與能力",
        "breadcrumb_cases": "應用案例",
        "home": "首頁",
        "products": "產品與能力",
        "cases": "應用案例",
        "contact": "開始詢問",
        "source_label": "SOURCE RECORD",
        "visual_alt": "汽車零件展示架的示意圖；不是本案正式現場照片",
        "visual_note": "頁面主視覺為展示設備示意素材；歷史來源照片與授權狀態需另行確認。",
        "sections": [
            ("客戶問題", "相容性與使用方式", "來源往返信件討論 4-side peg board rack 的 head support 是否相容，以及如何讓 POP／Sign Holder 固定在展示架上。Big Fame 回覆以磁力固定與替代材料降低模具、MOQ 與成本風險。"),
            ("設計範圍", "旋轉架、洞洞板與 POP 配件", "專案資料包含 auto clip rotating rack、4-way peg board rack、hook shelf、POP／Sign Holder 與多版本尺寸／細節圖面。正式合約範圍未公開。"),
            ("Big Fame 實際承擔範圍", "從需求回覆到工程文件", "來源文件可支持 Big Fame 進行需求回覆、設計方案、圖面迭代、缺陷分析、結構／表面保護改善與組裝文件整理；正式合約範圍仍依專案確認。"),
            ("改善紀錄", "把缺陷轉成結構與包裝對策", "缺陷報告記錄粉體塗層剝落、運輸／試組裝損傷與底座強度問題；改善方向包含三角金屬補強、腳部保護、完成後塑膠袋與出口紙箱保護。"),
            ("組裝與交付準備", "讓現場可以理解如何組裝", "組裝說明列出 base、connecting tubes、L posts、frame boxes、hook shelves、洞洞板與腳輪，並整理旋轉架與四向洞洞板架的組裝步驟。"),
        ],
        "faq": [
            ("這是已完成交付的客戶案例嗎？", "目前公開為匿名工程／交付紀錄；來源能支持需求、設計、改善與組裝文件，但客戶授權、正式數量、交期與交貨地不公開。"),
            ("Big Fame 在專案中做了什麼？", "來源文件可支持 Big Fame 進行需求回覆、設計方案、圖面迭代、缺陷分析、結構／表面保護與組裝文件整理；正式合約分工仍依專案確認。"),
            ("可以做類似的展示架或洞洞板架嗎？", "可從產品用途、尺寸、安裝方式、展示物重量、數量與運輸條件開始評估；請提供照片、圖面或概念說明。"),
        ],
        "boundary_title": "公開證據邊界",
        "boundary": "本頁不公開客戶名稱、Logo、正式訂單數量、交期、交貨地、承重、測試標準或目前 SKU 承諾。歷史圖面與照片是專案來源，不等同於目前型錄。",
        "cta_title": "從您的展示架問題開始",
        "cta": "提供尺寸、展示物、安裝系統、數量與目標時程，讓我們先判斷需要圖面、樣品或規格資料。",
        "cta_text": "提交展示架需求",
    },
    "en": {
        "lang": "en",
        "label": "EN",
        "title": "Automotive Parts Display Rack Engineering Record",
        "description": "An anonymous engineering record covering pegboard and rotating-rack compatibility, POP holders, structural reinforcement, surface protection, assembly and packaging improvements.",
        "kicker": "ANONYMOUS ENGINEERING RECORD",
        "lede": "When a display fixture must solve compatibility, structure, transport protection and assembly issues together, Big Fame turns the questions into an engineering path through replies, drawing iterations and improvement records.",
        "breadcrumb_products": "Products and capabilities",
        "breadcrumb_cases": "Applications",
        "home": "Home",
        "products": "Products",
        "cases": "Applications",
        "contact": "Start an inquiry",
        "source_label": "SOURCE RECORD",
        "visual_alt": "Illustrative automotive parts display rack; not a formal project-site photograph",
        "visual_note": "The hero visual is an illustrative display-fixture asset; historical source photographs and publication permission require separate confirmation.",
        "sections": [
            ("Client problem", "Compatibility and use method", "The source correspondence discusses whether a head support would fit a 4-side peg board rack and how to hold a POP／Sign Holder on the rack. Big Fame proposed a magnetic holder and alternative materials to reduce tooling, MOQ and cost risk."),
            ("Design scope", "Rotating rack, pegboard and POP hardware", "The project files include an auto clip rotating rack, 4-way peg board rack, hook shelves, POP／Sign Holder and multiple drawing iterations. The formal contract scope is not public."),
            ("Big Fame's actual scope", "From requirement replies to engineering documents", "The sources support requirement replies, design proposals, drawing iterations, defect analysis, structural／surface-protection improvements and assembly-document preparation. Formal contract responsibility remains project-specific."),
            ("Improvement record", "Turning defects into structural and packing actions", "The defect report records powder-coating damage, transport／trial-assembly damage and base-strength questions. The documented responses include triangular metal reinforcement, leg protection, plastic-bag protection and export-carton protection."),
            ("Assembly and delivery preparation", "Making the fixture understandable on site", "Assembly guides list the base, connecting tubes, L posts, frame boxes, hook shelves, pegboard panels and casters, then show how to assemble the rotating and four-way pegboard racks."),
        ],
        "faq": [
            ("Is this a completed customer delivery case?", "It is currently published as an anonymous engineering and delivery record. The sources support the questions, design, improvement and assembly work, while authorization, quantity, lead time and destination remain undisclosed."),
            ("What did Big Fame handle?", "The source documents support requirement replies, design proposals, drawing iterations, defect analysis, structural／surface-protection improvements and assembly-document preparation. Formal contract responsibility remains project-specific."),
            ("Can you develop a similar rack or pegboard fixture?", "Start with the display item, dimensions, mounting system, load context, quantity and transport conditions. Photos, drawings or a concept brief are useful starting points."),
        ],
        "boundary_title": "Evidence boundary",
        "boundary": "This page does not publish the client name, logo, formal order quantity, lead time, destination, load rating, test standard or current SKU commitment. Historical drawings and photographs are project sources, not a current catalogue.",
        "cta_title": "Start with your fixture problem",
        "cta": "Share dimensions, display items, mounting system, quantity and target schedule so we can determine whether drawings, samples or specification data should come first.",
        "cta_text": "Submit a fixture inquiry",
    },
    "jp": {
        "lang": "ja",
        "label": "JP",
        "title": "自動車部品ディスプレイラック｜エンジニアリング記録",
        "description": "有孔ボードと回転ラックの互換性、POPホルダー、構造補強、表面保護、組立てと梱包改善を整理した匿名のエンジニアリング記録です。",
        "kicker": "ANONYMOUS ENGINEERING RECORD",
        "lede": "互換性、構造、輸送保護、組立てを同時に検討する展示什器について、Big Fameは問い合わせ、図面の反復、改善記録を通じて検討経路を整理します。",
        "breadcrumb_products": "製品と能力",
        "breadcrumb_cases": "導入分野",
        "home": "ホーム",
        "products": "製品",
        "cases": "導入分野",
        "contact": "お問い合わせ",
        "source_label": "SOURCE RECORD",
        "visual_alt": "自動車部品ディスプレイラックのイメージ。正式な現場写真ではありません",
        "visual_note": "メインビジュアルは展示什器のイメージ素材です。歴史資料の写真と公開許諾は別途確認が必要です。",
        "sections": [
            ("顧客の課題", "互換性と使用方法", "資料の往復メールでは、4面有孔ボードラックにヘッドサポートを組み合わせられるか、またPOP／サインホルダーを固定する方法が検討されています。Big Fameは磁力を使うホルダーと代替素材を提案しました。"),
            ("設計範囲", "回転ラック、有孔ボード、POP金具", "資料にはオートクリップ回転ラック、4面有孔ボードラック、フックシェルフ、POP／サインホルダーと複数の図面改訂が含まれます。正式な契約範囲は公開していません。"),
            ("Big Fameの対応範囲", "要件への回答からエンジニアリング資料まで", "資料からは、要件への回答、設計提案、図面改訂、不具合分析、構造・表面保護の改善、組立て資料の準備を確認できます。正式な契約範囲は案件ごとに確認します。"),
            ("改善記録", "不具合を構造・梱包対策へ", "不具合資料には粉体塗装の剥離、輸送・試組立て時の損傷、ベース強度の課題が記録されています。三角補強、脚部保護、ビニール袋、輸出用カートンの対策が整理されています。"),
            ("組立てと納品準備", "現場で組み立てやすい資料", "組立て資料ではベース、接続パイプ、Lポスト、フレームボックス、フックシェルフ、有孔ボード、キャスターを一覧化し、回転ラックと4面ラックの手順を整理しています。"),
        ],
        "faq": [
            ("完成納品済みの顧客事例ですか？", "現在は匿名のエンジニアリング／納品準備記録として公開しています。課題、設計、改善、組立て資料は確認できますが、公開許諾、数量、納期、納品先は非公開です。"),
            ("Big Fameの担当範囲は？", "資料からは、要件への回答、設計提案、図面改訂、不具合分析、構造・表面保護の改善、組立て資料の準備を確認できます。正式な契約範囲は案件ごとに確認します。"),
            ("類似のラックや有孔ボード什器を相談できますか？", "展示物、寸法、取付システム、数量、輸送条件から確認します。写真、図面、コンセプト資料をご用意ください。"),
        ],
        "boundary_title": "公開情報の範囲",
        "boundary": "顧客名、ロゴ、正式な数量、納期、納品先、耐荷重、試験基準、現在のSKU供給を掲載していません。歴史図面と写真は案件資料であり、現行カタログとは異なります。",
        "cta_title": "展示什器の課題から相談する",
        "cta": "寸法、展示物、取付システム、数量、希望時期をお知らせください。図面、サンプル、仕様資料のどこから始めるか確認します。",
        "cta_text": "展示什器を相談する",
    },
}


def href(path: str, clean: bool) -> str:
    return f"../{path}" if clean else path


def render(locale: str, clean: bool) -> str:
    cfg = PAGES[locale]
    url = f"{BASE}/{locale}/{SLUG}"
    prefix = "../" if clean else ""
    contact = href("contact?role=designer&category=system_fixtures&requested_files=dimension_drawing", clean)
    product_links = " · ".join(
        f'<a href="{href(path, clean)}">{label}</a>'
        for path, label in [
            ("display-hooks", "展示掛勾" if locale == "tw" else "Display hooks" if locale == "en" else "ディスプレイフック"),
            ("slatwall-pegboard-accessories", "槽板／洞洞板配件" if locale == "tw" else "Slatwall / pegboard accessories" if locale == "en" else "スラットウォール／有孔ボード金具"),
            ("modular-fixtures", "模組化展示架" if locale == "tw" else "Modular fixtures" if locale == "en" else "モジュール什器"),
            ("custom-metal-parts", "客製金屬零件" if locale == "tw" else "Custom metal parts" if locale == "en" else "カスタム金属部品"),
        ]
    )
    schema_breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"{BASE}/{locale}/"},
            {"@type": "ListItem", "position": 2, "name": cfg["breadcrumb_cases"], "item": f"{BASE}/{locale}/applications"},
            {"@type": "ListItem", "position": 3, "name": cfg["title"], "item": url},
        ],
    }
    schema_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in cfg["faq"]]}
    schema_page = {"@context": "https://schema.org", "@type": "Article", "name": cfg["title"], "description": cfg["description"], "url": url, "author": {"@type": "Organization", "name": "Big Fame IND. CORP."}, "about": "Retail display fixture engineering"}
    alternates = "".join(f'<link rel="alternate" hreflang="{h}" href="{BASE}/{l}/{SLUG}">' for h, l in [("zh-TW", "tw"), ("en", "en"), ("ja", "jp")])
    section_html = "".join(f'<article class="location-card reveal"><span class="section-subtitle">{html.escape(k)}</span><h3>{html.escape(t)}</h3><p>{html.escape(body)}</p></article>' for k, t, body in cfg["sections"])
    faq_html = "".join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in cfg["faq"])
    return f'''<!DOCTYPE html>
<html lang="{cfg["lang"]}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(cfg["description"], quote=True)}"><meta property="og:type" content="article"><meta property="og:title" content="{html.escape(cfg["title"], quote=True)} | Big Fame"><meta property="og:description" content="{html.escape(cfg["description"], quote=True)}"><meta property="og:url" content="{url}"><meta property="og:site_name" content="Big Fame IND. CORP."><title>{html.escape(cfg["title"])} | Big Fame</title><link rel="canonical" href="{url}">{alternates}<link rel="stylesheet" href="{prefix}../css/style.css"><script type="application/ld+json">{json.dumps(schema_page, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(schema_breadcrumb, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(schema_faq, ensure_ascii=False)}</script></head>
<body><header class="header"><div class="container header-inner"><a href="{href('', clean)}" class="logo">BIG FAME</a><nav class="nav-menu"><a href="{href('', clean)}" class="nav-link">{cfg["home"]}</a><a href="{href('products', clean)}" class="nav-link">{cfg["products"]}</a><a href="{href('applications', clean)}" class="nav-link active">{cfg["cases"]}</a><a href="{contact}" class="nav-link nav-cta">{cfg["contact"]}</a></nav></div></header>
<main><section class="case-hero"><div class="container case-hero-grid"><div class="reveal"><div class="case-hero-kicker">{cfg["kicker"]}</div><h1>{html.escape(cfg["title"])}</h1><p class="case-hero-lede">{html.escape(cfg["lede"])}</p><div class="case-hero-actions"><a class="btn btn-primary" href="{contact}">{cfg["cta_text"]}</a><a class="btn btn-secondary" href="{href('applications', clean)}">{cfg["cases"]}</a></div></div><div class="case-hero-visual reveal"><img class="hero-image-main" src="{prefix}../images/case_h_electronics.jpg" alt="{html.escape(cfg["visual_alt"], quote=True)}"><div class="case-hero-note"><strong>{cfg["source_label"]}</strong><span>{html.escape(cfg["visual_note"])}</span></div></div></div></section>
<section class="section section-light"><div class="container"><div class="section-header reveal"><span class="section-subtitle">ENGINEERING EVIDENCE</span><h2 class="section-title">{html.escape(cfg["title"])}</h2></div><div class="grid-2">{section_html}</div><p class="section-note reveal">{html.escape(cfg["boundary"])}</p></div></section>
<section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-header reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">FAQ</h2></div><div class="grid-3">{faq_html}</div></div></section>
<section class="section section-light"><div class="container"><div class="section-header reveal"><span class="section-subtitle">RELATED CAPABILITIES</span><h2 class="section-title">{cfg["breadcrumb_products"]}</h2></div><p class="reveal">{product_links}</p></div></section>
<section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{html.escape(cfg["cta_title"])}</h2><p>{html.escape(cfg["cta"])}</p><a class="btn btn-primary" href="{contact}">{cfg["cta_text"]}</a></div></div></section></main>
<footer class="footer"><div class="container footer-bottom"><p>© Big Fame IND. CORP.</p><a href="{href('applications', clean)}">{cfg["cases"]}</a></div></footer><script src="{prefix}../js/main.js"></script></body></html>'''


for locale in PAGES:
    (ROOT / locale / f"{SLUG}.html").write_text(render(locale, False), encoding="utf-8")
    folder = ROOT / locale / SLUG
    folder.mkdir(exist_ok=True)
    (folder / "index.html").write_text(render(locale, True), encoding="utf-8")
