# Modular Fixtures Product Properties｜公開讀回

## 1. 目的

將模組化展示架頁面中已由來源資料支持的尺寸、腳輪、板材與表面處理，加入 Product JSON-LD 的 `additionalProperty`，讓搜尋引擎與 AI 更容易理解頁面能回答的具體規格。

## 2. 變更

- Commit：`dac4cc6`
- `js/main.js`：`1.3.15` → `1.3.17`
- 三語共 162 個 HTML 頁面同步引用 `main.js?v=1.3.17`
- 產品頁品質稽核：24／24 通過
- 新增的 5 個已核對屬性：
  1. YC-1524L：24 × 30 × 56 in 或 48 × 30 × 56 in
  2. YC-1524L：3 in rubber casters
  3. ARC67-A：24.5 × 24.5 × 59 in
  4. ARC67-A：4 white acrylic panels
  5. Powder-coat metal finish

## 3. 公開 runtime readback

讀取日期：2026-08-05。公開網址唯讀讀取，沒有送出表單。

| 語系 | H1 | Product entity | `additionalProperty` | JS |
|---|---:|---:|---:|---|
| `/tw/modular-fixtures` | 1 | `Product` | 5 | `1.3.17` |
| `/en/modular-fixtures` | 1 | `Product` | 5 | `1.3.17` |
| `/jp/modular-fixtures` | 1 | `Product` | 5 | `1.3.17` |

## 4. 證據邊界

這些屬性是 Sunny Display 來源資料中的代表性變體，不代表所有模組化展示架共用規格，也不代表目前可直接下單的單一 SKU。

仍不加入：

- MOQ
- 交期
- 價格／Offers
- 承重
- 未核准的現行 SKU 或交付承諾

正式規格仍需依對應圖面、樣品、報價與專案條件確認。
