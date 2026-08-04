"""Add an evidence-safe commercial specification gate to all public product pages."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUGS = (
    "display-hooks",
    "optical-hooks",
    "anti-theft-hooks",
    "slatwall-pegboard-accessories",
    "price-tag-holders",
    "pos-displays",
    "modular-fixtures",
    "custom-metal-parts",
)

COPY = {
    "tw": {
        "subtitle": "SPECIFICATION GATE",
        "title": "採購與設計需要確認的規格欄位",
        "intro": "以下欄位是正式詢價前的共同確認框架；只有在對應 SKU、圖面、報價或樣品可核對時，才會形成正式規格。",
        "cards": [
            ("適用店型與系統", "依店型、背板／安裝系統、展示商品與現場條件確認。"),
            ("材質與表面處理", "依 SKU、圖面、報價與樣品確認材質牌號、顏色、表面處理與外觀。"),
            ("尺寸與承載條件", "尺寸、線徑、板厚、承載或固定方式依代表性圖面與專案條件確認。"),
            ("MOQ 與交期", "沒有所有產品共用的 MOQ 或交期；依型式、數量、材料、表面處理與專案確認。"),
            ("客製範圍", "可先提供尺寸、照片、圖面、數量與使用方式，再判斷改尺寸、材料、表面或結構的可行性。"),
            ("證據與正式資料", "代表性照片、圖面與案例用於初步判斷；正式 PDF、CAD、樣品與商業條件需依核准版本提供。"),
        ],
        "resource": "需要尺寸圖、CAD、材質或規格摘要？先查看技術資源，再提交詢問。",
        "resource_link": "technical-resources",
    },
    "en": {
        "subtitle": "SPECIFICATION GATE",
        "title": "Specification fields to confirm before sourcing",
        "intro": "These fields form the shared confirmation frame before a formal quotation. A field becomes a formal specification only when it is supported by the matching SKU, drawing, quotation or sample.",
        "cards": [
            ("Store format and system", "Confirm the store type, backing or mounting system, displayed product and site conditions."),
            ("Material and finish", "Confirm material grade, colour, finish and appearance against the SKU, drawing, quotation and sample."),
            ("Dimensions and load conditions", "Confirm dimensions, wire diameter, board thickness, load or fixing method against the representative drawing and project conditions."),
            ("MOQ and lead time", "There is no universal MOQ or lead time for every product; confirm by type, quantity, material, finish and project."),
            ("Customization scope", "Share dimensions, photos, drawings, quantity and use conditions so changes to size, material, finish or structure can be assessed."),
            ("Evidence and formal files", "Representative images, drawings and cases support initial evaluation; formal PDF, CAD, samples and commercial terms follow the approved version."),
        ],
        "resource": "Need dimension drawings, CAD, material or specification data? Review technical resources before starting an inquiry.",
        "resource_link": "technical-resources",
    },
    "jp": {
        "subtitle": "SPECIFICATION GATE",
        "title": "調達・設計前に確認する仕様項目",
        "intro": "正式見積の前に共通して確認する項目です。該当 SKU、図面、見積、サンプルで確認できた内容だけを正式仕様とします。",
        "cards": [
            ("店舗タイプとシステム", "店舗タイプ、背板・取付システム、展示商品、現場条件を確認します。"),
            ("材料と仕上げ", "材料グレード、色、仕上げ、外観は SKU、図面、見積、サンプルで確認します。"),
            ("寸法と荷重条件", "寸法、線径、板厚、荷重、固定方法は代表図面と案件条件で確認します。"),
            ("MOQ と納期", "全製品共通の MOQ・納期はありません。型式、数量、材料、仕上げ、案件条件で確認します。"),
            ("カスタム範囲", "寸法、写真、図面、数量、使用条件を共有いただき、サイズ、材料、仕上げ、構造変更の可否を判断します。"),
            ("証拠と正式資料", "代表写真、図面、事例は初期検討用です。正式な PDF、CAD、サンプル、商業条件は承認版に基づき提供します。"),
        ],
        "resource": "寸法図、CAD、材料、仕様概要が必要ですか。技術資料を確認してからお問い合わせください。",
        "resource_link": "technical-resources",
    },
}


def section(locale: str, clean: bool) -> str:
    c = COPY[locale]
    prefix = "../" if clean else ""
    cards = "".join(
        f'<article class="location-card reveal"><h3>{title}</h3><p>{body}</p></article>'
        for title, body in c["cards"]
    )
    return (
        f'<section class="section section-light" data-bf-spec-gate="1"><div class="container">'
        f'<div class="section-heading reveal"><span class="section-subtitle">{c["subtitle"]}</span>'
        f'<h2 class="section-title">{c["title"]}</h2><p>{c["intro"]}</p></div>'
        f'<div class="grid-3">{cards}</div>'
        f'<p class="section-note reveal">{c["resource"]} '
        f'<a href="{prefix}{c["resource_link"]}">{c["resource_link"]}</a></p></div></section>'
    )


for locale in COPY:
    for slug in SLUGS:
        for path in (ROOT / locale / f"{slug}.html", ROOT / locale / slug / "index.html"):
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            if 'data-bf-spec-gate="1"' in text:
                continue
            marker = '<section class="section section-light" data-bf-faq="1">'
            if marker not in text:
                marker = '<section class="section section-light" data-bf-ta-links="1">'
            if marker not in text:
                raise SystemExit(f"insert marker missing: {path}")
            clean = path.parent.name == slug
            text = text.replace(marker, section(locale, clean) + marker, 1)
            path.write_text(text, encoding="utf-8")
