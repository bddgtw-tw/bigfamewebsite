"""Generate an evidence-controlled anonymous modular storage case in three locales."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
IMAGE = "https://www.bigfame.co/images/case-urban-storage.jpg"

DATA = {
    "tw": {
        "lang": "zh-Hant-TW",
        "title": "匿名城市儲物空間模組化案例",
        "description": "匿名城市儲物空間案例：以可複製的模組化儲物單元、K/D 結構與多種金屬元件回應空間服務需求。",
        "nav": ("首頁", "產品", "應用案例", "提交需求"),
        "need_title": "把城市儲物服務變成可複製的模組",
        "need": "原始專案敘述指出，城市人口需要更多儲物空間，而客戶希望把迷你儲物單元發展成可在不同城市複製的商業模組。這不是單一櫃體採購，而是需要尺寸、功能、運輸與後續擴充一起被考慮的系統問題。",
        "record_title": "原始資料可核對的交付方向",
        "record": [
            ("模組與規模", "來源敘述記錄一套完整迷你儲物單元，包含超過 50 個元件；標準儲物單元約 3.4 m³，並可透過其他元件調整尺寸與功能。"),
            ("材料與表面", "來源記錄使用鋼板、鋼管與鋼線，並採用客製粉體塗裝方向；原始文字另描述其對濕氣與刮傷的考量。"),
            ("結構與運輸", "單元採 K/D（knock-down）結構，原始敘述將其與降低運輸成本的需求連結；正式包裝與運輸條件未在公開頁面推定。"),
            ("功能組合", "來源記錄帶門的儲物單元、可調整尺寸與功能的元件，以及供小型物品使用的雙層儲物櫃。"),
            ("專案承擔範圍", "來源以第一人稱記錄設計完整迷你儲物單元與元件開發；正式合約分工、供應範圍與 Big Fame 的法律角色仍需依專案文件確認。"),
            ("成果與公開邊界", "原始敘述記錄該迷你儲物空間已開放使用，業主可沿用原始設計複製到其他城市；客戶名稱、日期、最終店數、數量與授權未公開。"),
        ],
        "faq": [
            ("這個案例適合哪類需求？", "適合需要模組化儲物櫃、可拆裝結構、跨據點複製或多元金屬元件整合的商業空間需求。正式尺寸與承重需依圖面和樣品確認。"),
            ("如果我要開發類似系統，應先提供什麼？", "請提供單元尺寸、門片與鎖具需求、功能變體、數量、場地條件、運輸方式、目標時程與圖面或現有樣品。"),
        ],
        "cta": "討論模組化儲物與金屬結構需求",
        "boundary": "本頁為匿名專案紀錄；客戶名稱、日期、正式數量、最終交付地、價格、合約分工與公開授權需逐案確認。",
        "related": ("客製金屬零件", "custom-metal-parts", "模組化展示架", "modular-fixtures"),
    },
    "en": {
        "lang": "en",
        "title": "Anonymous Urban Self-Storage Modular Case",
        "description": "An anonymous urban self-storage case covering a replicable modular unit, knock-down structure and coordinated metal components.",
        "nav": ("Home", "Products", "Applications", "Submit inquiry"),
        "need_title": "Turn a city-storage service into a repeatable module",
        "need": "The source narrative describes growing demand for storage in cities and a customer who wanted a mini-storage unit that could be duplicated in other locations. The requirement was a system question: size, function, transport and future variation had to be considered together.",
        "record_title": "What the source record confirms",
        "record": [
            ("Module and scale", "The source records a complete mini-storage unit with more than 50 components. A standard unit is described as approximately 3.4 m³, with additional components for size and function changes."),
            ("Materials and finish", "The source records steel plate, steel pipe and steel wire, with a customized powder-coating direction. The narrative also describes consideration of humidity and scratch resistance."),
            ("Structure and transport", "The units use a K/D (knock-down) structure. The source connects this approach with reducing transport cost; formal packing and freight conditions are not inferred."),
            ("Functional set", "The source records locker doors, components for changing size and function, and a two-tier storage cabinet for smaller items."),
            ("Project scope boundary", "The first-person source narrative records designing a complete mini-storage unit and developing its components. Formal contract division, supply scope and legal role require project-document confirmation."),
            ("Outcome and publication boundary", "The source records that the mini-storage facility opened and that the owner could duplicate the original design in other cities. Client name, date, final store count, quantity and authorization are not published."),
        ],
        "faq": [
            ("What kind of project is this relevant to?", "It is relevant to modular storage units, knock-down structures, multi-site replication and commercial spaces that combine multiple metal components. Confirm final dimensions and load requirements from drawings and samples."),
            ("What should I share for a similar development?", "Share unit dimensions, door and lock requirements, functional variants, quantity, site conditions, transport approach, target timing and drawings or an existing sample."),
        ],
        "cta": "Discuss modular storage and metal structure needs",
        "boundary": "This is an anonymous project record. Client name, date, formal quantity, final delivery location, price, contract division and publication authorization require case-by-case confirmation.",
        "related": ("Custom metal parts", "custom-metal-parts", "Modular fixtures", "modular-fixtures"),
    },
    "jp": {
        "lang": "ja",
        "title": "匿名都市型セルフストレージのモジュール事例",
        "description": "匿名の都市型セルフストレージ事例。複製可能なモジュール、ノックダウン構造、金属部品の組み合わせを記録します。",
        "nav": ("ホーム", "製品", "用途事例", "相談を送る"),
        "need_title": "都市型ストレージを再現可能なモジュールへ",
        "need": "原資料では、都市部で収納スペースの需要が増え、顧客が別の都市にも展開できるミニストレージのモジュールを希望したと記録されています。寸法、機能、輸送、将来のバリエーションを一体で検討する必要がありました。",
        "record_title": "原資料で確認できる内容",
        "record": [
            ("モジュールと規模", "完全なミニストレージユニットと50点を超える部品が記録されています。標準ユニットは約3.4 m³とされ、追加部品でサイズと機能を変更できます。"),
            ("材料と仕上げ", "鋼板、鋼管、鋼線、およびカスタム粉体塗装の方向が原資料に記録されています。湿気と傷への配慮についても原文に記載があります。"),
            ("構造と輸送", "K/D（ノックダウン）構造を採用し、原資料では輸送コストを抑える考え方と結び付けています。正式な梱包・運送条件は推測しません。"),
            ("機能構成", "扉付き収納ユニット、サイズと機能を変更する部品、小物向けの2段収納キャビネットが記録されています。"),
            ("担当範囲の境界", "原資料の一人称記述には、ミニストレージユニット全体の設計と部品開発が含まれます。正式な契約分担、供給範囲、Big Fameの法的役割は案件資料で確認が必要です。"),
            ("成果と公開範囲", "ミニストレージが開業し、オーナーが元の設計を他都市にも複製できる状態になったと原資料に記録されています。顧客名、日付、拠点数、数量、公開許諾は掲載していません。"),
        ],
        "faq": [
            ("どのような相談に向いていますか？", "モジュール収納、ノックダウン構造、多拠点展開、複数の金属部品を組み合わせる商空間の相談に向いています。最終寸法と荷重は図面とサンプルで確認します。"),
            ("同様の開発で何を共有すればよいですか？", "ユニット寸法、扉と錠、機能バリエーション、数量、現場条件、輸送方法、希望時期、図面または既存サンプルをご共有ください。"),
        ],
        "cta": "モジュール収納と金属構造を相談する",
        "boundary": "匿名のプロジェクト記録です。顧客名、日付、正式数量、最終納品地、価格、契約分担、公開許諾は案件ごとに確認します。",
        "related": ("カスタム金属部品", "custom-metal-parts", "モジュール什器", "modular-fixtures"),
    },
}


def page(folder: str, d: dict) -> str:
    base = f"https://www.bigfame.co/{folder}/case-urban-storage"
    alternates = "".join(
        f'<link rel="alternate" hreflang="{hreflang}" href="https://www.bigfame.co/{locale}/case-urban-storage">'
        for hreflang, locale in (("zh-TW", "tw"), ("en", "en"), ("ja", "jp"))
    )
    article = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": d["title"], "description": d["description"], "image": IMAGE, "url": base}, ensure_ascii=False)
    breadcrumb = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"https://www.bigfame.co/{folder}/"}, {"@type": "ListItem", "position": 2, "name": d["nav"][2], "item": f"https://www.bigfame.co/{folder}/applications"}, {"@type": "ListItem", "position": 3, "name": d["title"], "item": base}]}, ensure_ascii=False)
    faq = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}, ensure_ascii=False)
    cards = "".join(f'<article class="location-card reveal"><h3>{html.escape(h)}</h3><p>{html.escape(b)}</p></article>' for h, b in d["record"])
    faqs = "".join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in d["faq"])
    rel_name_1, rel_slug_1, rel_name_2, rel_slug_2 = d["related"]
    contact = "contact?category=system_fixtures&role=designer"
    return f'''<!DOCTYPE html><html lang="{d["lang"]}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(d["description"], quote=True)}"><title>{html.escape(d["title"])} | Big Fame</title><link rel="canonical" href="{base}">{alternates}<link rel="stylesheet" href="../css/style.css"><script type="application/ld+json">{article}</script><script type="application/ld+json">{breadcrumb}</script><script type="application/ld+json">{faq}</script></head><body><header class="header"><div class="container header-inner"><a href="./" class="logo">BIG FAME</a><nav class="nav-menu"><a href="./" class="nav-link">{d["nav"][0]}</a><a href="products" class="nav-link">{d["nav"][1]}</a><a href="applications" class="nav-link active">{d["nav"][2]}</a><a href="{contact}" class="nav-link nav-cta">{d["nav"][3]}</a></nav></div></header><main><section class="hero"><div class="container hero-content reveal"><p class="hero-kicker">ANONYMOUS MODULAR STORAGE PROJECT</p><h1>{html.escape(d["title"])}</h1><p class="hero-description">{html.escape(d["description"])}</p><a class="btn btn-primary" href="{contact}">{html.escape(d["cta"])}</a></div></section><section class="section section-light"><div class="container grid-2"><div class="reveal"><img class="hero-image-main" src="../images/case-urban-storage.jpg" alt="{html.escape(d["title"], quote=True)}" loading="eager"></div><div class="location-card reveal"><span class="section-subtitle">THE DESIGN NEED</span><h2>{html.escape(d["need_title"])}</h2><p>{html.escape(d["need"])}</p></div></div></section><section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">PROJECT EVIDENCE</span><h2 class="section-title">{html.escape(d["record_title"])}</h2></div><div class="grid-3">{cards}</div><p class="section-note reveal">{html.escape(d["boundary"])}</p></div></section><section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">FAQ</h2></div><div class="grid-2">{faqs}</div></div></section><section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{html.escape(d["cta"])}</h2><p><a href="{rel_slug_1}">{html.escape(rel_name_1)}</a> · <a href="{rel_slug_2}">{html.escape(rel_name_2)}</a></p><a class="btn btn-primary" href="{contact}">{html.escape(d["nav"][3])}</a></div></div></section></main><footer class="footer"><div class="container footer-bottom"><p>© Big Fame IND. CORP.</p><a href="applications">{d["nav"][2]}</a></div></footer><script src="../js/main.js"></script></body></html>'''


for folder, data in DATA.items():
    (ROOT / folder / "case-urban-storage.html").write_text(page(folder, data), encoding="utf-8")
print("Generated three localized anonymous urban-storage case pages.")
