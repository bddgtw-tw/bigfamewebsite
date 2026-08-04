# 三語首頁 B2B 搜尋入口重建交接

日期：2026-08-05

## 本次修正

- 重建 `/tw/`、`/en/`、`/jp/` 首頁的可讀 metadata、Organization JSON-LD、FAQPage JSON-LD 與首屏文字。
- 三語首頁新增並明確串接：採購、店面設計／建築、VM／展示配件三類 TA 入口。
- 首頁直接連到 8 類優先產品、服飾／Urban Warehouse／眼鏡案例、技術資源與詢價流程。
- 保留高對比 Hero overlay、手機停用背景影片的既有行為，以及已壓縮的 `hero-apparel-store-blurred-foot-traffic-web-20260804.mp4`。
- 角色卡先導向 TA clean route，再由 TA 入口頁帶入詢價，避免首頁直接跳過搜尋內容層。

## 本機驗收

- 三語首頁各 1 個 H1。
- 三語首頁各 2 個可解析 JSON-LD：Organization、FAQPage。
- 全站 HTML 內部 `.html` href：0。
- 全站 JSON-LD 解析錯誤：0。
- `audit_case_page_contract.py`：36 頁，0 failures。
- `audit_product_page_quality.py`：24 頁，0 failures。

## 公開 runtime 驗收

公開網址：

- `https://www.bigfame.co/tw/`
- `https://www.bigfame.co/en/`
- `https://www.bigfame.co/jp/`

三頁均 HTTP 200，且確認：1 個 H1、Organization、FAQPage、三個 TA clean route、優先產品連結存在，且未再出現本次稽核所辨識的編碼損壞字串。

最新發布 commit：`6353e42`。

## 行動版與表單 runtime 驗收

- 以公開 `/tw/` 於 `390 × 844` viewport 驗收：Hero 標題可見、首屏兩個 CTA 均可見，按鈕高度 53px，頁面寬度沒有水平溢出。
- 行動版選單按鈕可見，尺寸 44 × 44px。
- 由公開聯絡頁讀回：`inquiry_type=quote`、`product_category=display_hardware`、`buyer_role=buyer_trading_agent`、`requested_files=dimension_drawing`、`source_page=/tw/display-hooks`、`source_product=display-hooks`，未送出表單。

## 尚未證明

- 尚未有足夠 GA4／Search Console 資料證明首頁重建已帶來有效詢問或非品牌流量。
- 影片仍需持續觀察 LCP、行動裝置流量與實際瀏覽器效能。
