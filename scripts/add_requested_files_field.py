"""Add a non-sensitive requested-file choice to the three inquiry forms."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELD = {
    "tw": '<div class="form-group"><label for="requested_files">希望取得的資料</label><select id="requested_files" name="requested_files" class="form-control"><option value="">請選擇</option><option value="dimension_drawing">尺寸圖／規格摘要</option><option value="cad_files">PDF／CAD／DWG／DXF／STEP</option><option value="material_finish">材質／表面處理資料</option><option value="sampling_review">打樣可行性討論</option><option value="technical_pack">請協助判斷需要哪些資料</option></select></div>',
    "en": '<div class="form-group"><label for="requested_files">Information requested</label><select id="requested_files" name="requested_files" class="form-control"><option value="">Select</option><option value="dimension_drawing">Dimension drawing / specification summary</option><option value="cad_files">PDF / CAD / DWG / DXF / STEP</option><option value="material_finish">Material / finish information</option><option value="sampling_review">Sampling feasibility review</option><option value="technical_pack">Help identify the right files</option></select></div>',
    "jp": '<div class="form-group"><label for="requested_files">希望する資料</label><select id="requested_files" name="requested_files" class="form-control"><option value="">選択してください</option><option value="dimension_drawing">寸法図／仕様概要</option><option value="cad_files">PDF／CAD／DWG／DXF／STEP</option><option value="material_finish">材料／仕上げ資料</option><option value="sampling_review">試作可否の相談</option><option value="technical_pack">必要な資料の選定を相談</option></select></div>',
}


for language, field in FIELD.items():
    path = ROOT / language / "contact.html"
    text = path.read_text(encoding="utf-8")
    if 'id="requested_files"' in text:
        continue
    marker = '<div class="form-group"><label for="estimated_quantity">'
    if marker not in text:
        raise SystemExit(f"Insertion marker not found: {path}")
    text = text.replace(marker, field + marker, 1)
    path.write_text(text, encoding="utf-8", newline="")
print("Added requested-files field to three inquiry forms.")
