# 手機版 390×844 Runtime 驗收｜2026-08-05

## 驗收頁面

`https://www.bigfame.co/tw/?release=0346b54b`

驗收使用 390×844 的明確行動版視窗；驗收完成後已恢復瀏覽器原本的視窗設定。

## 首頁結果

- `h1` 完整存在，版面範圍：`left=18`、`right=357`、`top=284`、`bottom=438`
- 主要 CTA 範圍：`left=18`、`right=357`、`top=583`、`bottom=635`
- 次要 CTA 範圍：`left=18`、`right=357`、`top=647`、`bottom=700`
- Hero 高度：`844px`
- 手機選單按鈕可見；初始導覽列隱藏
- Hero 影片在手機版為 `display:none`，保留 fallback 圖像
- `body.scrollWidth=375`、`body.clientWidth=375`，沒有水平溢位

## 選單互動

- 開啟後：`.nav-menu.active=true`、`aria-expanded=true`、`body.menu-open=true`
- 關閉後：`.nav-menu.active=false`、`aria-expanded=false`、`body.menu-open=false`
- 行動版導覽連結數：6

## CTA 與詢價表單

從首頁「描述我的需求」進入：

- URL 保留 `category=integration&role=buyer`
- `source_category=integration`
- `source_role=buyer`
- `source_page=/tw/`
- `source_product=unspecified`
- `buyer_role=buyer_trading_agent`
- `inquiry_type=integration`
- 表單控制項：21 個
- 超出視窗的控制項：0

## 結論

首頁 390×844 的首屏可讀性、CTA 可點擊性、手機選單與詢價上下文預填均通過公開 runtime 驗收。這證明手機版基礎體驗已完成；仍不代表所有產品、案例與三語頁面都完成逐頁視覺驗收。
