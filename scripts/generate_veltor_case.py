"""Generate the VELTOR Motorcycle Gear Store Twin Case pages across TW, EN, and JP."""

from pathlib import Path
import html
import json
import re

ROOT = Path(r"F:\共用雲端硬碟\營運資料庫\60_數位資產\B2B_網站與行銷\Website_Big_Fame")
SLUG = "case-veltor-motorcycle-store"
BASE = "https://www.bigfame.co"

PAGES = {
    "tw": {
        "lang": "zh-Hant-TW",
        "label": "繁中",
        "title": "VELTOR 摩托部品品牌店模組化展示系統",
        "description": "VELTOR 摩托部品品牌概念店雙生案例：從日常通勤到週末遠行，整合 7 大模組化展示設備、重磅結構、異材質美學與單一製造窗口。",
        "kicker": "DIGITAL TWIN / RETAIL CONCEPT CASE",
        "lede": "當專業騎士裝備同時面對高重量、多元配件與品牌風格呈現，Big Fame 以「一間店・一個製造夥伴」整合 7 大模組化展示設備系統（F01–F07），將日常通勤與週末遠行的裝備體驗轉化為可量產、可跨店複製的專業零售空間。",
        "breadcrumb_cases": "應用案例",
        "home": "首頁",
        "products": "產品與能力",
        "cases": "應用案例",
        "contact": "開始詢問",
        "source_label": "DIGITAL TWIN EVIDENCE",
        "visual_alt": "VELTOR 摩托部品品牌門市完整展示空間概念圖",
        "visual_note": "本頁呈現 VELTOR 城市巡航與旅程店之數位雙生概念配置與設備研發紀錄；正式量產與個別據點合約依專案確認。",
        "sections": [
            ("客戶問題／需求脈絡", "騎士裝備多樣與高載重展示挑戰", "摩托部品涵蓋安全帽、重磅防摔外套、車靴、手套與旅行配件，尺寸與重量落差極大。傳統現成貨架承重不足、視覺生硬，且無法呈現高品質騎行生活風格。品牌方與設計師需要一套兼具專業重載結構、精緻異材質工藝與靈活擴充性的全店展示解決方案。"),
            ("店型與空間規劃", "從日常通勤到週末遠行（Urban & Touring）", "空間配置採「分區明確、動線流暢」原則：外圈牆面承擔大容量商品收納與分類；中央規劃中島桌組合一趟完整旅程裝備；入口與主動線設置主題展示架串連通勤與旅行情境；後側配置整合性諮詢櫃台提供專業服務與庫存管理。"),
            ("Big Fame 實際承擔範圍", "全店 7 大模組化展示系統工程開發", "Big Fame 擔任單一製造整合窗口（One Store, One Manufacturing Partner），負責 7 大設備系統之 3D 結構展開、五金掛載開發、金屬加工、表面塗裝、木作與壓克力異材質整合，並提供樣品驗證與包裝運輸規劃。正式工程範圍與合約規範依專案確認。"),
            ("材料與工藝方向", "工業強度鋼構與細緻質感的平衡", "採用炭灰粉體烤漆鋼管結構（高承重防刮）、礦物米色紋理牆板、白蠟木與沙色木質板材、耐磨五金掛勾、高透光壓克力與整合式線性照明，確保堅固耐用同時兼顧現代風格零售美學。"),
            ("交付準備與模組化邊界", "模組化預製與跨店鋪快速複製", "所有壁面與島架單元均採模組化工程結構設計，支援預先加工、平整包裝（Flat Pack）與標準化現場組裝，大幅縮短施工期並利於品牌跨城市展店。"),
        ],
        "fixtures_title": "7 大模組化展示設備單元 (F01–F07)",
        "fixtures": [
            ("F01 城市巡航鞋靴牆", "承擔大容量車靴與騎士鞋履展示，採用炭灰粉體烤漆鋼構結合礦物米色紋理牆板，多層防滑傾斜鞋托與下方收納抽屜。", "fixture-f01-footwear-wall.jpg"),
            ("F02 安全帽與旅行裝備牆", "專用弧形帽托確保安全帽穩固陳列，金屬重載懸臂與壁掛結構，可靈活混搭防摔護具與後背包懸掛。", "fixture-f02-helmet-wall.jpg"),
            ("F03 手套雨具與旅行配件牆", "密集配件展示牆，整合防盜掛勾、多功能層網、手套立體展架與長雨衣懸掛系統，配件清晰可視且易於補貨。", "fixture-f03-accessories-wall.jpg"),
            ("F04 通勤與旅行服飾架", "針對重磅真皮皮衣與防摔服設計之高承重雙桿吊掛系統，結合白蠟木層板與輔助射燈，耐重防變形。", "fixture-f04-apparel-rack.jpg"),
            ("F05 旅程規劃中島桌", "全店核心陳列點，以沙色桌面呈現主題行程的整套穿搭與裝備推薦，下方具備開放式試穿取放格位。", "fixture-f05-island-table.jpg"),
            ("F06 城市旅行主題展示架", "彈性多邊展示島架，專為季節主打商品、新上市騎士配件與限量聯名裝備打造，便於視覺陳列更換。", "fixture-f06-feature-rack.jpg"),
            ("F07 旅程諮詢櫃台與收納", "雙層服務檯面整合 POS 系統、隱藏式走線、裝備調度抽屜與保固維修收納櫃，建立專業服務形象。", "fixture-f07-counter.jpg"),
        ],
        "delivery_fields": [
            ("店型", "摩托部品專門店／騎士生活風格品牌門市（Urban Mobility Retail）"),
            ("展示產品", "7 大模組化設備（鞋靴牆、安全帽牆、配件網架、重磅服飾架、中島桌、主題架、諮詢櫃台）"),
            ("材料方向", "炭灰粉體烤漆鋼構、礦物紋理板、白蠟木、高透壓克力、展示五金配件與線性燈光"),
            ("實際承擔範圍", "展示系統概念深化、結構設計、異材質整合、樣品試製、量產製造與交付包裝規劃"),
            ("交付地／目的地", "概念發布與全球展店支援；出口由台灣單一窗口統籌海空運交付"),
            ("數量／交期", "依展店規模與模組配置量身報價；正式 MOQ 與交付時程依專案逐案確認"),
            ("公開程度", "數位雙生概念案例；特定經銷商名稱、商業報價與合約數據不予公開"),
        ],
        "faq": [
            ("這是已完成實際店面的案例嗎？", "本頁為 VELTOR 數位雙生／店鋪概念案例，展示 Big Fame 針對專業複合店型的全店模組化設備研發能力；正式專案規格與現場交付依新案簽約確認。"),
            ("Big Fame 在此類專案中能提供什麼服務？", "我們提供從店面平面需求對接、設備 3D/CAD 結構拆解、樣品試作、金屬/木作/壓克力異材質量產，到包裝與外銷出口的一站式製造夥伴服務。"),
            ("可以依照我們特定店鋪尺寸客製調整設備嗎？", "可以。所有 F01–F07 模組皆具備尺寸伸縮彈性與多種材質表面處理選項，歡迎提供平面配置圖與展示品清單進行評估。"),
            ("如何開始進行類似店鋪的專案諮詢？", "請提供店面坪數/平面圖、目標展示品類、數量、預計開幕時程與地點，我們的專案團隊將快速為您評估可行結構與報價路徑。"),
        ],
        "boundary_title": "公開證據與專案邊界",
        "boundary": "本頁公開之展示設備配置圖、3D 透視與單元規格為 Big Fame 開發之數位雙生概念模型，旨在展現系統化製造與異材質工程整合實力。特定商標權利屬原持有者所有；正式訂單、交期與測試標準依商業合約為準。",
        "cta_title": "打造您的專業品牌展示空間",
        "cta": "無論是重機部品、戶外裝備或生活風格門市，提供您的空間平面與商品規劃，讓 Big Fame 成為您的全店製造夥伴。",
        "cta_text": "提出展示設備需求",
    },
    "en": {
        "lang": "en",
        "label": "EN",
        "title": "VELTOR Motorcycle Gear Store Modular Fixture System",
        "description": "VELTOR Motorcycle Gear Store Twin Case: from daily commute to weekend touring, integrating 7 modular display systems, heavy-duty engineering, mixed materials, and single-source manufacturing.",
        "kicker": "DIGITAL TWIN / RETAIL CONCEPT CASE",
        "lede": "When professional motorcycle riding gear demands heavy load capacity, diverse hardware accessories, and refined brand lifestyle aesthetics, Big Fame provides 7 modular fixture systems (F01–F07) under a single manufacturing partner model to turn complex retail challenges into scalable, reproducible store environments.",
        "breadcrumb_cases": "Applications",
        "home": "Home",
        "products": "Products",
        "cases": "Applications",
        "contact": "Start an inquiry",
        "source_label": "DIGITAL TWIN EVIDENCE",
        "visual_alt": "VELTOR motorcycle gear store complete concept retail display space",
        "visual_note": "This page documents the digital twin configuration and fixture engineering of the VELTOR Urban & Touring Store; production orders and site contracts are project-specific.",
        "sections": [
            ("Client Problem & Context", "Heavyweight Gear & Diverse Retail Challenges", "Motorcycle gear encompasses heavy riding jackets, helmets, riding boots, gloves, rainwear, and touring accessories with extreme variations in weight and dimensions. Standard retail shelves lack structural load capacity and fail to convey high-end lifestyle quality. Designers and brands need a complete store fixture system combining heavy-duty engineering with architectural craftsmanship."),
            ("Store Type & Space Layout", "From Urban Commute to Weekend Touring", "The layout follows clear functional zoning: perimeter walls provide high-capacity product storage and disciplined categorization; the central island table curates complete journey gear outfits; feature display racks at entrances capture dynamic seasonal highlights; and a consultation counter integrates customer service with inventory operations."),
            ("Big Fame's Actual Scope", "Engineering 7 Modular Fixture Systems", "Acting as a single manufacturing window (One Store, One Manufacturing Partner), Big Fame developed 3D structural drawings, custom brackets, metal fabrication, powder coating, ash wood joinery, acrylic components, and packaging engineering. Formal contractual responsibility is confirmed per project."),
            ("Materials & Craftsmanship", "Balancing Industrial Durability with Architectural Warmth", "Features charcoal grey powder-coated steel frames (scratch-resistant and high load capacity), mineral beige textured wall panels, ash wood and sand-toned surfaces, heavy-duty display hooks, clear acrylics, and integrated linear lighting."),
            ("Delivery Preparation & Modularity", "Flat-Pack Logistics & Multi-Store Scalability", "All wall and island fixtures are engineered with prefabricated modular connections for flat-pack export shipping and rapid on-site assembly, drastically reducing installation downtime across multi-city store expansions."),
        ],
        "fixtures_title": "7 Modular Display Fixture Units (F01–F07)",
        "fixtures": [
            ("F01 Urban Cruising Footwear Wall", "High-capacity riding boot and shoe display featuring charcoal grey powder-coated steel frames, mineral textured wall panels, angled non-slip trays, and lower storage drawers.", "fixture-f01-footwear-wall.jpg"),
            ("F02 Helmet & Touring Gear Wall", "Ergonomic curved helmet mounts providing secure presentation, reinforced cantilever brackets, and flexible mounting for gloves and backpacks.", "fixture-f02-helmet-wall.jpg"),
            ("F03 Gloves, Rainwear & Accessories Wall", "High-density accessory display wall combining anti-theft hooks, wire mesh grids, gloves stands, and heavy rain gear hanging systems.", "fixture-f03-accessories-wall.jpg"),
            ("F04 Commuter & Touring Apparel Rack", "Heavy-duty double-rail hanging system engineered for heavyweight leather jackets and armored riding suits, mounted on ash wood pedestals with integrated lighting.", "fixture-f04-apparel-rack.jpg"),
            ("F05 Journey Planning Island Table", "The centerpiece of the retail space, featuring a sand-toned ash wood table presenting curated touring outfits and open lower cubbies for customer fitting.", "fixture-f05-island-table.jpg"),
            ("F06 Urban Touring Feature Display Rack", "A dynamic multi-tiered feature island designed for seasonal highlights, newly launched riding accessories, and collaborative capsule releases.", "fixture-f06-feature-rack.jpg"),
            ("F07 Touring Consultation Counter & Storage", "Two-tier customer service counter integrating POS management, hidden wire routing, inventory drawers, and maintenance equipment storage.", "fixture-f07-counter.jpg"),
        ],
        "delivery_fields": [
            ("Store Type", "Motorcycle Gear Specialty Store / Urban Mobility Lifestyle Retail"),
            ("Products Displayed", "7 Modular Fixture Systems (Footwear wall, helmet wall, accessories wall, apparel rack, island table, feature rack, consultation counter)"),
            ("Material Direction", "Charcoal grey powder-coated steel, textured mineral panels, ash wood, acrylics, hardware hooks, and linear LED lighting"),
            ("Actual Scope", "Concept development, structural engineering, mixed-material fabrication, sample prototyping, mass production, and export packing"),
            ("Delivery Destination", "Concept launch and global retail support; coordinated export delivery via Taiwan shipping hub"),
            ("Quantity & Lead Time", "Quoted per store layout and modular configuration; formal MOQ and schedule confirmed upon project brief"),
            ("Public Boundary", "Digital twin concept case; individual dealer identities, commercial pricing, and contract agreements are not public"),
        ],
        "faq": [
            ("Is this a completed brick-and-mortar store project?", "This page presents the VELTOR digital twin concept store, showcasing Big Fame's full-store fixture engineering capabilities for specialized retail. Formal commercial deliveries are negotiated on a project basis."),
            ("What can Big Fame deliver in such retail projects?", "We provide complete end-to-end manufacturing coordination: architectural requirement alignment, 3D/CAD fixture drafting, prototyping, multi-material mass production, and export logistics."),
            ("Can the fixture dimensions be customized for specific floor plans?", "Yes. All units F01–F07 feature scalable modular frameworks and customizable finishes to fit your exact store architecture and visual identity."),
            ("How do we begin an inquiry for a similar store?", "Share your store layout, target merchandise categories, anticipated unit quantities, target schedule, and destination for a rapid engineering review and feasibility assessment."),
        ],
        "boundary_title": "Evidence & Project Boundaries",
        "boundary": "The store layouts, 3D renderings, and fixture specifications presented here represent Big Fame's digital twin retail concept model designed to demonstrate integrated manufacturing capabilities. Formal order volume, delivery schedules, and testing standards are governed by commercial agreements.",
        "cta_title": "Start Your Retail Fixture Project",
        "cta": "Whether developing motorcycle lifestyle, outdoor gear, or specialty retail spaces, provide your floor plan and product brief to make Big Fame your single manufacturing partner.",
        "cta_text": "Submit a Fixture Inquiry",
    },
    "jp": {
        "lang": "ja",
        "label": "JP",
        "title": "VELTOR モーターサイクルギア店舗｜モジュール什器システム",
        "description": "VELTOR モーターサイクルギア店舗デジタルツイン事例：日常の通勤から週末のツーリングまで、7大モジュール什器、高耐荷重構造、異素材美学、ワンストップ製造を統合。",
        "kicker": "DIGITAL TWIN / RETAIL CONCEPT CASE",
        "lede": "重量物、多彩なアクセサリー、ブランドの世界観を同時に満たすモーターサイクルギア店舗に向けて、Big Fameは「1店舗・1つの製造パートナー（One Store, One Manufacturing Partner）」として7大モジュール什器システム（F01〜F07）を開発。再現性と拡張性に優れたプロフェッショナルな小売空間を実現します。",
        "breadcrumb_cases": "導入分野",
        "home": "ホーム",
        "products": "製品",
        "cases": "導入分野",
        "contact": "お問い合わせ",
        "source_label": "DIGITAL TWIN EVIDENCE",
        "visual_alt": "VELTOR モーターサイクルギア店舗の全体展示空間コンセプトパース",
        "visual_note": "本ページは VELTOR アーバン＆ツーリング店舗のデジタルツイン配置および什器開発記録です。量産受注および個別店舗契約は案件ごとに確認します。",
        "sections": [
            ("顧客の課題・背景", "重量級ギアと多様な陳列要件への対応", "ヘルメット、重厚なライディングジャケット、ブーツ、グローブ、雨具、ツーリング用品など、モーターサイクルギアは寸法と重量の幅が極めて広い商材です。既成の什器では耐荷重が不足し、ブランドの高品質なライフスタイルを表現できません。プロの要求に応える堅牢な構造と精緻な意匠性を両立した店舗什器システムが求められていました。"),
            ("店舗タイプと動線計画", "日常の通勤から週末の遠出まで（Urban & Touring）", "空間は「明確なゾーニングと流れるような動線」で構成：外周壁面は大容量の展示と分類を担当；中央のアイランドテーブルで一連のツーリング装備を提案；入口と主動線にはシーズン企画什器を配置；後方には専門的なサービスと在庫管理を担うカウンターを設置しています。"),
            ("Big Fameの対応範囲", "全店7大モジュール什器システムの設計・製造", "Big Fameは単一の製造パートナー窓口として、7大什器の3D構造図面展開、特注金具開発、金属加工、粉体塗装、ホワイトアッシュ木工、アクリル加工、試作検証、輸出梱包設計までを一貫して担当。正式な契約範囲は案件ごとに確認します。"),
            ("素材と工芸の方向性", "工業的強度と上質な素材感の調和", "チャコールグレー粉体塗装スチール（高耐荷重・耐傷性）、ミネラルベージュテクスチャー壁板、ホワイトアッシュおよびサンド調木質パネル、高耐摩耗金具、高透明度アクリル、LEDライン照明を採用し、耐久性と洗練された美しさを両立しています。"),
            ("納品準備とモジュール展開", "ノックダウン梱包と多店舗展開への適合", "すべての壁面・アイランド什器はモジュール構造で設計されており、プレハブ加工、フラットパック（平積み）梱包、標準化された現場組立に対応。多都市・多店舗展開時の工期短縮に貢献します。"),
        ],
        "fixtures_title": "7大モジュール展示什器ユニット (F01–F07)",
        "fixtures": [
            ("F01 アーバンクルージング・シューズ壁", "炭灰粉体塗装スチールとミネラル調壁板を組み合わせ、多段の傾斜シューズトレイと下部収納引出を備えた大容量ブーツ展示壁。", "fixture-f01-footwear-wall.jpg"),
            ("F02 ヘルメット＆ツーリング装備壁", "ヘルメットを安全に支える専用カーブトレイ、高耐荷重片持ちブラケット、グローブやバックパックの吊り下げにも対応。", "fixture-f02-helmet-wall.jpg"),
            ("F03 グローブ・雨具＆ツーリングアクセサリー壁", "防犯フック、ワイヤーメッシュ、グローブ立体スタンド、ロングレインウェア吊り下げを統合した高密度アクセサリー壁。", "fixture-f03-accessories-wall.jpg"),
            ("F04 通勤＆ツーリングアパレルラック", "重量のあるレザージャケットやプロテクター入りウェア専用の高耐荷重2段ハンガーバー。アッシュ材台座と照明を統合。", "fixture-f04-apparel-rack.jpg"),
            ("F05 ツーリングプランニング・アイランドテーブル", "店内中央に位置し、サンド調アッシュ材天板上にフル装備コーディネートを提案。下部はオープンな試着・収納スペース。", "fixture-f05-island-table.jpg"),
            ("F06 アーバンツーリング・テーマ企画什器", "季節ごとの注目商品や新作アクセサリー、限定コラボ装備の展開に適した、柔軟な多面アイランド什器。", "fixture-f06-feature-rack.jpg"),
            ("F07 カウンター＆ストレージ", "POS端末の配線隠蔽、サービス受付、フィッティング用品やメンテ機材の引出収納を統合した2段式カウンター。", "fixture-f07-counter.jpg"),
        ],
        "delivery_fields": [
            ("店舗タイプ", "モーターサイクルギア専門店／アーバンモビリティ・ライフスタイル店舗"),
            ("展示製品", "7大モジュール什器（シューズ壁、ヘルメット壁、アクセサリー壁、アパレルラック、アイランドテーブル、企画什器、カウンター）"),
            ("材料の方向性", "チャコールグレー粉体塗装鋼管、テクスチャー化粧板、ホワイトアッシュ材、アクリル、展示金物、LED照明"),
            ("実際の対応範囲", "什器コンセプト具体化、構造設計、異素材統合、試作検証、量産製造、輸出梱包計画"),
            ("納品先／目的地", "コンセプト発表およびグローバル店舗展開支援；台湾輸出拠点からの集約出荷に対応"),
            ("数量／納期", "店舗規模・モジュール構成に応じた個別見積；正式なMOQと納期は案件ごとに確認"),
            ("公開範囲", "デジタルツイン概念事例；個別販売店情報、商業見積、契約詳細は非公開"),
        ],
        "faq": [
            ("完成納品済みの実店舗事例ですか？", "本ページは VELTOR デジタルツイン・店舗コンセプト事例であり、Big Fame の複合型専門店向け什器開発力を示すものです。実案件の仕様は個別契約によります。"),
            ("Big Fame はどのようなサポートを提供できますか？", "店舗レイアウトの確認から、3D/CAD構造図面展開、試作サンプルの製作、金属・木工・アクリルの量産製造、輸出物流までワンストップで対応します。"),
            ("店舗の指定寸法に合わせてカスタマイズできますか？", "可能です。F01〜F07の全什器は伸縮性と表面仕上げの自由度を備えたモジュール設計となっており、空間寸法に合わせて調整できます。"),
            ("相談を始めるにはどのような情報が必要ですか？", "店舗面積または平面図、展示予定の商品ジャンル、什器数量、オープン希望時期、納品先をご提供いただければ、速やかに構造提案と概算確認を進めます。"),
        ],
        "boundary_title": "公開情報の範囲と境界",
        "boundary": "本ページに掲載されている什器配置図、パース、寸法仕様は Big Fame が開発したデジタルツイン概念モデルです。正式な発注数量、納期、耐荷重試験基準は個別契約に基づいて決定されます。",
        "cta_title": "店舗什器プロジェクトのご相談",
        "cta": "モーターサイクル、アウトドア、ライフスタイル店舗の什器開発について、平面図や商品要件をお知らせください。Big Fame が最適な製造体制をご提案します。",
        "cta_text": "什器要件を相談する",
    },
}


def render(locale: str, clean: bool) -> str:
    cfg = PAGES[locale]
    url = f"{BASE}/{locale}/{SLUG}"
    prefix = "../../" if clean else "../"
    contact = f"{prefix}{locale}/contact?role=designer&category=system_fixtures&requested_files=dimension_drawing"
    
    product_links = " · ".join(
        f'<a href="{prefix}{locale}/{path}">{label}</a>'
        for path, label in [
            ("modular-fixtures", "模組化展示架" if locale == "tw" else "Modular fixtures" if locale == "en" else "モジュール什器"),
            ("custom-metal-parts", "客製金屬零件" if locale == "tw" else "Custom metal parts" if locale == "en" else "カスタム金属部品"),
            ("slatwall-pegboard-accessories", "槽板／洞洞板配件" if locale == "tw" else "Slatwall / pegboard accessories" if locale == "en" else "スラットウォール／有孔ボード金具"),
            ("display-hooks", "展示掛勾" if locale == "tw" else "Display hooks" if locale == "en" else "ディスプレイフック"),
            ("pos-displays", "POS 展示架" if locale == "tw" else "POS displays" if locale == "en" else "POSディスプレイ"),
        ]
    )

    schema_breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"{BASE}/{locale}/"},
            {"@type": "ListItem", "position": 2, "name": cfg["breadcrumb_cases"], "item": f"{BASE}/{locale}/applications"},
            {"@type": "ListItem", "position": 3, "name": cfg["title"], "item": url},
        ],
    }
    schema_faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in cfg["faq"]
        ],
    }
    schema_page = {
        "@context": "https://schema.org",
        "@type": "Article",
        "name": cfg["title"],
        "headline": cfg["title"],
        "description": cfg["description"],
        "image": f"{BASE}/images/case-veltor/hero-veltor-store.jpg",
        "url": url,
        "author": {"@type": "Organization", "name": "Big Fame IND. CORP."},
        "about": "Motorcycle store retail display fixture engineering and digital twin concept",
    }

    alternates = "".join(
        f'<link rel="alternate" hreflang="{h}" href="{BASE}/{l}/{SLUG}">'
        for h, l in [("zh-TW", "tw"), ("en", "en"), ("ja", "jp"), ("x-default", "en")]
    )

    section_html = "".join(
        f'<article class="location-card reveal"><span class="section-subtitle">{html.escape(k)}</span><h3>{html.escape(t)}</h3><p>{html.escape(body)}</p></article>'
        for k, t, body in cfg["sections"]
    )

    fixtures_html = "".join(
        f'''<article class="case-library-card reveal" style="border: 1px solid var(--border-color, #e5e5e5); border-radius: 8px; overflow: hidden; background: #fff;">
            <img src="{prefix}images/case-veltor/{img}" alt="{html.escape(title)}" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
            <div style="padding: 20px;">
                <h3 style="margin-top: 0; font-size: 1.15rem; color: #1a1a1a;">{html.escape(title)}</h3>
                <p style="font-size: 0.92rem; line-height: 1.6; color: #555; margin-bottom: 0;">{html.escape(desc)}</p>
            </div>
        </article>'''
        for title, desc, img in cfg["fixtures"]
    )

    delivery_fields_html = "".join(
        f'<article class="location-card reveal"><h3>{html.escape(label)}</h3><p>{html.escape(val)}</p></article>'
        for label, val in cfg["delivery_fields"]
    )

    faq_html = "".join(
        f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>'
        for q, a in cfg["faq"]
    )

    home_link = f"{prefix}{locale}/"
    products_link = f"{prefix}{locale}/products"
    apps_link = f"{prefix}{locale}/applications"

    return f'''<!DOCTYPE html>
<html lang="{cfg["lang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{html.escape(cfg["description"], quote=True)}">
<meta property="og:type" content="article">
<meta property="og:title" content="{html.escape(cfg["title"], quote=True)} | Big Fame">
<meta property="og:description" content="{html.escape(cfg["description"], quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/images/case-veltor/hero-veltor-store.jpg">
<meta property="og:site_name" content="Big Fame IND. CORP.">
<title>{html.escape(cfg["title"])} | Big Fame</title>
<link rel="canonical" href="{url}">
{alternates}
<link rel="stylesheet" href="{prefix}css/style.css?v=20260805-p2">
<script type="application/ld+json">{json.dumps(schema_page, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(schema_breadcrumb, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(schema_faq, ensure_ascii=False)}</script>
</head>
<body>
<header class="header">
  <div class="container header-inner">
    <a href="{home_link}" class="logo">BIG FAME</a>
    <nav class="nav-menu">
      <a href="{home_link}" class="nav-link">{cfg["home"]}</a>
      <a href="{products_link}" class="nav-link">{cfg["products"]}</a>
      <a href="{apps_link}" class="nav-link active">{cfg["cases"]}</a>
      <a href="{contact}" class="nav-link nav-cta">{cfg["contact"]}</a>
    </nav>
  </div>
</header>

<main>
<section class="case-hero">
  <div class="container case-hero-grid">
    <div class="reveal">
      <div class="case-hero-kicker">{cfg["kicker"]}</div>
      <h1>{html.escape(cfg["title"])}</h1>
      <p class="case-hero-lede">{html.escape(cfg["lede"])}</p>
      <div class="case-hero-actions">
        <a class="btn btn-primary" href="{contact}">{cfg["cta_text"]}</a>
        <a class="btn btn-secondary" href="{apps_link}">{cfg["cases"]}</a>
      </div>
    </div>
    <div class="case-hero-visual reveal">
      <img class="hero-image-main" src="{prefix}images/case-veltor/hero-veltor-store.jpg" alt="{html.escape(cfg["visual_alt"], quote=True)}" loading="eager">
      <div class="case-hero-note">
        <strong>{cfg["source_label"]}</strong>
        <span>{html.escape(cfg["visual_note"])}</span>
      </div>
    </div>
  </div>
</section>

<!-- Layout and Blueprint Section -->
<section class="section section-light">
  <div class="container">
    <div class="section-header reveal">
      <span class="section-subtitle">STORE LAYOUT & FLOW</span>
      <h2 class="section-title">空間配置與動線規劃</h2>
    </div>
    <div class="grid-2" style="align-items: center; margin-bottom: 40px;">
      <div class="reveal">
        <img src="{prefix}images/case-veltor/layout-veltor-store.svg" alt="VELTOR 城市巡航與旅程店配置圖" style="width: 100%; border-radius: 8px; border: 1px solid var(--border-color, #e0e0e0); background: #eee9df; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
      </div>
      <div class="reveal">
        <article class="location-card" style="height: 100%;">
          <span class="section-subtitle">配置核心原則</span>
          <h3>「從日常通勤到週末遠行」陳列脈絡</h3>
          <p><strong>牆面承載容量：</strong>外圍高壁面集中展示大件重裝備（靴鞋、安全帽、護具雨具），分類清楚且取放有序。<br><br>
          <strong>中島整合穿搭：</strong>中央「旅程規劃中島桌」將服飾、頭盔與手套組成一趟行程建議，提升整體連帶購買體驗。<br><br>
          <strong>主題架動態調整：</strong>入口主動線配置「城市旅行主題架」，因應季節或新進系列動態更換陳列重點。<br><br>
          <strong>諮詢櫃台服務樞紐：</strong>兼顧 POS 結帳、安全走線管理與專用零件備品抽屜收納。</p>
        </article>
      </div>
    </div>
  </div>
</section>

<!-- 7 Fixture Units Section -->
<section class="section">
  <div class="container">
    <div class="section-header reveal">
      <span class="section-subtitle">MODULAR FIXTURE UNITS</span>
      <h2 class="section-title">{html.escape(cfg["fixtures_title"])}</h2>
      <p style="color: var(--text-secondary); max-width: 760px; margin: 0 auto; font-weight: 300;">每一項設備皆為重載使用情境獨立研發，兼顧五金耐用度、模組化通用規格與極致的陳列質感。</p>
    </div>
    <div class="grid-3" style="gap: 24px; margin-top: 36px;">
      {fixtures_html}
    </div>
  </div>
</section>

<!-- Concept Drawings & System Isometric -->
<section class="section section-light">
  <div class="container">
    <div class="section-header reveal">
      <span class="section-subtitle">ENGINEERING & SYSTEM ARCHITECTURE</span>
      <h2 class="section-title">系統爆炸軸測與空間透視</h2>
    </div>
    <div class="grid-2" style="gap: 32px; align-items: stretch;">
      <div class="reveal" style="background: #fff; border-radius: 8px; border: 1px solid #e5e5e5; padding: 24px; text-align: center;">
        <img src="{prefix}images/case-veltor/concept-isometric-system.jpg" alt="展示系統爆炸軸測圖" style="width: 100%; max-height: 480px; object-fit: contain; margin-bottom: 16px;">
        <h4 style="margin: 0 0 8px 0;">展示系統模組爆炸軸測圖</h4>
        <p style="font-size: 0.9rem; color: #666; margin: 0;">預製矩形鋼管立柱、模組化橫撐結構、水平掛軌與快速可拆式配件系統。</p>
      </div>
      <div class="reveal" style="background: #fff; border-radius: 8px; border: 1px solid #e5e5e5; padding: 24px; text-align: center;">
        <img src="{prefix}images/case-veltor/store-aisle-view.jpg" alt="店內中央主走道實景透視" style="width: 100%; max-height: 480px; object-fit: cover; border-radius: 6px; margin-bottom: 16px;">
        <h4 style="margin: 0 0 8px 0;">中央走道空間透視與異材質搭配</h4>
        <p style="font-size: 0.9rem; color: #666; margin: 0;">炭灰鋼構消光烤漆與溫潤白蠟木結合，輔以線性投射燈光引導視線焦點。</p>
      </div>
    </div>
  </div>
</section>

<!-- Contract Delivery Evidence & Boundaries -->
<section class="section section-light" data-bf-case-contract="1">
  <div class="container">
    <div class="section-header reveal">
      <span class="section-subtitle">CONTRACT DELIVERY RECORD</span>
      <h2 class="section-title">可公開核對的交付與證據欄位</h2>
    </div>
    <div class="grid-3">
      {delivery_fields_html}
    </div>
    <p class="section-note reveal">{html.escape(cfg["boundary"])}</p>
  </div>
</section>

<!-- Case Brief & Detail Scope -->
<section class="section section-light" data-bf-case-brief="1">
  <div class="container">
    <div class="section-header reveal">
      <span class="section-subtitle">CASE BRIEF</span>
      <h2 class="section-title">摩托部品專案需求、交付維度與製造邊界</h2>
    </div>
    <div class="grid-2">
      {section_html}
    </div>
  </div>
</section>

<!-- FAQ Section -->
<section class="section section-light" data-bf-faq="1">
  <div class="container">
    <div class="section-header reveal">
      <span class="section-subtitle">FAQ</span>
      <h2 class="section-title">常見問題與合作諮詢</h2>
    </div>
    <div class="grid-2">
      {faq_html}
    </div>
  </div>
</section>

<!-- Related Capabilities -->
<section class="section section-light">
  <div class="container">
    <div class="section-header reveal">
      <span class="section-subtitle">RELATED CAPABILITIES</span>
      <h2 class="section-title">相關產品與展示系統</h2>
    </div>
    <p class="reveal" style="text-align: center; font-size: 1.05rem;">{product_links}</p>
  </div>
</section>

<!-- Contextual Inquiry CTA -->
<section class="section section-dark">
  <div class="container">
    <div class="cta-block reveal">
      <h2>{html.escape(cfg["cta_title"])}</h2>
      <p>{html.escape(cfg["cta"])}</p>
      <a class="btn btn-primary" href="{contact}">{cfg["cta_text"]}</a>
    </div>
  </div>
</section>
</main>

<footer class="footer">
  <div class="container footer-bottom">
    <p>© Big Fame IND. CORP.</p>
    <a href="{apps_link}">{cfg["cases"]}</a>
  </div>
</footer>
<script src="{prefix}js/main.js?v=1.3.25"></script>
</body>
</html>'''


def main():
    print(f"Generating case pages for {SLUG}...")
    for locale in PAGES:
        # 1. Flat HTML: tw/case-veltor-motorcycle-store.html
        flat_path = ROOT / locale / f"{SLUG}.html"
        flat_content = render(locale, False)
        flat_path.write_text(flat_content, encoding="utf-8")
        print(f"Wrote {flat_path}")

        # 2. Clean URL folder: tw/case-veltor-motorcycle-store/index.html
        folder = ROOT / locale / SLUG
        folder.mkdir(exist_ok=True)
        clean_path = folder / "index.html"
        clean_content = render(locale, True)
        clean_path.write_text(clean_content, encoding="utf-8")
        print(f"Wrote {clean_path}")

    # 3. Update applications.html across tw, en, jp
    cards = {
        "tw": '''<article class="case-library-card reveal"><a href="case-veltor-motorcycle-store"><img src="../images/case-veltor-store.jpg" alt="VELTOR 摩托部品品牌店展示空間" loading="lazy"></a><div class="case-library-card-body"><div class="case-meta">Concept & Twin Case · 數位雙生／店鋪概念案例</div><h3><a href="case-veltor-motorcycle-store">VELTOR 摩托部品品牌店</a></h3><p>從日常通勤到週末遠行：整合 7 大模組化展示設備（鞋靴牆、安全帽牆、配件牆、服飾架、中島桌、主題架與諮詢櫃台），展現全店展示系統開發與一站式製造整合能力。</p><a class="case-card-link" href="case-veltor-motorcycle-store">查看店鋪概念與模組化設備配置</a></div></article>''',
        "en": '''<article class="case-library-card reveal"><a href="case-veltor-motorcycle-store"><img src="../images/case-veltor-store.jpg" alt="VELTOR Motorcycle Gear Store Display Space" loading="lazy"></a><div class="case-library-card-body"><div class="case-meta">Concept & Twin Case · Retail Concept & Twin Store</div><h3><a href="case-veltor-motorcycle-store">VELTOR Motorcycle Gear Store</a></h3><p>From daily urban commute to weekend touring: integrating 7 modular fixture systems (footwear wall, helmet wall, accessories wall, apparel rack, island table, feature rack, and consultation counter) for complete store manufacturing integration.</p><a class="case-card-link" href="case-veltor-motorcycle-store">View store concept & modular fixture configuration</a></div></article>''',
        "jp": '''<article class="case-library-card reveal"><a href="case-veltor-motorcycle-store"><img src="../images/case-veltor-store.jpg" alt="VELTOR モーターサイクルギア店舗什器空間" loading="lazy"></a><div class="case-library-card-body"><div class="case-meta">Concept & Twin Case · デジタルツイン・店舗コンセプト</div><h3><a href="case-veltor-motorcycle-store">VELTOR モーターサイクルギア店舗</a></h3><p>日常の通勤から週末のツーリングまで：7つのモジュール什器（シューズ壁、ヘルメット壁、アクセサリー壁、アパレルラック、アイランドテーブル、企画什器、カウンター）を統合した店舗什器開発記録。</p><a class="case-card-link" href="case-veltor-motorcycle-store">店舗コンセプトとモジュール什器配置を見る</a></div></article>'''
    }

    for locale, card in cards.items():
        for path in [ROOT / locale / "applications.html", ROOT / locale / "applications" / "index.html"]:
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            if SLUG not in text:
                # Find insertion position in case-library-grid
                marker = '<!-- Audience & Store Type Navigation -->'
                if marker in text:
                    marker_idx = text.find(marker)
                    grid_end_idx = text.rfind('</div>\n  </div>\n  </section>', 0, marker_idx)
                    if grid_end_idx == -1:
                        grid_end_idx = text.rfind('</div>\n </div>\n </section>', 0, marker_idx)
                    if grid_end_idx != -1:
                        text = text[:grid_end_idx] + f"   {card}\n   " + text[grid_end_idx:]
                        # Update case count if present
                        text = re.sub(r'<strong>\s*11\s*</strong>', '<strong>12</strong>', text)
                        text = re.sub(r'<span>\s*11\s*</span>', '<span>12</span>', text)
                        path.write_text(text, encoding="utf-8")
                        print(f"Updated case card in {path}")
                    else:
                        print(f"Could not find grid end before marker in {path}")
                else:
                    print(f"Marker not found in {path}")
            else:
                print(f"{SLUG} already in {path}")

    # 4. Update sitemap.xml
    sitemap_path = ROOT / "sitemap.xml"
    if sitemap_path.exists():
        sitemap_text = sitemap_path.read_text(encoding="utf-8")
        if SLUG not in sitemap_text:
            sitemap_entries = []
            for locale in ["tw", "en", "jp"]:
                sitemap_entries.append(f"  <url>\n    <loc>{BASE}/{locale}/{SLUG}</loc>\n  </url>")
            entries_str = "\n".join(sitemap_entries)
            if "</urlset>" in sitemap_text:
                sitemap_text = sitemap_text.replace("</urlset>", f"{entries_str}\n</urlset>")
                sitemap_path.write_text(sitemap_text, encoding="utf-8")
                print(f"Updated sitemap.xml with {SLUG} URLs")

    # 5. Also copy this script into Website_Big_Fame/scripts/
    scripts_dest = ROOT / "scripts" / "generate_veltor_case.py"
    scripts_dest.write_text(Path(__file__).read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Saved generator script to {scripts_dest}")

    print("VELTOR case generation completed successfully!")


if __name__ == "__main__":
    main()
