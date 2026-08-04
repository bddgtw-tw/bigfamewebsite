"""Replace non-product-specific MOQ and timing baselines with evidence-safe gates."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPLACEMENTS = {
    "tw": {
        "通用專案討論基準：客製五金通常 500 pcs 起、打樣約 2–3 週；正式數量與交期需按 SKU 確認。": "目前未公開通用 MOQ 或交期；正式數量與交期需按 SKU、圖面與專案確認。",
        "客製五金通常由 500 pcs 起討論；正式數量與交期依 SKU／專案確認。": "目前未公開通用 MOQ 或交期；正式數量與交期依 SKU／專案確認。",
    },
    "en": {
        "General project baseline: custom hardware is commonly discussed from 500 pcs and sampling from about 2–3 weeks; confirm the actual SKU.": "No universal MOQ or lead time is published here; confirm quantity and schedule by SKU, drawing and project.",
        "Custom hardware is commonly discussed from 500 pcs; confirm quantity and schedule by SKU or project.": "No universal MOQ or lead time is published here; confirm quantity and schedule by SKU or project.",
    },
    "jp": {
        "一般的な相談基準はカスタム金具 500 pcs から、サンプル約 2–3 週間。実際の SKU で確認します。": "共通の MOQ や納期は公開していません。数量と納期は SKU、図面、案件条件で確認します。",
        "カスタム金具は 500 pcs から相談することが多く、数量と納期は SKU ごとに確認します。": "共通の MOQ や納期は公開していません。数量と納期は SKU と案件条件で確認します。",
    },
}

for lang, replacements in REPLACEMENTS.items():
    for path in (ROOT / lang).glob("*.html"):
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in replacements.items():
            updated = updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
