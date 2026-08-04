"""Add evidence-safe FAQ sections to multilingual hub pages."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]

FAQS = {
    "tw": {
        "index": [("Big Fame 可以協助哪些展示設備需求？", "可以從店面展示設備、展示掛勾、POS 展示、模組化什器與客製金屬零件開始整理；正式產品、規格與交付範圍依專案確認。"), ("可以從照片或 CAD 開始嗎？", "可以。可先提供照片、PDF、DWG、DXF、STEP、商品尺寸、數量、目標日期與交貨地，再依產品與圖面確認。"), ("MOQ 與交期是否有通用答案？", "目前不公開適用所有產品的通用 MOQ 或交期；需依 SKU、材料、數量、排程與交貨地確認。")],
        "about": [("Big Fame 在展示設備專案中扮演什麼角色？", "Big Fame 可協助整理需求、配對製造夥伴、確認圖面與樣品、追蹤生產及協調品質、包裝與出口；正式承擔範圍依專案文件確認。"), ("可以處理哪些材料方向？", "金屬、木材、壓克力與複合材質可作為討論方向；正式材質牌號、加工與供應範圍需依圖面、樣品與專案確認。")],
        "products": [("應該從哪一類產品開始？", "先提供店型、展示商品、安裝系統、尺寸與數量，再比較展示掛勾、槽板配件、POS、模組化展示架或客製金屬零件。"), ("產品頁上的規格都適用所有型號嗎？", "不適用。公開頁面只呈現已核對的代表性證據；正式 SKU、材質、尺寸、表面處理、MOQ 與交期需逐項確認。"), ("可以索取 CAD 或尺寸圖嗎？", "可以先提供產品或系統、圖面／照片、數量、時程與交貨地，再依 SKU、版本與專案條件確認可提供的檔案。")],
        "services": [("要如何開始一個展示設備專案？", "請提供店型、展示商品、安裝系統、圖面或照片、數量、目標時程與交貨地，先建立可確認的需求範圍。"), ("Big Fame 是否直接承諾固定交期？", "不公開所有產品共用的固定交期；樣品、生產、包裝與出貨時程需依圖面版本、材料、數量、排程與交貨地確認。")],
    },
    "en": {
        "index": [("What display-equipment needs can Big Fame support?", "Start with retail fixtures, display hooks, POS displays, modular fixtures or custom metal parts; formal products, specifications and delivery scope are confirmed by project."), ("Can we start with a photo or CAD file?", "Yes. Share photos, PDF, DWG, DXF, STEP, merchandise dimensions, quantity, target timing and destination so the product and drawing can be reviewed."), ("Is there one MOQ or lead time for every product?", "No universal MOQ or lead time is published. Confirm by SKU, material, quantity, schedule and destination.")],
        "about": [("What role can Big Fame play in a display-equipment project?", "Big Fame can help scope requirements, match manufacturing partners, review drawings and samples, follow production and coordinate quality, packing and export; formal scope is confirmed by project documents."), ("Which material directions can be discussed?", "Metal, wood, acrylic and composite materials can be discussed as directions; formal grades, processes and supply scope require drawing, sample and project confirmation.")],
        "products": [("Which product category should we start with?", "Share the store format, merchandise, mounting system, dimensions and quantity, then compare display hooks, slatwall accessories, POS, modular fixtures or custom metal parts."), ("Do the specifications on a product page apply to every model?", "No. Public pages present documented or representative evidence; formal SKU, material, dimensions, finish, MOQ and lead time require confirmation."), ("Can we request CAD or dimension drawings?", "Yes. Share the product or system, drawings or photos, quantity, timing and destination; available files are confirmed by SKU, revision and project conditions.")],
        "services": [("How should a display-equipment project start?", "Share the store format, merchandise, mounting system, drawings or photos, quantity, target timing and destination to establish a reviewable requirement scope."), ("Does Big Fame promise one fixed lead time?", "No universal lead time is published. Sampling, production, packing and shipment timing are confirmed by drawing revision, material, quantity, schedule and destination.")],
    },
    "jp": {
        "index": [("どのような店舗什器を相談できますか？", "店舗什器、ディスプレイフック、POS什器、モジュール什器、カスタム金属部品から相談できます。正式な製品、仕様、納品範囲は案件ごとに確認します。"), ("写真やCADから相談できますか？", "はい。写真、PDF、DWG、DXF、STEP、商品寸法、数量、希望時期、納品地を共有し、製品と図面を確認します。"), ("全製品共通のMOQや納期はありますか？", "全製品共通のMOQや納期は公開していません。SKU、材料、数量、工程、納品地で確認します。")],
        "about": [("Big Fameは什器案件で何を担当しますか？", "要件整理、製造パートナーとの調整、図面・サンプル確認、生産フォロー、品質・梱包・輸出の調整を相談できます。正式な範囲は案件資料で確認します。"), ("どの材料を相談できますか？", "金属、木材、アクリル、複合材を方向として相談できます。正式な材料、加工、供給範囲は図面、サンプル、案件条件で確認します。")],
        "products": [("どの製品から相談すればよいですか？", "業態、商品、取付システム、寸法、数量を共有し、ディスプレイフック、スラットウォール金具、POS、モジュール什器、カスタム金属部品を比較します。"), ("製品ページの仕様は全型式に共通ですか？", "いいえ。公開ページは確認済みまたは代表的な証拠を示します。正式なSKU、材料、寸法、仕上げ、MOQ、納期は確認が必要です。"), ("CADや寸法図を依頼できますか？", "製品またはシステム、図面・写真、数量、希望時期、納品地を共有してください。提供可能な資料はSKU、版、案件条件で確認します。")],
        "services": [("什器案件は何から始めますか？", "業態、商品、取付システム、図面または写真、数量、希望時期、納品地を共有し、確認可能な要件範囲を整理します。"), ("固定納期を約束できますか？", "全製品共通の固定納期は公開していません。図面の版、材料、数量、工程、納品地で試作・生産・梱包・出荷時期を確認します。")],
    },
}


def add_faq(path: Path, items: list[tuple[str, str]], lang: str) -> None:
    text = path.read_text(encoding="utf-8")
    if '"@type":"FAQPage"' in text or '"@type": "FAQPage"' in text:
        return
    schema = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}, ensure_ascii=False)
    visible = "".join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in items)
    heading = {"tw": "常見問題", "en": "Frequently asked questions", "jp": "よくある質問"}[lang]
    section = f'<section class="section section-light" data-bf-faq="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">{heading}</h2></div><div class="grid-3">{visible}</div></div></section>'
    if "</head>" not in text or ("</main>" not in text and "<footer" not in text):
        raise SystemExit(f"Missing injection marker: {path}")
    text = text.replace("</head>", f'<script type="application/ld+json">{schema}</script></head>', 1)
    if "</main>" in text:
        text = text.replace("</main>", section + "</main>", 1)
    else:
        text = text.replace("<footer", section + "<footer", 1)
    path.write_text(text, encoding="utf-8")


for lang, pages in FAQS.items():
    for slug, items in pages.items():
        add_faq(ROOT / lang / f"{slug}.html", items, lang)
print("Added evidence-safe FAQ sections to 12 multilingual hub pages.")
