"""Add related EYEHK drawing evidence to the anonymous eyewear case."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

SECTIONS = {
    "tw": '''<section class="section section-light" data-bf-related-product-evidence="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">RELATED PRODUCT EVIDENCE</span><h2 class="section-title">從門市影像走到可核對的眼鏡掛勾條件</h2><p>2016 年門市照片只能支持展示方向；以下 EYEHK 圖面是相關產品資料，不宣稱就是本案例使用的正式 SKU。</p></div><div class="grid-2"><article class="location-card reveal"><h3>洞洞板掛勾圖面</h3><p>2025 圖面可核對 160、175、150.93、128 與 25.4 mm 等尺寸，並記錄雷射切割掛片與背面焊接方向。</p></article><article class="location-card reveal"><h3>鎖螺絲／槽板掛勾圖面</h3><p>2018 圖面記錄 t2.0 鐵板、4.0 mm 橫向鐵線、黑色粉體烤漆、尾端倒角與約 2° 上仰，並可見 145／175 mm 外包與 40 mm 安裝片尺寸。</p></article><article class="location-card reveal"><h3>如何用在新案</h3><p>請提供背板孔距或槽距、展示商品、掛勾長度、預估數量與照片，再由最新圖面、樣品與產品版本確認相容性。</p></article><article class="location-card reveal"><h3>證據邊界</h3><p>EYEHK 圖面年份與 2016 門市照片不同，不能直接證明照片中的掛勾就是 EYEHK SKU；正式材質、色號、MOQ、交期與供貨狀態需逐案確認。</p></article></div><p class="section-note reveal"><a href="optical-hooks">查看眼鏡展示掛勾圖面證據</a> · <a href="contact?category=display_hardware&role=designer&product=optical-hooks&requested_files=dimension_drawing">以店型與圖面開始詢問</a></p></div></section>''',
    "en": '''<section class="section section-light" data-bf-related-product-evidence="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">RELATED PRODUCT EVIDENCE</span><h2 class="section-title">Move from a store image to confirmable eyewear-hook conditions</h2><p>The 2016 store image supports a display direction. The EYEHK drawings below are related product evidence, not a claim that the photographed store used a specific formal SKU.</p></div><div class="grid-2"><article class="location-card reveal"><h3>Pegboard-hook drawing</h3><p>The 2025 drawing shows 160, 175, 150.93, 128 and 25.4 mm dimensions, with a laser-cut mounting tab and a rear-welding direction.</p></article><article class="location-card reveal"><h3>Screw-on / slatwall hook drawing</h3><p>The 2018 drawing notes a t2.0 iron plate, 4.0 mm horizontal wire, black powder coating, chamfered ends and an approximately 2° upward angle, with 145 / 175 mm outer dimensions and a 40 mm mounting plate.</p></article><article class="location-card reveal"><h3>How to use this for a new project</h3><p>Share the backing pitch or slot spacing, displayed product, hook length, estimated quantity and photos. Compatibility is then checked against the current drawing, sample and product revision.</p></article><article class="location-card reveal"><h3>Evidence boundary</h3><p>The EYEHK drawing years differ from the 2016 store image, so the image does not prove an EYEHK SKU. Formal material, colour, MOQ, lead time and availability require project confirmation.</p></article></div><p class="section-note reveal"><a href="optical-hooks">View the eyewear-hook drawing evidence</a> · <a href="contact?category=display_hardware&role=designer&product=optical-hooks&requested_files=dimension_drawing">Start with a store and drawing brief</a></p></div></section>''',
    "jp": '''<section class="section section-light" data-bf-related-product-evidence="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">RELATED PRODUCT EVIDENCE</span><h2 class="section-title">店舗画像から確認可能なメガネフック条件へ</h2><p>2016年の店舗画像は展示方向を示すものです。以下の EYEHK 図面は関連製品資料であり、画像の店舗が特定 SKU を使用したという意味ではありません。</p></div><div class="grid-2"><article class="location-card reveal"><h3>有孔ボード用フック図面</h3><p>2025年図面には 160、175、150.93、128、25.4 mm の寸法と、レーザー切断した掛片を背面へ溶接する方向が記録されています。</p></article><article class="location-card reveal"><h3>ねじ固定／スラットウォール用図面</h3><p>2018年図面には t2.0 鉄板、4.0 mm 横方向鉄線、黒色粉体塗装、端部面取り、約 2° の上向き角度、145／175 mm 外形、40 mm 取付板が記録されています。</p></article><article class="location-card reveal"><h3>新案件への使い方</h3><p>背板のピッチまたはスロット間隔、展示商品、フック長さ、予定数量、写真を共有してください。最新図面、サンプル、製品改訂版で互換性を確認します。</p></article><article class="location-card reveal"><h3>証拠の範囲</h3><p>EYEHK 図面の年と 2016年の店舗画像は異なるため、画像だけで EYEHK SKU を証明できません。正式な材料、色、MOQ、納期、供給可否は案件ごとに確認します。</p></article></div><p class="section-note reveal"><a href="optical-hooks">メガネ展示フックの図面証拠を見る</a> · <a href="contact?category=display_hardware&role=designer&product=optical-hooks&requested_files=dimension_drawing">店舗条件と図面から相談する</a></p></div></section>''',
}


for language, section in SECTIONS.items():
    for path in (
        ROOT / language / "case-eyewear-2016.html",
        ROOT / language / "case-eyewear-2016" / "index.html",
    ):
        source = path.read_text(encoding="utf-8")
        if 'data-bf-related-product-evidence="1"' in source:
            continue
        marker = re.search(r'<section\b[^>]*data-bf-faq="1"[^>]*>', source, re.I)
        if not marker:
            raise RuntimeError(f"FAQ section not found: {path}")
        source = source[: marker.start()] + section + source[marker.start() :]
        path.write_text(source, encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}")
