"""Connect TA entry pages to evidence-backed product and case routes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "tw": {
        "procurement": [
            ('href="modular-fixtures">模組化展示架</a>。</p>', 'href="modular-fixtures">模組化展示架</a>、<a href="cosmetic-organizers">化妝品收納展示</a>。</p>'),
            ('<a href="case-eyewear-2016">眼鏡零售展示案例</a>，再', '<a href="case-eyewear-2016">眼鏡零售展示案例</a>；也可查看<a href="case-japanese-wine-bar">酒吧酒類展示案例</a>，再'),
        ],
        "design-support": [
            ('href="pos-displays">POS展示設備</a>。</p>', 'href="pos-displays">POS展示設備</a>、<a href="cosmetic-organizers">化妝品收納展示</a>。</p>'),
            ('可先查看<a href="case-eyewear-2016">眼鏡零售展示案例</a>，再', '可先查看<a href="case-eyewear-2016">眼鏡零售展示案例</a>與<a href="case-japanese-wine-bar">酒吧展示案例</a>，再'),
        ],
    },
    "en": {
        "procurement": [
            ('href="modular-fixtures">modular fixtures</a>.', 'href="modular-fixtures">modular fixtures</a> or <a href="cosmetic-organizers">cosmetic organizers</a>.'),
            ('<a href="case-eyewear-2016">eyewear retail display case</a>, then', '<a href="case-eyewear-2016">eyewear retail display case</a> or the <a href="case-japanese-wine-bar">wine-bar display case</a>, then'),
        ],
        "design-support": [
            ('href="pos-displays">POS displays</a>.</p>', 'href="pos-displays">POS displays</a> and <a href="cosmetic-organizers">cosmetic organizers</a>.</p>'),
            ('Review the <a href="case-eyewear-2016">eyewear retail display case</a>, then', 'Review the <a href="case-eyewear-2016">eyewear retail display case</a> and the <a href="case-japanese-wine-bar">wine-bar display case</a>, then'),
        ],
    },
    "jp": {
        "procurement": [
            ('href="modular-fixtures">モジュール什器</a>。</p>', 'href="modular-fixtures">モジュール什器</a>、<a href="cosmetic-organizers">化粧品オーガナイザー</a>。</p>'),
            ('<a href="case-eyewear-2016">アイウェア店舗ディスプレイ事例</a>から確認し', '<a href="case-eyewear-2016">アイウェア店舗ディスプレイ事例</a>、<a href="case-japanese-wine-bar">ワインバー展示事例</a>から確認し'),
        ],
        "design-support": [
            ('href="pos-displays">POS什器</a>。</p>', 'href="pos-displays">POS什器</a>、<a href="cosmetic-organizers">卓上化粧品オーガナイザー</a>。</p>'),
            ('<a href="case-eyewear-2016">アイウェア店舗ディスプレイ事例</a>を確認し', '<a href="case-eyewear-2016">アイウェア店舗ディスプレイ事例</a>と<a href="case-japanese-wine-bar">ワインバー展示事例</a>を確認し'),
        ],
    },
}

for lang, pages in REPLACEMENTS.items():
    for slug, replacements in pages.items():
        path = ROOT / lang / f"{slug}.html"
        text = path.read_text(encoding="utf-8")
        for old, new in replacements:
            if text.count(old) != 1:
                raise SystemExit(f"Expected one anchor in {path}: {old}")
            text = text.replace(old, new, 1)
        path.write_text(text, encoding="utf-8")

print("Connected localized procurement and design-support entries to cosmetic and wine-bar evidence routes.")
