"""Generate a trilingual technical-resource and CAD-request entry."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
SLUG = "technical-resources"

DATA = {
    "tw": {
        "lang": "zh-Hant-TW", "title": "展示設備規格與 CAD 資料索取", "description": "展示設備規格、尺寸圖與 CAD 資料索取入口：先查看已核對的代表性證據，再依 SKU、圖面與樣品確認正式資料。", "nav": ("首頁", "產品", "應用案例", "索取資料"), "kicker": "TECHNICAL RESOURCE ENTRY", "hero": "讓設計意圖進入可確認的規格流程", "intro": "先從公開可核對的尺寸圖、產品證據與案例紀錄開始；若需要 PDF、CAD、DWG、DXF 或 STEP，請附上產品、系統、數量與專案條件，讓資料依 SKU 與版本提供。", "cards": [("可直接查看", "展示掛勾代表性尺寸圖與 PAGE 化妝品展示資料紀錄可直接查看，內容標示適用的版本與證據邊界。"), ("可索取的格式", "可依專案條件討論 PDF、CAD、DWG、DXF、STEP、尺寸圖或材質／表面處理資料；是否提供與版本以正式文件確認。"), ("需要先確認", "背板或安裝系統、商品尺寸、預估數量、目標日期、交貨地、材質與表面處理方向，會影響資料與報價確認。"), ("不公開通用資料包", "不同 SKU、尺寸、材質與版本不能用一份通用檔案代替；未核准的 CAD、承重、MOQ、交期與測試資料不在本頁推定。")], "faq": [("可以直接取得 CAD 或 STEP 嗎？", "請先提供產品或系統、照片／圖面、數量、目標日期與交貨地；正式 CAD、PDF、DWG、DXF 或 STEP 依 SKU、版本與專案條件確認。"), ("MOQ 與交期是否有統一資料？", "目前不公開所有產品共用的 MOQ 或交期。已核對的個別文件可提供代表性方向，正式條件仍需依型號、數量、版本與排程確認。"), ("設計師要先準備什麼？", "準備現有圖面或照片、安裝系統與尺寸、展示商品、數量、材質／表面方向、目標時程及交貨地，即可開始規格討論。" )], "cta": "索取 CAD 與規格資料", "download": "查看展示掛勾代表性尺寸圖", "download_href": "images/product-display-hooks-dim.jpg", "download_note": "代表性 DBTHK001-SLW 尺寸圖；不代表所有展示掛勾 SKU。", "related": (("展示掛勾", "display-hooks"), ("PAGE 化妝品展示資料紀錄", "case-page-cosmetic-organizer"))
    },
    "en": {
        "lang": "en", "title": "Technical Resources & CAD Request", "description": "Technical resources, dimension evidence and CAD request entry for retail display equipment. Start with verified evidence, then confirm formal files by SKU, drawing and sample.", "nav": ("Home", "Products", "Applications", "Request files"), "kicker": "TECHNICAL RESOURCE ENTRY", "hero": "Move design intent into confirmable specifications", "intro": "Start with publicly verifiable dimension evidence, product records and case records. If you need PDF, CAD, DWG, DXF or STEP files, share the product, system, quantity and project conditions so the correct SKU and revision can be reviewed.", "cards": [("Available to view", "A representative display-hook dimension drawing and the PAGE cosmetic display record are available to view, with their version and evidence boundaries stated."), ("Formats to request", "Depending on the project, we can discuss PDF, CAD, DWG, DXF, STEP, dimension drawings or material and finish information. Availability and revision are confirmed against formal documents."), ("Confirm these first", "Backing or mounting system, merchandise dimensions, estimated quantity, target date, destination, material and finish direction affect the file and quotation review."), ("No universal data pack", "Different SKUs, dimensions, materials and revisions cannot be replaced by one generic file. Unapproved CAD, load, MOQ, lead-time or test data is not inferred here.")], "faq": [("Can we receive CAD or STEP directly?", "Share the product or system, photos or drawings, quantity, target date and destination first. Formal CAD, PDF, DWG, DXF or STEP files are confirmed by SKU, revision and project conditions."), ("Is there one MOQ and lead time for every product?", "No universal MOQ or lead time is published for all products. Individual documented records may show representative directions; formal conditions require model, quantity, revision and schedule confirmation."), ("What should a designer prepare?", "Prepare existing drawings or photos, mounting system and dimensions, merchandise, quantity, material or finish direction, target timing and destination to start the specification review.")], "cta": "Request CAD and specification files", "download": "View representative display-hook drawing", "download_href": "images/product-display-hooks-dim.jpg", "download_note": "Representative DBTHK001-SLW drawing; not a specification for every display-hook SKU.", "related": (("Display Hooks", "display-hooks"), ("PAGE Cosmetic Display Record", "case-page-cosmetic-organizer"))
    },
    "jp": {
        "lang": "ja", "title": "店舗什器の仕様・CAD資料を相談する", "description": "店舗什器の仕様、寸法資料、CADデータの相談入口。確認済みの資料から始め、SKU・図面・サンプルで正式データを確認します。", "nav": ("ホーム", "製品", "用途事例", "資料を相談"), "kicker": "TECHNICAL RESOURCE ENTRY", "hero": "設計意図を確認可能な仕様へ", "intro": "公開できる寸法資料、製品記録、事例記録から始めます。PDF、CAD、DWG、DXF、STEP が必要な場合は、製品、システム、数量、案件条件を共有し、SKU と版を確認します。", "cards": [("閲覧できる資料", "代表的なディスプレイフック寸法図と PAGE 化粧品展示資料記録を確認できます。対象バージョンと証拠の範囲を明記しています。"), ("相談できる形式", "案件条件に応じて PDF、CAD、DWG、DXF、STEP、寸法図、材料・仕上げ資料を相談できます。提供可否と版は正式資料で確認します。"), ("先に確認する条件", "背板・取付システム、商品寸法、予定数量、希望時期、納品地、材料・仕上げの方向が資料と見積確認に影響します。"), ("共通データパックではありません", "SKU、寸法、材料、版が異なるため、共通ファイルで代替しません。未承認のCAD、荷重、MOQ、納期、試験データは推測しません。")], "faq": [("CAD や STEP を直接受け取れますか？", "製品またはシステム、写真・図面、数量、希望時期、納品地を共有してください。正式な CAD、PDF、DWG、DXF、STEP は SKU、版、案件条件で確認します。"), ("MOQ と納期は共通ですか？", "全製品共通の MOQ・納期は掲載していません。個別資料に代表方向が記録されている場合も、正式条件は型式、数量、版、工程で確認します。"), ("設計者は何を準備すればよいですか？", "既存図面や写真、取付システムと寸法、展示商品、数量、材料・仕上げ、希望時期、納品地を準備すると仕様相談を始められます。")], "cta": "CAD・仕様資料を相談する", "download": "代表的なディスプレイフック寸法図を見る", "download_href": "images/product-display-hooks-dim.jpg", "download_note": "代表的な DBTHK001-SLW 寸法図であり、全 SKU の仕様を示すものではありません。", "related": (("ディスプレイフック", "display-hooks"), ("PAGE 化粧品展示資料記録", "case-page-cosmetic-organizer"))
    },
}


def page(folder: str, d: dict) -> str:
    base = f"https://www.bigfame.co/{folder}/{SLUG}"
    alts = "".join(f'<link rel="alternate" hreflang="{code}" href="https://www.bigfame.co/{loc}/{SLUG}">' for code, loc in (("zh-TW", "tw"), ("en", "en"), ("ja", "jp")))
    collection = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": d["title"], "description": d["description"], "url": base}, ensure_ascii=False)
    breadcrumb = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"https://www.bigfame.co/{folder}/"}, {"@type": "ListItem", "position": 2, "name": d["nav"][1], "item": f"https://www.bigfame.co/{folder}/products"}, {"@type": "ListItem", "position": 3, "name": d["title"], "item": base}]}, ensure_ascii=False)
    faq = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}, ensure_ascii=False)
    cards = "".join(f'<article class="location-card reveal"><h3>{html.escape(h)}</h3><p>{html.escape(b)}</p></article>' for h, b in d["cards"])
    faqs = "".join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in d["faq"])
    related = " · ".join(f'<a href="{slug}">{html.escape(name)}</a>' for name, slug in d["related"])
    contact = "contact?category=display_hardware&role=buyer"
    return f'''<!DOCTYPE html><html lang="{d["lang"]}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(d["description"], quote=True)}"><title>{html.escape(d["title"])} | Big Fame</title><link rel="canonical" href="{base}">{alts}<link rel="stylesheet" href="../css/style.css"><script type="application/ld+json">{collection}</script><script type="application/ld+json">{breadcrumb}</script><script type="application/ld+json">{faq}</script></head><body><header class="header"><div class="container header-inner"><a href="./" class="logo">BIG FAME</a><nav class="nav-menu"><a href="./" class="nav-link">{d["nav"][0]}</a><a href="products" class="nav-link active">{d["nav"][1]}</a><a href="applications" class="nav-link">{d["nav"][2]}</a><a href="{contact}" class="nav-link nav-cta">{d["nav"][3]}</a></nav></div></header><main><section class="hero"><div class="container hero-content reveal"><p class="hero-kicker">{d["kicker"]}</p><h1>{html.escape(d["title"])}</h1><p class="hero-description">{html.escape(d["intro"])}</p><a class="btn btn-primary" href="{contact}">{html.escape(d["cta"])}</a></div></section><section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">TECHNICAL EVIDENCE</span><h2 class="section-title">{html.escape(d["hero"])}</h2></div><div class="grid-2">{cards}</div><div class="cta-block reveal"><p><a class="btn btn-secondary" href="../{d["download_href"]}" target="_blank" rel="noopener">{html.escape(d["download"])}</a></p><p class="section-note">{html.escape(d["download_note"])}</p></div></div></section><section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">FAQ</h2></div><div class="grid-3">{faqs}</div></div></section><section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{html.escape(d["cta"])}</h2><p>{related}</p><a class="btn btn-primary" href="{contact}">{html.escape(d["nav"][3])}</a></div></div></section></main><footer class="footer"><div class="container footer-bottom"><p>© Big Fame IND. CORP.</p><a href="applications">{d["nav"][2]}</a></div></footer><script src="../js/main.js"></script></body></html>'''


for folder, data in DATA.items():
    (ROOT / folder / f"{SLUG}.html").write_text(page(folder, data), encoding="utf-8")

links = {
    "tw": '<a href="technical-resources">索取 CAD／規格資料</a>',
    "en": '<a href="technical-resources">Request CAD / specification files</a>',
    "jp": '<a href="technical-resources">CAD・仕様資料を相談する</a>',
}
targets = {
    "tw": ("tw/procurement.html", "流程：需求摘要 → 圖面／樣品確認"),
    "en": ("en/procurement.html", "Workflow: requirement brief → drawing or sample review"),
    "jp": ("jp/procurement.html", "流れ：要件概要 → 図面・サンプル確認"),
}
for folder, (relative, marker) in targets.items():
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    if "technical-resources" not in text:
        if marker not in text:
            raise SystemExit(f"Cannot find procurement marker: {folder}")
        text = text.replace(marker, marker + " → " + links[folder], 1)
        path.write_text(text, encoding="utf-8")

sitemap = ROOT / "sitemap.xml"
text = sitemap.read_text(encoding="utf-8")
for folder in DATA:
    line = f"  <url><loc>https://www.bigfame.co/{folder}/{SLUG}</loc></url>"
    if line not in text:
        text = text.replace("</urlset>", line + "\n</urlset>")
sitemap.write_text(text, encoding="utf-8")
print(f"Generated {SLUG} in tw/en/jp, linked procurement pages, and updated sitemap.")
