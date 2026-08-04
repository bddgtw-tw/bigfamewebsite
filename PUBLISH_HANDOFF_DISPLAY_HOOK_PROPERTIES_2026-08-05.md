# 發布交接：展示掛勾 Product properties｜2026-08-05

## 狀態

- 已寫入：`js/main.js` 的 `verifiedProperties['display-hooks']`
- 已套用：162 個三語 HTML 頁面的 `main.js?v=1.3.18`
- 已推送：`main` 與 `draft`
- commit：`4a5d7a8`
- 已公開驗證：三語 clean URL 均回傳 200，且 runtime 注入 Product JSON-LD

## 公開的代表性資料

Product schema 的 `additionalProperty` 共 4 項：

1. 文件記載掛勾長度：50、75、100、150、200 mm
2. 文件記載線徑：5.0、6.0、8.0、10.0 mm
3. DBTHK001-SLW 代表圖面長度：50、100、150、200 mm
4. 文件記載橫桿尺寸：10×20、14×24、20×40、15×30 mm

所有欄位均使用 documented／representative 的語意，未宣稱為所有現行 SKU 的固定規格。

## 公開 runtime readback

| URL | HTTP | `main.js` | H1 | Product | properties | CTA |
|---|---:|---:|---:|---:|---:|---:|
| `/tw/display-hooks` | 200 | 1.3.18 | 1 | true | 4 | 4 |
| `/en/display-hooks` | 200 | 1.3.18 | 1 | true | 4 | 4 |
| `/jp/display-hooks` | 200 | 1.3.18 | 1 | true | 4 | 4 |

驗收時間：2026-08-05（Asia/Taipei）。驗收方式：公開頁面 DOM／runtime readback；未提交詢價表單。

## 尚未被本次發布證明的事項

- 正式 SKU 對照、材質牌號、色號、MOQ、交期、包裝、承重與現行供貨範圍。
- 以上代表性資料是否適用於特定客戶專案，仍須由 SKU、最新圖面、報價與樣品確認。
