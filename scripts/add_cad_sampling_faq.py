"""Add a direct CAD-led sampling FAQ to the trilingual technical-resource pages."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = {
    "tw": ("Big Fame 是否支援 CAD 打樣？", "可以以 PDF、DWG、DXF、STEP 或照片作為規格討論與打樣起點；正式打樣可行性、版本、費用與交期仍需依產品、材質、數量與專案條件確認。"),
    "en": ("Can Big Fame support CAD-led sampling?", "PDF, DWG, DXF, STEP or photos can start a specification and sampling discussion. Sampling feasibility, revision, cost and timing are confirmed by product, material, quantity and project conditions."),
    "jp": ("CADを起点に試作を相談できますか？", "PDF、DWG、DXF、STEP、写真を仕様確認と試作相談の起点にできます。試作可否、版、費用、納期は製品、材料、数量、案件条件で確認します。"),
}

for folder, (question, answer) in DATA.items():
    path = ROOT / folder / "technical-resources.html"
    text = path.read_text(encoding="utf-8")
    if question in text:
        continue
    faq_start = text.find('data-bf-faq="1"')
    if faq_start < 0:
        raise SystemExit(f"FAQ section not found: {folder}")
    grid_start = text.find('<div class="grid-3">', faq_start)
    grid_end = text.find('</div></div></section>', grid_start)
    if grid_start < 0 or grid_end < 0:
        raise SystemExit(f"FAQ grid not found: {folder}")
    card = f'<article class="location-card reveal"><h3>{question}</h3><p>{answer}</p></article>'
    text = text[:grid_end] + card + text[grid_end:]

    schema_start = text.find('"@type": "FAQPage"')
    schema_end = text.find('</script>', schema_start)
    if schema_start < 0 or schema_end < 0:
        raise SystemExit(f"FAQ schema not found: {folder}")
    segment = text[schema_start:schema_end]
    close = segment.rfind(']')
    if close < 0:
        raise SystemExit(f"FAQ schema array not found: {folder}")
    entry = json.dumps({"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}}, ensure_ascii=False)
    segment = segment[:close] + "," + entry + segment[close:]
    text = text[:schema_start] + segment + text[schema_end:]
    path.write_text(text, encoding="utf-8")
    print(f"UPDATED {folder}/technical-resources.html")
