"""Add direct TA-entry navigation to the main product, application and service hubs."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COPY = {
    "tw": {
        "subtitle": "TA ENTRY",
        "title": "依你的工作角色進入",
        "intro": "不用先知道正確 SKU；從採購、設計或展示配件的工作問題開始。",
        "cards": [
            ("採購與商社", "比較產品、數量、MOQ、交期、包裝與交貨地。", "採購展示設備", "procurement"),
            ("店面設計與建築", "整理平面、立面、材質、CAD 與打樣需求。", "進入設計支援", "design-support"),
            ("VM 與展示配件", "尋找展示掛勾、槽板配件、價格條與 POS 零件。", "找展示掛勾與配件", "display-hooks"),
        ],
    },
    "en": {
        "subtitle": "TA ENTRY",
        "title": "Choose your work entry",
        "intro": "You do not need the exact SKU first. Start with the work problem: procurement, design or display hardware.",
        "cards": [
            ("Procurement & trading", "Compare products, quantity, MOQ, lead time, packing and delivery location.", "Enter procurement", "procurement"),
            ("Retail design & architecture", "Turn plans, elevations, materials, CAD and sampling needs into reviewable conditions.", "Enter design support", "design-support"),
            ("VM & display hardware", "Find display hooks, slatwall accessories, price-tag holders and POS parts.", "Find display hooks", "display-hooks"),
        ],
    },
    "jp": {
        "subtitle": "TA ENTRY",
        "title": "担当業務から入る",
        "intro": "正確なSKUを先に知る必要はありません。購買、設計、展示金具の課題から始められます。",
        "cards": [
            ("購買・商社", "製品、数量、MOQ、納期、梱包、納品地を比較します。", "購買相談へ", "procurement"),
            ("店舗設計・建築", "平面、立面、素材、CAD、試作の条件を整理します。", "設計サポートへ", "design-support"),
            ("VMD・展示金具", "ディスプレイフック、スラットウォール金具、値札、POS部品を探します。", "展示フックを見る", "display-hooks"),
        ],
    },
}


def render(lang: str) -> str:
    c = COPY[lang]
    cards = "".join(
        f'<article class="location-card reveal"><h3>{heading}</h3><p>{body}</p><a class="case-card-link" href="{href}">{label}</a></article>'
        for heading, body, label, href in c["cards"]
    )
    return (
        f'<section class="section section-light" data-bf-ta-entry="1"><div class="container">'
        f'<div class="section-heading reveal"><span class="section-subtitle">{c["subtitle"]}</span>'
        f'<h2 class="section-title">{c["title"]}</h2><p class="section-note">{c["intro"]}</p></div>'
        f'<div class="grid-3">{cards}</div></div></section>\n'
    )


def main() -> None:
    changed = 0
    for lang in COPY:
        block = render(lang)
        for page in ("products.html", "applications.html", "services.html"):
            path = ROOT / lang / page
            text = path.read_text(encoding="utf-8")
            if 'data-bf-ta-entry="1"' in text:
                continue
            marker = '<section class="section section-light" data-bf-faq="1">'
            if page == "applications.html":
                marker = '<footer class="footer">'
            if marker not in text:
                raise SystemExit(f"FAQ marker not found: {path}")
            path.write_text(text.replace(marker, block + marker, 1), encoding="utf-8")
            changed += 1
    print(f"Updated {changed} hub pages.")


if __name__ == "__main__":
    main()
