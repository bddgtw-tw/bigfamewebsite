from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

SECTIONS = {
    "tw": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">可追溯的產品開發資料</h2></div><div class="grid-3"><article class="location-card reveal"><h3>Offer Form 版本</h3><p>來源為 Project PAGE／Tabletop Cosmetic Organizer 的 2020-03-30 ver.01 Offer Form，可追蹤本頁的規格版本。</p></article><article class="location-card reveal"><h3>尺寸／材質資料</h3><p>來源包含尺寸圖與產品影像，支持 W250 × D120 × H240 mm、Clear Acrylic、Edge polished 與 Solid wood 的版本紀錄。</p></article><article class="location-card reveal"><h3>包裝／時程資料</h3><p>來源記錄 1 SET/CTN、樣品約 15–25 天與訂單確認後量產約 25–35 天；正式條件仍需依新案確認。</p></article></div><p class="section-note reveal">這些資料支持特定文件版本的產品開發與報價討論；不代表已核准客戶名稱、MOQ、訂單數量、交付地或完成成果。</p></div></section>''',
    "en": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">Traceable product-development records</h2></div><div class="grid-3"><article class="location-card reveal"><h3>Offer Form version</h3><p>The source is the 2020-03-30 ver.01 Offer Form for Project PAGE / Tabletop Cosmetic Organizer, providing the version boundary for this page.</p></article><article class="location-card reveal"><h3>Dimension / material records</h3><p>The source includes dimension drawings and product images supporting the version record of W250 × D120 × H240 mm, Clear Acrylic, Edge polished and Solid wood.</p></article><article class="location-card reveal"><h3>Packout / timing records</h3><p>The source records 1 SET/CTN, samples at approximately 15–25 days and volume production at approximately 25–35 days after order confirmation; formal terms require a new review.</p></article></div><p class="section-note reveal">These records support product-development and quotation discussion for a specific document version; approved client name, MOQ, order quantity, destination and final outcome are not claimed.</p></div></section>''',
    "jp": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">追跡可能な製品開発資料</h2></div><div class="grid-3"><article class="location-card reveal"><h3>Offer Form の版</h3><p>Project PAGE／Tabletop Cosmetic Organizer の 2020-03-30 ver.01 Offer Form を基準に、このページの版の範囲を示します。</p></article><article class="location-card reveal"><h3>寸法／材料記録</h3><p>寸法図と製品画像から、W250 × D120 × H240 mm、Clear Acrylic、Edge polished、Solid wood の版情報を確認できます。</p></article><article class="location-card reveal"><h3>梱包／時期の記録</h3><p>1 SET/CTN、サンプル約15–25日、注文確認後の量産約25–35日の記録があります。正式条件は新規案件で確認します。</p></article></div><p class="section-note reveal">これらの資料は特定版の製品開発・見積検討を支えますが、承認済み顧客名、MOQ、受注数量、納入先、完成成果を示すものではありません。</p></div></section>''',
}


for language, section in SECTIONS.items():
    candidates = [ROOT / language / "case-page-cosmetic-organizer.html", ROOT / language / "case-page-cosmetic-organizer" / "index.html"]
    for path in [candidate for candidate in candidates if candidate.exists()]:
        source = path.read_text(encoding="utf-8")
        if 'data-bf-source-record="1"' in source:
            continue
        match = re.search(r'<section\b[^>]*data-bf-faq="1"[^>]*>', source, re.I)
        if not match:
            raise RuntimeError(f"FAQ section not found: {path}")
        source = source[:match.start()] + section + source[match.start():]
        path.write_text(source, encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}")
