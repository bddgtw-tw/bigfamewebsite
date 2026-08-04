# Big Fame URL、canonical、hreflang 與 sitemap 一致性稽核

日期：2026-08-05

## 本機結果

- 本地 clean route：75 個。
- sitemap URL：96 個。
- 本地 clean route 未列入 sitemap：0。
- sitemap 中的優先頁未找到對應本地 route：0。
- 三語 HTML 頁面 metadata 檢查：171 頁，canonical 與 hreflang 無不一致。

## 公開結果

- sitemap 內 96 個 URL 全部 HTTP 200。
- 舊網址導向均為 HTTP 301：
  - `/overview` → `/en/about`
  - `/contact-us` → `/en/contact`
  - `/tw/overview` → `/tw/about`
  - `/tw/contact-us` → `/tw/contact`
  - `/en/overview` → `/en/about`
  - `/en/contact-us` → `/en/contact`
  - `/jp/overview` → `/jp/about`
  - `/jp/contact-us` → `/jp/contact`
- 舊 `.html` 公開頁由主機導向對應 clean URL；內部 HTML 連結維持 0。

## 邊界

本次證明的是 URL 宣告、sitemap 與公開 HTTP 可達性一致；Search Console 的收錄狀態與 Google／AI 實際排名仍需以後續查詢資料觀察，不能由 sitemap HTTP 200 推論已被收錄。
