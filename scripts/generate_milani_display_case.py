"""Generate an anonymous, evidence-controlled Milani retail-display engineering record."""

from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
SLUG = "case-hair-display-spinner-engineering"
BASE = "https://www.bigfame.co"

PAGES = {
    "tw": {
        "lang": "zh-Hant-TW",
        "title": "美妝展示旋轉架與端架工程紀錄",
        "description": "匿名美妝／假髮展示工程紀錄：整理端架、雙面旋轉架、槽板、展示掛勾、尺寸、展示容量與平板運輸方向。",
        "home": "首頁", "products": "產品與能力", "cases": "應用案例", "contact": "提出專案需求",
        "lede": "從產品包裝尺寸出發，整理端架與雙面旋轉架的結構、展示掛勾、槽板、尺寸、容量與運輸方式；這是一筆可核對的設計／樣品工程紀錄，不是目前型錄規格。",
        "visual_note": "原始專案影像含品牌識別，公開版本暫不使用；先公開可核對的圖面與工程條件。",
        "sections": [
            ("客戶需求／來源狀態", "讓髮品盒裝商品可以被看見、拿取與彈性調整", "來源圖面以髮品盒尺寸與端架、雙面旋轉架的組合需求為設計起點；正式客戶名稱與商業背景不在公開頁面呈現。"),
            ("產品與店型", "美妝、髮品與小型盒裝商品的零售展示", "端架適合靠牆或端面展示；雙面旋轉架適合中島或需要從不同方向取貨的零售動線。兩者共享主要框架概念。"),
            ("材料與製程", "壓克力板、金屬框架、槽板與鋼線掛勾", "來源資料記錄白色壓克力底座、白色粉體塗裝金屬框架、9 槽壓克力槽板、壓克力招牌與白色粉體／鍍鉻鋼線掛勾。正式板厚、線徑與加工條件仍依核准圖面確認。"),
            ("尺寸／展示容量", "把商品尺寸轉成可核對的展示條件", "端架圖面記錄約 W23 × D13 5/8 × H66 5/8 英吋，來源標示展示容量 20 箱；雙面旋轉架約 W24 × D24 × H72 1/2 英吋，來源標示展示容量 40 箱。這些是歷史工程紀錄，不是現行承重保證。"),
            ("Big Fame 實際承擔範圍", "從材料替代、樣品討論到結構與運輸改善", "來源包含材料與成本方向建議、樣品說明、框架共用、旋轉軸、槽板調整與拆解運輸思考；正式合約責任與最終交付範圍仍需逐案確認。"),
            ("數量／交期／交付", "把歷史報價與目前專案條件分開", "歷史報價文件記錄樣品預估交期 3 週，且含出貨與目的地欄位；公開頁面不把它當成目前交期，也不公開正式數量、價格、客戶或目的地。"),
        ],
        "faq": [
            ("這是已完成安裝的客戶案例嗎？", "目前以匿名設計／樣品／規格工程紀錄公開。來源支持圖面、材料、容量、樣品與報價討論，但公開頁面不宣稱目前客戶安裝、正式訂單或最終交付。"),
            ("可以依照髮品盒尺寸做旋轉展示架嗎？", "可以先從商品盒尺寸、取貨方向、展示數量、店面位置與是否需要端架／中島旋轉架開始，接著確認圖面、樣品與量產條件。"),
            ("可以取得 CAD、尺寸或報價嗎？", "可以提出圖面與規格資料需求；正式 CAD、材料、MOQ、交期與報價需依型號、數量、版本與交付地確認。"),
        ],
        "boundary": "公開頁面不呈現客戶名稱、品牌標誌、正式訂單數量、價格、目的地、現行 SKU、測試標準或未核准的交付主張。歷史圖面與報價是專案證據，不等於目前型錄規格。",
        "cta_title": "從商品尺寸開始討論展示架",
        "cta": "提供商品盒尺寸、展示數量、希望的取貨方向、店型、交貨地與目標時程，我們再確認端架、旋轉架、掛勾、槽板與樣品路徑。",
        "cta_text": "提出美妝展示需求",
    },
    "en": {
        "lang": "en", "title": "Hair Display Spinner and End-Cap Engineering Record",
        "description": "An anonymous retail-display engineering record covering a hair-product end cap, two-way spinner, slat board, hooks, dimensions, loading capacity and flat-pack thinking.",
        "home": "Home", "products": "Products and capabilities", "cases": "Applications", "contact": "Start an inquiry",
        "lede": "Starting from packaged hair-product dimensions, this record connects the end cap and two-way spinner structure, display hooks, slot board, dimensions, capacity and transport logic. It is an evidence-controlled design and sample record, not a current catalogue specification.",
        "visual_note": "The source photographs include project identification; the public version withholds them and publishes the verifiable engineering conditions first.",
        "sections": [
            ("Client need / source status", "Making boxed hair products visible, accessible and adjustable", "The source drawings begin with hair-box dimensions and a combined end-cap / two-way-spinner requirement. The client name and commercial background are withheld."),
            ("Product and store fit", "Retail display for beauty, hair-care and boxed products", "The end cap suits a wall or aisle-end position; the two-way spinner suits an island or a route where products should be accessed from more than one direction. The two concepts share a main-frame logic."),
            ("Materials and process", "Acrylic panels, metal frame, slot board and wire hooks", "The source records white acrylic panels, a white powder-coated metal frame, a nine-slot acrylic board, an acrylic header and white powder-coated or chrome steel-wire hooks. Final thickness, wire gauge and processing follow approved drawings."),
            ("Dimensions / loading", "Turning package dimensions into checkable display conditions", "The end-cap drawing records approximately W23 × D13 5/8 × H66 5/8 in and a source-stated capacity of 20 boxes. The two-way spinner records approximately W24 × D24 × H72 1/2 in and a source-stated capacity of 40 boxes. These are historical engineering conditions, not a current load guarantee."),
            ("Big Fame scope", "From material alternatives and samples to structure and transport", "The sources include material and cost-direction recommendations, sample discussion, shared-frame logic, a rotating axis, slot-board adjustment and flat-pack transport thinking. Formal contractual responsibility remains project-specific."),
            ("Quantity / lead time / delivery", "Keeping historical quotation data separate from current terms", "A historical quotation records an estimated three-week sample lead time and shipment fields. The public page does not present that as a current lead time and withholds formal quantity, price, client and destination."),
        ],
        "faq": [
            ("Is this a confirmed installed customer case?", "It is published as an anonymous design, sample and specification engineering record. The sources support drawings, materials, loading conditions, sample and quotation discussion; the public page does not claim a current installation, formal order or final delivery."),
            ("Can you develop a spinner for boxed hair products?", "Start with package dimensions, display quantity, access direction, store position and whether an end cap or island spinner is needed. We can then determine the drawing, sample and production path."),
            ("Can I request CAD, dimensions or a quotation?", "Yes. Share the drawing and specification request; final CAD, materials, MOQ, lead time and quotation depend on the model, quantity, version and delivery location."),
        ],
        "boundary": "The public page withholds the client name, brand mark, formal order quantity, price, destination, current SKU, test standard and unapproved delivery claims. Historical drawings and quotation records are project evidence, not current catalogue specifications.",
        "cta_title": "Start with the product dimensions",
        "cta": "Share package dimensions, display quantity, access direction, store type, delivery location and target schedule so we can assess the end cap, spinner, hooks, slot board and sample path.",
        "cta_text": "Submit a beauty-display inquiry",
    },
    "jp": {
        "lang": "ja", "title": "ヘアケア什器 回転ラック・エンドキャップ設計記録",
        "description": "ヘアケア商品のエンドキャップと両面回転ラックについて、スロットボード、フック、寸法、収納数、輸送設計を整理した匿名エンジニアリング記録です。",
        "home": "ホーム", "products": "製品と対応力", "cases": "事例", "contact": "案件を相談する",
        "lede": "ヘアケア商品の箱寸法を起点に、エンドキャップと両面回転ラックの構造、フック、スロットボード、寸法、収納数、輸送方法を整理した設計・サンプル記録です。現行カタログ仕様ではありません。",
        "visual_note": "原資料の写真には案件識別情報が含まれるため、公開版では使用せず、確認できる技術条件を先に公開しています。",
        "sections": [
            ("顧客課題／資料状態", "箱入りヘアケア商品を見やすく、取りやすく、変更しやすくする", "原図面はヘアケア商品の箱寸法と、エンドキャップおよび両面回転ラックを組み合わせる要件から始まります。顧客名と商取引情報は非公開です。"),
            ("製品と店舗用途", "美容・ヘアケア・箱入り商品の店舗展示", "エンドキャップは壁面や通路端、両面回転ラックは島什器や複数方向から商品を取る売場に適した検討方向です。主要フレームの考え方を共有します。"),
            ("材料と加工", "アクリル板、金属フレーム、スロットボード、ワイヤーフック", "資料には白色アクリル板、白色粉体塗装の金属フレーム、9スロットのアクリル板、アクリルヘッダー、白色粉体塗装またはクロームのワイヤーフックが記録されています。最終条件は承認図面で確認します。"),
            ("寸法／収納数", "商品寸法を確認できる展示条件へ変換", "エンドキャップは約 W23 × D13 5/8 × H66 5/8 inch、資料上の収納数は20箱。両面回転ラックは約 W24 × D24 × H72 1/2 inch、資料上の収納数は40箱です。歴史資料の条件であり、現行の耐荷重保証ではありません。"),
            ("Big Fame の対応範囲", "材料提案、サンプル、構造、輸送方法の検討", "材料・コスト方向の提案、サンプル説明、共通フレーム、回転軸、スロット調整、分解輸送の考え方を確認できます。正式な契約範囲は案件ごとに確認します。"),
            ("数量／納期／納品", "過去の見積条件と現在の条件を分けて扱う", "過去の見積にはサンプルの想定納期3週間と出荷欄があります。公開ページでは現在の納期として扱わず、正式数量、価格、顧客、納品先は非公開です。"),
        ],
        "faq": [
            ("実際に設置された顧客事例ですか？", "匿名の設計・サンプル・仕様エンジニアリング記録として公開しています。図面、材料、収納条件、サンプル、見積の資料は確認できますが、現在の設置、正式注文、最終納品は主張していません。"),
            ("箱入りヘアケア商品の回転ラックを開発できますか？", "商品の箱寸法、数量、取り出し方向、店舗内の位置、エンドキャップか島什器かを共有してください。図面、サンプル、量産条件を順に確認します。"),
            ("CAD、寸法、見積を依頼できますか？", "依頼できます。型式、数量、仕様、納品先によって正式なCAD、材料、MOQ、納期、見積条件を確認します。"),
        ],
        "boundary": "顧客名、ブランドマーク、正式注文数量、価格、納品先、現行SKU、試験規格、未承認の納品主張は公開していません。過去の図面と見積は案件資料であり、現行カタログ仕様ではありません。",
        "cta_title": "商品寸法から展示を相談する",
        "cta": "商品の箱寸法、展示数量、取り出し方向、店舗タイプ、納品先、希望時期を共有いただければ、エンドキャップ、回転ラック、フック、スロットボード、サンプルの進め方を確認します。",
        "cta_text": "美容什器の相談を送る",
    },
}


def href(path: str, clean: bool) -> str:
    return f"../{path}" if clean else path


def render(locale: str, clean: bool) -> str:
    d = PAGES[locale]
    url = f"{BASE}/{locale}/{SLUG}"
    prefix = "../" if clean else ""
    contact = href("contact?role=designer&category=system_fixtures&requested_files=dimension_drawing", clean)
    sections = "".join(f'<article class="location-card reveal"><span class="section-subtitle">{html.escape(k)}</span><h3>{html.escape(t)}</h3><p>{html.escape(b)}</p></article>' for k, t, b in d["sections"])
    faq = "".join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in d["faq"])
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}
    article_schema = {"@context": "https://schema.org", "@type": "Article", "headline": d["title"], "description": d["description"], "url": url, "author": {"@type": "Organization", "name": "Big Fame IND. CORP."}, "about": "Retail display fixture engineering"}
    crumb_schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"{BASE}/{locale}/"}, {"@type": "ListItem", "position": 2, "name": d["cases"], "item": f"{BASE}/{locale}/applications"}, {"@type": "ListItem", "position": 3, "name": d["title"], "item": url}]}
    alternates = "".join(f'<link rel="alternate" hreflang="{h}" href="{BASE}/{l}/{SLUG}">' for h, l in [("zh-TW", "tw"), ("en", "en"), ("ja", "jp")])
    related = " · ".join(f'<a href="{href(path, clean)}">{label}</a>' for path, label in [("display-hooks", "展示掛勾" if locale == "tw" else "Display hooks" if locale == "en" else "展示フック"), ("modular-fixtures", "模組化展示架" if locale == "tw" else "Modular fixtures" if locale == "en" else "モジュール什器"), ("technical-resources", "技術與 CAD 資源" if locale == "tw" else "Technical and CAD resources" if locale == "en" else "技術・CAD資料")])
    return f'''<!DOCTYPE html>
<html lang="{d["lang"]}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(d["description"], quote=True)}"><meta property="og:type" content="article"><meta property="og:title" content="{html.escape(d["title"], quote=True)} | Big Fame"><meta property="og:description" content="{html.escape(d["description"], quote=True)}"><meta property="og:url" content="{url}"><meta property="og:site_name" content="Big Fame IND. CORP."><title>{html.escape(d["title"])} | Big Fame</title><link rel="canonical" href="{url}">{alternates}<link rel="stylesheet" href="{prefix}../css/style.css"><script type="application/ld+json">{json.dumps(article_schema, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(crumb_schema, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script></head>
<body><header class="header"><div class="container header-inner"><a href="{href('', clean)}" class="logo">BIG FAME</a><nav class="nav-menu"><a href="{href('', clean)}" class="nav-link">{d["home"]}</a><a href="{href('products', clean)}" class="nav-link">{d["products"]}</a><a href="{href('applications', clean)}" class="nav-link active">{d["cases"]}</a><a href="{contact}" class="nav-link nav-cta">{d["contact"]}</a></nav></div></header>
<main><section class="case-hero"><div class="container case-hero-grid"><div class="reveal"><div class="case-hero-kicker">ANONYMOUS ENGINEERING RECORD · 2011</div><h1>{html.escape(d["title"])}</h1><p class="case-hero-lede">{html.escape(d["lede"])}</p><div class="case-hero-actions"><a class="btn btn-primary" href="{contact}">{d["cta_text"]}</a><a class="btn btn-secondary" href="{href('applications', clean)}">{d["cases"]}</a></div></div><div class="case-hero-visual reveal"><div class="case-source-placeholder"><span class="section-subtitle">SOURCE VISUALS WITHHELD</span><strong>W23 × D13 5/8 × H66 5/8 in</strong><strong>W24 × D24 × H72 1/2 in</strong><span>{html.escape(d["visual_note"])}</span></div></div></div></section>
<section class="section section-light" data-bf-case-contract="1"><div class="container"><div class="section-header reveal"><span class="section-subtitle">ENGINEERING EVIDENCE</span><h2 class="section-title">{html.escape(d["title"])}</h2></div><div class="grid-2">{sections}</div><p class="section-note reveal">{html.escape(d["boundary"])}</p></div></section>
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
    "tw": '<article class="case-library-card reveal"><div class="case-library-card-body"><div class="case-meta">2011 · Retail Display Engineering · 匿名設計／樣品紀錄</div><h3><a href="case-hair-display-spinner-engineering">美妝展示旋轉架與端架</a></h3><p>從髮品盒尺寸、槽板與掛勾，到共用框架、展示容量、樣品與平板運輸方向，整理可核對的工程條件。</p><a class="btn btn-secondary" href="case-hair-display-spinner-engineering">查看工程證據與公開邊界</a></div></article>',
    "en": '<article class="case-library-card reveal"><div class="case-library-card-body"><div class="case-meta">2011 · Retail Display Engineering · Anonymous design and sample record</div><h3><a href="case-hair-display-spinner-engineering">Hair Display Spinner and End Cap</a></h3><p>From hair-box dimensions, slot board and hooks to shared framing, loading capacity, samples and flat-pack transport logic.</p><a class="btn btn-secondary" href="case-hair-display-spinner-engineering">View evidence and boundaries</a></div></article>',
    "jp": '<article class="case-library-card reveal"><div class="case-library-card-body"><div class="case-meta">2011 · Retail Display Engineering · 匿名設計・サンプル記録</div><h3><a href="case-hair-display-spinner-engineering">ヘアケア什器 回転ラック・エンドキャップ</a></h3><p>箱寸法、スロットボード、フック、共通フレーム、収納数、サンプル、輸送設計を整理した記録です。</p><a class="btn btn-secondary" href="case-hair-display-spinner-engineering">根拠と公開範囲を見る</a></div></article>',
}
for locale, card in cards.items():
    for path in [ROOT / locale / "applications.html", ROOT / locale / "applications" / "index.html"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if SLUG not in text:
            marker = "\n      </div>\n    </div>\n  </section>\n\n  <!-- Audience & Store Type Navigation -->"
            if marker not in text:
                raise SystemExit(f"applications grid marker missing: {path}")
            text = text.replace(marker, f"\n        {card}{marker}", 1)
            text = text.replace("<span>07</span>", "<span>08</span>", 1)
            path.write_text(text, encoding="utf-8")

for locale in ["tw", "en", "jp"]:
    for path in [ROOT / locale / "display-hooks.html", ROOT / locale / "display-hooks" / "index.html", ROOT / locale / "modular-fixtures.html", ROOT / locale / "modular-fixtures" / "index.html"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if SLUG in text:
            continue
        prefix = "../" if path.parent.name in {"display-hooks", "modular-fixtures"} else ""
        label = {"tw": "美妝展示旋轉架與端架工程紀錄", "en": "Hair display spinner engineering record", "jp": "ヘアケア什器の設計記録"}[locale]
        marker = "</p></div></section>"
        if marker in text:
            text = text.replace(marker, f" · <a href=\"{prefix}{SLUG}\">{label}</a></p></div></section>", 1)
            path.write_text(text, encoding="utf-8")

sitemap = ROOT / "sitemap.xml"
text = sitemap.read_text(encoding="utf-8")
for locale in ["tw", "en", "jp"]:
    url = f"  <url><loc>{BASE}/{locale}/{SLUG}</loc></url>"
    if url not in text:
        text = text.replace("</urlset>", f"{url}\n</urlset>")
sitemap.write_text(text, encoding="utf-8")
