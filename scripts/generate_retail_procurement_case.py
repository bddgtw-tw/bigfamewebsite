"""Generate an anonymous, evidence-controlled retail fixture procurement record."""

from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
SLUG = "case-retail-fixture-procurement-integration"
BASE = "https://www.bigfame.co"

PAGES = {
    "tw": {
        "lang": "zh-Hant-TW", "title": "匿名零售店面展示設備採購整合紀錄",
        "description": "匿名零售店面展示設備採購整合紀錄：從牆面層板、展示掛勾、壓克力配件、桌架、衣架到 POS 與化妝品展示，整理歷史 PI 與訂購清單可核對的範圍。",
        "home": "首頁", "products": "產品與能力", "cases": "應用案例", "contact": "提出採購需求",
        "lede": "這是一筆以歷史 PI、訂購清單與品類資料為核心的匿名採購整合紀錄。它展示如何把多種店面展示設備、配件、尺寸與交付條件放在同一個採購脈絡中確認。",
        "visual_note": "原始商業文件含客戶與品牌識別，公開版只呈現採購結構與可核對的品類證據。",
        "sections": [
            ("Client problem / 採購問題／來源狀態", "多品類店面什器需要被放進同一份採購脈絡", "來源包含店面什器訂購清單與三組歷史 Pro Forma Invoice，品類從層板、掛勾、壓克力盒到桌架、衣架、POP 與化妝品展示配件。客戶與品牌名稱不公開。"),
            ("店型與採購範圍", "海外零售店的牆面、島架與桌面展示整合", "可核對的採購方向涵蓋 wall bay、floor bay、gondola、table、hanger、signage、acrylic accessory 與 cosmetics display。這是採購整合記錄，不等於現場安裝證明。"),
            ("產品與材料方向", "木材、金屬、壓克力、PET 與展示五金的組合", "來源品項包含木製層板與桌架、鋼製掛勾／支架、壓克力盒與階梯架、PET 分隔板、POP 盒與標示配件；正式材料牌號、板厚與表面處理依圖面與樣品確認。"),
            ("數量與規格", "先按品類、單位與圖面整理，再確認正式數量", "歷史文件以 PC、SET 等單位分列品項，並記錄部分 W／D／H 尺寸與商品用途；正式訂購數量、單價與總額不在公開頁面呈現。"),
            ("Big Fame 實際承擔範圍", "把品類、圖面、報價與交付欄位整理成可執行的採購文件", "來源文件具有 Big Fame 正式文件識別與簽署區，支持其參與品項整理、PI／報價文件與採購協調；來源不足以單獨證明每一品項的製造、安裝或最終現場交付責任。"),
            ("交期與交付", "從台灣出貨欄位進入海外專案的交付確認", "歷史 PI 記錄台灣出貨欄位、海外專案目的地欄位與預定時程欄位；公開版不揭露目的地與正式時程，也不把歷史欄位當成目前交期承諾。"),
        ],
        "faq": [
            ("這是已完成安裝的零售店案例嗎？", "目前以匿名採購／文件整合紀錄公開。來源支持訂購清單、PI、品類、單位與交付欄位，但公開頁面不宣稱特定客戶安裝、正式數量或最終現場結果。"),
            ("Big Fame 可以協助多種展示設備一起採購嗎？", "可以先從店型、平面或照片、品類清單、商品尺寸、數量、希望時程與交貨地開始，分別確認展示架、掛勾、壓克力配件、桌架與標示配件。"),
            ("採購前需要準備哪些資料？", "建議提供店面區域、展示商品、尺寸、數量、材料方向、包裝需求、目標日期、交貨地與 PDF／CAD／照片。正式 MOQ、交期與報價需逐項確認。"),
        ],
        "boundary": "公開頁面不呈現客戶名稱、品牌、PI／訂單編號、正式數量、價格、目的地、現行 SKU、測試標準或未核准的製造／安裝主張。歷史採購文件是證據，不等於目前型錄或報價。",
        "cta_title": "從採購清單開始整理店面需求",
        "cta": "提供店型、品類清單、商品尺寸、數量、目標日期與交貨地，我們再確認產品、圖面、樣品與採購文件路徑。",
        "cta_text": "提出店面採購需求",
    },
    "en": {
        "lang": "en", "title": "Anonymous Retail Fixture Procurement Integration Record",
        "description": "An anonymous retail fixture procurement record covering wall shelves, display hooks, acrylic accessories, tables, hangers, POS and beauty-display components through historical PI and order-list evidence.",
        "home": "Home", "products": "Products and capabilities", "cases": "Applications", "contact": "Start a procurement inquiry",
        "lede": "This anonymous procurement record is built from historical pro forma invoices, an order list and category-level evidence. It shows how multiple retail fixtures, accessories, dimensions and delivery fields can be brought into one sourcing conversation.",
        "visual_note": "The source commercial documents include client and brand identifiers; the public version presents the procurement structure and verifiable categories only.",
        "sections": [
            ("Client problem / Procurement problem", "Bringing many fixture categories into one procurement context", "The sources include a retail-fixture order list and three historical pro forma invoices. Categories range from shelves and hooks to acrylic boxes, tables, hangers, POP and beauty-display accessories. Client and brand names are withheld."),
            ("Store type and scope", "Coordinating wall, island and tabletop displays for an overseas retail project", "The documented directions include wall bays, floor bays, gondolas, tables, hangers, signage, acrylic accessories and cosmetics display. This is a procurement-integration record, not proof of site installation."),
            ("Products and material directions", "Combining wood, metal, acrylic, PET and display hardware", "Source items include wooden shelves and tables, steel hooks and brackets, acrylic boxes and stepped racks, PET dividers, POP cases and signage accessories. Final grades, thicknesses and finishes require drawings and samples."),
            ("Quantity and specification", "Organising by category, unit and drawing before confirming the final quantity", "Historical documents list items by units such as PC and SET, with selected W / D / H dimensions and product-use descriptions. Formal order quantities, unit prices and totals are withheld from the public page."),
            ("Big Fame scope", "Turning categories, drawings, quotations and delivery fields into workable procurement documents", "The source documents carry Big Fame document identification and an authorised-signature area, supporting participation in item organisation, PI / quotation documentation and procurement coordination. The sources alone do not prove manufacturing, installation or final site-delivery responsibility for every item."),
            ("Lead time and delivery", "Moving from Taiwan shipment fields into an overseas project-delivery discussion", "Historical PIs record a Taiwan shipment field, an overseas destination field and a schedule field. The public page withholds the destination and formal schedule and does not present historical fields as a current lead-time promise."),
        ],
        "faq": [
            ("Is this a completed retail-store installation case?", "It is published as an anonymous procurement and document-integration record. The sources support the order list, PIs, categories, units and delivery fields; the public page does not claim a named installation, formal quantity or final site result."),
            ("Can Big Fame coordinate several fixture categories in one purchase?", "Start with the store type, plan or photos, category list, product dimensions, quantities, target schedule and delivery location. We can then separate fixtures, hooks, acrylic accessories, tables and signage into a confirmation path."),
            ("What should I prepare before sourcing?", "Share the store zones, displayed products, dimensions, quantities, material direction, packing needs, target date, delivery location and PDF, CAD or photos. Formal MOQ, lead time and quotation terms are confirmed item by item."),
        ],
        "boundary": "The public page withholds the client name, brand, PI / order numbers, formal quantities, prices, destination, current SKU, test standards and unapproved manufacturing or installation claims. Historical procurement documents are evidence, not a current catalogue or quotation.",
        "cta_title": "Start with the procurement list",
        "cta": "Share the store type, category list, product dimensions, quantities, target date and delivery location so we can map the product, drawing, sample and procurement-document path.",
        "cta_text": "Submit a retail procurement inquiry",
    },
    "jp": {
        "lang": "ja", "title": "匿名・店舗什器 調達統合記録",
        "description": "壁面棚、展示フック、アクリル什器、テーブル、ハンガー、POS、化粧品什器を、過去のPIと発注リストから整理した匿名の店舗什器調達記録です。",
        "home": "ホーム", "products": "製品と対応力", "cases": "事例", "contact": "調達案件を相談する",
        "lede": "過去のプロフォーマインボイス、発注リスト、品目資料をもとに、複数の店舗什器、アクセサリー、寸法、納品欄を一つの調達相談にまとめる考え方を整理しています。",
        "visual_note": "原資料には顧客・ブランド識別情報が含まれるため、公開版では調達構造と確認できる品目だけを扱います。",
        "sections": [
            ("調達課題／資料状態", "多品目の什器を一つの調達条件へまとめる", "店舗什器の発注リストと3組の過去PIを確認できます。棚、フック、アクリルボックス、テーブル、ハンガー、POP、化粧品什器まで含まれます。顧客名とブランド名は非公開です。"),
            ("店舗タイプと範囲", "壁面・島什器・卓上展示を海外小売案件で調整", "資料上は wall bay、floor bay、gondola、table、hanger、signage、アクリルアクセサリー、化粧品展示の方向が確認できます。現場設置の証明ではありません。"),
            ("製品と材料方向", "木材、金属、アクリル、PET、展示金具の組み合わせ", "木製棚・テーブル、金属フック・ブラケット、アクリルボックス・段差ラック、PET仕切り、POPケース、表示アクセサリーが記録されています。正式な材料・板厚・仕上げは図面とサンプルで確認します。"),
            ("数量と仕様", "品目、単位、図面を整理してから正式数量を確定", "過去資料には PC、SET などの単位、部分的な W／D／H 寸法、用途説明があります。正式数量、単価、合計金額は公開していません。"),
            ("Big Fame の対応範囲", "品目、図面、見積、納品欄を実行可能な調達資料へ整理", "原資料には Big Fame の文書識別と署名欄があり、品目整理、PI／見積資料、調達調整への関与を確認できます。ただし、全品目の製造、設置、最終納品責任までは資料だけで断定しません。"),
            ("納期と納品", "台湾出荷欄から海外案件の納品条件へつなぐ", "過去PIには台湾出荷欄、海外向け納品先欄、予定時期欄があります。公開版では納品先と正式時期を伏せ、現在の納期として扱いません。"),
        ],
        "faq": [
            ("完成した店舗設置事例ですか？", "匿名の調達・資料統合記録として公開しています。発注リスト、PI、品目、単位、納品欄は確認できますが、特定店舗の設置、正式数量、最終結果は主張していません。"),
            ("複数の什器カテゴリーをまとめて調達できますか？", "店舗タイプ、平面または写真、品目、商品寸法、数量、希望時期、納品先から始め、什器、フック、アクリル、テーブル、表示アクセサリーを分けて確認します。"),
            ("調達前に何を準備すればよいですか？", "店舗ゾーン、商品、寸法、数量、材料方向、梱包条件、希望日、納品先、PDF／CAD／写真をご共有ください。MOQ、納期、見積条件は品目ごとに確認します。"),
        ],
        "boundary": "顧客名、ブランド名、PI／注文番号、正式数量、価格、納品先、現行SKU、試験規格、未承認の製造・設置主張は公開していません。過去の調達資料は証拠であり、現行カタログや見積ではありません。",
        "cta_title": "調達リストから店舗条件を整理する",
        "cta": "店舗タイプ、品目リスト、商品寸法、数量、希望日、納品先を共有いただければ、製品、図面、サンプル、調達資料の進め方を確認します。",
        "cta_text": "店舗什器の調達を相談する",
    },
}


def href(path: str, clean: bool) -> str:
    return f"../{path}" if clean else path


def render(locale: str, clean: bool) -> str:
    d = PAGES[locale]
    url = f"{BASE}/{locale}/{SLUG}"
    prefix = "../" if clean else ""
    contact = href("contact?role=buyer&category=system_fixtures&requested_files=dimension_drawing", clean)
    sections = "".join(f'<article class="location-card reveal"><span class="section-subtitle">{html.escape(k)}</span><h3>{html.escape(t)}</h3><p>{html.escape(b)}</p></article>' for k, t, b in d["sections"])
    faq = "".join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in d["faq"])
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}
    article_schema = {"@context": "https://schema.org", "@type": "Article", "headline": d["title"], "description": d["description"], "url": url, "author": {"@type": "Organization", "name": "Big Fame IND. CORP."}, "about": "Retail fixture procurement integration"}
    crumb_schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"{BASE}/{locale}/"}, {"@type": "ListItem", "position": 2, "name": d["cases"], "item": f"{BASE}/{locale}/applications"}, {"@type": "ListItem", "position": 3, "name": d["title"], "item": url}]}
    alternates = "".join(f'<link rel="alternate" hreflang="{h}" href="{BASE}/{l}/{SLUG}">' for h, l in [("zh-TW", "tw"), ("en", "en"), ("ja", "jp")])
    related = " · ".join(f'<a href="{href(path, clean)}">{label}</a>' for path, label in [("display-hooks", "展示掛勾" if locale == "tw" else "Display hooks" if locale == "en" else "展示フック"), ("modular-fixtures", "模組化展示架" if locale == "tw" else "Modular fixtures" if locale == "en" else "モジュール什器"), ("pos-displays", "POS 展示架" if locale == "tw" else "POS displays" if locale == "en" else "POS什器"), ("technical-resources", "技術與 CAD 資源" if locale == "tw" else "Technical and CAD resources" if locale == "en" else "技術・CAD資料")])
    return f'''<!DOCTYPE html>
<html lang="{d["lang"]}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(d["description"], quote=True)}"><meta property="og:type" content="article"><meta property="og:title" content="{html.escape(d["title"], quote=True)} | Big Fame"><meta property="og:description" content="{html.escape(d["description"], quote=True)}"><meta property="og:url" content="{url}"><meta property="og:site_name" content="Big Fame IND. CORP."><title>{html.escape(d["title"])} | Big Fame</title><link rel="canonical" href="{url}">{alternates}<link rel="stylesheet" href="{prefix}../css/style.css"><script type="application/ld+json">{json.dumps(article_schema, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(crumb_schema, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script></head>
<body><header class="header"><div class="container header-inner"><a href="{href('', clean)}" class="logo">BIG FAME</a><nav class="nav-menu"><a href="{href('', clean)}" class="nav-link">{d["home"]}</a><a href="{href('products', clean)}" class="nav-link">{d["products"]}</a><a href="{href('applications', clean)}" class="nav-link active">{d["cases"]}</a><a href="{contact}" class="nav-link nav-cta">{d["contact"]}</a></nav></div></header>
<main><section class="case-hero"><div class="container case-hero-grid"><div class="reveal"><div class="case-hero-kicker">ANONYMOUS PROCUREMENT RECORD · 2011</div><h1>{html.escape(d["title"])}</h1><p class="case-hero-lede">{html.escape(d["lede"])}</p><div class="case-hero-actions"><a class="btn btn-primary" href="{contact}">{d["cta_text"]}</a><a class="btn btn-secondary" href="{href('applications', clean)}">{d["cases"]}</a></div></div><div class="case-hero-visual reveal"><div class="case-source-placeholder"><span class="section-subtitle">PROCUREMENT EVIDENCE</span><strong>PI + ORDER LIST</strong><strong>Multi-category retail fixtures</strong><span>{html.escape(d["visual_note"])}</span></div></div></div></section>
<section class="section section-light" data-bf-case-contract="1"><div class="container"><div class="section-header reveal"><span class="section-subtitle">PROCUREMENT EVIDENCE</span><h2 class="section-title">{html.escape(d["title"])}</h2></div><div class="grid-2">{sections}</div><p class="section-note reveal">{html.escape(d["boundary"])}</p></div></section>
<section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-header reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">FAQ</h2></div><div class="grid-3">{faq}</div></div></section>
<section class="section section-light"><div class="container"><div class="section-header reveal"><span class="section-subtitle">RELATED CAPABILITIES</span><h2 class="section-title">{d["products"]}</h2></div><p class="reveal">{related}</p></div></section>
<section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{html.escape(d["cta_title"])}</h2><p>{html.escape(d["cta"])}</p><a class="btn btn-primary" href="{contact}">{d["cta_text"]}</a></div></div></section></main>
<footer class="footer"><div class="container footer-bottom"><p>© Big Fame IND. CORP.</p><a href="{href('applications', clean)}">{d["cases"]}</a></div></footer><script src="{prefix}../js/main.js"></script></body></html>'''


for locale in PAGES:
    (ROOT / locale / f"{SLUG}.html").write_text(render(locale, False), encoding="utf-8")
    folder = ROOT / locale / SLUG
    folder.mkdir(exist_ok=True)
    (folder / "index.html").write_text(render(locale, True), encoding="utf-8")

cards = {
    "tw": '<article class="case-library-card reveal"><div class="case-library-card-body"><div class="case-meta">2011 · Retail Procurement · 匿名採購／文件整合紀錄</div><h3><a href="case-retail-fixture-procurement-integration">零售店面展示設備採購整合</a></h3><p>從層板、掛勾、壓克力配件、桌架、衣架到 POS 與化妝品展示，整理歷史 PI 與訂購清單可核對的採購範圍。</p><a class="btn btn-secondary" href="case-retail-fixture-procurement-integration">查看採購證據與公開邊界</a></div></article>',
    "en": '<article class="case-library-card reveal"><div class="case-library-card-body"><div class="case-meta">2011 · Retail Procurement · Anonymous procurement record</div><h3><a href="case-retail-fixture-procurement-integration">Retail Fixture Procurement Integration</a></h3><p>From shelves, hooks and acrylic accessories to tables, hangers, POS and beauty displays, organised through historical PI and order-list evidence.</p><a class="btn btn-secondary" href="case-retail-fixture-procurement-integration">View procurement evidence and boundaries</a></div></article>',
    "jp": '<article class="case-library-card reveal"><div class="case-library-card-body"><div class="case-meta">2011 · Retail Procurement · 匿名調達・資料統合記録</div><h3><a href="case-retail-fixture-procurement-integration">店舗什器の調達統合</a></h3><p>棚、フック、アクリル什器、テーブル、ハンガー、POS、化粧品什器を、過去のPIと発注リストから整理します。</p><a class="btn btn-secondary" href="case-retail-fixture-procurement-integration">根拠と公開範囲を見る</a></div></article>',
}
for locale, card in cards.items():
    path = ROOT / locale / "applications.html"
    text = path.read_text(encoding="utf-8")
    if SLUG not in text:
        marker = "\n      </div>\n    </div>\n  </section>\n\n  <!-- Audience & Store Type Navigation -->"
        if marker not in text:
            raise SystemExit(f"applications grid marker missing: {path}")
        text = text.replace(marker, f"\n        {card}{marker}", 1)
        text = text.replace("<span>08</span>", "<span>09</span>", 1)
        path.write_text(text, encoding="utf-8")

sitemap = ROOT / "sitemap.xml"
text = sitemap.read_text(encoding="utf-8")
for locale in ["tw", "en", "jp"]:
    url = f"  <url><loc>{BASE}/{locale}/{SLUG}</loc></url>"
    if url not in text:
        text = text.replace("</urlset>", f"{url}\n</urlset>")
sitemap.write_text(text, encoding="utf-8")
