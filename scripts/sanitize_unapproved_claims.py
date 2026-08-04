"""Replace evidence-gated legacy claims with conservative public-safe wording."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    # Shared visual/footer claims.
    '<span class="logo-sub">IND. CORP. EST. 1988</span>': '<span class="logo-sub">IND. CORP.</span>',
    '&copy; 1988-2026 Big Fame IND. CORP. All Rights Reserved.': '&copy; Big Fame IND. CORP. All Rights Reserved.',
    # Generic company positioning without a founding-year claim.
    '創立於 1988 年。商業展示設備與零售陳列五金的全球整合夥伴。': '商業展示設備與零售陳列五金的整合夥伴。',
    '創立於 1988 年。協助海外客戶在台灣完成商業展示設備採購與出口整合。': '協助海外客戶在台灣完成商業展示設備採購與出口整合。',
    'Established in 1988. A global integration partner for commercial display fixtures and retail merchandising hardware.': 'A global integration partner for commercial display fixtures and retail merchandising hardware.',
    'Established in 1988. We help overseas buyers source commercial display fixtures from Taiwan and coordinate export delivery.': 'We help overseas buyers source commercial display fixtures from Taiwan and coordinate export delivery.',
    '1988年設立。小売ブランドの成長を支える、店舗什器および陳列金具のグローバル統合パートナー。': '小売ブランドの成長を支える、店舗什器および陳列金具のグローバル統合パートナー。',
    '1988年設立。海外企業の台湾調達を支援し、店舗什器の生産と輸出を調整します。': '海外企業の台湾調達を支援し、店舗什器の生産と輸出を調整します。',
    # About-page descriptions.
    '創立於 1988 年，總部位於台灣台北，是一家專業的商業展示設備與零售陳列五金整合開發公司。': '以台灣為採購與整合切入，專注於商業展示設備與零售陳列五金的開發協作。',
    'Established in 1988, Big Fame IND. CORP. is a Taiwan-based B2B partner for commercial display fixtures and retail merchandising hardware integration.': 'Big Fame IND. CORP. is a B2B partner for commercial display fixtures and retail merchandising hardware integration, with Taiwan as a sourcing base.',
    'ビッグフェイム（碧豐實業）は1988年に台湾台北で設立された、商業用店舗什器・小売店陳列用五金（金具）の専門メーカーおよび統合企業です。': 'ビッグフェイム（碧豐實業）は、台湾を調達・連携の拠点とする商業用店舗什器・小売店陳列用金具のB2Bパートナーです。',
    'ビッグフェイム（碧豐實業有限公司）は1988年、台湾の台北市で設立されました。私たちは、小売空間における「商品展示デバイス（什器・金具）」のカスタム開発およびサプライチェーン統合のスペシャリストです。': 'ビッグフェイム（碧豐實業有限公司）は、台湾を拠点に小売空間の商品展示デバイス（什器・金具）のカスタム開発とサプライチェーン連携を支援します。',
    # Public-safe location/capability wording.
    '三大服務據點的分工': '專案協作方式',
    'Synergy Across Three Locations': 'Project Collaboration Model',
    '彰化倉儲據點': '製造與物流協作',
    'Changhua Logistics': 'Manufacturing and Logistics Coordination',
    '彰化物流拠点': '製造・物流の連携',
    '彰化物流拠点での出荷前確認': '出荷前のプロジェクト確認',
    '彰化物流拠点での出荷前品質確認 (QC)': '出荷前のプロジェクト品質確認 (QC)',
    'Malaysia Branch': 'Supply Coordination',
    '馬來西亞分公司': '供應協作',
    'Located near manufacturing clusters in central Taiwan, this facility manages secondary quality checks, coating testing, secure flat-packing, cargo consolidation, and container dispatching.': 'Depending on the project, we coordinate secondary checks, packing, cargo consolidation and container dispatching with the relevant partners.',
    '面對零售通路變化劇烈、交期緊迫的特質，我們以台北團隊的高效開發實力、彰化據點的嚴格品管把關、以及馬來西亞的備份生產能力，為客戶提供高度彈性的客製化採購協調，成為值得長期信賴的策略夥伴。': '依專案條件協調需求釐清、製造夥伴、品質確認、包裝與出口安排；實際承擔範圍以核准規格確認。',
    'Established in 1988. A global integration partner': 'A global integration partner',
    '1988年設立。店舗什器および陳列金具のグローバル統合パートナー。': '店舗什器および陳列金具のグローバル統合パートナー。',
    '<!-- Changhua -->': '<!-- Logistics coordination -->',
    '<!-- Malaysia -->': '<!-- Supply coordination -->',
    '碧豐實業有限公司 (Big Fame IND. CORP.) 創立於 1988 年，總部位於台灣台北。我們是一間專業的商業展示設備與零售陳列五金整合開發公司。': '碧豐實業有限公司 (Big Fame IND. CORP.) 以台灣為採購與整合切入，專注於商業展示設備與零售陳列五金的開發協作。',
    '碧豐實業自 1988 年成立以來，專注於商業展示設備與零售陳列五金的專案整合。': '碧豐實業專注於商業展示設備與零售陳列五金的專案整合。',
    '碧豐實業自 1988 年成立以來，專注於商業展示設備與零售陳列五金的專案整合。': '碧豐實業專注於商業展示設備與零售陳列五金的專案整合。',
    '碧豐實業有限公司 (Big Fame IND. CORP.) 創立於 1988 年，總部位於台灣台北。我們是一間專業的商業展示設備與零售陳列五金整合開發公司。': '碧豐實業有限公司 (Big Fame IND. CORP.) 以台灣為採購與整合切入，專注於商業展示設備與零售陳列五金的開發協作。',
    '位於製造資源豐富的彰化地區，擁有大面積倉庫。主要負責金屬五金的尺寸比對、烤漆電鍍膜厚與防鏽測試、拼箱混載、包裝跌落測試與大型貨櫃裝載出貨調度。': '依專案條件協調尺寸、外觀、數量、包裝、集貨與出貨安排；檢查項目以核准規格確認。',
    '台湾中部の製造集積地に近い彰化に大規模倉庫を構えています。製品のアセンブリ検査、防錆確認、パッケージングの強度検査を行った後、コンテナ詰めや混載出荷の手配を行います。': '案件条件に応じて、組立、外観、数量、梱包、混載、出荷条件を調整します。確認項目は承認仕様に基づきます。',
    'Since 1988, Big Fame has helped overseas clients source commercial display fixtures and retail merchandising hardware from suitable Taiwan manufacturing partners.': 'Big Fame helps overseas clients source commercial display fixtures and retail merchandising hardware from suitable Taiwan manufacturing partners.',
    '近四十載深耕，專注實體現場的陳列硬體整合': '專注實體現場的陳列硬體整合',
    'Decades of Display Fixture & Retail Hardware Integration': 'Display Fixture & Retail Hardware Integration',
    '近四十年にわたる、小売店舗ディスプレイ什器の統合実績': '小売店舗ディスプレイ什器の統合協作',
    'For nearly 40 years, we have served leading B2B retail markets across Japan, Europe, and North America. Our partnerships span diverse retail industries, including daily goods, apparel, sports lifestyle, eyewear accessories, and large retail chain stores.': 'Our capability materials cover retail display fixtures, merchandising hardware and project integration across multiple store-type scenarios.',
    '長期以來，我們深耕日本、歐美等國際零售市場。合作的產業非常廣泛，涵蓋生活用品、服飾、運動用品、眼鏡配件與大型連鎖通路等領域。': '公開素材涵蓋生活用品、服飾、運動用品、眼鏡配件與零售店型等展示情境；實際專案範圍依需求確認。',
    '長年にわたり、日本、欧米などのグローバル小売市場に深く関わり、生活雑貨、アパレル、スポーツ用品、アイウェア、および大型のドラッグストアやスーパーマーケットチェーンなど、多岐にわたる産業に対して店舗資材を提供してまいりました。': '公開素材では、生活雑貨、アパレル、スポーツ用品、アイウェアなどの店舗展示シーンを紹介しています。実際の案件範囲は要件により確認します。',
    '38+': '—',
    '國際專案執行經驗 (年)': '可追蹤專案流程',
    'Years of Project Experience': 'Project Workflow',
    'グローバルプロジェクト経験（年）': 'プロジェクト連携',
    '全球主要服務據點': '專案協作範圍',
    '3つのB2B連携の役割': 'B2B連携の役割',
    'ASEAN Resources Integration & Supply Chain Diversity': 'Project-based Supplier Coordination',
    '東南亞生產與供應鏈整合、地緣風險分散': '依專案條件協調供應夥伴與交付安排',
    '東南アジア生産管理・地理的分散供給': '案件ごとのサプライヤー連携',
    '碧豐實業前進東南亞市場的重要門戶。管理當地合約代工廠的產能與品質，以合理的生產成本結構，為客戶提供在台灣之外的供應備份，抵禦單一地緣政治風險。': '依專案條件協調供應夥伴、品質確認與交付安排；實際供應角色需逐案確認。',
    'Serving as our expansion hub for Southeast Asia, this location monitors local production partners and coordinates supply backup lines, mitigating trade disruptions and geopolitical risks.': 'We coordinate relevant suppliers and delivery conditions according to each project; the actual supply role is confirmed case by case.',
    'ASEAN市場への展開ハブとして機能するとともに、現地サプライヤーの開拓・生産品質管理を行います。地政学的リスクによるサプライチェーンの停滞を防ぎ、安定的な供給オプションを提供します。': '案件条件に応じてサプライヤー、品質確認、納品条件を調整します。実際の供給範囲は案件ごとに確認します。',
}

for folder in ("tw", "en", "jp"):
    for path in (ROOT / folder).glob("*.html"):
        text = path.read_text(encoding="utf-8")
        for old, new in REPLACEMENTS.items():
            text = text.replace(old, new)
        # Repair a previous normalizer edge case where an optional path prefix
        # was serialized as the literal string "None".
        text = text.replace('href="Noneapplications#brand"', 'href="procurement"')
        text = text.replace('href="Noneapplications#designer"', 'href="design-support"')
        text = text.replace('href="Noneapplications#trading"', 'href="procurement"')
        text = text.replace('href="Noneapplications', 'href="applications')
        text = text.replace('href="Noneproducts', 'href="products')
        text = text.replace('href="Nonecontact', 'href="contact')
        # Remove the gated JSON-LD foundingDate field without damaging the object.
        text = re.sub(r'\s*"foundingDate"\s*:\s*"1988"\s*,?', '', text)
        # Replace remaining named-site claims in service narratives.
        text = text.replace("Changhua warehouse inspections", "project-based inspection coordination")
        text = text.replace("a Changhua logistics point", "a designated logistics point")
        text = text.replace("Changhua QC inspect hubs, and Malaysia supply lines backup", "project-based QC coordination and supplier coordination")
        text = text.replace("彰化倉庫での検品", "案件ごとの検品調整")
        text = text.replace("彰化の物流拠点", "指定物流拠点")
        text = text.replace("彰化倉庫での徹底した検品、マレーシア支社による供給バックアップ", "案件ごとの検品調整とサプライヤー連携")
        text = text.replace("塗膜附著力檢測", "依核准規格確認")
        text = text.replace("coating adhesion", "approved-specification checks")
        text = text.replace("塗膜の付着", "承認仕様に基づく確認")
        # The numeric history tile is not a verified public fact yet.
        text = re.sub(r'<div class="num">1988</div>', '<div class="num">—</div>', text)
        text = text.replace('Global Locations', 'B2B Integration')
        text = text.replace('グローバル拠点', 'B2B連携')
        path.write_text(text, encoding="utf-8")
