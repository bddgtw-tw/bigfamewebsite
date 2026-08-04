from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SECTIONS = {
    "tw": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">Product_Slatwall 型錄可追溯紀錄</h2></div><div class="grid-3"><article class="location-card reveal"><h3>來源文件</h3><p>一頁式 Product_Slatwall PDF 將 Slatwall 描述為店面安裝的基礎元素與展示空間配置平台。</p></article><article class="location-card reveal"><h3>文件可支持的方向</h3><p>文件以照片與文字呈現槽板可調整展示配置、材料與顏色，以及可延伸配件的產品方向。</p></article><article class="location-card reveal"><h3>尚未由型錄確認</h3><p>此型錄沒有提供特定 SKU、尺寸、板厚、承重、MOQ 或交期；正式條件仍需依圖面、樣品與專案確認。</p></article></div><p class="section-note reveal">本段是型錄來源紀錄，不把概念型錄描述擴張為所有槽板配件的正式規格或通用承諾。</p></div></section>''',
    "en": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">Traceable Product_Slatwall brochure record</h2></div><div class="grid-3"><article class="location-card reveal"><h3>Source document</h3><p>The one-page Product_Slatwall PDF describes slatwall as a basic store-installation element and a platform for arranging display space.</p></article><article class="location-card reveal"><h3>What the brochure supports</h3><p>The document presents adjustable display layouts, changes in materials and colours, and an expandable accessory direction through photos and descriptive text.</p></article><article class="location-card reveal"><h3>What it does not confirm</h3><p>The brochure does not provide a specific SKU, dimensions, board thickness, load rating, MOQ or lead time. Confirm formal conditions by drawing, sample and project.</p></article></div><p class="section-note reveal">This is a brochure source record; its general description is not extended into formal specifications or universal commitments for every slatwall accessory.</p></div></section>''',
    "jp": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">Product_Slatwall カタログの追跡可能な記録</h2></div><div class="grid-3"><article class="location-card reveal"><h3>出典資料</h3><p>1ページの Product_Slatwall PDF は、スラットウォールを店舗施工の基本要素と展示空間を構成するプラットフォームとして説明しています。</p></article><article class="location-card reveal"><h3>カタログで確認できる方向</h3><p>写真と説明文から、展示レイアウトの変更、材料・色の変更、アクセサリーで機能を拡張する方向を確認できます。</p></article><article class="location-card reveal"><h3>カタログでは未確認</h3><p>特定 SKU、寸法、板厚、耐荷重、MOQ、納期は記載されていません。正式条件は図面、サンプル、案件で確認します。</p></article></div><p class="section-note reveal">カタログの出典記録です。一般的な説明を、すべてのスラットウォール用アクセサリーの正式仕様や共通条件へ拡張しません。</p></div></section>''',
}

for language, section in SECTIONS.items():
    path = ROOT / language / "slatwall-pegboard-accessories.html"
    text = path.read_text(encoding="utf-8")
    marker = '<section class="section section-light" data-bf-spec-gate="1">'
    if 'data-bf-source-record="1"' not in text:
        if text.count(marker) != 1:
            raise RuntimeError(f"unexpected marker count for {path}: {text.count(marker)}")
        text = text.replace(marker, section + marker, 1)
        path.write_text(text, encoding="utf-8")
        print(f"updated {path}")
