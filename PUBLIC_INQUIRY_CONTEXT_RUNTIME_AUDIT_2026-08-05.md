# Big Fame 公開詢價上下文 Runtime 驗證｜2026-08-05

## 驗證目的

確認 TA 從產品、採購或設計情境進入公開聯絡頁後，表單是否真的保留角色、詢問類型、產品類別與所需資料，而不是只確認原始 HTML 或 JavaScript 存在。

## 公開網址與測試結果

測試網址：`https://www.bigfame.co/tw/contact`

| 情境 | 查詢參數 | 表單實際結果 |
|---|---|---|
| 採購／商社 | `category=display_hardware&role=buyer&product=display-hooks&requested_files=dimension_drawing&source_page=/tw/display-hooks` | `buyer_trading_agent`、`quote`、`display_hardware`、`dimension_drawing`；來源產品 `display-hooks`、來源頁 `/tw/display-hooks` |
| 店面設計／工程 | `category=system_fixtures&role=designer&requested_files=cad_files` | `store_design_engineering`、`quote`、`system_fixtures`、`cad_files` |
| VM／陳列 | `category=pos_displays&role=vm&requested_files=sampling_review` | `visual_merchandising`、`quote`、`pos_displays`、`sampling_review` |
| 品牌／展店 | `category=custom_metal_components&role=brand&requested_files=material_finish` | `brand_store_development`、`custom_dev`、`custom_metal_components`、`material_finish` |

## 判定

- 目標五的「角色區分」與「上下文預填」已通過公開 runtime 驗證。
- 產品頁的產品 slug、來源頁與資料需求可被帶入聯絡表單。
- 本次未送出真實表單，沒有產生外部郵件或商業資料變更；只驗證頁面載入後的欄位值。
- GA4 後台自訂維度註冊、事件是否進入正確報表，以及有效商機對帳，仍未由本次測試證明。

