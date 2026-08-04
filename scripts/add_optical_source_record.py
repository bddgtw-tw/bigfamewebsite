from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SECTIONS = {
    "tw": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">EYEHK 眼鏡展示掛勾圖面來源紀錄</h2></div><div class="grid-3"><article class="location-card reveal"><h3>2025 洞洞板圖面</h3><p>來源圖面標示 Eyewear Display Hook (pegboard)，可見 160、175、150.93、128 與 25.4 mm 等尺寸，以及 1.5 mm、2 mm 局部尺寸。這些尺寸限於該圖面版本。</p></article><article class="location-card reveal"><h3>2018 溝槽板／鎖螺絲圖面</h3><p>來源圖面可見 t2.0 鐵板、4.0 鐵線、145／175 mm 外包、40 mm 安裝片、尾端倒角、向上仰 2 度與黑色粉體烤漆等設計備註。</p></article><article class="location-card reveal"><h3>證據邊界</h3><p>圖面上的估價數量 1000 支不是通用 MOQ 或已驗證訂單；照片檔名中的 EYEHK 代碼、B／C／W 也不直接等同正式 SKU 或顏色定義。</p></article></div><p class="section-note reveal">正式 SKU、材質牌號、承重、MOQ、交期與目前可供應性，仍需以最新圖面、報價與樣品確認。</p></div></section>''',
    "en": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">EYEHK eyewear display-hook drawing record</h2></div><div class="grid-3"><article class="location-card reveal"><h3>2025 pegboard drawing</h3><p>The source drawing identifies Eyewear Display Hook (pegboard) and shows dimensions including 160, 175, 150.93, 128 and 25.4 mm, with local 1.5 mm and 2 mm details. These are limited to that drawing version.</p></article><article class="location-card reveal"><h3>2018 slatwall / screw-lock drawing</h3><p>The source shows t2.0 iron sheet, 4.0 iron wire, 145／175 mm outer dimensions, a 40 mm mounting plate, a rounded end to protect frames, a 2-degree upward angle and black powder coating notes.</p></article><article class="location-card reveal"><h3>Evidence boundary</h3><p>The drawing note of 1,000 pieces is a quotation condition, not a universal MOQ or verified order. EYEHK filenames and B／C／W markers are not treated as formal SKU or colour definitions.</p></article></div><p class="section-note reveal">Confirm formal SKU, material grade, load, MOQ, lead time and current availability against the latest drawing, quotation and sample.</p></div></section>''',
    "jp": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">EYEHK メガネ展示フック図面の出典記録</h2></div><div class="grid-3"><article class="location-card reveal"><h3>2025 有孔ボード図面</h3><p>出典図面は Eyewear Display Hook (pegboard) と記載し、160、175、150.93、128、25.4 mm などの寸法と、部分的な 1.5 mm、2 mm を示します。これらは該当図面版に限ります。</p></article><article class="location-card reveal"><h3>2018 スラットウォール／ねじ固定図面</h3><p>t2.0 鉄板、4.0 鉄線、外形 145／175 mm、40 mm の取付板、フレームを傷つけない端部面取り、2度の上向き角度、黒色粉体塗装の注記があります。</p></article><article class="location-card reveal"><h3>証拠の範囲</h3><p>図面の見積数量 1,000本は共通 MOQ や確認済み注文ではありません。EYEHK のファイル名と B／C／W の記号も、正式 SKU や色定義とは扱いません。</p></article></div><p class="section-note reveal">正式 SKU、材料グレード、荷重、MOQ、納期、現在の供給可否は、最新図面、見積、サンプルで確認します。</p></div></section>''',
}

for language, section in SECTIONS.items():
    path = ROOT / language / "optical-hooks.html"
    text = path.read_text(encoding="utf-8")
    marker = '<section class="section section-light" data-bf-spec-gate="1">'
    if 'data-bf-source-record="1"' not in text:
        if text.count(marker) != 1:
            raise RuntimeError(f"unexpected marker count for {path}: {text.count(marker)}")
        path.write_text(text.replace(marker, section + marker, 1), encoding="utf-8")
        print(f"updated {path}")
