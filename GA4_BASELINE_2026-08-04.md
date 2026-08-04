# Big Fame 官網 GA4 實際基準

> 讀取日期：2026-08-04（Asia/Taipei）  
> 資料來源：Google Analytics 4 正式 Big Fame Website 資料流  
> 狀態：已從 GA4 介面讀回；本文件不代表已修改 GA4 設定。

## 一、確認的正式資料流

| 項目 | 實際值 |
|---|---|
| Analytics 帳戶 | Big Fame 401463369 |
| GA4 資源 | Big Fame Website 545985356 |
| 資料流名稱 | Big Fame Website |
| 網址 | `https://www.bigfame.co` |
| 串流 ID | `15271609506` |
| Measurement ID | `G-PDW4NPHHW8` |
| 資料流狀態 | GA4 顯示已啟用，正在接收過去 48 小時資料 |

曾在 Analytics 通用挑選器中看到另一個 Flood-It 應用程式資源；該資源不是 Big Fame 官網，本基準不採用其數據。

## 二、過去 7 天實際讀值

GA4 首頁當時選取「過去 7 天」；介面快照未顯示精確起訖日，因此不自行推算日期。

| 指標 | 讀值 |
|---|---:|
| 活躍使用者 | 12 |
| 新使用者 | 10 |
| 事件計數 | 122 |
| 重要活動／Key events | 0 |
| 即時使用者（讀取當下） | 0 |

### 工作階段來源

| 預設管道群組 | 工作階段 |
|---|---:|
| Direct | 11 |
| Organic Search | 2 |

GA4 顯示的工作階段來源／媒介另包含：`google / organic` 1、`ph.search.yahoo.com / referral` 1、`bing / organic` 0。

### 已讀到的事件

| 事件 | 事件計數 |
|---|---:|
| `page_view` | 45 |
| `scroll` | 25 |
| `user_engagement` | 27 |
| `session_start` | 14 |
| `first_visit` | 10 |
| `bf_contact_cta_click` | 1 |
| `form_start` | 0 |

`generate_lead` 未出現在首頁事件卡片當時顯示的前七個事件中；尚未以完整事件報表確認其精確數量，因此不把它寫成 0。

## 三、初步判讀邊界

- 網站已被 GA4 正式資料流收集，且自訂事件至少已有 `bf_contact_cta_click` 實際記錄。
- 目前 Organic Search 工作階段只有 2，尚不足以判斷哪些 TA 搜尋入口有效。
- 重要活動為 0，只能確認目前沒有被 GA4 首頁卡片列為 Key event 的活動數；不能直接推論表單程式失效。
- `form_start` 為 0，需持續觀察並用公開網站 runtime 測試補強；目前不能宣稱已有表單轉換。
- 國家／地區資料包含台灣、菲律賓、美國等，不能僅以國家判定 TA 身分。

## 四、下一步

1. 以完整 GA4 事件報表確認 `generate_lead` 是否收到事件。
2. 確認 `generate_lead` 是否已由管理者設定為 Key event；本次只讀，未修改設定。
3. 累積至少 28 天資料後，再依 `page_type`、`ta_entry`、`content_slug`、`inquiry_role` 判斷內容與轉換。
4. 將本文件與 [SEARCH_CONSOLE_BASELINE_2026-08-04.md](SEARCH_CONSOLE_BASELINE_2026-08-04.md) 一起作為網站改善前基準。
