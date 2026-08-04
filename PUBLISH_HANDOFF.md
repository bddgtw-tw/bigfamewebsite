# Big Fame 網站升級發布交接

更新日期：2026-08-04

## 目前已確認的狀態

### 本地／Git

- 專案位置：本專案工作樹
- 正式分支：`main`
- 開發分支：`draft`
- Git remote：`https://github.com/bddgtw-tw/bigfamewebsite.git`
- `main` 與 `draft` 目前同步至同一發布提交：`7f053d5`
- 網站內容包含三語首頁、TA 入口、產品頁、案例頁、服務頁與詢問頁。

### 公開 `bigfame.co`

目前已由公開 HTTP 與 DOM 檢查確認：

- `https://www.bigfame.co/tw/` 回應 200
- 三個語言版本的 TA 入口、產品頁、詢問頁與 sitemap 可公開讀取
- 公開版已具備 clean URL、canonical、hreflang、TA 入口、案例與詢問流程
- 舊 `/thank-you-page`、`/our-works` 等網址可導向新頁面
- 公開版 `main.js` 已驗證包含 `bf_page_context`、`bf_contact_cta_click`、`form_start` 與 `generate_lead`

完整 sitemap 驗收（2026-08-04）：81 個公開網址全部回應 200；81／81 具備單一 canonical、至少三個 hreflang 與單一 H1。

最新新增的 PAGE 桌上型化妝品收納展示器「產品開發資料紀錄」已在三語公開網址驗證；頁面保留 2020-03-30 ver.01 文件的尺寸、材質、包裝與交期證據，並明確標示未核准的客戶、MOQ、交付與成果欄位。

最新新增的「展示設備規格與 CAD 資料索取」三語入口已公開驗證；頁面提供代表性尺寸圖與 CAD／PDF／DWG／DXF／STEP 索取流程，但不公開未核准的通用 CAD 或產品承重資料。

三語技術入口的 CAD 打樣 FAQ 已以 UTF-8 公開內容驗證：繁中、英文、日文頁面皆回應 200，且各自包含對應語言的 CAD 打樣問題與條件邊界。

三語「服飾店展示設備」店型搜尋入口已公開驗證：三個頁面皆回應 200，具備單一 H1、FAQ 與展示設備需求情境；此頁是 TA／搜尋入口，不是已核准的具名客戶案例，產品、數量、交期與交付地仍需逐案確認。

三語首頁主要「提交需求／專案諮詢」CTA 已公開驗證帶有 `category=integration&role=buyer`，可將首頁訪客帶入展示設備整合與採購角色脈絡；通用導覽列仍保留未預填的聯絡入口。

三語 `case-apparel-2016` 已公開驗證：頁面使用來源資料夾中的服飾門市照片，整理為匿名、證據控制的照片紀錄，並明確標示不能由照片推定客戶、Big Fame 承擔範圍、數量、交期、交付地或成果；此頁不是完整交付案例。

公開瀏覽器驗證 `apparel-store-fixtures` 的 GA4 `bf_page_context` 已回報 `page_type=ta_entry`、`ta_entry=apparel-store-fixtures`，網站版本為 `1.3.13`；服飾店型入口可與其他 TA 入口分開量測。

舊 `/overview`、`/contact-us`、`/thank-you-page`、`/our-works`、`/know-how`、`/blog` 與兩個舊 blog 路徑已公開回應 301，分別導向現行的 about、contact、applications、services、about 或 display-hooks clean URL。

英文目錄目前 43 個 HTML 頁面均具備 title、meta description 與 canonical；首頁、services、applications、anti-theft hooks、PAGE cosmetic record 與 technical resources 的描述已完成採購、展示設備、案例或 CAD 搜尋語意盤點，後續仍可依 Search Console 查詢詞做精修。

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
