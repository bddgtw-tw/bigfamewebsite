"""Generate the first English and Japanese TA entry pages from one content map."""

from pathlib import Path
import html
import json


ROOT = Path(__file__).resolve().parents[1]

CONTENT = {
    "en": {
        "lang": "en",
        "home": "Home", "products": "Products", "cases": "Applications", "cta": "Start an inquiry",
        "contact": "contact", "role_buyer": "buyer", "role_designer": "designer",
        "pages": {
            "procurement": {
                "title": "Retail Display Equipment Sourcing in Taiwan | Big Fame",
                "description": "A sourcing entry for buyers, trading companies and retail display procurement teams looking for Taiwan display fixture manufacturing, project integration and export coordination.",
                "kicker": "FOR BUYERS / SOURCING TEAMS",
                "h1": "Retail display sourcing is more than finding a factory",
                "lede": "Big Fame helps turn supplier comparison into verifiable specifications, samples, production checkpoints and delivery coordination.",
                "cta": "Share your sourcing requirements",
                "sub": "What buyers need to know",
                "h2": "Reduce the back-and-forth from the first inquiry",
                "cards": [("Can it be made?", "Start with display fixtures, display hardware, POS displays and custom metal parts, then confirm drawings and materials."), ("How do we verify it?", "Use requirement scoping, sampling or tooling, production and quality checkpoints to keep the project traceable."), ("Can it be delivered?", "Discuss quantity, packing, destination and export conditions. Delivery commitments follow the confirmed project scope.")],
                "next": "Start with one SKU or one store format",
            },
            "design-support": {
                "title": "Retail Space Design and Display Fixture Engineering | Big Fame",
                "description": "A design collaboration entry for retail designers, architects and VM teams working on display fixtures, materials, drawings, sampling and production.",
                "kicker": "FOR DESIGNERS / ARCHITECTS / VM",
                "h1": "Turn design intent into manufacturable display equipment",
                "lede": "Work with the manufacturing side to confirm structure, hardware, finishes, sampling and production conditions for retail spaces.",
                "cta": "Submit drawings and design requirements",
                "sub": "Design collaboration scope",
                "h2": "Move beyond a simple yes-or-no feasibility answer",
                "cards": [("Display structure", "Review modular fixtures, shelves, hanging and store-format requirements against the product flow."), ("Material integration", "Discuss metal, wood, acrylic and lighting directions against the actual drawings and samples."), ("Engineering translation", "Turn PDF, DWG, DXF, STEP or concept images into questions for sampling and production.")],
                "next": "Concept drawings are enough to begin",
            },
            "display-hooks": {
                "title": "Display Hooks and Retail Merchandising Hardware | Big Fame",
                "description": "B2B sourcing entry for display hooks, optical hooks, anti-theft hooks, slatwall and pegboard accessories, price tag holders and retail merchandising hardware.",
                "kicker": "DISPLAY HARDWARE / B2B SOURCING",
                "h1": "Display hooks and merchandising accessories",
                "lede": "From standard accessories to drawing-based development, clarify what needs to hang, how it is fixed and how it will be produced.",
                "cta": "Ask for a matching recommendation",
                "sub": "Start with the display situation",
                "h2": "Find the right accessory by how it will be used",
                "cards": [("Slatwall and pegboard hooks", "For slatwall, pegboard, square tubing and modular display structures; fixing and load requirements need confirmation."), ("Optical and small-product display", "Confirm product dimensions, access, visibility and anti-theft requirements before selecting the hook direction."), ("Price tag and connection parts", "Discuss price tags, holders, brackets and connectors together with the display system materials and finish.")],
                "next": "You can start with a photo if you do not know the name",
            },
        },
    },
    "jp": {
        "lang": "ja",
        "home": "ホーム", "products": "製品", "cases": "導入事例", "cta": "お問い合わせ",
        "contact": "contact", "role_buyer": "buyer", "role_designer": "designer",
        "pages": {
            "procurement": {"title": "店舗什器の調達・台湾メーカー | Big Fame", "description": "店舗什器、ディスプレイ金具、POS什器の調達と台湾での製造・輸出連携を検討するバイヤー向けの入口です。", "kicker": "FOR BUYERS / SOURCING TEAMS", "h1": "店舗什器の調達を、工場探しだけで終わらせない", "lede": "要件、図面、サンプル、量産、品質確認、出荷まで、確認すべき工程を整理して進めます。", "cta": "調達要件を相談する", "sub": "バイヤーが確認したいこと", "h2": "最初の問い合わせから往復を減らす", "cards": [("製造できるか", "店舗什器、ディスプレイ金具、POS什器、カスタム金属部品について図面と材質を確認します。"), ("どう検証するか", "要件整理、サンプルまたは治具、量産、品質確認の節目を共有します。"), ("納品できるか", "数量、梱包、納入先、輸出条件を確認し、確定した条件で納期を検討します。")], "next": "まずは1 SKU、または1店舗から"},
            "design-support": {"title": "店舗設計・什器設計の製造連携 | Big Fame", "description": "店舗設計者、建築家、VMチーム向け。什器構造、金具、材質、図面、試作と量産条件を製造側と確認します。", "kicker": "FOR DESIGNERS / ARCHITECTS / VM", "h1": "設計意図を、製造できる店舗什器へ", "lede": "構造、金具、仕上げ、試作、量産条件を、図面と実際の店舗計画に合わせて確認します。", "cta": "図面と設計要件を送る", "sub": "設計連携の範囲", "h2": "できる・できないだけで終わらせない", "cards": [("什器構造", "モジュール什器、棚、ハンギング、店舗動線と商品陳列を確認します。"), ("異素材の統合", "金属、木、アクリル、照明の方向を図面とサンプルで検討します。"), ("図面の翻訳", "PDF、DWG、DXF、STEPや参考写真を試作・量産の確認事項に整理します。")], "next": "概念図から相談できます"},
            "display-hooks": {"title": "店舗用ディスプレイフック・陳列金具 | Big Fame", "description": "ディスプレイフック、メガネフック、防犯フック、スラットウォール・有孔ボード用金具、プライスレールを探すB2B向けページです。", "kicker": "DISPLAY HARDWARE / B2B SOURCING", "h1": "ディスプレイフックと陳列アクセサリー", "lede": "標準アクセサリーから図面ベースの開発まで、何を掛けるか、どう固定するか、どう量産するかを整理します。", "cta": "適合する金具を相談する", "sub": "使用シーンから探す", "h2": "用途から適切なアクセサリーへ", "cards": [("スラットウォール・有孔ボード", "スラットウォール、有孔ボード、角パイプなどに使う金具。固定方法と荷重は確認が必要です。"), ("メガネ・小物ディスプレイ", "商品の寸法、取り出しやすさ、視認性、防犯条件を確認します。"), ("プライスレール・接続部品", "プライスホルダー、ブラケット、接続部品を什器の材質と仕上げに合わせて検討します。")], "next": "名称が分からなくても写真から相談できます"},
        },
    },
}


def render(lang: str, slug: str, data: dict, cfg: dict) -> str:
    base = f"https://www.bigfame.co/{lang}/{slug}"
    links = "".join([
        f'<link rel="alternate" hreflang="{hreflang}" href="https://www.bigfame.co/{folder}/{slug}">' for hreflang, folder in (("en", "en"), ("ja", "jp"), ("zh-TW", "tw"))
    ])
    cards = "".join(f'<article class="location-card reveal"><h3>{html.escape(h)}</h3><p>{html.escape(p)}</p></article>' for h, p in data["cards"])
    role = cfg["role_buyer"] if slug == "procurement" or slug == "display-hooks" else cfg["role_designer"]
    category = "display_hardware" if slug == "display-hooks" else ("integration" if slug == "procurement" else "system_fixtures")
    contact = f'{cfg["contact"]}?role={role}&category={category}'
    return f'''<!DOCTYPE html>
<html lang="{cfg["lang"]}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{html.escape(data["description"], quote=True)}"><title>{html.escape(data["title"])}</title><link rel="canonical" href="{base}">{links}<link rel="stylesheet" href="../css/style.css"><script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"Service","@id":base+"#service","name":data["title"],"serviceType":data["title"],"description":data["description"],"url":base,"provider":{"@type":"Organization","name":"Big Fame IND. CORP.","url":"https://www.bigfame.co/"}}, ensure_ascii=False)}</script></head>
<body><header class="header"><div class="container header-inner"><a href="./" class="logo">BIG FAME</a><nav class="nav-menu"><a href="./" class="nav-link">{cfg["home"]}</a><a href="products" class="nav-link">{cfg["products"]}</a><a href="applications" class="nav-link">{cfg["cases"]}</a><a href="{contact}" class="nav-link nav-cta">{cfg["cta"]}</a></nav></div></header><main><section class="hero"><div class="container hero-content reveal"><p class="hero-kicker">{html.escape(data["kicker"])}</p><h1>{html.escape(data["h1"])}</h1><p class="hero-description">{html.escape(data["lede"])}</p><a class="btn btn-primary" href="{contact}">{html.escape(data["cta"])}</a></div></section><section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">{html.escape(data["sub"])}</span><h2 class="section-title">{html.escape(data["h2"])}</h2></div><div class="grid-3">{cards}</div></div></section><section class="section section-dark"><div class="container"><div class="cta-block reveal"><h2>{html.escape(data["next"])}</h2><a class="btn btn-primary" href="{contact}">{html.escape(data["cta"])}</a></div></div></section></main><footer class="footer"><div class="container footer-bottom"><p>© 1988-2026 Big Fame IND. CORP.</p><a href="{contact}">{html.escape(cfg["cta"])}</a></div></footer><script src="../js/main.js"></script></body></html>'''


for lang, cfg in CONTENT.items():
    for slug, data in cfg["pages"].items():
        (ROOT / lang / f"{slug}.html").write_text(render(lang, slug, data, cfg), encoding="utf-8")
