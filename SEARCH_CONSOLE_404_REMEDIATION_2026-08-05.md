# Search Console 404 修正讀回

> 讀回與修正日期：2026-08-05（Asia/Taipei）  
> Search Console property：`sc-domain:bigfame.co`

## 一、Search Console 實際列出的 404 範例

Search Console 網頁索引報告（上次更新 2026/7/24）顯示「找不到網頁（404）」共 17 頁。可讀到的範例包括：

- `/thank-you-page`
- `/our-works`
- `/know-how`
- `/overview`
- `/blog`
- `/blog/author/benny`
- `/blog/retail-fixture-blog`
- `/portfolio?hsLang=en`
- `/downloads/project-brief-template.docx?hsLang=en`
- `/downloads/catalog.pdf?hsLang=en`
- `/contact?hsLang=en`
- `/downloads/material-guide.pdf?hsLang=en`
- `/cdn-cgi/l/email-protection`
- `http://to.bigfame.co/6sra82`、`6srad4`、`6srac7`、`6srabn`

報告頁面每頁顯示 10 筆，共 17 筆；上述清單包含目前畫面可讀到的範例，不將未顯示的 URL 臆測補列。

## 二、已採取的修正

原有舊內容路徑已具備導向：

- `/thank-you-page` → `/en/contact`
- `/our-works` → `/en/applications`
- `/know-how` → `/en/services`
- `/overview` → `/en/about`
- `/blog` → `/en/applications`
- `/blog/author/benny` → `/en/about`
- `/blog/retail-fixture-blog` → `/en/display-hooks`

本次新增：

- `/portfolio` → `/en/applications`
- `/downloads/project-brief-template.docx` → `/en/technical-resources`
- `/downloads/catalog.pdf` → `/en/products`
- `/downloads/material-guide.pdf` → `/en/technical-resources`
- `/contact` → `/en/contact`

部署後公開 GET 讀回上述新增路徑均已回應 301，並保留原 query string，例如 `?hsLang=en` 會被保留到導向網址。

## 三、不能由本網站直接修正的項目

- `/cdn-cgi/l/email-protection` 是 Cloudflare email protection 產生的系統路徑，不應導向一般內容頁。
- `to.bigfame.co` 是另一個短網址子網域；目前工作區與本網站 `_redirects` 無法替其設定目的地。需由該短網址服務或 DNS／Cloudflare 管理者另行處理。

## 四、驗收邊界

- 這次已修正的是可由本網站控制的歷史入口，不宣稱 Search Console 17 筆會立即歸零；Google 需要重新抓取後才會更新報表。
- 舊 `.html` 路徑的三語回歸共檢查 96 個路徑，未發現意外 404；公開站抽樣主要回應 308 導向 clean URL。
- 目前 sitemap、canonical、內部連結仍以 clean URL 為標準。
- 需在下一次 Search Console 更新後重新讀回 404 數量與剩餘 URL。
