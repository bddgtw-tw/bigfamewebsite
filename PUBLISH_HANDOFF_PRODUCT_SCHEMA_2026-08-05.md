# 產品 Product schema 發布交接

> 變更與讀回日期：2026-08-05（Asia/Taipei）  
> commit：`fc08416 Bump frontend asset version for product schema`

## 變更內容

八類產品頁、三種語言，共 24 頁，透過版本化共用腳本補足或保留 `schema.org/Product`：

- 展示掛勾
- 眼鏡展示掛勾
- 防盜展示掛勾
- 槽板／洞洞板配件
- 價格條與標示配件
- POS 展示架
- 模組化展示架
- 客製金屬零件

新增 runtime Product schema 只使用頁面已公開且可核對的基本資料：

- Product name
- clean URL 與 `#product` entity ID
- 頁面 description
- Product category
- Big Fame brand
- 頁面代表圖片

不加入：

- SKU
- Offers／價格
- MOQ
- lead time／交期
- 未核准承重、測試或交付主張

若頁面原本已有靜態 Product schema，腳本會跳過，不重複建立第二個 Product entity。

## 快取版本

產品頁共用腳本已由 `1.3.14` 升至 `1.3.15`，避免瀏覽器或 CDN 沿用只含舊 Service schema 的版本。

## 本地驗收

- `node --check js/main.js`：通過
- `git diff --check`：通過
- `PRODUCT_QUALITY_PAGES=24`
- `PRODUCT_QUALITY_FAILURES=0`
- `main`、`draft`、`origin/main`、`origin/draft`：已同步至 `fc08416`

## 公開 runtime 讀回

三語八類產品頁逐一讀取公開 DOM：

- Product entity：24／24
- entity type：`Product`
- 新增 runtime entity 的圖片：已讀回
- `offers`：0
- `sku`：0
- MOQ 欄位：0
- lead time 欄位：0

公開讀回使用 `?v=fc08416`，並確認產品頁載入 `js/main.js?v=1.3.15`。

## 證據邊界

- Product schema 只標示產品／產品集合頁的已核對身份，不代表每個頁面已有單一 SKU 或現行報價。
- 不宣稱 Google 已建立索引、產生 Rich Result 或 AI 引用；這些需由 Search Console 與後續 28 天量測確認。
- 正式 MOQ、交期、材質牌號、承重與客製條件仍依 SKU、圖面、報價、樣品與專案確認。
