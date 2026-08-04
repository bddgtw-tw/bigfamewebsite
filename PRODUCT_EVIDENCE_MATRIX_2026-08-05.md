# Big Fame 八類產品證據矩陣｜2026-08-05

## 用途

本矩陣把目前可用於公開產品頁、SEO／AI 搜尋理解與詢價轉換的素材，分成「可公開的文件／圖面證據」與「仍需按 SKU／專案確認的欄位」。

判斷原則：產品頁可以公開代表性資料，但不得把單一圖面、檔名、估價數量或內部文件誤寫成所有 SKU 的正式規格、MOQ、交期或已完成交付成果。

## 產品盤點

| 產品類別 | 目前可公開的證據 | 可支援的 TA 搜尋／判斷 | 主要缺口 | 目前動作 |
|---|---|---|---|---|
| 展示掛勾 | Product Hook.docx；掛勾長度 50／75／100／150／200 mm；線徑 Φ5／Φ6／Φ8／Φ10；DBTHK001-SLW 代表圖面 50／100／150／200 mm；橫桿尺寸 10×20、14×24、20×40、15×30 mm；PEG／SLW 等方向 | display hooks、slatwall hooks、pegboard hooks、retail display hardware、掛勾尺寸 | 正式 SKU、材質牌號、現行色號、MOQ、交期、包裝與承重仍須確認 | 本輪補入 Product JSON-LD 的代表性 additionalProperty |
| 眼鏡展示掛鉤 | 25 mm pitch、Ø6 mm 孔；2025／2018 圖面尺寸；材料與表面處理的圖面記載；代表性影像檔名 | optical display hooks、eyewear display hardware、眼鏡店展示 | 目前 SKU、正式材質／色號、MOQ、交期與實際供貨範圍 | 已有靜態 Product schema 與證據段落 |
| 防盜展示掛鉤 | 安全需求、安裝系統、商品與現場條件的規格閘門 | anti-theft display hooks、security retail display | 缺少可公開的特定 SKU、尺寸、鎖定機制、承重與案例交付證據 | 保持需求導向，不虛構規格 |
| 洞洞板／層板配件 | 系統方向、代表性產品與圖像素材；部分圖面／尺寸線索 | pegboard accessories、slatwall accessories、retail fixture accessories | 各系列正式尺寸、材質、相容性、MOQ、交期 | 維持產品頁規格確認閘門，待建立 SKU 對照 |
| 價格牌夾／標示配件 | BF-TP-PH0001-01～06 影像系列；壓克力／金屬方向 | price tag holders、shelf label holders、retail signage hardware | 正式尺寸、安裝方式、材質牌號、MOQ、交期 | 已修正 Breadcrumb；暫不新增未充分證據的 schema 屬性 |
| POS／桌上展示 | 目錄中的櫃檯與桌上展示分類；產品／案例導覽 | POS display、countertop display、retail display stand | 正式尺寸、材質、展示容量、包裝、MOQ、交期 | 保持「按型號／圖面／樣品確認」 |
| 模組化展示架 | YC-1524L 尺寸與 3 in 橡膠輪；ARC67-A 尺寸與 4 片白色壓克力板；粉體烤漆方向 | modular retail fixtures、display rack system、store fixture | 正式 SKU 版本、承重、包裝、MOQ、交期、實際專案成果授權 | 已補入 Product JSON-LD 5 項 additionalProperty |
| 客製金屬零件 | 可從照片、PDF、DWG、DXF、STEP、尺寸、材質、表面處理、數量與時程開始評估 | custom metal parts、custom retail hardware、店面五金客製 | 缺少可公開的完整報價／量產／交付證據與通用交期 | 以需求收斂與詢價表單為主，不宣稱通用能力數值 |

## 判斷

目前最值得優先公開結構化的產品順序：

1. 展示掛勾：素材最完整，且直接對應採購、店面設計與 VM 的高意圖搜尋。
2. 模組化展示架：已有可核對的產品欄位，已完成第一輪補強。
3. 眼鏡展示掛鉤：已有圖面級證據，適合持續累積 SKU／圖面版本。
4. 其餘五類：先補 SKU、圖面、尺寸、材質、交期或案例證據，再擴充 Product schema。

## 本輪邊界

- 「文件記載」不等於所有現行 SKU 的正式規格。
- 「代表圖面」不等於已完成交付案例。
- 「詢價表單事件」不等於合格商機或成交。
- 正式 MOQ、交期、承重、材質牌號、報價與交付地點，仍需由 SKU／報價／圖面／樣品／授權案例支持。
