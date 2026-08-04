# TA 入口與詢問上下文 Runtime 稽核

日期：2026-08-05  
公開網址：<https://www.bigfame.co>

## 三個繁中 TA 入口

公開 DOM 唯讀驗收結果：

| 頁面 | H1 | FAQ | 產品連結 | 案例連結 | CTA | 橫向溢位 |
|---|---:|---:|---:|---:|---:|---:|
| `/tw/procurement` | 1 | 1 | 5 | 4 | 4 | 無 |
| `/tw/design-support` | 1 | 1 | 4 | 4 | 4 | 無 |
| `/tw/display-hooks` | 1 | 1 | 6 | 5 | 4 | 無 |

三頁均能從 TA 工作問題進入產品、案例與詢問路徑。

## 實際點擊展示掛勾 CTA

未提交表單，只進行公開頁面導覽與欄位讀回：

- 來源頁：`https://www.bigfame.co/tw/display-hooks`
- 聯絡頁：`/tw/contact?category=display_hardware&role=buyer&product=display-hooks`
- `source_product`：`display-hooks`
- `source_category`：`display_hardware`
- `source_role`：`buyer`
- `source_page`：保留原始展示掛勾頁 URL
- 聯絡頁選擇欄位：`display_hardware`／`buyer`

## 判讀

產品頁到詢問頁的上下文預填已在公開 runtime 驗證；訪客不需重新說明來源產品與角色。這是流程與欄位驗收，不代表已產生真實 `generate_lead`，因本次未送出表單。

手機 390 × 844 的先前公開 runtime 驗收已記錄在既有發布紀錄；本輪未重複送出表單或產生外部副作用。

## 2026-08-05 詢價初始化整理

- 三語聯絡頁移除歷史 inline fallback，改由 `main.js?v=1.3.21` 單一初始化邏輯處理。
- 公開版讀回：`body > script` 由 3 個預填／主程式相關腳本收斂為 2 個（主程式與頁面必要腳本），不再重複執行類別與來源欄位寫入。
- 公開 `/tw/contact?category=display_hardware&role=buyer&product=display-hooks&requested_files=dimension_drawing` 讀回：`buyer_role=buyer_trading_agent`、`inquiry_type=quote`、`product_category=display_hardware`、`requested_files=dimension_drawing`、`source_product=display-hooks`，均由單一主程式正確填入。
- 直接開啟帶參數網址時沒有同站 `document.referrer`，所以 `source_page` 留空是預期結果；由產品／案例 CTA 點入時沿用同站來源頁的既有行為。
