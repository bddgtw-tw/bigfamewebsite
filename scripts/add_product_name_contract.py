"""Add the trilingual product-name contract to pages where it was missing."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
NAMES = {
    "optical-hooks": {
        "tw": ("中英日名稱：", "眼鏡展示掛鉤／Optical Display Hooks／メガネディスプレイフック"),
        "en": ("Product names:", "Optical Display Hooks／眼鏡展示掛鉤／メガネディスプレイフック"),
        "jp": ("名称：", "メガネディスプレイフック／Optical Display Hooks／眼鏡展示掛鉤"),
    },
    "slatwall-pegboard-accessories": {
        "tw": ("中英日名稱：", "槽板／洞洞板配件／Slatwall and Pegboard Accessories／スラットウォール・有孔ボード用金具"),
        "en": ("Product names:", "Slatwall and Pegboard Accessories／槽板／洞洞板配件／スラットウォール・有孔ボード用金具"),
        "jp": ("名称：", "スラットウォール・有孔ボード用金具／Slatwall and Pegboard Accessories／槽板／洞洞板配件"),
    },
    "custom-metal-parts": {
        "tw": ("中英日名稱：", "客製金屬零件／Custom Metal Parts／カスタム金属部品"),
        "en": ("Product names:", "Custom Metal Parts／客製金屬零件／カスタム金属部品"),
        "jp": ("名称：", "カスタム金属部品／Custom Metal Parts／客製金屬零件"),
    },
}

for slug, localized in NAMES.items():
    for language, (label, value) in localized.items():
        path = ROOT / language / f"{slug}.html"
        text = path.read_text(encoding="utf-8")
        paragraph = f'<p class="product-names reveal"><strong>{label}</strong> {value}</p>'
        pattern = re.compile(r'<p class="product-names reveal">.*?</p>', re.S)
        if pattern.search(text):
            text = pattern.sub(paragraph, text, count=1)
        else:
            marker = '<div class="product-visual reveal">'
            if marker not in text:
                marker = '<section class="section section-light">'
            if marker not in text:
                raise SystemExit(f"Product content marker missing: {path}")
            text = text.replace(marker, paragraph + marker, 1)
        path.write_text(text, encoding="utf-8")

print("Added trilingual product names to optical hooks, slatwall accessories and custom metal parts.")
