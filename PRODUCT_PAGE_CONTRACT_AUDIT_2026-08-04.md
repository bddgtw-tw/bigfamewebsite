# Big Fame 產品頁契約驗收

更新日期：2026-08-04

## 驗收範圍

8 類產品 × 繁中、英文、日文，共 24 個產品頁：

- 展示掛勾
- 眼鏡展示掛勾
- 防盜掛勾
- 槽板／洞洞板配件
- 價格條與標示配件
- POS 展示架
- 模組化展示架
- 客製金屬零件

## 本次結果

使用 `scripts/audit_product_page_contract.py` 逐頁檢查以下頁面契約欄位：

- H1 與 meta description
- 適用店型／展示系統
- 材質、尺寸、表面處理
- MOQ／交期的確認邊界
- 客製範圍
- 圖片或圖面
- 相關案例
- 詢價 CTA
- FAQPage 結構化資料
- 中英日產品名稱

結果：24／24 頁未出現 `MISSING_CONTRACT`。

另以 `scripts/audit_product_page_quality.py` 進行可見內容驗收，確認產品名稱、適用店型／系統、材質、尺寸、表面處理、MOQ／交期邊界、客製範圍、圖像／圖面、相關案例、詢價 CTA 與可見 FAQ 均實際存在；結果為 `PRODUCT_QUALITY_PAGES=24`、`PRODUCT_QUALITY_FAILURES=0`。

18 個產品頁原本只有 FAQPage JSON-LD、缺少可供驗收的可見 FAQ 標記，已補上 `data-bf-faq="1"`，使可見 FAQ 與結構化資料可以互相核對。

## 判讀限制

這是「頁面契約存在性」驗收，不代表每個產品的規格都已完整核准。正式材質牌號、SKU、MOQ、交期、承重與客製條件，仍依來源文件、SKU、圖面、樣品與專案確認。未有證據支持的通用商業數字不得由此驗收推導。
