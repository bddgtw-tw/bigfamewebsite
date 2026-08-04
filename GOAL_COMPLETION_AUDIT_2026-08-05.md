# Big Fame 官網目標完成稽核（2026-08-05）

判斷原則：本地寫入不等於公開發布，公開發布不等於搜尋引擎索引；結構化資料存在也不等於 AI 已引用。未取得授權或正式商務資料的欄位，維持待確認狀態。

## 七項目標現況

| 目標 | 目前證據 | 判定 | 尚未證明／尚待完成 |
|---|---|---|---|
| 1. 統一正式網站架構 | 167 個 HTML 全站靜態檢查通過：JSON-LD 可解析、內容頁 H1=1、canonical 存在、內部不再使用 `.html`；公開 sitemap 96 URL 全部可連線；Git `main`、`draft` 與 `release/draft` 已同步至 `357638d` | 部分完成 | Search Console 全量重新處理與索引狀態仍需觀察 |
| 2. 三類 TA 搜尋入口 | 三語 `procurement`、`design-support`、`display-hooks` 已有問題、產品、案例、流程、FAQ、CTA；九頁 Service schema 已靜態公開驗收 | 頁面已證明 | 非品牌曝光與 TA 實際找到入口尚未證明 |
| 3. 可搜尋產品頁 | 八類產品三語 24 頁品質驗收通過；48 個 flat／clean 頁有產品身分、圖片、分類、canonical；未具備正式商務資料者使用 specification gate | 部分完成 | 各 SKU 正式 MOQ、交期、承重、材質牌號與客製商務條件仍需核准 |
| 4. 可驗證 B2B 案例 | 案例頁含需求、使用方向、材料／工程範圍、證據狀態、CTA；三耳機展示組補上工程交付包，眼鏡門市案例補上 EYEHK 圖面相關產品證據與年份／SKU 邊界，Urban Warehouse 三語 clean／flat 頁補上模組、材料、K/D 結構、使用結果與來源邊界 | 部分完成 | 客戶授權、正式合約角色、正式交付數量／交期／交付地仍未普遍取得 |
| 5. TA 詢價轉換 | 表單包含角色、階段、產品類別、需求文件、數量、目標時間、交貨地與圖面連結；CTA 可保留 category／role／product／source_page；手機首屏與公開預填已驗證 | 部分完成 | 尚未授權送出真實表單，不能宣稱有效 `generate_lead` 已驗證 |
| 6. Google／AI 理解 | TA 問題矩陣已有對應頁；FAQ、Breadcrumb、Organization、Service、Product schema 與產品／案例／店型內部連結已補齊；代表性尺寸圖可下載 | 結構已建立 | Google 索引、AI 引用、排名與回答採用仍需外部觀察 |
| 7. 搜尋／轉換量測 | Search Console 與 GA4 基準、事件命名與 28 天觀察週期已建立 | 基準已建立 | 尚未形成完整 28 天非品牌查詢、入口曝光、產品 CTA、form_start 與有效 lead 比較資料 |

## 本輪新增可驗證成果

- Service schema：三語九頁，公開驗收 9/9 通過。
- 案例產品／能力回連：三語六頁，公開驗收 6/6 通過。
- Technical Resources 代表性尺寸圖下載：三語 3/3 頁通過，圖片資產 HTTP 200。
- 目前最新提交：`357638d`；本輪 Urban Warehouse 三語頁內容已寫入並完成公開 runtime 讀回。
- 舊網址 13 組已於公開端讀回 301；`scripts/generate_redirect_rules.py` 已與 `_redirects` 對齊，避免日後重建規則時遺失 `portfolio`、下載路徑與 `/contact` 導向。

## 最新量測讀回（2026-08-05）

### Search Console

- 期間：2026-07-16 至 2026-08-02
- 點擊 4、曝光 383、CTR 1%、平均排名 9.7、查詢 26
- 已出現少量非品牌查詢：`陳列什器 製造 oem 体制`、`店舗什器 量産 コスト 効率`、`shelving system`
- 目前這些非品牌查詢尚未形成點擊；品牌詞與舊網址仍占主要可見度。

### GA4

- 近 7 天：活躍使用者 12、事件 258、Organic Search 工作階段 5、`bf_contact_cta_click` 3
- 近 28 天（2026-07-08 至 2026-08-04）：事件 527、使用者 50、`bf_contact_cta_click` 7／4 位使用者、`form_start` 2／2 位使用者、`generate_lead` 2／2 位使用者
- 近 7 天 404 頁瀏覽 15 次；可控制的歷史網址已建立導向，外部短網址與 Cloudflare 系統路徑仍需另行處理或持續觀察。

### 客觀判讀

量測管線已實際收到 CTA、表單開始與 `generate_lead` 事件；目前只能證明網站行為，不足以證明有效商機、TA 身分或成交。下一個 28 天週期應把非品牌 query、產品／案例頁進入量、事件參數與實際收到的詢問逐筆對帳。

## 目前最重要的下一步

1. 等待本次發布後重新讀回 404 fallback 與 redirect；目前已知不可由網站控制的 404 僅剩 Cloudflare 系統路徑與外部短網址。
2. 取得一個可公開或明確匿名授權的完整案例，補確認 Big Fame 範圍、交付內容與可公開欄位。
3. 完成至少一個 Search Console／GA4 觀察週期，檢查非品牌 query、TA 入口、產品 CTA 與 `form_start`。
4. 依正式核准資料逐 SKU 補材質、尺寸、表面、MOQ、交期與 CAD／規格檔，不用推測內容填滿頁面。

## 本輪證據核對補充

- PAGE 桌上型化妝品收納展示器：原始 `Big Fame Offer Form - PAGE Cosmetic Organizer.pdf` 共 2 頁，直接讀到 `2020.03.30 ver.01`、W250 × D120 × H240 mm、Clear Acrylic／Edge polished、Solid wood、1 SET/CTN、樣品約 15–25 天、量產約 25–35 天（訂單確認後）。網站產品頁已公開這些已核對欄位，並將 MOQ、正式 SKU、數量、交付條件保留為確認項目。
- PAGE 三語產品頁公開抽查：中、英、日各 200；各頁 H1=1、Product JSON-LD=1、FAQPage=1、canonical=1。
- 匿名零售店面展示設備採購整合案：網站公開頁回答了採購問題、店型／品類、Big Fame 文件整合範圍與交付欄位，但仍明確限制為匿名採購／文件整合紀錄，不宣稱安裝完成、正式數量或現行交期。
- 本輪結論：產品證據單元已更接近可搜尋、可核對與可詢問；仍不能把它升格為「已完成客戶案例」，除非取得授權或更完整的交付證據。
- 案例升格優先順序：On Time 汽車零件展示架目前具備需求往返、Big Fame 設計回覆、圖面迭代、缺陷改善、組裝文件與 shipping mark；已另列出正式承擔範圍、獨立交付證據、數量、交期、交付地與公開授權的最小補件清單，避免重複掃描資料庫。
- 詢價流程整理：三語聯絡頁已移除重複的歷史 inline 預填腳本，公開版由 `main.js?v=1.3.22` 單一邏輯讀取角色、類別、產品、需求文件與來源頁；來源頁現在可由 CTA URL 帶入，並以同站 referrer 作 fallback。公開帶參數 URL 已讀回正確欄位。這證明上下文初始化，不代表真實表單送出或有效商機。
- On Time 案例跨資料夾查找：以 `TRANSBEC`、`0001643`、`AUTO CLIP RACK`、`4-Sides Peg Board Rack` 與專案名稱交叉查找 `10_內部營運`、`90_歷史封存` 後，未找到專案資料夾外的獨立訂單／出貨／簽收／驗收文件；目前仍維持匿名工程／交付準備紀錄。
- 八類產品頁需求稽核：中英日 24 頁均通過頁面欄位與內容契約；目前的未完成項是逐 SKU 正式商務資料核准，不是頁面缺少 MOQ／交期欄位。詳細區分已寫入 `PRODUCT_PAGE_REQUIREMENTS_AUDIT_2026-08-05.md`。
- 三類 TA 入口搜尋問答稽核：採購、設計支援、展示掛勾入口均已用自然問句回答供應商／報價、CAD 協作、眼鏡掛勾與槽板／洞洞板確認方式；答案均保留正式供貨與商務條件的確認邊界。詳細讀回已寫入 `TA_ENTRY_SEARCH_ANSWER_AUDIT_2026-08-05.md`。
- 發布後全站一致性稽核：產品 24 頁、案例 36 頁、TA 入口 9 頁、sitemap 96 筆與主要公開 URL 均通過；167 個 HTML 中的 5 個例外是 404／語言選擇／legacy／內部工具頁，已與正式內容頁分開判讀。詳細結果已寫入 `PUBLIC_CONSISTENCY_AUDIT_2026-08-05.md`。

## 本次外部量測更新

- Search Console 重新讀回：目前 16 頁已索引、51 頁未索引；實際期間 2026-07-16～2026-08-02 為 4 點擊、383 曝光、26 查詢。非品牌查詢已有曝光，但尚未形成點擊。
- GA4 重新讀回：28 天 `bf_contact_cta_click` 7 次、`form_start` 2 次、`generate_lead` 2 次；這些是事件證據，不是已驗證的有效商機。
- 目前目標判定不升級：網站結構、TA 入口、產品／案例內容與量測管線已有可驗證成果；SEO 找到、TA 歸因、案例商務證據與有效 lead 仍在觀察或待補件。

## 本輪 P0／P1 現況稽核補充

- Hero 可讀性：首頁 CSS 已使用高對比遮罩；桌機顯示背景影片，手機與 `prefers-reduced-motion` 會停用影片，保留靜態 fallback。
- Hero 資產：目前首頁使用的 web 影片約 0.39 MB；未再使用約 21.95 MB 的舊版 `hero_bg.mp4` 作為首頁來源。
- 英文 metadata：英文首頁、產品、服務、TA 入口與優先產品頁均已讀到 title、description、Open Graph、canonical 與 hreflang；產品頁的英文搜尋詞仍需依 Search Console 實際查詢持續調整。
- 詢價上下文：`source_category`、`source_role`、`source_product`、`source_page` 與 `requested_files` 已由單一 `main.js` 初始化並送入事件；公開 URL 讀回已證明預填邏輯，尚不等於有效商機。
- 版本文件：目前記錄實際提交 SHA `357638d`；正式 URL runtime 已讀回，不以 Git SHA 單獨代替公開驗收。

本輪判斷：P0 的可直接修正項目前已具備可驗證實作；Urban Warehouse 已補成可追溯的匿名系統證據頁，但仍不是正式完整交付案例。下一步應取得 Search Console 的非品牌點擊、逐筆對帳 GA4 lead，並持續補具正式交付證據與公開授權的案例。

## GA4 參數稽核補充

- `generate_lead` 28 天報表讀回為 2 次、2 位使用者；來源均為 Direct，有效待開發客戶 0、已轉換 0。
- GA4 目前已註冊 `inquiry_category`、`product_category`、`contact_method`、`site_language`、`inquiry_type` 五個事件維度。
- 網站程式已送出 `inquiry_role`、`inquiry_product`、`requested_files`、`source_page_path`，但這四個參數尚未在 GA4 管理頁註冊為自訂維度，因此 TA 角色與來源頁仍無法在標準報表中可靠切分。
- 本輪曾進入 GA4 管理頁建立維度，但儲存視窗無法可靠完成點擊；外部設定維持原狀，未宣稱已完成。

## 2026-08-05 目標稽核再讀回

- Git `main`、`draft`、`release/draft` 已同步至 `357638d`，並以 `git ls-remote` 核對三者相同。
- 本地 167 個 HTML：內部 `.html` 連結 `0`、canonical `.html` `0`、sitemap `<loc>` `96`。
- 產品頁品質稽核：24 頁、0 失敗；案例頁契約稽核：36 頁、0 失敗；Urban Warehouse 六個 flat／clean 版本另通過模組交付、來源標記、FAQ、H1、JSON-LD 與內部連結驗收。
- Search Console Sitemap：2026-08-05 送出與讀取均成功，Google 發現頁面 `96`、影片 `0`。
- Search Console 索引報表最後更新仍為 2026-07-24：已索引 `16`、未索引 `51`；這不能用來判定本次最新發布頁面已完成索引。
- Search Console Performance（2026-07-16 至 2026-08-02）：4 點擊、383 曝光、CTR 1%、平均排名 9.7；非品牌查詢已有曝光但尚未產生點擊。
- 本次新增的採購案例來源紀錄已在三語公開網址讀回：HTTP 200、H1=1、FAQPage、CTA 與來源區塊存在，無連續問號亂碼。
- Urban Warehouse 三語 clean URL 已公開讀回：HTTP 200、H1=1、JSON-LD=3、`data-bf-urban-deliverables="1"`、`data-bf-source-record="1"`、FAQ 與兩個相關目標連結均存在；技術資料頁與聯絡頁均回傳 HTTP 200。

### 目前仍不能升格為完成的項目

1. Google 尚未證明 96 個 sitemap URL 已全部索引。
2. 非品牌查詢尚未形成穩定點擊與 TA 入口導流。
3. `generate_lead` 尚未與真實收到的有效詢問逐筆對帳。
4. 多數案例仍缺正式授權、完整交付數量、交期與交付地，因此維持匿名證據紀錄定位。
