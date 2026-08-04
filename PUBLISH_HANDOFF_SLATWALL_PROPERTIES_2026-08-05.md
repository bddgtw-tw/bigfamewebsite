# 發布交接：GLOOVING 槽板／洞洞板 Product properties｜2026-08-05

## 狀態

- 已寫入：`js/main.js` 的 `verifiedProperties['slatwall-pegboard-accessories']`
- 已修改：既有靜態 Product JSON-LD 的安全補強流程；不另製造重複 Product entity
- 已套用：162 個三語 HTML 頁面的 `main.js?v=1.3.19`
- 已推送：`main` 與 `draft`
- 最新 commit：`a12dd17`
- 已公開驗證：三語 clean URL 均回傳 200，且 runtime 將 3 項 properties 補入既有 Product entity

## 公開的文件／圖像線索

1. GLOOVING 系列圖記載 `800 × 450 mm`
2. 尺寸圖檔名標示 `10 cm` 與 `15 cm` 變體
3. 影像標示 `Aluminium` 材質方向

以上均保留 documented／source image label 語意；正式 SKU、板厚、承重、相容性、材質牌號、MOQ、交期與表面處理仍須按圖面、報價與樣品確認。

## 公開 runtime readback

| URL | HTTP | `main.js` | H1 | Product | properties | CTA |
|---|---:|---:|---:|---:|---:|---:|
| `/tw/slatwall-pegboard-accessories` | 200 | 1.3.19 | 1 | true | 3 | 3 |
| `/en/slatwall-pegboard-accessories` | 200 | 1.3.19 | 1 | true | 3 | 3 |
| `/jp/slatwall-pegboard-accessories` | 200 | 1.3.19 | 1 | true | 3 | 3 |

驗收時間：2026-08-05（Asia/Taipei）。驗收方式：公開頁面 DOM／runtime readback；未提交詢價表單。

## 案例證據邊界

PAGE 化妝品展示器目前仍是產品開發／報價文件紀錄，已有尺寸、材質、包裝與文件時程，但尚未證明客戶授權、正式 Big Fame 合約分工、最終交付與成果。因此本輪不把它升格為完整客戶案例。
