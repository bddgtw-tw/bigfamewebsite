"""Keep apparel evidence and store-type pages available at flat and clean routes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

for lang in ("tw", "en", "jp"):
    case_flat = ROOT / lang / "case-apparel-2016.html"
    entry_flat = ROOT / lang / "apparel-store-fixtures.html"
    case = case_flat.read_text(encoding="utf-8")
    source_marker = '<section class="section section-light"><div class="container grid-2">'
    source_replacement = '<section class="section section-light" data-bf-source-record="1"><div class="container grid-2">'
    if source_marker in case and 'data-bf-source-record="1"' not in case:
        case = case.replace(source_marker, source_replacement, 1)
    boundary_marker = '<section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">EVIDENCE BOUNDARY</span>'
    boundary_replacement = '<section class="section section-light" data-bf-case-contract="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">EVIDENCE BOUNDARY</span>'
    if boundary_marker in case and 'data-bf-case-contract="1"' not in case:
        case = case.replace(boundary_marker, boundary_replacement, 1)
    required_case = ('data-bf-source-record="1"', 'data-bf-case-contract="1"', 'data-bf-faq="1"', 'case-apparel-2016')
    missing = [marker for marker in required_case if marker not in case]
    if missing:
        raise RuntimeError(f"{lang} apparel case missing: {missing}")
    case_flat.write_text(case, encoding="utf-8", newline="\n")
    entry = entry_flat.read_text(encoding="utf-8")
    if 'data-bf-faq="1"' not in entry:
        raise RuntimeError(f"{lang} apparel entry missing FAQ marker")
    entry_flat.write_text(entry, encoding="utf-8", newline="\n")
    (ROOT / lang / "case-apparel-2016").mkdir(exist_ok=True)
    (ROOT / lang / "apparel-store-fixtures").mkdir(exist_ok=True)
    (ROOT / lang / "case-apparel-2016" / "index.html").write_text(case, encoding="utf-8", newline="\n")
    (ROOT / lang / "apparel-store-fixtures" / "index.html").write_text(entry, encoding="utf-8", newline="\n")

print("Synchronized apparel case and store-entry flat/clean routes for tw/en/jp")
