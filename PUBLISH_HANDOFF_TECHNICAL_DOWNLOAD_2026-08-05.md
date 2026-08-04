# 技術資源代表性尺寸圖下載交接

日期：2026-08-05  
提交：`0ea11b8`

## 本次處理

三語 `technical-resources` 頁面的代表性 DBTHK001-SLW 尺寸圖連結，新增明確的 `download` 屬性；同時更新 `scripts/generate_technical_resources.py`，避免日後生成頁面時遺失。

下載內容仍明確標示為代表性尺寸圖，不代表所有展示掛勾 SKU，也沒有把它宣稱為通用 CAD、正式承重、MOQ 或交期資料。

## 驗收結果

- 本地 `TECHNICAL_DOWNLOAD_AUDIT=3`，失敗 0
- 公開三語頁面均 HTTP 200、H1=1，下載屬性與圖片連結均可讀回
- 公開圖片資產 `https://www.bigfame.co/images/product-display-hooks-dim.jpg`：HTTP 200
- `python -m py_compile scripts/generate_technical_resources.py`：通過
- `git diff --check`：通過

## 後續

PDF、CAD、DWG、DXF、STEP 與材質／表面處理資料仍採詢問流程，依 SKU、版本、圖面、樣品與專案條件確認，不建立未核准的通用資料包。
