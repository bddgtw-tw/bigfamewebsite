# Big Fame 官網工作目標狀態（R2）

稽核日期：2026-08-05

本文件以目前工作區、Git main 與公開網站讀回為準。頁面已存在，不等於 Google 已索引；事件已送出，不等於有效商機；來源文件有敘述，也不等於客戶授權或完整交付證明。

## 七項目標現況

| 目標 | 目前判定 | 已取得的證據 | 尚未完成或不能推論 |
|---|---|---|---|
| 1. 統一正式網站架構 | 已達網站端標準 | 本地 171 個 HTML；內部 `.html` 連結 0、canonical `.html` 0；sitemap 96 筆且公開全部 HTTP 200；主要舊網址 301 導向 clean URL | Search Console 仍需觀察索引處理，不把 sitemap 發現當成全部索引 |
| 2. 三類 TA 搜尋入口 | 頁面已達標 | `procurement`、`design-support`、`display-hooks` 三語頁均有問題、產品、案例、流程、FAQ、Service schema 與詢價 CTA | 尚未證明非品牌搜尋已穩定帶來 TA 流量 |
| 3. 可搜尋產品頁 | 頁面結構已達標，商務資料部分待核准 | 八類產品三語 flat／clean 共 48 頁通過產品品質稽核；產品、案例、詢價路徑已互相連結 | 各 SKU 的正式 MOQ、交期、承重、材質牌號與可承諾商務條件仍需核准 |
| 4. 可驗證 B2B 案例 | 證據型案例已建立，完整交付案例仍不足 | 零售採購整合、Urban Warehouse、二手 3C、旅宿、酒吧、眼鏡與展示產品頁均標示來源與證據邊界；案例契約稽核 72 頁 0 失敗 | 普遍缺正式授權、完整合約角色、交付數量、交期與交付地；不可把匿名紀錄寫成無條件客戶成果 |
| 5. TA 詢價轉換 | 網站端已達標，真實商機尚待對帳 | 角色、階段、產品、資料需求、數量、時程、交貨地、圖面連結已具備；公開預填已驗證；CTA 與產品來源脈絡已保留 | 尚未逐筆將 `generate_lead` 與實際收件內容對帳 |
| 6. Google／AI 理解 | 結構已達標，外部採用待觀察 | H1／H2／FAQ、Organization、Service、Breadcrumb、代表性 Product schema、產品／案例／店型內鏈已建立 | 尚未證明 Google 已索引、排名或 AI 已引用 |
| 7. 搜尋／轉換量測 | 管線已建立，資料週期尚未成熟 | GA4 已有 CTA、form start、submit attempt、lead、error 事件；本輪新增 `content_role` 與 `bf_inquiry_context_ready`；Search Console 已重新發現 sitemap 96 頁 | GA4 四個新自訂維度尚未完成後台註冊；尚未有完整 28 天非品牌、入口、產品 CTA 與有效 lead 比較 |

## 最新版本一致性

- 本地 HEAD：`8779502a0f79d1c93e3a4042742eff820968041e`
- Git `origin/main`、`origin/draft`、`origin/release/draft`：同一 SHA
- 公開 `main.js`：`SITE_VERSION=1.3.24`
- 工作區：clean
- 公開 sitemap URL：96／96 HTTP 200
- 主要舊網址：`/overview`、`/contact-us`、三語舊路徑與 `/portfolio` 等已讀回 301

## 本輪新增

- 眼鏡品牌門市案例三語 flat／clean 共六頁新增 `CASE BRIEF`，明確分開客戶問題來源、店型、Big Fame 可核對範圍、交付內容、未公開商務欄位與公開邊界。
- 本地案例契約稽核仍為 72 頁、0 失敗；公開六頁均已讀回 HTTP 200、單一 H1、FAQPage、canonical 與 `data-bf-case-brief="1"`。
- 發布分支原先落後於 `main`，已同步至同一 SHA；這次同步後公開網站才讀回眼鏡案例的新內容。

## 目前最值得投入的三件事

1. 取得一個可公開或明確匿名授權的完整交付案例，補上 Big Fame 正式承擔範圍、數量、交期、交付地與結果證據。
2. 完成 GA4 自訂維度與商機對帳，讓網站能回答哪個 TA、產品或案例真正產生有效需求。
3. 以 2026-08-05 至 2026-09-01 為觀察窗，追蹤非品牌查詢、TA 入口、產品頁 CTA、表單開始與 lead 的變化；依實際查詢再調整內容，不無限制增加新頁。

## 現階段不應宣稱

- 96 個 sitemap URL 已全部索引。
- 非品牌搜尋已穩定帶來詢問。
- GA4 的 2 次 `generate_lead` 已等同 2 筆有效商機。
- 所有案例都是已完成、已安裝、已交付的客戶專案。
- 所有產品都有可直接公開承諾的通用 MOQ、交期或規格。
