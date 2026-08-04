# GA4 Live Readback｜2026-08-05

## 1. 讀取範圍

- Property：Big Fame Website
- Account：Big Fame Industrial CORP.
- Measurement ID：`G-PDW4NPHHW8`
- 讀取日期：2026-08-05
- 時區：Asia/Taipei
- 方式：GA4 後台唯讀讀取；本次沒有由代理人送出表單

本紀錄是目前量測基線，不代表因果關係，也不等於 SEO 已經成功或已取得有效商機。

## 2. GA4 首頁「過去 7 天」摘要

| 指標 | 讀值 |
|---|---:|
| 活躍使用者 | 12，較前期下降 36.8% |
| 事件次數 | 258，較前期上升 52.7% |
| 新使用者 | 16，較前期下降 11.1% |
| 即時活躍使用者 | 1（台灣 1） |
| 重要事件卡片 | 0 |

主要頁面瀏覽／頁面標題包括：中文首頁 20、404 頁 15、語言選擇根頁 12、英文首頁 9、中文聯絡頁 9、日文採購頁 3。

主要流量來源卡片顯示：Direct 15、Organic Search 5、Unassigned 6；來源／媒介可見 Direct 15、google/organic 2、bing/organic 1、ph.search.yahoo.com/referral 1、cn.bing.com/referral 1。

首頁摘要中的 `bf_contact_cta_click` 為 3 次。

## 3. GA4 Events 報表「過去 28 天」

報表期間：2026-07-08～2026-08-04。

| 事件 | 次數 | 使用者 | 目前意義 |
|---|---:|---:|---|
| 所有事件 | 527 | 50 | 量測管線有持續收到資料 |
| `page_view` | 186 | — | 頁面瀏覽 |
| `user_engagement` | 93 | — | 互動停留 |
| `scroll` | 90 | — | 捲動行為 |
| `session_start` | 76 | — | 工作階段開始 |
| `first_visit` | 56 | — | 首次造訪 |
| `bf_page_context` | 15 | — | 頁面脈絡事件 |
| `bf_contact_cta_click` | 7 | 4 | 聯絡 CTA 點擊 |
| `form_start` | 2 | 2 | 表單開始 |
| `generate_lead` | 2 | 2 | GA4 已記錄轉換事件，但尚未完成商機品質驗證 |

整體事件／使用者為 10.54，收益為 0。

## 4. 客觀判讀

### 已經得到的證據

1. 網站的 GA4 量測不是只有程式碼存在；後台已實際收到 `bf_contact_cta_click`、`form_start` 與 `generate_lead`。
2. `generate_lead` 在 28 天報表中有 2 次、2 位使用者。這只能證明事件被記錄，尚不能證明是有效詢問、合格商機，或來自特定 TA。
3. 首頁與聯絡頁確實是目前主要互動入口；Organic Search 在近 7 天仍屬小量。
4. 404 頁在近 7 天有 15 次頁面瀏覽，應持續觀察既有舊網址重導後是否下降。

### 目前不能宣稱的事項

- 不能把 2 次 `generate_lead` 直接寫成 2 筆有效商機。
- 尚未從事件明細確認 `source_role`、`source_category`、`inquiry_category`、`page_path` 與事件來源，因此不能判斷哪一個 persona 已被成功吸引。
- 不能以目前數據宣稱自然搜尋已經穩定帶來採購、設計師、建築師或 VM 詢問。

## 5. 接下來的量測目標

1. 在 GA4 事件明細中，依 `generate_lead` 檢查事件時間、頁面路徑、來源／媒介及角色／品類參數。
2. 將 `form_start`、`generate_lead` 與聯絡表單實際收到的詢問逐筆對照；未完成對照前，只列為「事件」，不列為「有效商機」。
3. 每 28 天追蹤 Organic Search、TA 入口頁、產品頁、技術資源頁與 404 頁的變化。
4. 持續補足可公開的案例證據：客戶／品牌授權、專案角色、數量、交期、交付地點與成果；未取得授權的資料只保留在內部證據庫。

## 6. 本次驗收界線

- 已讀取：GA4 後台目前可見的摘要與事件報表。
- 未執行：代理人送出真實表單、逐筆確認詢問內容、判定商務品質。
- 狀態：量測管線已獲得實際事件證據；商機品質與 persona 歸因仍待驗證。

## 7. 2026-08-05 再次讀回：事件已存在，但尚未完成商機對帳

GA4 Events 報表期間為 2026-07-08～2026-08-04，重新確認：

- `bf_contact_cta_click`：7 次／4 位使用者。
- `form_start`：2 次／2 位使用者。
- `generate_lead`：2 次／2 位使用者。
- 首頁近 7 天 Organic Search 工作階段為 5；404 頁瀏覽為 15 次。

客觀結論：網站已能收到 CTA、表單開始與 lead 事件，但目前尚未從事件明細與實際收件匣逐筆對照 `source_role`、`source_category`、頁面路徑與詢問內容，因此仍只能稱為「已記錄事件」，不能稱為「2 筆有效商機」。

## 8. `generate_lead` 事件與 TA 參數註冊狀態

GA4「獲取待開發客戶」報表再次讀回：

- 28 天內新的待開發客戶：2，來源均為 Direct。
- 有效待開發客戶：0。
- 已轉換的待開發客戶：0。
- 事件重要事件發生率：4.55%；此數字不能取代人工商機品質判定。

GA4 管理頁「自訂定義」目前實際存在 5 個事件維度：

| 顯示名稱 | 事件參數 |
|---|---|
| CTA 需求分類 | `inquiry_category` |
| 產品類別 | `product_category` |
| 直接聯絡方式 | `contact_method` |
| 網站語言 | `site_language` |
| 詢價類型 | `inquiry_type` |

網站 `main.js` 的 `generate_lead` 已送出、但 GA4 管理頁尚未註冊為可分析自訂維度的參數為：

- `inquiry_role`
- `inquiry_product`
- `requested_files`
- `source_page_path`

因此目前可以看到「詢價類型／語言／產品類別」的部分切分，但還不能可靠回答「哪一種 TA 角色、從哪個產品或案例頁、索取哪種資料」最容易產生 lead。這四個維度是下一個 GA4 管理設定待辦；本次沒有把尚未成功儲存的設定宣稱為完成。
