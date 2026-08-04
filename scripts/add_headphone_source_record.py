from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

SOURCE_SECTIONS = {
    "tw": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">可追溯的工程文件鏈</h2></div><div class="grid-3"><article class="location-card reveal"><h3>Packout 文件</h3><p>來源包含最終裝箱配置、填充件、外箱、套管與保護流程，用來核對運輸保護方向。</p></article><article class="location-card reveal"><h3>BOM／圖面文件</h3><p>來源包含展示組零件編號、展示外殼、金屬支撐件、按鈕、播放器與掛勾組件的工程資料。</p></article><article class="location-card reveal"><h3>工廠組裝說明</h3><p>來源包含鉚接、圖像貼合、按鈕與播放器安裝、電源線固定，以及外殼與支撐件組合步驟。</p></article></div><p class="section-note reveal">這些文件支持工程範圍、組裝與包裝的可追溯性；不公開客戶名稱、訂單數量、交期或正式商業交付結果。</p></div></section>''',
    "en": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">Traceable engineering document chain</h2></div><div class="grid-3"><article class="location-card reveal"><h3>Packout records</h3><p>The source includes final packout configuration, fillers, carton, sleeve and protection steps used to review the transport-protection direction.</p></article><article class="location-card reveal"><h3>BOM / drawing records</h3><p>The source includes engineering records for display-set parts, display housing, metal supports, buttons, media player and hook assemblies.</p></article><article class="location-card reveal"><h3>Plant assembly instructions</h3><p>The source includes riveting, graphic application, button and player installation, power-cable fixing, and housing-to-support assembly steps.</p></article></div><p class="section-note reveal">These records support traceability of the engineering, assembly and packout scope; client name, order quantity, lead time and formal commercial delivery outcome are not published.</p></div></section>''',
    "jp": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">追跡可能なエンジニアリング資料</h2></div><div class="grid-3"><article class="location-card reveal"><h3>Packout 記録</h3><p>最終梱包配置、充填材、外箱、スリーブ、保護手順を含む資料から、輸送保護の方向を確認できます。</p></article><article class="location-card reveal"><h3>BOM／図面記録</h3><p>展示セット部品、展示外装、金属支持部品、ボタン、メディアプレーヤー、フック組立のエンジニアリング資料を確認できます。</p></article><article class="location-card reveal"><h3>工場組立手順</h3><p>リベット、グラフィック貼付、ボタンとプレーヤーの取付、電源ケーブル固定、外装と支持部品の組立手順を含みます。</p></article></div><p class="section-note reveal">これらの資料は設計、組立、梱包範囲の追跡性を示します。顧客名、受注数量、納期、正式な商業納品結果は公開していません。</p></div></section>''',
}


for language, section in SOURCE_SECTIONS.items():
    for path in (ROOT / language / "case-headphone-display-set.html", ROOT / language / "case-headphone-display-set" / "index.html"):
        source = path.read_text(encoding="utf-8")
        if 'data-bf-source-record="1"' in source:
            continue
        match = re.search(r'<section\b[^>]*data-bf-faq="1"[^>]*>', source, re.I)
        if not match:
            raise RuntimeError(f"FAQ section not found: {path}")
        source = source[:match.start()] + section + source[match.start():]
        path.write_text(source, encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}")
