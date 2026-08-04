from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = {
    "tw": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">Product Hook 圖面與產品資料來源紀錄</h2></div><div class="grid-3"><article class="location-card reveal"><h3>掛勾長度</h3><p>Product Hook 資料可核對 wire hook 長度 50、75、100、150、200 mm 的代表性變體。</p></article><article class="location-card reveal"><h3>線徑與橫桿</h3><p>資料可見 Ø5.0、Ø6.0、Ø8.0、Ø10.0 線徑方向，以及 10×20、14×24、20×40、15×30 mm 橫桿尺寸方向。</p></article><article class="location-card reveal"><h3>適用系統與邊界</h3><p>資料呈現 pegboard、slatwall、wire shelving 與 crossbar 的適用方向；正式 SKU、材質牌號、承重、MOQ 與交期仍需依圖面與樣品確認。</p></article></div><p class="section-note reveal">上述是 Product Hook 資料中的代表性尺寸方向，不是所有展示掛勾的統一規格或通用商業條件。</p></div></section>''',
    "en": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">Product Hook drawing and data record</h2></div><div class="grid-3"><article class="location-card reveal"><h3>Hook lengths</h3><p>The Product Hook data identifies representative wire-hook length variants of 50, 75, 100, 150 and 200 mm.</p></article><article class="location-card reveal"><h3>Wire diameters and crossbars</h3><p>The data shows Ø5.0, Ø6.0, Ø8.0 and Ø10.0 wire directions, plus crossbar directions of 10×20, 14×24, 20×40 and 15×30 mm.</p></article><article class="location-card reveal"><h3>Systems and boundary</h3><p>The data presents pegboard, slatwall, wire shelving and crossbar directions; formal SKU, material grade, load, MOQ and lead time require drawing and sample confirmation.</p></article></div><p class="section-note reveal">These are representative dimensions from the Product Hook data, not universal specifications or commercial terms for every display hook.</p></div></section>''',
    "jp": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">Product Hook 図面・製品資料の出典記録</h2></div><div class="grid-3"><article class="location-card reveal"><h3>フック長さ</h3><p>Product Hook 資料には、ワイヤーフックの代表的な長さとして 50、75、100、150、200 mm の方向があります。</p></article><article class="location-card reveal"><h3>線径とクロスバー</h3><p>Ø5.0、Ø6.0、Ø8.0、Ø10.0 の線径方向と、10×20、14×24、20×40、15×30 mm のクロスバー方向を確認できます。</p></article><article class="location-card reveal"><h3>システムと範囲</h3><p>有孔ボード、スラットウォール、ワイヤーシェルフ、クロスバーへの使用方向を示します。正式 SKU、材料グレード、荷重、MOQ、納期は図面とサンプルで確認します。</p></article></div><p class="section-note reveal">代表的な寸法方向の記録であり、すべての展示フックに共通する仕様や商業条件ではありません。</p></div></section>''',
}

for language, section in SECTIONS.items():
    path = ROOT / language / "display-hooks.html"
    text = path.read_text(encoding="utf-8")
    marker = '<section class="section section-light" data-bf-spec-gate="1">'
    if 'data-bf-source-record="1"' not in text:
        if text.count(marker) != 1:
            raise RuntimeError(f"unexpected marker count for {path}: {text.count(marker)}")
        path.write_text(text.replace(marker, section + marker, 1), encoding="utf-8")
        print(f"updated {path}")
