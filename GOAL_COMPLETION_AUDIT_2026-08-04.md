# Big Fame 官網目標完成稽核

更新日期：2026-08-04

## 判定規則

- **已證明**：有目前工作樹、公開 HTML／runtime 或既有量測讀回可直接支持。
- **部分完成**：頁面或流程已存在，但仍缺公開部署、實際轉換、授權或商業證據。
- **尚未證明**：不能用目前的契約檢查或意圖矩陣推導完成。

## 七項目標狀態

| 目標 | 目前證據 | 狀態 | 尚缺什麼 |
|---|---|---|---|
| 1. 統一正式網站架構 | clean URL、canonical、絕對 hreflang、sitemap、舊網址 redirects 已在本地驗證；`main` 與 `draft` 已同步；最新三語案例、Applications 與 sitemap 已公開回傳 200 | 部分完成 | 仍需持續以公開抽樣與 Search Console 驗證完整 URL 集合；Search Console 是否已重新處理不能由本地檔案證明 |
| 2. 三類 TA 搜尋入口 | `procurement`、`design-support`、`display-hooks` 三語頁面；搜尋意圖矩陣與 FAQ 已建立 | 已證明頁面存在 | Google／AI 是否已索引與帶來非品牌曝光仍未證明 |
| 3. 可搜尋產品頁 | 8 類產品 × 3 語，共 24 頁；產品頁契約與可見內容驗收均為 24／24 通過 | 部分完成 | 契約通過不等於所有 SKU、材質牌號、MOQ、交期與承重均已正式核准 |
| 4. 可驗證 B2B 案例 | 30 頁案例契約通過；新增匿名汽車零件展示架與三耳機展示組工程紀錄，來源具備需求、圖面／BOM、Big Fame 工程脈絡、組裝／包裝文件與公開邊界 | 部分完成 | 客戶公開授權、正式數量、交期、交付地、現場照片授權與正式合約範圍仍未公開；尚不能稱為具名完整交付案例 |
| 5. TA 詢價轉換 | 三語表單已有角色、階段、資料需求、數量、目標時間、交貨地、圖面連結；CTA 會保留 category／role／source_page／requested_files；公開 runtime 已驗證預填；桌機與 390 × 844 手機 Hero／CTA 均已驗證 | 部分完成 | 尚未取得真實 `generate_lead` 轉換讀回，因未授權提交測試表單 |
| 6. Google／AI 可理解 | H1／H2／FAQ、FAQPage、Breadcrumb、Organization、Service 與內部連結已存在；搜尋意圖矩陣已建立 | 部分完成 | 仍需擴充「一個問題一個頁面」的內容群集，並以公開索引與 AI 引用結果驗證，不可只看 JSON-LD 存在 |
| 7. 搜尋與轉換量測 | Search Console 與 GA4 baseline 已建立；`form_start`、`bf_contact_cta_click`、`generate_lead` 等事件已埋設 | 部分完成 | 尚未形成 28 天非品牌查詢、TA 入口、產品頁到表單與實際 lead 的穩定比較資料 |

## 目前最重要的三個工作

### 1. 完成一個證據完整案例

優先從原始專案檔中取得：

- 可公開授權或明確匿名授權
- Big Fame 實際承擔範圍
- 最終交付內容
- 數量、交期、交付地，或明確的未公開證明
- 可連到產品與詢價流程的照片／圖面

目前最接近的素材包括匿名汽車零件展示架工程紀錄、匿名三耳機展示組工程紀錄、二手 3C 模組化展示、城市儲物系統，以及小型旅館旋轉式可變家具。汽車零件展示架與三耳機展示組已建立公開匿名證據頁，但仍不應宣稱為具名完整交付案例。2026-08-04 的交付線索掃描另讀到晁雍／金久盛歷史報價，以及 OMO 生活用品的報價／Invoice，但來源角色或產品類型不符合展示設備完整案例門檻，詳見 `CASE_EVIDENCE_READBACK_DELIVERY_SCAN_2026-08-04.md`。三耳機展示組的原始圖面、BOM、packout 與工廠組裝讀回見 `CASE_EVIDENCE_READBACK_HEADPHONE_DISPLAY_2026-08-04.md`。

公開驗收補充：`case-headphone-display-set` 三語頁與 Applications 已回傳 200，sitemap 已包含三語新案例。`6a002f6` 修正後，contact 頁的 `requested_files` 上下文已在公開 runtime 讀回；尚未提交真實表單，因此 `generate_lead` 仍不宣稱已重新驗證。

### 2. 做最新公開版本的延遲讀回

每次發布後至少確認：

- clean URL 回應 200
- canonical／hreflang／sitemap 使用同一 URL
- CTA 進入聯絡頁後的角色、類別與來源頁預填
- 桌機與手機首屏可讀、可點擊

### 3. 建立第一個可比較的搜尋／轉換週期

先不追求流量總量，固定觀察：

- 非品牌查詢是否出現展示設備、展示掛勾、retail fixture、CAD sampling
- 三類 TA 入口的曝光與進入產品頁比例
- 產品頁到聯絡頁的 CTA 點擊
- `form_start` 與 `generate_lead`
- 角色與語言分布

## 明確不列為完成的事項

- 產品頁契約 24／24 通過，不代表商業規格全部核准。
- 案例頁契約 24／24 通過，不代表已取得客戶授權或已證明交付。
- JSON-LD 存在，不代表 Google 已索引或 AI 已引用。
- 表單事件程式存在，不代表已有真實 lead。
- 本地 `main`／`draft` 同步，不代表最新版本已完成公開 CDN 讀回。
