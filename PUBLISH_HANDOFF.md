# Big Fame 網站升級發布交接

更新日期：2026-08-04

## 目前已確認的狀態

### 本地／Git

- 專案位置：本專案工作樹
- 正式分支：`main`
- 開發分支：`draft`
- Git remote：`https://github.com/bddgtw-tw/bigfamewebsite.git`
- `main` 與 `draft` 目前同步至同一發布提交：`66bcc9c`
- 網站內容包含三語首頁、TA 入口、產品頁、案例頁、服務頁與詢問頁。

### 公開 `bigfame.co`

目前已由公開 HTTP 與 DOM 檢查確認：

- `https://www.bigfame.co/tw/` 回應 200
- 三個語言版本的 TA 入口、產品頁、詢問頁與 sitemap 可公開讀取
- 公開版已具備 clean URL、canonical、hreflang、TA 入口、案例與詢問流程
- 舊 `/thank-you-page`、`/our-works` 等網址可導向新頁面
- 公開版 `main.js` 已驗證包含 `bf_page_context`、`bf_contact_cta_click`、`form_start` 與 `generate_lead`

完整 sitemap 驗收（2026-08-04）：72 個公開網址全部回應 200；72／72 具備單一 canonical、至少三個 hreflang 與單一 H1。

最新新增的 PAGE 桌上型化妝品收納展示器「產品開發資料紀錄」已在三語公開網址驗證；頁面保留 2020-03-30 ver.01 文件的尺寸、材質、包裝與交期證據，並明確標示未核准的客戶、MOQ、交付與成果欄位。

### 最新部署驗證

已於 2026-08-04 重新讀取公開網址並確認：

- 三語 `/procurement` 均回應 200，且包含 `custom-metal-parts` 連結。
- 三語 `/display-hooks` 均回應 200，且包含 `anti-theft-hooks` 連結。
- 這六個連結已由本地、Git `main`、Git `draft` 與公開網站逐層驗證。

## 發布後仍需持續確認

1. 持續檢查公開版 sitemap、canonical、hreflang 與 Git `main` 是否一致。
2. 持續補足證據登錄表中尚未核准公開的數量、交期、客戶名稱與成果主張。
3. 以 GA4 與 Search Console 28 天資料判斷 TA 入口、產品頁與詢問轉換。

## 不能宣稱的事項

- 不把本地或 Git 已完成的變更直接稱為公開網站已完成部署。
- 不把候選案例當成已取得公開授權的正式客戶案例。
- 不把未核對的測試數據、客戶名稱、所有權、MOQ、交期或市場地位寫成既定事實。
