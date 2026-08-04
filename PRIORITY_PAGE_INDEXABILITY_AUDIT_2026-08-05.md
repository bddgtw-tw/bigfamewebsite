# 優先頁面可索引條件排除檢查｜2026-08-05

## 檢查範圍

- `/tw/procurement`
- `/en/display-hooks`
- `/tw/technical-resources`

## 網站端結果

- `robots.txt`：`User-agent: *`、`Allow: /`
- Sitemap 宣告：`https://www.bigfame.co/sitemap.xml`
- 三頁均在本地 Sitemap 中
- 三頁均有 canonical，且 canonical 為同頁 clean URL
- 三頁均無 `noindex`
- 三頁公開 HTTP 200
- 三頁均有四組 hreflang：`zh-TW`、`en`、`ja`、`x-default`
- 三頁均有可通往產品、案例、技術資源或詢價頁的內部連結
- 公開 response header 未發現 `X-Robots-Tag: noindex`

## 結論

目前沒有證據顯示 Big Fame 的 robots、noindex、HTTP 狀態、canonical 或 Sitemap 對應阻擋上述頁面。Search Console 顯示「Google 尚未辨識的網址」，較符合新頁面尚未完成個別抓取的狀態。

## 外部待辦

可對三個優先 URL 使用 Search Console 的「要求建立索引」。這是外部帳戶操作，本次未代為執行；提交後仍需觀察 Google 是否抓取、選定 canonical，以及是否產生非品牌曝光與點擊。
