# GA4 自訂維度註冊交接規格｜2026-08-05

## 目前狀態

- Measurement ID：`G-PDW4NPHHW8`
- Property：Big Fame Website
- 前端事件已送出上下文參數，但後台尚未完成四個自訂維度註冊。
- 本次直接進入 GA4 管理頁檢查時，登入帳號收到「缺少權限」訊息，無法變更設定，也未送出存取申請。

## 需要註冊的四個事件層級自訂維度

| 顯示名稱 | 事件參數 | Scope | 用途 |
|---|---|---|---|
| Inquiry role | `inquiry_role` | Event | 比較 buyer、designer、vm、brand 等角色的 CTA、表單與 lead |
| Inquiry product | `inquiry_product` | Event | 比較產品頁／產品 slug 對詢問與 lead 的影響 |
| Requested files | `requested_files` | Event | 判斷 dimension drawing、CAD、material、sampling 等資料需求 |
| Source page path | `source_page_path` | Event | 判斷哪個 TA、產品或案例頁帶來詢問 |

## 前端證據

`js/main.js` 已在以下事件帶出參數：

- `bf_inquiry_context_ready`
- `bf_contact_cta_click`
- `generate_lead`

既有 GA4 自訂維度包含 `inquiry_category`、`product_category`、`contact_method`、`site_language`、`inquiry_type`；本次四個新增參數尚未列入後台註冊清單。

## 有權限後的驗收順序

1. 在 GA4 Admin → Data display → Custom definitions 建立上表四個 Event-scoped custom dimensions。
2. 使用公開聯絡頁測試採購、設計、VM、品牌／展店四種查詢參數。
3. 於 DebugView 或即時事件確認四個參數值非空且只包含受控值。
4. 以 `form_start`、`generate_lead`、`bf_contact_cta_click` 建立角色／產品／來源頁切分報表。
5. 將有效商機人工對帳後，才把 `generate_lead` 當成有效 B2B lead KPI。

## 邊界

本文件是註冊規格與驗收交接，不代表 GA4 後台已完成設定；目前阻礙是登入帳號對 Big Fame GA4 資源沒有足夠權限。

