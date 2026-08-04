from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

DELIVERABLES = {
    "tw": '''<section class="section section-light" data-bf-urban-deliverables="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">DOCUMENTED DELIVERABLES</span><h2 class="section-title">來源可核對的系統交付內容</h2></div><div class="grid-2"><article class="location-card reveal"><h3>模組與元件</h3><p>來源記錄完整迷你儲物單元、超過 50 個元件與約 3.4 m³ 標準單元，並包含可因尺寸與功能調整的元件。</p></article><article class="location-card reveal"><h3>材料與表面方向</h3><p>來源記錄鋼板、鋼管、鋼線與客製粉體塗裝方向；濕氣與刮傷考量屬於設計敘述，不延伸為測試標準。</p></article><article class="location-card reveal"><h3>結構與運輸考量</h3><p>K/D（可拆裝）結構與多種單元配置被記錄為系統方向；來源將此結構與降低運輸成本連結，但未提供正式包裝、運費或節省金額。</p></article><article class="location-card reveal"><h3>使用結果</h3><p>來源記錄空間已開放使用，業主可將原始設計複製到其他城市；這不等同於已核准的訂單數量、交期或出貨成果。</p></article></div><p class="section-note reveal">以上是來源文件可支持的設計、系統與使用結果；正式合約分工、交付明細與公開授權仍需逐案確認。</p></div></section>''',
    "en": '''<section class="section section-light" data-bf-urban-deliverables="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">DOCUMENTED DELIVERABLES</span><h2 class="section-title">System deliverables supported by the source</h2></div><div class="grid-2"><article class="location-card reveal"><h3>Module and components</h3><p>The source records a complete mini-storage unit, more than 50 components and an approximately 3.4 m³ standard unit, with components for size and function changes.</p></article><article class="location-card reveal"><h3>Materials and finish direction</h3><p>The source records steel plate, steel pipe, steel wire and a custom powder-coating direction. Humidity and scratch considerations remain design narrative, not test standards.</p></article><article class="location-card reveal"><h3>Structure and transport consideration</h3><p>A K/D (knock-down) structure and multiple unit configurations are documented as system directions. The source connects K/D with lower transport cost but provides no formal packing, freight or savings amount.</p></article><article class="location-card reveal"><h3>Use result</h3><p>The source records that the space opened for use and that the owner could duplicate the original design in other cities. This is not a claim about approved order quantity, lead time or shipment results.</p></article></div><p class="section-note reveal">These are design, system and use-result details supported by the source. Formal contract scope, delivery details and publication authorization require case-by-case confirmation.</p></div></section>''',
    "jp": '''<section class="section section-light" data-bf-urban-deliverables="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">DOCUMENTED DELIVERABLES</span><h2 class="section-title">資料で確認できるシステム内容</h2></div><div class="grid-2"><article class="location-card reveal"><h3>ユニットと部品</h3><p>資料には、完成したミニ収納ユニット、50を超える部品、約3.4 m³の標準ユニット、サイズと機能を変更する部品が記録されています。</p></article><article class="location-card reveal"><h3>材料と仕上げの方向</h3><p>鋼板、鋼管、鋼線、カスタム粉体塗装の方向が記録されています。湿気や傷への配慮は設計記述であり、試験規格を意味しません。</p></article><article class="location-card reveal"><h3>構造と輸送の考慮</h3><p>K/D（ノックダウン）構造と複数のユニット構成がシステムの方向として記録されています。資料はK/Dと輸送費低減を関連付けますが、正式な梱包、運賃、削減額は示していません。</p></article><article class="location-card reveal"><h3>利用結果</h3><p>空間が利用開始され、原設計を他都市へ複製できると資料に記録されています。承認済みの注文数量、納期、出荷結果を示すものではありません。</p></article></div><p class="section-note reveal">資料が支持する設計・システム・利用結果を掲載しています。正式な契約範囲、納入内容、公開許諾は案件ごとに確認が必要です。</p></div></section>''',
}


def normalize_flat(html: str, lang: str) -> str:
    if 'data-bf-urban-deliverables="1"' not in html:
        marker = '<section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span>'
        if marker not in html:
            raise RuntimeError(f"SOURCE RECORD insertion point missing: {lang}")
        html = html.replace(marker, DELIVERABLES[lang] + marker, 1)

    html = html.replace('<section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span>', '<section class="section section-light" data-bf-source-record="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SOURCE RECORD</span>', 1)
    html = html.replace('data-bf-source-record="0"', 'data-bf-source-record="1"')
    html = html.replace('href="../technical-resources"', 'href="technical-resources"')
    html = html.replace('href="../contact?role=designer&category=system_fixtures"', 'href="contact?role=designer&category=system_fixtures"')
    return html


for lang in ("tw", "en", "jp"):
    flat_path = ROOT / lang / "case-urban-storage.html"
    clean_path = ROOT / lang / "case-urban-storage" / "index.html"
    flat = normalize_flat(flat_path.read_text(encoding="utf-8"), lang)
    flat_path.write_text(flat, encoding="utf-8", newline="\n")

    # The clean URL is served without a trailing slash; keep one content source
    # while retaining the relative paths that work for both generated variants.
    clean = flat
    clean_path.write_text(clean, encoding="utf-8", newline="\n")

print("Synchronized Urban Warehouse flat and clean variants for tw/en/jp")
