# EYEHK 眼鏡展示掛勾靜態 Product Schema 發布交接

日期：2026-08-05  
版本：`5a9d96b`

## 本次變更

將 EYEHK 圖面可核對的眼鏡展示掛勾資訊直接寫入三語 flat／clean HTML 的 Product JSON-LD：

1. Drawing pitch：25 mm
2. Drawing hole diameter：6 mm
3. EYEHK 2025 pegboard drawing dimensions：160／175／150.93／128／25.4 mm 圖面標示
4. EYEHK 2018 drawing material notes：t2.0 iron plate、4.0 mm iron wire
5. EYEHK 2018 drawing finish note：Black powder coating
6. EYEHK 2018 design notes：end chamfer、approximately 2° upward angle

估價文件中的 1000 支備註沒有放入 Schema，避免被解讀為訂單數量或 MOQ。

## 本地驗收

- `node --check js/main.js`：通過
- `audit_product_page_quality.py`：24／24 通過
- `audit_case_page_contract.py`：36／36 通過
- 三語 flat／clean Product JSON-LD：各 6 項 `additionalProperty`

## 公開驗收

三語 clean URL 均 HTTP 200、單一 H1、公開 `main.js` 為 `1.3.21`，靜態 Product JSON-LD 各讀回 6 項屬性：

- `https://www.bigfame.co/tw/optical-hooks`
- `https://www.bigfame.co/en/optical-hooks`
- `https://www.bigfame.co/jp/optical-hooks`

## 證據邊界

這些是 EYEHK 圖面／文件可核對的代表性證據，不代表所有眼鏡掛勾 SKU、目前庫存、正式 MOQ、交期、承重或已完成客戶交付。正式條件仍依 SKU、最新圖面、樣品與專案確認。
