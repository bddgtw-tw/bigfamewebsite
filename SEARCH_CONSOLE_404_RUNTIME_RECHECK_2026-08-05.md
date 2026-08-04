# Search Console 404 與公開網址再驗證｜2026-08-05

## Search Console 目前讀回

- Property：`sc-domain:bigfame.co`
- 404 報表上次更新：2026-07-24
- 報表列出的 404 數量：17
- Sitemap：2026-08-05 送出與讀取均成功
- Google 發現頁面：96
- Google 發現影片：0

## 404 報表與現場狀態的差異

Search Console 的 404 示例仍包含：

- `/thank-you-page`
- `/our-works`
- `/know-how`
- `/overview`
- `/blog`
- `/blog/author/benny`
- `/blog/retail-fixture-blog`

這些資料的最後檢索日期落在 2026-07-13～2026-07-25，早於目前的 redirect 版本。

## 公開現場再驗證

2026-08-05 以 HTTP HEAD 讀回：

| 舊網址 | 現況 |
|---|---|
| `/thank-you-page` | 301 → `/en/contact` |
| `/our-works` | 301 → `/en/applications` |
| `/know-how` | 301 → `/en/services` |
| `/overview` | 301 → `/en/about` |
| `/blog` | 301 → `/en/applications` |

`/blog/author/benny` 與 `/blog/retail-fixture-blog` 也已在 `_redirects` 中設定導向，待 Search Console 下一輪重新抓取後再觀察報表數量是否下降。

## 結論與邊界

- 目前不能宣稱 Search Console 404 報表已清零，因為 Google 尚未重新處理全部舊資料。
- 可以確認主要舊網址在公開站現場已不再直接 404。
- 不提交「驗證修正後的項目」操作，保留 Search Console 外部狀態變更給具備明確操作授權的人員。
