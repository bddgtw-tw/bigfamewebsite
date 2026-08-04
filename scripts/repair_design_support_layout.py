"""Repair the design-support FAQ layout and add a direct technical-resources route."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLOW = {
    "tw": ("協作流程：場景摘要 → 資料盤點 → 規格確認 → 樣品／報價討論 → 交付條件確認。", "技術與 CAD 資源"),
    "en": ("Collaboration flow: scene brief → source review → specification confirmation → sample or quotation discussion → delivery conditions.", "Technical and CAD resources"),
    "jp": ("流れ：場面概要 → 資料確認 → 仕様確認 → サンプル・見積 → 納品条件確認。", "技術・CAD資料"),
}

for locale, (flow, label) in FLOW.items():
    path = ROOT / locale / "design-support.html"
    text = path.read_text(encoding="utf-8")
    faq_start = text.index('<section class="section section-light" data-bf-faq="1">')
    dark_start = text.index('<section class="section section-dark">', faq_start)
    dark_end = text.index('</section>', dark_start) + len('</section>')
    dark = text[dark_start:dark_end]
    moved = []
    marker = '<article class="location-card reveal">'
    while marker in dark:
        begin = dark.index(marker)
        end = dark.index('</article>', begin) + len('</article>')
        moved.append(dark[begin:end])
        dark = dark[:begin] + dark[end:]
    if moved:
        faq = text[faq_start:dark_start]
        faq_end = faq.rfind('</div></div></section>')
        if faq_end < 0:
            raise SystemExit(f"FAQ closing marker missing: {path}")
        faq = faq[:faq_end] + ''.join(moved) + faq[faq_end:]
        text = text[:faq_start] + faq + dark + text[dark_end:]
    if 'technical-resources' not in text:
        old = f"{flow}</p>"
        new = f'{flow} · <a href="technical-resources">{label}</a></p>'
        if old not in text:
            raise SystemExit(f"flow marker missing: {path}")
        text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")
