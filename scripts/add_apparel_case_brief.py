"""Add an explicit evidence brief to the anonymous apparel photo record."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

SECTIONS = {
    "tw": '''<section class="section section-light" data-bf-case-brief="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">CASE BRIEF</span><h2 class="section-title">店型問題、可討論範圍與證據邊界</h2></div><div class="grid-3"><article class="location-card reveal"><h3>客戶問題／來源狀態</h3><p>現有來源是 3 張檔名含「CASE-01, 2016, clothing brand」的匿名照片，沒有可核對的客戶問題文字；不從照片推定業主需求。</p></article><article class="location-card reveal"><h3>店型與展示內容</h3><p>照片可辨識服飾門市、中島桌架、壁面陳列、吊掛系統、獨立展示架，以及包款、鞋類與桌面配件展示。</p></article><article class="location-card reveal"><h3>Big Fame 可核對範圍</h3><p>目前來源支持店型與展示情境的需求討論，不足以核准 Big Fame 的合約角色、設計、製造、安裝或供應範圍。</p></article><article class="location-card reveal"><h3>可討論的產品條件</h3><p>可從動線、展示密度、吊掛高度、中島尺寸、壁面系統、配件展示與多店複製條件開始；正式產品、材質與尺寸需由新案圖面確認。</p></article><article class="location-card reveal"><h3>數量／交期／交付地</h3><p>照片未提供正式數量、MOQ、交期或交付地；新案需提供預估數量、目標時程、交貨地與圖面或現場照片。</p></article><article class="location-card reveal"><h3>結果與公開程度</h3><p>本頁是匿名、受證據控制的照片紀錄，不宣稱完成交付、安裝成果或成效數據；照片公開授權與專案角色仍需逐案確認。</p></article></div></div></section>''',
    "en": '''<section class="section section-light" data-bf-case-brief="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">CASE BRIEF</span><h2 class="section-title">Store problem, discussable scope and evidence boundary</h2></div><div class="grid-3"><article class="location-card reveal"><h3>Client problem / source status</h3><p>The source currently contains 3 anonymous photos whose filenames include “CASE-01, 2016, clothing brand”. No fully confirmable client problem is provided, so the owner’s request is not inferred from the photos.</p></article><article class="location-card reveal"><h3>Store type and display content</h3><p>The images show an apparel store, island tables, wall merchandising, hanging systems, freestanding fixtures, and presentation of bags, footwear and tabletop accessories.</p></article><article class="location-card reveal"><h3>Confirmable Big Fame scope</h3><p>The source supports a discussion of store type and display context, but does not approve Big Fame’s contractual role or design, manufacturing, installation or supply scope.</p></article><article class="location-card reveal"><h3>Discussable product conditions</h3><p>Start with customer flow, display density, hanging height, island dimensions, wall system, accessory display and repeatable-store conditions. Confirm products, materials and dimensions against the new project drawings.</p></article><article class="location-card reveal"><h3>Quantity / lead time / destination</h3><p>The photos do not provide final quantity, MOQ, lead time or destination. A new brief should include estimated quantity, target timing, destination, drawings or site photos.</p></article><article class="location-card reveal"><h3>Result and publication boundary</h3><p>This is an anonymous, evidence-controlled photo record. It does not claim completed delivery, installation results or performance data; photo permission and project role require case-by-case confirmation.</p></article></div></div></section>''',
    "jp": '''<section class="section section-light" data-bf-case-brief="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">CASE BRIEF</span><h2 class="section-title">店舗課題、相談できる範囲、証拠の境界</h2></div><div class="grid-3"><article class="location-card reveal"><h3>顧客課題／出典の状態</h3><p>出典はファイル名に「CASE-01, 2016, clothing brand」を含む匿名写真 3 枚です。確認できる顧客課題の文章はなく、写真から要望を推定していません。</p></article><article class="location-card reveal"><h3>店舗形態と展示内容</h3><p>アパレル店舗、島什器、壁面陳列、ハンギングシステム、独立什器、バッグ、靴、卓上アクセサリーの展示を確認できます。</p></article><article class="location-card reveal"><h3>確認できる Big Fame の範囲</h3><p>店舗形態と展示場面の相談はできますが、Big Fame の契約上の役割、設計、製造、設置、供給範囲は出典で承認されていません。</p></article><article class="location-card reveal"><h3>相談できる製品条件</h3><p>動線、展示密度、ハンギング高さ、島什器寸法、壁面システム、アクセサリー展示、多店舗展開の条件から始めます。正式な製品、材料、寸法は新案件の図面で確認します。</p></article><article class="location-card reveal"><h3>数量／納期／納入地</h3><p>写真から最終数量、MOQ、納期、納入地は確認できません。新案件では予定数量、希望時期、納入地、図面、現場写真を共有してください。</p></article><article class="location-card reveal"><h3>結果と公開範囲</h3><p>匿名で証拠管理された写真記録です。納品完了、設置結果、効果数値は宣言していません。写真の許諾と担当範囲は案件ごとに確認します。</p></article></div></div></section>''',
}


for language, section in SECTIONS.items():
    for path in (ROOT / language / "case-apparel-2016.html", ROOT / language / "case-apparel-2016" / "index.html"):
        source = path.read_text(encoding="utf-8")
        if 'data-bf-case-brief="1"' in source:
            continue
        marker = re.search(r'<section\b[^>]*data-bf-faq="1"[^>]*>', source, re.I)
        if not marker:
            raise RuntimeError(f"FAQ section not found: {path}")
        path.write_text(source[:marker.start()] + section + source[marker.start():], encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}")
