"""Add clear TA routes to product and case pages in all three languages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = {
    "display-hooks", "optical-hooks", "anti-theft-hooks",
    "slatwall-pegboard-accessories", "price-tag-holders", "pos-displays",
    "modular-fixtures", "custom-metal-parts",
}
CASES = {
    "case-eyewear-2016", "case-apparel-2016", "case-boutique-hotel-furniture",
    "case-japanese-wine-bar", "case-urban-storage", "case-ivy-modular-system",
    "case-modular-3c-store", "case-page-cosmetic-organizer",
}
LABELS = {
    "tw": (
        "依需求進入：",
        "採購入口", "設計支援", "技術與 CAD 資源",
    ),
    "en": (
        "Choose a route: ",
        "Procurement", "Design support", "Technical resources",
    ),
    "jp": (
        "目的別に進む：",
        "購買相談", "設計サポート", "技術資料・CAD",
    ),
}


def route_prefix(path: Path) -> str:
    return "../" if path.parent.name in {"products", "applications"} or path.name == "index.html" else ""


def is_target(path: Path) -> bool:
    if path.name == "index.html":
        slug = path.parent.name
    else:
        slug = path.stem
    return slug in PRODUCTS or slug in CASES


def main() -> None:
    changed = 0
    for language in LABELS:
        for path in (ROOT / language).rglob("*.html"):
            if not is_target(path):
                continue
            text = path.read_text(encoding="utf-8")
            if 'data-bf-ta-links="1"' in text:
                continue
            prefix = "../" if path.name == "index.html" else ""
            lead, procurement, design, technical = LABELS[language]
            block = (
                f'<section class="section section-light" data-bf-ta-links="1">'
                f'<div class="container"><p class="section-note reveal">{lead}'
                f'<a href="{prefix}procurement">{procurement}</a> · '
                f'<a href="{prefix}design-support">{design}</a> · '
                f'<a href="{prefix}technical-resources">{technical}</a></p></div></section>'
            )
            marker = '<section class="section section-dark">'
            if text.count(marker) != 1:
                raise SystemExit(f"Expected one CTA section in {path}, found {text.count(marker)}")
            path.write_text(text.replace(marker, block + marker, 1), encoding="utf-8")
            changed += 1
            print(f"UPDATED {path.relative_to(ROOT)}")
    print(f"TA_LINK_PAGES={changed}")


if __name__ == "__main__":
    main()
