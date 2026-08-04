from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

SECTIONS = {
    "tw": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">可追溯的工程文件鏈</h2></div><div class="grid-3"><article class="location-card reveal"><h3>需求與回覆</h3><p>來源包含相容性、POP／Sign Holder 固定方式與替代材料的往返信件，支持需求釐清與方案回覆。</p></article><article class="location-card reveal"><h3>圖面與缺陷改善</h3><p>來源包含技術圖面、旋轉架／四向洞洞板架方案，以及粉體塗層、運輸損傷與底座強度的改善紀錄。</p></article><article class="location-card reveal"><h3>組裝與包裝</h3><p>來源包含旋轉架與洞洞板架組裝說明、完成品影像與 shipping mark；標示可作為包裝線索，但不等同獨立貨運簽收。</p></article></div><p class="section-note reveal">這些來源支持需求、工程迭代、改善、組裝與包裝準備範圍；客戶名稱、PO、授權、正式交期與商業交付結果不在公開頁宣稱。</p></div></section>''',
    "en": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">Traceable engineering document chain</h2></div><div class="grid-3"><article class="location-card reveal"><h3>Requirement and reply records</h3><p>The source includes correspondence about compatibility, POP / sign-holder fixing and alternative materials, supporting requirement clarification and solution replies.</p></article><article class="location-card reveal"><h3>Drawings and defect improvements</h3><p>The source includes technical drawings, rotating-rack / four-way pegboard solutions, and improvement records for coating, transport damage and base strength.</p></article><article class="location-card reveal"><h3>Assembly and packing</h3><p>The source includes assembly guides for the rotating rack and pegboard rack, final-product images and a shipping mark; the mark is a packing clue, not an independent freight receipt.</p></article></div><p class="section-note reveal">These records support the requirement, engineering iteration, improvement, assembly and packing-preparation scope; client name, PO, authorization, formal lead time and commercial delivery outcome are not claimed publicly.</p></div></section>''',
    "jp": '''<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">追跡可能なエンジニアリング資料</h2></div><div class="grid-3"><article class="location-card reveal"><h3>要件と回答</h3><p>適合性、POP／サインホルダーの固定方法、代替材料に関する往復記録から、要件整理と提案回答を確認できます。</p></article><article class="location-card reveal"><h3>図面と不具合改善</h3><p>技術図面、回転ラック／四面有孔ボードラックの案、塗装、輸送損傷、ベース強度の改善記録を含みます。</p></article><article class="location-card reveal"><h3>組立と梱包</h3><p>回転ラックと有孔ボードラックの組立手順、完成品画像、shipping mark を含みます。表示は梱包の手掛かりであり、独立した運送受領証ではありません。</p></article></div><p class="section-note reveal">これらの資料は要件、設計反復、改善、組立、梱包準備の範囲を示します。顧客名、PO、許諾、正式納期、商業納品結果は公開していません。</p></div></section>''',
}


for language, section in SECTIONS.items():
    for path in (ROOT / language / "case-automotive-parts-rack.html", ROOT / language / "case-automotive-parts-rack" / "index.html"):
        source = path.read_text(encoding="utf-8")
        if 'data-bf-source-record="1"' in source:
            continue
        match = re.search(r'<section\b[^>]*data-bf-faq="1"[^>]*>', source, re.I)
        if not match:
            raise RuntimeError(f"FAQ section not found: {path}")
        source = source[:match.start()] + section + source[match.start():]
        path.write_text(source, encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}")
