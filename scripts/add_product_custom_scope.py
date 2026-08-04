"""Add explicit, evidence-safe customization scope and a related case link."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SCOPE = {
    "optical-hooks": {
        "tw": ("客製範圍", "可從背板孔位、掛勾長度、安裝方向與表面處理需求開始確認；是否能客製依 SKU、圖面與樣品評估。"),
        "en": ("Customization scope", "Start with backing pitch, hook length, mounting direction and finish requirements; customization is assessed against the SKU, drawing and sample."),
        "jp": ("カスタム範囲", "背板ピッチ、フック長さ、取付方向、仕上げ条件から確認します。カスタム可否は SKU、図面、サンプルを基に判断します。"),
    },
    "slatwall-pegboard-accessories": {
        "tw": ("客製範圍", "可從槽板／洞洞板孔距、配件長度、安裝方向與表面處理需求開始確認；實際客製範圍依 SKU、圖面與樣品評估。"),
        "en": ("Customization scope", "Start with slatwall or pegboard pitch, accessory length, mounting direction and finish requirements; actual scope is assessed against the SKU, drawing and sample."),
        "jp": ("カスタム範囲", "スラットウォール／有孔ボードのピッチ、アクセサリー長さ、取付方向、仕上げ条件から確認します。範囲は SKU、図面、サンプルを基に判断します。"),
    },
}

CASE_LINK = {
    "tw": ('href="applications">應用場景</a>', 'href="applications">應用場景</a> · <a href="case-ivy-modular-system">相關系統開發案例</a>'),
    "en": ('href="applications">Applications</a>', 'href="applications">Applications</a> · <a href="case-ivy-modular-system">Related system development case</a>'),
    "jp": ('href="applications">用途</a>', 'href="applications">用途</a> · <a href="case-ivy-modular-system">関連するシステム開発事例</a>'),
}

for slug, localized in SCOPE.items():
    for lang, (heading, body) in localized.items():
        path = ROOT / lang / f"{slug}.html"
        text = path.read_text(encoding="utf-8")
        marker = '<p class="section-note reveal">'
        block = f'<article class="location-card reveal"><h3>{heading}</h3><p>{body}</p></article>'
        if text.count(marker) != 1:
            raise SystemExit(f"Expected one section-note marker in {path}")
        text = text.replace(marker, block + marker, 1)
        path.write_text(text, encoding="utf-8")

for lang, (old, new) in CASE_LINK.items():
    path = ROOT / lang / "custom-metal-parts.html"
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise SystemExit(f"Expected one applications link in {path}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")

print("Added customization scope to six localized product pages and a related case link to three custom-metal pages.")
