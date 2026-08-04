"""Add an explicit evidence brief to the anonymous eyewear case pages."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

SECTIONS = {
    "tw": '''<section class="section section-light" data-bf-case-brief="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">CASE BRIEF</span><h2 class="section-title">客戶問題、Big Fame 範圍與可核對內容</h2></div><div class="grid-3"><article class="location-card reveal"><h3>客戶問題／來源狀態</h3><p>現有公開來源是 2016 年匿名眼鏡門市影像，沒有可完整核對的客戶問題文字；本頁不從照片推定店主需求或成效。</p></article><article class="location-card reveal"><h3>店型與使用情境</h3><p>可確認為眼鏡零售展示情境，適合討論展示密度、掛勾形式、背板系統與店頭取放方式。</p></article><article class="location-card reveal"><h3>Big Fame 可核對範圍</h3><p>頁面可連結 EYEHK 2018／2025 圖面作為相關產品證據；來源未核准正式合約分工，因此不把圖面或照片寫成已承擔的完整交付範圍。</p></article><article class="location-card reveal"><h3>可核對內容</h3><p>可公開核對的是匿名門市影像與相關掛勾圖面中的尺寸、材料備註與加工方向；照片與圖面年份不同，不能直接證明照片使用特定 SKU。</p></article><article class="location-card reveal"><h3>數量／交期／交付地</h3><p>來源未提供或未核准正式數量、交期與最終交付地；這些欄位需依新案圖面、數量、排程與目的地確認。</p></article><article class="location-card reveal"><h3>結果與公開程度</h3><p>本頁是匿名影像與規格討論入口，不宣稱已完成安裝、供貨結果或成效數據；客戶名稱與完整商務資料不公開。</p></article></div></div></section>''',
    "en": '''<section class="section section-light" data-bf-case-brief="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">CASE BRIEF</span><h2 class="section-title">Client problem, Big Fame scope and confirmable content</h2></div><div class="grid-3"><article class="location-card reveal"><h3>Client problem / source status</h3><p>The available source is an anonymous 2016 eyewear-store image. It does not contain a fully confirmable written client problem, so the page does not infer a store request or result from the photograph.</p></article><article class="location-card reveal"><h3>Store type and use context</h3><p>The source supports an eyewear retail display context for discussing display density, hook form, backing system and in-store handling.</p></article><article class="location-card reveal"><h3>Confirmable Big Fame scope</h3><p>The page links to the EYEHK 2018 and 2025 drawings as related product evidence. The source does not approve a formal contract scope, so the drawings and image are not presented as a complete delivery claim.</p></article><article class="location-card reveal"><h3>Confirmable content</h3><p>The public record is the anonymous store image plus dimensions, material notes and process directions visible in related hook drawings. The drawing years differ from the image, so no photographed SKU is inferred.</p></article><article class="location-card reveal"><h3>Quantity / lead time / destination</h3><p>The source does not provide or approve the final quantity, lead time or destination. Confirm these against the new project drawings, quantity, schedule and destination.</p></article><article class="location-card reveal"><h3>Result and publication boundary</h3><p>This is an anonymous image and specification-discussion entry. It does not claim completed installation, supply outcome or performance data; client identity and full commercial data remain unpublished.</p></article></div></div></section>''',
    "jp": '''<section class="section section-light" data-bf-case-brief="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">CASE BRIEF</span><h2 class="section-title">顧客課題、Big Fame の範囲、確認できる内容</h2></div><div class="grid-3"><article class="location-card reveal"><h3>顧客課題／出典の状態</h3><p>公開できる出典は匿名の 2016 年メガネ店舗画像です。顧客課題を完全に確認できる文章はなく、写真から要望や成果を推定していません。</p></article><article class="location-card reveal"><h3>店舗形態と使用場面</h3><p>メガネ小売の展示場面は確認できます。展示密度、フック形状、背板システム、店頭での取り扱いを相談する起点です。</p></article><article class="location-card reveal"><h3>確認できる Big Fame の範囲</h3><p>EYEHK の 2018 年／2025 年図面を関連製品資料として参照できます。正式な契約範囲は出典で承認されていないため、画像や図面を完全な納品の証拠として扱いません。</p></article><article class="location-card reveal"><h3>確認できる内容</h3><p>匿名店舗画像と、関連フック図面に見える寸法、材料注記、加工方向を公開できます。画像と図面の年が異なるため、写真の SKU は推定していません。</p></article><article class="location-card reveal"><h3>数量／納期／納入地</h3><p>最終数量、納期、納入地は出典に記載または承認されていません。新案件の図面、数量、工程、納入地で確認します。</p></article><article class="location-card reveal"><h3>結果と公開範囲</h3><p>匿名画像と仕様相談の入口です。設置完了、供給結果、効果数値は宣言していません。顧客名と完全な商務資料は非公開です。</p></article></div></div></section>''',
}


for language, section in SECTIONS.items():
    for path in (ROOT / language / "case-eyewear-2016.html", ROOT / language / "case-eyewear-2016" / "index.html"):
        source = path.read_text(encoding="utf-8")
        if 'data-bf-case-brief="1"' in source:
            continue
        marker = re.search(r'<section\b[^>]*data-bf-faq="1"[^>]*>', source, re.I)
        if not marker:
            raise RuntimeError(f"FAQ section not found: {path}")
        path.write_text(source[:marker.start()] + section + source[marker.start():], encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}")
