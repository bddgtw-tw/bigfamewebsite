# TA Service Schema 與案例產品回連交接

日期：2026-08-05  
提交：`fd72bf9`（前一個案例回連提交：`5ecfde9`）

## 本次處理

### 三語 TA 入口

在以下九頁的原始 HTML 補上靜態 `Service` JSON-LD：

- `procurement`
- `design-support`
- `display-hooks`

每個 Service 都包含服務名稱、服務類型、描述、canonical 對應的 `url`、`@id` 與 Big Fame Organization provider。原有 FAQ、Breadcrumb 與產品頁的 Product schema 保留。

同時更新 `scripts/generate_localized_entry_pages.py`，讓日後生成入口頁時不會退回只有 CollectionPage 或依賴 JavaScript 的狀態。

### 案例到產品／能力頁

三語的兩組案例各補上回連：

- IVY Collection 模組展示系統 → 模組化展示架、客製金屬零件
- 精品旅宿家具 → 客製金屬零件、模組化展示架

旅宿案例使用「相關能力方向」而非標準產品宣稱，維持來源證據邊界。

## 驗收結果

本地：

- `STATIC_SERVICE_SCHEMA_AUDIT=9`，失敗 0
- `CASE_CONTRACT_PAGES=36`，失敗 0
- `CASE_PRODUCT_LINK_AUDIT=6`，失敗 0
- `node --check js/main.js`：通過
- `python -m py_compile scripts/generate_localized_entry_pages.py`：通過
- `git diff --check`：通過

公開站：

- `PUBLIC_STATIC_SERVICE_AUDIT=9`，失敗 0
- 九頁均 HTTP 200、H1=1
- Service 名稱、provider、url 與 canonical 均可直接讀回
- 六頁案例均 HTTP 200、H1=1、canonical 正確，且可讀到產品／能力回連

## 後續觀察

Service schema 讓搜尋引擎與 AI 更容易理解 Big Fame 的三種服務入口，但不等於已取得排名、AI 引用或商機。後續仍需以 Search Console 觀察非品牌查詢、以 GA4 觀察入口到詢價的行為，並逐案取得正式規格與公開授權。
