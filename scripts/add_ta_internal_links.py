"""Add missing high-intent product links to the trilingual TA entry pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPLACEMENTS = {
    "tw/procurement.html": (
        '<a href="cosmetic-organizers">化妝品收納展示</a>。',
        '<a href="cosmetic-organizers">化妝品收納展示</a>、<a href="custom-metal-parts">客製金屬零件</a>。',
    ),
    "en/procurement.html": (
        '<a href="cosmetic-organizers">cosmetic organizers</a>.',
        '<a href="cosmetic-organizers">cosmetic organizers</a> or <a href="custom-metal-parts">custom metal parts</a>.',
    ),
    "jp/procurement.html": (
        '<a href="cosmetic-organizers">化粧品オーガナイザー</a>。',
        '<a href="cosmetic-organizers">化粧品オーガナイザー</a>、<a href="custom-metal-parts">カスタム金属部品</a>。',
    ),
    "tw/display-hooks.html": (
        '<a href="optical-hooks">眼鏡展示掛勾</a>、<a href="slatwall-pegboard-accessories">槽板／洞洞板配件</a>',
        '<a href="optical-hooks">眼鏡展示掛勾</a>、<a href="anti-theft-hooks">防盜展示掛勾</a>、<a href="slatwall-pegboard-accessories">槽板／洞洞板配件</a>',
    ),
    "en/display-hooks.html": (
        '<a href="optical-hooks">Optical Display Hooks</a>, <a href="slatwall-pegboard-accessories">Slatwall / Pegboard Accessories</a>',
        '<a href="optical-hooks">Optical Display Hooks</a>, <a href="anti-theft-hooks">Anti-theft Display Hooks</a>, <a href="slatwall-pegboard-accessories">Slatwall / Pegboard Accessories</a>',
    ),
    "jp/display-hooks.html": (
        '<a href="optical-hooks">眼鏡用ディスプレイフック</a>、<a href="slatwall-pegboard-accessories">スラットウォール／有孔ボード用アクセサリー</a>',
        '<a href="optical-hooks">眼鏡用ディスプレイフック</a>、<a href="anti-theft-hooks">防犯ディスプレイフック</a>、<a href="slatwall-pegboard-accessories">スラットウォール／有孔ボード用アクセサリー</a>',
    ),
}

for relative, (old, new) in REPLACEMENTS.items():
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected one replacement in {relative}, found {count}")
    path.write_text(text.replace(old, new), encoding="utf-8")
    print(f"UPDATED {relative}")
