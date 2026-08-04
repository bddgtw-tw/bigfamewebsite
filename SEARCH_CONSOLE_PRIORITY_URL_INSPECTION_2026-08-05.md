# Search Console 重要頁面網址審查｜2026-08-05

## 審查頁面

以 Search Console `sc-domain:bigfame.co` 的「網址審查」只讀檢查：

- `https://www.bigfame.co/tw/procurement`
- `https://www.bigfame.co/en/display-hooks`
- `https://www.bigfame.co/tw/technical-resources`

## 實測結果

三個頁面目前都顯示：

- 網址不在 Google 服務中
- 尚未編入索引
- Google 尚未辨識的網址
- Sitemap：未偵測到任何參照 Sitemap
- 上次檢索時間：不適用
- 使用者宣告的標準網址：不適用
- Google 所選的標準網址：不適用

## 與 Sitemap 的關係

本地 `sitemap.xml` 已包含上述網址，且 Search Console 在 2026-08-05 顯示：

- Sitemap 狀態：成功
- Google 發現頁面：96
- Google 發現影片：0

因此目前較精確的判讀是：Sitemap 已被讀取，但 Google 尚未對這些新頁面完成個別發現／抓取；不能解讀為 canonical、robots 或頁面內容已被判定有問題。

## 已確認的網站端條件

- 三頁均為公開 clean URL。
- 三頁均有 canonical、`zh-TW`／`en`／`ja`／`x-default`。
- 三頁均有 H1、FAQ 與對應內部連結。
- 公開頁面 HTTP 200。

## 下一個外部操作

可在 Search Console 對三個優先網址使用「要求建立索引」，但這會改變外部帳戶狀態，本次只完成讀取，沒有代為提交。提交後仍不能保證立即索引或排名，需再觀察抓取與搜尋成效。
