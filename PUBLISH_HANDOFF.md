# Big Fame 網站升級發布交接

更新日期：2026-08-04

## 目前已確認的狀態

### 本地／Git

- 專案位置：本專案工作樹
- 正式分支：`main`
- 開發分支：`draft`
- Git remote：`https://github.com/bddgtw-tw/bigfamewebsite.git`
- `main` 與 `draft` 目前同步至同一提交：`c2165ef`
- 網站內容包含三語首頁、TA 入口、產品頁、案例頁、服務頁與詢問頁。

### 公開 `bigfame.co`

目前已由公開 HTTP 與 DOM 檢查確認：

- `https://www.bigfame.co/tw/` 回應 200
- 三個語言版本的 TA 入口、產品頁、詢問頁與 sitemap 可公開讀取
- 公開版已具備 clean URL、canonical、hreflang、TA 入口、案例與詢問流程
- 舊 `/thank-you-page`、`/our-works` 等網址可導向新頁面
- 公開版 `main.js` 已驗證包含 `bf_page_context`、`bf_contact_cta_click`、`form_start` 與 `generate_lead`

### 本次最新變更的發布邊界

`c2165ef` 補強採購入口的客製金屬零件連結，以及展示掛勾入口的防盜掛勾連結。Git 與本地已完成；截至本文件更新時，公開 URL 仍回傳較早版本，尚未證明這六個新連結已完成部署。

## 發布後仍需確認

1. 重新檢查三語 `/procurement` 是否出現 `custom-metal-parts` 連結。
2. 重新檢查三語 `/display-hooks` 是否出現 `anti-theft-hooks` 連結。
3. 檢查公開版 sitemap、canonical、hreflang 與 Git `main` 是否仍一致。
4. 持續補足證據登錄表中尚未核准公開的數量、交期、客戶名稱與成果主張。
5. 以 GA4 與 Search Console 28 天資料判斷 TA 入口、產品頁與詢問轉換。

## 不能宣稱的事項

- 不把本地或 Git 已完成的變更直接稱為公開網站已完成部署。
- 不把候選案例當成已取得公開授權的正式客戶案例。
- 不把未核對的測試數據、客戶名稱、所有權、MOQ、交期或市場地位寫成既定事實。
