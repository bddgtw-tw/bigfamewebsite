# Big Fame 產品頁與 TA 入口欄位稽核

日期：2026-08-05

## 產品頁

範圍：8 類優先產品 × 3 語言，共 24 頁。

逐頁確認：

- 中／英／日產品名稱
- 適用店型或展示系統
- 材質與表面處理
- 尺寸或圖面依據
- MOQ／交期的證據邊界
- 客製範圍
- 圖片或圖面資產
- 至少一個案例連結
- 詢價 CTA
- FAQPage 與頁面 FAQ 標記

結果：24／24 通過。既有 `audit_product_page_quality.py`：24 pages、0 failures。

## TA 入口

範圍：

- `procurement`：台灣店面展示設備採購
- `design-support`：零售空間展示系統與設計支援
- `display-hooks`：展示掛勾與陳列五金

三語入口均具備：H1、FAQ、Service schema、產品連結、案例連結、技術資源連結與詢價脈絡。

## URL／案例補正

`case-page-cosmetic-organizer` 原有 flat page 與 sitemap，但缺三語 clean route；本次新增三個 `index.html`，並公開驗收 HTTP 200、H1、FAQPage、source record、case contract、產品連結、CTA 與 canonical 均正常。

## 邊界

產品頁的 MOQ、交期、正式 SKU、材質牌號與商業條件仍以型號、圖面、報價與樣品確認；稽核通過不等於所有產品已有固定商業承諾。
