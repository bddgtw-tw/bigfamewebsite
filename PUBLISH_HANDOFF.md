# Big Fame 網站升級發布交接

更新日期：2026-08-04

## 目前已確認的狀態

### 本地／Git

- 專案位置：本專案工作樹
- 正式分支：`main`
- 開發分支：`draft`
- Git remote：`https://github.com/bddgtw-tw/bigfamewebsite.git`
- 網站內容目前發布提交：`dce5c00`；後續若只修改本交接文件，不改變網站內容版本。
- 網站內容包含三語首頁、TA 入口、產品頁、案例頁、服務頁與詢問頁。

### 公開 `bigfame.co`

目前已由公開 HTTP 與 DOM 檢查確認：

- `https://www.bigfame.co/tw/` 回應 200
- 三個語言版本的 TA 入口、產品頁、詢問頁與 sitemap 可公開讀取
- 公開版已具備 clean URL、canonical、hreflang、TA 入口、案例與詢問流程
- 舊 `/thank-you-page`、`/our-works` 等網址可導向新頁面
- 公開版 `main.js` 已驗證包含 `bf_page_context`、`bf_contact_cta_click`、`form_start` 與 `generate_lead`

完整 sitemap 驗收（2026-08-04）：81 個公開網址全部回應 200；81／81 具備單一 canonical、至少三個 hreflang 與單一 H1。

最新新增的 PAGE 桌上型化妝品收納展示器「產品開發資料紀錄」已在三語公開網址驗證；頁面保留 2020-03-30 ver.01 文件的尺寸、材質、包裝與交期證據，並明確標示未核准的客戶、MOQ、交付與成果欄位。

最新新增的「展示設備規格與 CAD 資料索取」三語入口已公開驗證；頁面提供代表性尺寸圖與 CAD／PDF／DWG／DXF／STEP 索取流程，但不公開未核准的通用 CAD 或產品承重資料。

三語技術入口的 CAD 打樣 FAQ 已以 UTF-8 公開內容驗證：繁中、英文、日文頁面皆回應 200，且各自包含對應語言的 CAD 打樣問題與條件邊界。

三語「服飾店展示設備」店型搜尋入口已公開驗證：三個頁面皆回應 200，具備單一 H1、FAQ 與展示設備需求情境；此頁是 TA／搜尋入口，不是已核准的具名客戶案例，產品、數量、交期與交付地仍需逐案確認。

三語首頁主要「提交需求／專案諮詢」CTA 已公開驗證帶有 `category=integration&role=buyer`，可將首頁訪客帶入展示設備整合與採購角色脈絡；通用導覽列仍保留未預填的聯絡入口。

三語 `case-apparel-2016` 已公開驗證：頁面使用來源資料夾中的服飾門市照片，整理為匿名、證據控制的照片紀錄，並明確標示不能由照片推定客戶、Big Fame 承擔範圍、數量、交期、交付地或成果；此頁不是完整交付案例。

公開瀏覽器驗證 `apparel-store-fixtures` 的 GA4 `bf_page_context` 已回報 `page_type=ta_entry`、`ta_entry=apparel-store-fixtures`，網站版本為 `1.3.13`；服飾店型入口可與其他 TA 入口分開量測。

英文首頁、applications、services、anti-theft hooks、technical resources 與 PAGE cosmetic record 的公開 HTML 已讀回驗證：description 已更新，且各頁仍保有單一 canonical；其餘英文頁面也已完成 title／description／canonical 全量盤點。

三語 `/products` 公開 HTML 已驗證移除未有證據支持的通用 MOQ／交期數字與準時交付承諾；頁面改為依 SKU、圖面、材料、數量、排程與交貨地逐案確認。三語產品總頁皆回應 200、單一 H1，sitemap 維持 81 個網址。

三語 `apparel-store-fixtures` 公開 HTML 已驗證新增 `case-apparel-2016` 內部連結；服飾店型、照片證據、相關產品與詢價流程現在形成可追蹤的內容群集。

三語 `applications` 的服飾案例卡片已公開驗證新增圖片、標題與「照片證據／可確認範圍」入口，直接連到 `case-apparel-2016`；公開回讀三語均回應 200 且找到案例卡片 CTA。

三語 `applications` 的眼鏡案例卡片已公開驗證新增圖片、標題與「案例證據／展示掛勾脈絡」入口，直接連到 `case-eyewear-2016`；公開回讀三語均回應 200 且找到案例卡片 CTA。

三語 `applications` 案例網格已公開驗證在卡片層標示證據狀態：照片紀錄、匿名案例影像／專案紀錄與系統開發紀錄；此標示不增加任何未核准的客戶、數量或成果主張。

英文與日文 `applications` 案例網格已公開驗證由 4 張補齊為 7 張，新增 IVY 系統開發、匿名旅宿家具與匿名 3C 門市三筆既有證據頁入口；三語公開頁均回應 200 且找到三個對應 clean URL。

已重新讀回 `40_Projects_案例` 原始文件，確認 Urban Warehouse Self Storage 是目前最接近完整 B2B 證據的候選：來源可支持客戶問題、50+ 元件、約 3.4 m³、材料、K/D 運輸方向與已開放／可複製結果；正式合約角色、數量、交期、交付地與授權仍未核准。完整讀回見 `CASE_EVIDENCE_READBACK_2026-08-04.md`。

三語首頁、關於 Big Fame、產品總覽與服務頁共 12 個非聯絡核心頁已新增可見 FAQ 與 FAQPage JSON-LD；本地驗收 `NON_CONTACT_GAPS=0`，公開讀回也確認 12／12 回應 200、單一 H1、至少一個 H2、FAQPage 與單一 canonical。聯絡頁仍以表單流程為主，未套用一般內容頁 FAQ 條件。

三語關於、應用案例、產品總覽、服務、防盜展示掛勾、客製金屬零件與 POS 展示架頁面已補齊 BreadcrumbList；本地 30／30 檔案與公開 clean URL 21／21 讀回均通過。部署曾短暫回傳舊版，約 35 秒後再次讀回已確認新結構化資料生效；完整紀錄見 `STRUCTURED_DATA_AUDIT_2026-08-04.md`。

8 類產品三語頁面的可見內容品質驗收已通過 24／24；除 FAQPage JSON-LD 外，所有頁面均有可核對的可見 FAQ 標記、相關案例連結與帶 category 的詢價 CTA。公開 clean URL 24／24 第二次讀回通過，完整規則與限制見 `PRODUCT_PAGE_CONTRACT_AUDIT_2026-08-04.md`。

三語案例頁共 24 頁已補齊證據欄位狀態；對來源未提供或未核准的客戶問題、材質、Big Fame 分工、數量、交期與交付地，頁面明示未公開或需逐案確認。新增區塊的公開 clean URL 17／17 已驗證 200、單一 H1、FAQ、情境式 CTA 與單一 canonical；完整限制見 `CASE_PAGE_CONTRACT_AUDIT_2026-08-04.md`。

採購、設計支援、展示掛勾與技術資源四類三語入口，共 12 頁已加入直接貼近 TA 搜尋問法的 FAQ；本地 `SEARCH_INTENT_FAILURES=0`，公開第二次讀回 12／12 通過。搜尋意圖與頁面對應見 `SEARCH_INTENT_MAP_2026-08-04.md`。

`MEASUREMENT_BASELINE.md` 已同步至公開版本 `1.3.13`，新增 `apparel-store-fixtures` 的 TA 量測分類，並記錄 390px 公開瀏覽器驗收已確認首屏可讀與 CTA 可點擊；真實使用者速度與點擊率仍待 GA4／Search Console 資料累積。

2026-08-04 已從登入後 Search Console 實際讀回 2026-07-16 至 2026-08-02 的成效資料：4 clicks、383 impressions、CTR 1%、平均排序 9.7、26 個查詢與 24 個曝光頁；完整查詢／頁面清單與限制記錄於 `SEARCH_CONSOLE_LIVE_READBACK_2026-08-04.md`。資料仍以品牌詞與舊網址曝光為主，不能宣稱非品牌 TA 已大量轉換。

8 類產品的三語頁面契約驗收已記錄於 `PRODUCT_PAGE_CONTRACT_AUDIT_2026-08-04.md`：24／24 頁未出現 `MISSING_CONTRACT`；該驗收只證明欄位與確認邊界存在，不把未核准規格視為已完成。

舊 `/overview`、`/contact-us`、`/thank-you-page`、`/our-works`、`/know-how`、`/blog` 與兩個舊 blog 路徑已公開回應 301，分別導向現行的 about、contact、applications、services、about 或 display-hooks clean URL。

英文目錄目前 43 個 HTML 頁面均具備 title、meta description 與 canonical；首頁、services、applications、anti-theft hooks、PAGE cosmetic record 與 technical resources 的描述已完成採購、展示設備、案例或 CAD 搜尋語意盤點，後續仍可依 Search Console 查詢詞做精修。

### 最新部署驗證

已於 2026-08-04 重新讀取公開網址並確認：

- 三語 `/procurement` 均回應 200，且包含 `custom-metal-parts` 連結。
- 三語 `/display-hooks` 均回應 200，且包含 `anti-theft-hooks` 連結。
- 這六個連結已由本地、Git `main`、Git `draft` 與公開網站逐層驗證。
- `f1d6544` 發布後，公開 `/en/display-hooks`、`/en/case-eyewear-2016`、`/tw/optical-hooks`、`/jp/case-urban-storage` 均回應 200，並已讀回三個 TA 導流連結與正確 canonical；公開部署有短暫延遲，需以延遲後讀回結果為準。
- 英文 `case-page-cosmetic-organizer` 與 `technical-resources` clean URL 亦已讀回 200、正確 canonical、description 與 Open Graph description。
- 新增 `CASE_EVIDENCE_READBACK_3C_2026-08-04.md`：讀回 Second Hand Apple Store 原始長敘述，確認三語 `case-modular-3c-store` 已使用文件支持的客戶問題、展示物、材料方向、模組化、運輸／組裝與台北首店背景；數量、交期、交付地與合約範圍仍保留為未公開欄位。
- 三語首頁 `og:url` 已由 `/tw/index`、`/en/index`、`/jp/index` 統一修正為各自的 clean URL；延遲後公開讀回確認三頁均與 canonical 完全一致。
- 新增 `scripts/add_missing_open_graph.py`，以既有 title、description 與 canonical 為唯一來源，為 119 個原本缺少 Open Graph 的三語頁面補齊分享 metadata；未新增產品規格、客戶名稱或成果主張。發布後需抽驗案例、產品、TA 入口與聯絡頁。
- `97bf222` 發布後，公開 `/en/display-hooks`、`/en/case-modular-3c-store`、`/tw/procurement`、`/jp/contact`、`/en/technical-resources` 均回應 200；五頁均已讀回 Open Graph description，且 `og:url` 與 canonical 一致。產品／案例頁的 TA 導流連結亦正常。
- `c5ecbcd` 修正三語 `applications` 頁摘要數字：頁面實際有 7 個案例卡片，Hero 與 `SELECTED CASES` 已由 `04` 統一為 `07`。延遲部署後公開 `/tw/applications`、`/en/applications`、`/jp/applications` 均回應 200；公開 DOM 讀回三頁各 7 張案例卡、2 個 `07` 摘要數字、0 個舊 `04` 數字，且各頁維持單一 H1。
- 展示掛勾產品原始文件讀回記錄於 `PRODUCT_EVIDENCE_READBACK_DISPLAY_HOOKS_2026-08-04.md`：`Product Hook.docx` 支持 wire hook、50／75／100／150／200 mm 長度、Φ5／Φ6／Φ8／Φ10 線徑、crossbar 長條尺寸與 pegboard／slatwall／wire shelving 方向。三語 flat 與 clean route 共 6 個頁面已加入來源區塊；頁面明確保留 SKU、材質牌號、表面處理、MOQ 與交期的確認邊界。
- `a4bb888` 發布延遲後，公開 `/tw/display-hooks`、`/en/display-hooks`、`/jp/display-hooks` 均讀回 200、單一 H1、`Product Hook.docx` 來源標記與 50／75／100／150／200 mm 證據；三頁均未讀到未核准的 500 pcs 通用承諾。公開瀏覽器亦確認繁中頁的來源卡片、3 個 TA 導流連結與證據文字可見。
- EYEHK 三語 `optical-hooks` flat／clean route 共 6 頁已加入 PDF 圖面證據：2025 洞洞板版本的尺寸與雷射切割／焊接備註、2018 鎖螺絲／溝槽板版本的 t2.0 鐵板、4.0 mm 鐵線、黑色粉體烤漆、倒角與約 2° 上仰。`PRODUCT_EVIDENCE_READBACK_EYEHK_2026-08-04.md` 記錄了圖面可支持與不可宣稱的邊界；新增兩個圖面問題至可見 FAQ 與 FAQPage JSON-LD，未把 1000 支估價備註當成訂單數量或 MOQ。
- EYEHK 頁面另加入原始照片檔名中的代表識別 `EYEHK-010B／010C／010W／020B／020C／020W`，供採購詢問時提供線索；頁面與證據紀錄均明示這些檔名不等於正式 SKU、顏色代碼或目前供應承諾。

## 發布後仍需持續確認

- P0 metadata 已在本地更新：英文 `applications`、`case-page-cosmetic-organizer`、`technical-resources` 的 `og:description` 與結構化資料描述，已改為較精準的 B2B 搜尋語意，未新增未核准的客戶、數量、測試或交付主張。這三頁需隨下一次網站內容發布後，再做公開 URL readback。
- 三語產品與案例頁已補上「採購／設計支援／技術與 CAD 資源」TA 導流區塊，共 90 個本地頁面版本（含 clean route 對應的 `index.html`）；頁面只使用既有 clean URL，未引入 `.html` 內部連結。

1. 持續檢查公開版 sitemap、canonical、hreflang 與 Git `main` 是否一致；部署後需容許 CDN 延遲並以第二次讀回為準。
2. 持續補足證據登錄表中尚未核准公開的數量、交期、客戶名稱與成果主張。
3. 以 GA4 與 Search Console 28 天資料判斷 TA 入口、產品頁與詢問轉換。

## 不能宣稱的事項

- `MEASUREMENT_FORM_FUNNEL_UPDATE_2026-08-04.md` 記錄新增的 `bf_form_submit_attempt` 與 `bf_form_submit_error`；本次只完成程式與靜態驗證，未提交公開表單，尚未宣稱新的 `generate_lead` 已在 GA4 實際發生。
- `584e606` 發布延遲後，公開 `js/main.js` 已讀回 `bf_form_submit_attempt`、`bf_form_submit_error` 與既有 `generate_lead`；公開 `/en/contact` 回應 200，表單與來源脈絡 hidden fields 均存在。

- 不把本地或 Git 已完成的變更直接稱為公開網站已完成部署。
- 不把候選案例當成已取得公開授權的正式客戶案例。
- 不把未核對的測試數據、客戶名稱、所有權、MOQ、交期或市場地位寫成既定事實。

- 本輪新增 `scripts/normalize_hreflang_absolute.py`，將 `tw/`、`en/`、`jp/` 15 個語系主頁的 45 個相對 `hreflang` 連結統一為 `https://www.bigfame.co` 絕對 clean URL；本地讀回 `RELATIVE_HREFLANG_COUNT=0`。這只證明 URL 標記已統一，不代表 Search Console 已重新處理或排名已改善。
- `97b1404` 發布後，延遲讀回公開 `/tw/about`、`/en/products`、`/jp/about` 與 `/jp/products` 均回應 200，四個 hreflang 標記均為絕對 `https://www.bigfame.co/...` clean URL；`/overview` 與 `/tw/contact-us` 仍回應 301 至現行網址。第一次讀回日文 products 曾受部署延遲影響，第二次以 cache-buster 讀回後已更新。
- IVY／25×40 系統三語 flat／clean route 共 6 頁已加入兩份原始來源文件名稱、可核對的 25×40／600 mm／M6／元件證據與明確證據邊界；`CASE_EVIDENCE_READBACK_IVY_2026-08-04.md` 已記錄來源與不可宣稱項目。此頁定位為系統開發／樣品圖面紀錄，不宣稱客戶安裝或最終交付。
- `44a86bb` 公開部署第一次讀回仍是舊版；延遲後以 cache-buster 第二次讀回，`/tw/case-ivy-modular-system`、`/en/case-ivy-modular-system`、`/jp/case-ivy-modular-system` 均已出現 `SOURCE RECORD`、單一 H1 與正確 canonical。這次驗收明確區分 HTTP 200 與新內容已部署。
- 公開瀏覽器實際點擊繁中 IVY 案例 CTA 後，聯絡頁讀回 `buyer_role=store_design_engineering`、`inquiry_type=quote`、`product_category=system_fixtures`、`source_category=system_fixtures`、`source_role=designer` 與帶有案例 clean URL 的 `source_page`；未提交表單，因此未產生外部寄送副作用。
- 首頁公開桌機 runtime 讀回無橫向溢位、Hero 內有 2 個 CTA、影片已載入；手機 CSS 靜態條件包含 `100svh` Hero、單欄 CTA、44px 漢堡按鈕與 18px／24px 內距。當前瀏覽器連線未提供 viewport 切換，因此手機獨立 runtime 仍列為待驗證，不把桌機結果冒充手機驗收。
- `730403e` 修正 2 個英文頁的重複 `og:description`，並移除英文／日文 technical resources 中語意重複的 CAD FAQ；本地 384 個 JSON-LD 區塊全部可解析。公開 `/tw/technical-resources`、`/en/technical-resources`、`/jp/technical-resources` 延遲後均回應 200、每頁 1 個 `og:description`、5 個 FAQ Question 與正確 canonical；英文 PAGE 頁也已回應 200 且只保留 1 個 `og:description`。
- `ec48adb` 發布後第一次讀回精品旅宿案例仍是舊版；延遲後第二次以 cache-buster 讀回，三語 `/case-boutique-hotel-furniture` 均已出現來源文件段落、28 房背景、單一 H1 與正確 canonical。這三頁仍定位為匿名旅宿家具專案紀錄，不宣稱完整客戶交付。
- `109916f` 發布後第一次讀回 Urban Warehouse 案例仍是舊版；延遲後第二次以 cache-buster 讀回，三語 `/case-urban-storage` 均已出現來源文件段落、超過 50 個元件、單一 H1 與正確 canonical。頁面仍明確保留正式合約分工、最終數量、交期與交付地的證據邊界。
- `6f67c56` 新增技術資料需求欄位：三語 `technical-resources` CTA 會以 `requested_files=technical_pack` 帶入聯絡表單；表單可選尺寸／規格、PDF／CAD／DWG／DXF／STEP、材質／表面處理、打樣討論或請協助判斷資料類型。`form_start`、`bf_form_submit_attempt`、`generate_lead` 與 `bf_form_submit_error` 均納入此非個資欄位；本地 `node --check js/main.js` 通過。
- `6f67c56` 公開延遲讀回：`/tw/technical-resources?v=6f67c56-r2` 回應 200，CTA 已帶 `requested_files=technical_pack`；`/tw/contact?...&requested_files=technical_pack&v=6f67c56-r3` 回應 200，公開 HTML 已包含 `requested_files` 五個選項與 `technical_pack`。本次未提交表單，尚未宣稱實際 `generate_lead` 轉換已產生。
- 本輪新增 `CASE_EVIDENCE_READBACK_STYLISH_HOTEL_2026-08-04.md`：從 `Stylish Hotel Room Furniture\長敘述.docx` 讀回小型基隆旅館客房、食飲放置空間、折疊／巢狀桌評估與旋轉盤轉出／收回機能。此為未上線的匿名案例候選；客戶授權、Big Fame 正式角色、尺寸、數量、交期、交付地與照片公開性仍待確認，未把它當成已完成交付案例。
- 新增 `GOAL_COMPLETION_AUDIT_2026-08-04.md`，逐項區分七項官網目標的「已證明／部分完成／尚未完成」，並明確記錄案例授權、最新公開讀回、手機 runtime、真實 `generate_lead` 與非品牌搜尋數據仍是未完成的驗收條件。
- 最新公開 P0 讀回：公開 `sitemap.xml` 回應 200，共 81 個 clean URL；逐一請求後 81／81 回應 200，且 canonical 與 sitemap URL 一致。三語 `procurement`、`design-support`、`display-hooks`、`contact` 均為單一 H1；`/overview`、`/contact-us`、`/tw/contact-us` 分別正確回應 301 至現行 clean URL。
- 最新公開表單讀回：`/tw/contact?category=display_hardware&role=buyer&requested_files=technical_pack` 回應 200，已包含 `requested_files`、`estimated_quantity`、`target_date`、`market`、`drawings` 與採購角色選項；此為 HTML 欄位驗收，未提交表單，未宣稱產生實際 lead。
- 本輪新增 `PRODUCT_EVIDENCE_READBACK_ISLE_2026-08-04.md`：從 Big Fame 標頭的 2020-02-24 ISLE 估價圖面讀回木／石材底盤、鐵線掛件、戒指台、展示組合、孔位、螺牙、材料方向與部分數量標註。此目前是規格／設計證據候選，不宣稱已打樣、量產、交付或取得 ISLE 名稱與圖片公開授權。
- `feb88e2` 新增三語匿名 `jewelry-display-accessories` 設計／規格入口與 sitemap clean routes；第一次公開讀回短暫 404，延遲後第二次讀回三語均 200、單一 H1、FAQPage、證據邊界與正確 canonical。繁中頁 CTA 已帶 `role=designer&category=custom_metal_components&requested_files=dimension_drawing`，公開 sitemap 已包含 3 個新 URL。頁面明確標示示意圖不是本案正式照片，未宣稱 ISLE 已交付。
- `138f881` 將三語 `custom-metal-parts` 與 `design-support` 的 flat／clean 頁面共 12 頁連到 `jewelry-display-accessories`；公開延遲讀回 `/tw/custom-metal-parts`、`/tw/design-support`、`/en/custom-metal-parts`、`/jp/design-support` 均回應 200、canonical 正確且 HTML 已包含新入口連結。

2026-08-04 交付線索盤點：從 `40_Projects_案例` 實際讀回晁雍／鐵網製成的波浪架與金久盛／角鋼架歷史報價，以及 OMO 生活用品展的產品報價與 Invoice。晁雍文件顯示 `晁雍 → 碧豐` 的報價關係，金久盛文件是舊規格／計算表，OMO 是生活用品採購而非展示設備案例；三者均未升格為 Big Fame 公開案例。完整來源、可支持內容與邊界見 `CASE_EVIDENCE_READBACK_DELIVERY_SCAN_2026-08-04.md`。

2026-08-04 新增最強案例候選：從歷史 OEM／ODM 專案 `On Time Auto Parts Rack` 讀回客戶相容性問題、Big Fame 設計回覆、2011 年多版本圖面、缺陷改善報告、組裝說明、最終設計圖、實物組裝照片與 shipping mark 檔案。候選定位為匿名 `Automotive Parts Display Rack／汽車零件展示架工程紀錄`；不公開客戶名稱、Logo、數量、交期、交貨地或未核准照片授權。完整讀回見 `CASE_EVIDENCE_READBACK_ON_TIME_AUTO_PARTS_2026-08-04.md`。

`68b1aa8` 發布後延遲讀回：三語 `/case-automotive-parts-rack` 均回應 200、單一 H1、正確 clean canonical、Article／BreadcrumbList／FAQPage JSON-LD、`requested_files=dimension_drawing` CTA 與證據邊界；公開 `/tw/applications`、`/en/modular-fixtures`、`/jp/display-hooks` 均已讀回新案例連結；公開 sitemap 回應 200 並包含三個新案例 URL。此頁仍是匿名工程／交付紀錄，不宣稱具名客戶成果、正式數量、交期或交貨地。

`5733acc` 發布後延遲讀回：三語新案例頁均已讀回 shipping mark 證據邊界文字；公開案例與詢問 CTA 仍維持匿名與未授權欄位不公開。以 390 × 844 手機 viewport 做公開 runtime 驗收：首頁無橫向溢位，Hero 高度 844px，兩個首屏 CTA 均可見且可點擊；新案例頁無橫向溢位，第一個 CTA 可見。手機 viewport 已於驗收後恢復預設，未保留測試分頁。

2026-08-04 新增第二個高證據候選：從歷史 OEM／ODM 專案 `Thomas Game Headphone Set` 讀回三耳機展示組的客戶圖面、BOM、packout、工廠組裝說明與五種通路版本描述。新增匿名 `Three-Headphone Display Set／三耳機展示組工程紀錄` 三語 flat／clean route 共 6 頁，並加入 Applications 與展示掛勾頁的內部連結；公開頁不揭露客戶名稱、數量、交期、交貨地、成本或完整合約責任。完整證據讀回與邊界見 `CASE_EVIDENCE_READBACK_HEADPHONE_DISPLAY_2026-08-04.md`。

`0335704` 公開部署讀回：Git `main`／`draft` 均已同步，但 2026-08-04 延遲讀回三語 `case-headphone-display-set` 仍為 404，公開 Applications 與 sitemap 尚未出現新案例；因此目前狀態是 `pushed_not_publicly_verified`，不可宣稱已公開完成。

`4a9869b` 延遲公開讀回：三語 `case-headphone-display-set`、`tw/applications` 均回傳 200，頁面可讀到新案例內容；`sitemap.xml` 回傳 200，共 90 個 `<loc>`，三語新案例各有 1 筆。三語 contact 頁也已公開讀回 `requested_files` fallback。

`6a002f6` P0 修正與 runtime 讀回：發現案例 CTA 傳入 `requested_files=dimension_drawing` 後，公開表單未穩定選取，已在三語 contact 頁加入 inline fallback。公開讀回確認 `buyer_role=buyer_trading_agent`、`inquiry_type=quote`、`product_category=system_fixtures`、`requested_files=dimension_drawing`、`source_category=system_fixtures`、`source_role=buyer`；未提交表單。390 × 844 手機驗收確認案例頁寬度 375、scrollWidth 375、H1=1、首屏 CTA 可見；viewport 已恢復預設。

2026-08-04 URL 抽樣驗收：本地三語內容共掃描 0 個內部 `.html` href；公開 `/overview` 與 `/contact-us` 回傳 301，舊三語 `.html` 路徑抽樣回傳 308 至 clean URL（Cloudflare 先做結尾斜線正規化），目的頁為 `/tw/about`、`/en/products`、`/jp/services` 等 clean URL。
