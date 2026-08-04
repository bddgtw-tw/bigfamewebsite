# Product Breadcrumb Hierarchy｜公開讀回

## 1. 問題

價格條與標示配件、模組化展示架的 Breadcrumb JSON-LD，原本在部分三語頁面把 parent name 寫成「展示掛勾／Display Hooks／ディスプレイフック」。這會讓搜尋引擎與 AI 誤解產品階層。

## 2. 修正

- Commit：`caf118a`
- 修正頁面：價格條與標示配件、模組化展示架
- 三語 clean route 與 legacy HTML 共 12 頁
- 正確 parent：
  - 繁中：`產品與能力` → `https://www.bigfame.co/tw/products`
  - English：`Products` → `https://www.bigfame.co/en/products`
  - 日本語：`製品` → `https://www.bigfame.co/jp/products`

## 3. 公開驗收

讀取日期：2026-08-05。六個 clean URL 均回應 200，並逐頁解析公開 JSON-LD：

| 頁面群組 | 語系 | Breadcrumb parent | H1 | Product entity |
|---|---|---|---:|---:|
| 價格條與標示配件 | 繁中 | 產品與能力 | 1 | 有 |
| 模組化展示架 | 繁中 | 產品與能力 | 1 | 有 |
| Price Tag Holders | English | Products | 1 | 有 |
| Modular Fixtures | English | Products | 1 | 有 |
| 価格・表示アクセサリー | 日本語 | 製品 | 1 | 有 |
| モジュール什器 | 日本語 | 製品 | 1 | 有 |

瀏覽器 DOM 另讀回繁中價格條頁：Breadcrumb parent=`產品與能力`、H1=1、Product entity 存在。

## 4. 判定

本次完成的是產品階層語意修正，不改變產品規格、MOQ、交期或商業條件。後續仍需持續檢查新增產品頁是否沿用正確 parent 與 clean URL。
