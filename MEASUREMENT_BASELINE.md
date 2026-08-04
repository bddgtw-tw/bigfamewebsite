# Big Fame 官網 SEO／AI Search／TA 成效量測基準

> 更新日期：2026-08-04  
> 目的：讓網站的「被看見、被找到、被理解、被詢問」可以被持續觀察。  
> 原則：本文件只記錄已在程式或公開網站驗證的內容；未取得 GA4／Search Console 報表的項目，不視為已發生的成效。

## 一、目前已完成的量測契約

目前 `js/main.js` 版本為 `1.3.12`。本地版與公開版版本一致，公開版已驗證包含以下事件與欄位：

| 事件 | 觸發時機 | 主要欄位 | 用途 |
|---|---|---|---|
| `bf_page_context` | 頁面載入 | `site_locale`、`page_type`、`content_slug`、`ta_entry`、`page_path` | 判斷哪個語言、頁型與內容被看見 |
| `bf_contact_cta_click` | 點擊導向詢問頁的 CTA | `inquiry_category`、`inquiry_role`、`source_page_path`、`link_text`、`link_url` | 判斷哪個入口把 TA 帶進詢問流程 |
| `form_start` | 詢問表單第一次取得焦點 | `inquiry_category`、`inquiry_role`、`source_page_path` | 判斷 CTA 後是否真的開始填寫 |
| `generate_lead` | Web3Forms 成功回傳後 | `inquiry_type`、`product_category`、`inquiry_category`、`inquiry_role`、`source_page_path` | 判斷有效詢問是否完成 |
| `bf_contact_method_click` | 點擊 Email 或電話 | `contact_method`、`link_text` | 補充直接聯繫行為 |

事件不送出姓名、Email、電話、需求內容或圖面連結；表單內容不應放入 GA4 事件參數。

## 二、目前可用的頁型分類

`page_type` 目前依網址判斷：

- `home`：三語首頁
- `ta_entry`：`procurement`、`design-support`、`display-hooks`
- `product`：展示掛勾、光學掛勾、防盜掛勾、洞洞板／槽板配件、價牌／標示、POS 展示、模組化什器、客製金屬零件，以及已有產品頁的相關品項
- `case`：`case-` 開頭的案例頁
- `hub`：產品、應用案例、服務、關於 Big Fame
- `contact`：詢問頁
- `content`：尚未歸入上述類型的內容頁

`ta_entry` 的控制值目前為：

- `procurement`：採購、商社、代理商導向
- `design-support`：店面規劃、設計、建築、工程導向
- `display-hooks`：展示掛勾、陳列五金、店面展示配件導向

## 三、GA4 後續應觀察的漏斗

```text
頁面被看見
  ↓ bf_page_context
CTA 被點擊
  ↓ bf_contact_cta_click
表單開始填寫
  ↓ form_start
詢問成功送出
  ↓ generate_lead
```

第一階段只需建立以下探索報表，不急著用單一總流量判斷網站好壞：

1. `page_type` × `site_locale`：首頁、TA 入口、產品、案例各自被看見多少。
2. `content_slug` × `bf_contact_cta_click`：哪些頁面實際把人帶到詢問。
3. `ta_entry` × `form_start` × `generate_lead`：三個 TA 入口的流失位置。
4. `product_category` × `generate_lead`：詢問集中在掛勾、POS、什器系統或客製金屬哪一類。
5. `inquiry_role` × `generate_lead`：採購、設計／工程、品牌展店、VM 哪類角色真正產生詢問。

建議先觀察 28 天，再決定哪些頁面要改文案、CTA、案例證據或表單；在資料量不足前，不應以百分比做過度結論。

## 四、Search Console 應建立的搜尋詞分組

以下是依 TA 搜尋語言建立的「觀察分組」，不是目前已取得的搜尋結果：

- 品牌：`Big Fame`、`bigfame`、`Big Fame display`
- 店面展示設備：店面展示設備、零售展示設備、店面陳列五金、retail display hardware
- 展示掛勾：展示掛勾、眼鏡展示掛勾、光學掛勾、防盜掛勾、display hook、optical display hook、anti-theft hook
- 系統配件：洞洞板配件、槽板配件、slatwall accessories、pegboard display accessories
- POS 與桌上展示：POS 展示架、桌上型展示、counter display、point of purchase display
- 什器與規劃：模組化展示架、店面什器系統、retail fixture system、store fixture design support
- 客製開發：客製金屬零件、金屬展示配件、custom metal parts for retail display
- 應用情境：眼鏡店展示、服飾店展示、藥妝店展示、精品旅館展示、酒吧酒瓶展示、cosmetic display organizer
- 需求型問題：展示掛勾怎麼選、店面展示設備供應商、零售展示設備客製、展示設備 MOQ、展示設備打樣

應觀察的欄位為：曝光、點擊、CTR、平均排名、搜尋頁面、國家／地區與品牌／非品牌。這些數值目前尚未由 Search Console 讀回，故狀態為「待觀察」。

## 五、目前已驗證與尚未驗證

### 已驗證

- 公開 `https://www.bigfame.co/js/main.js` 與本地版本同為 `1.3.12`。
- 公開版包含 `bf_page_context`、`bf_contact_cta_click`、`form_start`、`generate_lead` 與 `source_page_path`。
- 從公開 POS 展示頁點擊 CTA，可將產品類別與來源頁帶入詢問頁；尚未送出表單。
- 公開網站的 URL、canonical、H1、sitemap、TA 入口與案例頁已完成既定的靜態／DOM 驗證。

### 尚未驗證

- GA4 是否已在正式資料流中收到上述事件。
- GA4 各事件的實際數量、漏斗轉換率與角色分布。
- Search Console 實際曝光、點擊、平均排名與非品牌搜尋詞。
- 事件是否已在 GA4 介面建立為轉換事件／Key event。
- 行動裝置的實際速度、可讀性與 CTA 點擊率；目前只有程式與公開 DOM 層級檢查。

## 六、後續執行順序

### P0：先取得基準數據

1. 確認 GA4 資料流收到 `bf_page_context`、`bf_contact_cta_click`、`form_start`、`generate_lead`。
2. 將 `generate_lead` 設為主要 Key event；CTA 與 `form_start` 作為診斷事件。
3. 建立 Search Console 28 天基準，分開品牌與非品牌。

### P1：依數據修正網站

1. 有曝光、低點擊：修正 title、description、H1、搜尋意圖對應與摘要。
2. 有點擊、低 CTA：修正首屏價值、案例證據、產品規格與 CTA 位置。
3. 有 CTA、低表單開始：檢查來源脈絡、表單負擔與行動版操作。
4. 有表單開始、低成功送出：檢查需求欄位、信任證據與送出錯誤。

### P2：擴充內容資產

以證據登錄表為準，逐步補齊八類產品頁與案例頁；任何 MOQ、交期、數量、客戶名稱、交付範圍或成果數字，先取得來源與公開授權再上線。

## 七、判斷標準

網站是否更能吸引 TA，不以「內容很多」判斷，而以以下鏈條判斷：

> TA 搜尋語言 → 對應頁面被找到 → 3 秒內理解 Big Fame 能處理什麼 → 看到可信證據 → 帶著上下文開始詢問 → 成功留下可跟進需求。

目前網站已完成這條鏈條的頁面與事件基礎；「搜尋真的帶來多少人」與「哪些 TA 真的轉換」仍須 GA4／Search Console 正式資料回填後才能判斷。
