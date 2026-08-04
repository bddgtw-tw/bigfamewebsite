"""Add an evidence-backed deliverables section to the headphone display record."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

SECTIONS = {
    "tw": '''<section class="section section-light" data-bf-deliverables="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">DOCUMENTED DELIVERABLES</span><h2 class="section-title">可核對的工程交付包</h2><p>目前來源支持的是工程文件與組裝／包裝準備內容；以下是採購與設計可以核對的交付物類型，不等同於公開宣稱已完成出貨。</p></div><div class="grid-2"><article class="location-card reveal"><h3>圖面與零件對應</h3><p>客戶來圖、專案編號 11-37607、零件編號與展示組 BOM，可用來確認展示外殼、支撐件與配件之間的對應關係。</p></article><article class="location-card reveal"><h3>展示組結構資料</h3><p>工程文件記錄真空成型外殼、金屬支撐件、背景圖像、按鈕、影音播放器與掛鉤組件的整合方向。</p></article><article class="location-card reveal"><h3>工廠組裝說明</h3><p>組裝文件將鉚接、圖像貼合、播放器與按鈕安裝、電源線固定，以及外殼與支撐件組合整理成可依循的步驟。</p></article><article class="location-card reveal"><h3>Packout 與運輸保護</h3><p>Packout 文件記錄填充件、外箱、套管、展示本體、金屬支架、螺絲包與說明文件的裝箱配置，支援運輸保護討論。</p></article></div><p class="section-note reveal">這些是來源文件可核對的工程交付物類型；正式合約責任、訂單數量、交期、交貨地、實際出貨與安裝結果仍需逐案確認。</p></div></section>''',
    "en": '''<section class="section section-light" data-bf-deliverables="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">DOCUMENTED DELIVERABLES</span><h2 class="section-title">What the engineering package can be checked against</h2><p>The source supports engineering documents and assembly / packout preparation. These are documented deliverable types, not a public claim of completed shipment.</p></div><div class="grid-2"><article class="location-card reveal"><h3>Drawings and part mapping</h3><p>Customer drawings, project number 11-37607, part numbers and the display-set BOM support review of the relationship between the housing, supports and accessories.</p></article><article class="location-card reveal"><h3>Display-set structure records</h3><p>The engineering files record a vacuum-formed housing, metal supports, graphics, buttons, an audio/video player and hook assemblies as an integrated direction.</p></article><article class="location-card reveal"><h3>Plant assembly instructions</h3><p>The assembly documents organize riveting, graphic application, player and button installation, power-cable fixing, and housing-to-support assembly into repeatable steps.</p></article><article class="location-card reveal"><h3>Packout and transport protection</h3><p>The packout records identify fillers, carton, sleeve, display body, metal brackets, screw pack and instructions in the packing configuration for transport-protection review.</p></article></div><p class="section-note reveal">These are source-supported engineering deliverable types. Formal contract scope, order quantity, lead time, destination, actual shipment and installation outcome require project confirmation.</p></div></section>''',
    "jp": '''<section class="section section-light" data-bf-deliverables="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">DOCUMENTED DELIVERABLES</span><h2 class="section-title">確認できるエンジニアリング成果物</h2><p>資料から確認できるのは、設計資料と組立・梱包準備の内容です。以下は確認可能な成果物の種類であり、出荷完了を公開するものではありません。</p></div><div class="grid-2"><article class="location-card reveal"><h3>図面と部品対応</h3><p>顧客図面、プロジェクト番号 11-37607、部品番号、展示セット BOM から、外装、支持部品、付属部品の対応関係を確認できます。</p></article><article class="location-card reveal"><h3>展示セットの構造記録</h3><p>真空成形ハウジング、金属支持部品、グラフィック、ボタン、映像プレーヤー、フック部品を組み合わせる方向が記録されています。</p></article><article class="location-card reveal"><h3>工場組立手順</h3><p>リベット、グラフィック貼付、プレーヤーとボタンの取付、電源ケーブル固定、外装と支持部品の組立を手順として確認できます。</p></article><article class="location-card reveal"><h3>Packout と輸送保護</h3><p>充填材、外箱、スリーブ、展示本体、金属ブラケット、ねじ袋、説明書の梱包配置を、輸送保護の検討資料として確認できます。</p></article></div><p class="section-note reveal">これらは資料から確認できるエンジニアリング成果物の種類です。正式な担当範囲、受注数量、納期、納品先、実際の出荷・施工結果は案件ごとに確認します。</p></div></section>''',
}


for language, section in SECTIONS.items():
    for path in (
        ROOT / language / "case-headphone-display-set.html",
        ROOT / language / "case-headphone-display-set" / "index.html",
    ):
        source = path.read_text(encoding="utf-8")
        if 'data-bf-deliverables="1"' in source:
            continue
        marker = re.search(r'<section\b[^>]*data-bf-source-record="1"[^>]*>', source, re.I)
        if not marker:
            raise RuntimeError(f"Source record section not found: {path}")
        source = source[: marker.start()] + section + source[marker.start() :]
        path.write_text(source, encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}")
