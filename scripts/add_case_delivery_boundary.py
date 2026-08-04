"""Add an explicit delivery/destination evidence boundary to the 3C case."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {
    "tw": ("交付地／目的地", "來源摘要指向台北首店；最終交付地、包裝與跨城市部署條件未公開，需依新案確認。"),
    "en": ("Delivery / destination", "The source brief points to a first Taipei store; final delivery location, packing and cross-city deployment conditions are not published and require a new-project review."),
    "jp": ("納品先・配送条件", "元資料は台北の初店舗を示しています。最終納品先、梱包、他都市展開の条件は公開されておらず、新規案件ごとに確認します。"),
}

for lang, (heading, body) in FIELDS.items():
    path = ROOT / lang / "case-modular-3c-store.html"
    text = path.read_text(encoding="utf-8")
    if lang == "tw":
        marker = '<h3>數量／交期</h3>'
    elif lang == "en":
        marker = '<h3>Quantity / lead time</h3>'
    else:
        marker = '<h3>数量・納期</h3>'
    if text.count(marker) != 1:
        raise SystemExit(f"Expected one quantity marker in {path}")
    block = f'<h3>{heading}</h3><p>{body}</p>'
    text = text.replace(marker, block + marker, 1)
    path.write_text(text, encoding="utf-8")

print("Added delivery/destination evidence boundaries to the three localized 3C case pages.")
