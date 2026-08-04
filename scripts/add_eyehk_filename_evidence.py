"""Expose representative EYEHK identifiers found in raw image filenames."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = {
    "tw": ("原始照片檔名中的代表識別", "原始照片檔名可見 EYEHK-010B、EYEHK-010C、EYEHK-010W、EYEHK-020B、EYEHK-020C 與 EYEHK-020W。這些是照片檔名中的識別線索，不把 B／C／W 推定為正式顏色代碼或目前可供應 SKU。"),
    "en": ("Representative identifiers in raw image filenames", "Raw image filenames include EYEHK-010B, EYEHK-010C, EYEHK-010W, EYEHK-020B, EYEHK-020C and EYEHK-020W. These are filename identifiers only; do not infer formal colour codes or current availability from B / C / W."),
    "jp": ("原画像ファイル名で確認できる識別", "原画像ファイル名には EYEHK-010B、EYEHK-010C、EYEHK-010W、EYEHK-020B、EYEHK-020C、EYEHK-020W が見られます。ファイル名の識別情報であり、B／C／W を正式な色コードや現行供給 SKU と推定しません。"),
}

for lang, (title, body) in DATA.items():
    card = f'<article class="location-card reveal"><h3>{title}</h3><p>{body}</p></article>'
    for rel in (f"{lang}/optical-hooks.html", f"{lang}/optical-hooks/index.html"):
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        if title in text:
            continue
        section_re = re.compile(r'(<section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">DRAWING VARIANTS</span>.*?<div class="grid-2">.*?)(</div><p class="section-note reveal">)', re.S)
        match = section_re.search(text)
        if not match:
            raise SystemExit(f"drawing variant section not found: {path}")
        text = text[:match.start()] + match.group(1) + card + match.group(2) + text[match.end():]
        path.write_text(text, encoding="utf-8", newline="")
