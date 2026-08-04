# 展示掛勾／槽板配件／模組化展示架靜態 Schema 發布交接

日期：2026-08-05  
版本：`af7bfab`

## 本次變更

將目前已有文件／圖面支持的代表性屬性，直接寫入三語 flat／clean HTML Product JSON-LD：

- `display-hooks`：4 項掛勾長度、線徑、DBTHK001-SLW 長度與 crossbar 尺寸。
- `slatwall-pegboard-accessories`：3 項 GLOOVING 系列尺寸、變體與材料標示。
- `modular-fixtures`：5 項 YC-1524L／ARC67-A 尺寸、腳輪、壓克力板與粉體塗裝方向。

## 本地驗收

- `node --check js/main.js`：通過
- `audit_product_page_quality.py`：24／24 通過
- `audit_case_page_contract.py`：36／36 通過
- 18 個頁面：各有 1 個 Product JSON-LD，屬性數量為 4／3／5

## 公開驗收

三語九個 clean URL 全部 HTTP 200、單一 H1、公開 `main.js=1.3.21`，並讀回：

- 展示掛勾：各 4 項 Product `additionalProperty`
- 槽板／洞洞板配件：各 3 項
- 模組化展示架：各 5 項

## 證據邊界

這些是文件、圖面或來源影像可核對的代表性屬性，不代表所有現行 SKU、承重、MOQ、交期、庫存或已完成客戶交付。正式條件仍依 SKU、最新圖面、報價、樣品與專案確認。
