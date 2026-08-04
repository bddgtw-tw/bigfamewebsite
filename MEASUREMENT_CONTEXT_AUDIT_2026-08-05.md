# Big Fame 網站量測與詢價脈絡稽核

稽核日期：2026-08-05

## 結論

網站端已能把「角色、需求類別、產品、希望資料、來源頁」帶入詢價表單；本輪補正兩項量測問題：

1. `display-hooks` 同時是產品入口與 TA 入口，現在會以 `content_role=ta_entry_and_product` 保存雙重脈絡，不再被單一分類覆蓋。
2. 詢價頁完成脈絡預填後，新增 `bf_inquiry_context_ready` 事件，只送受控分類值，不送姓名、Email、電話或需求文字。

## 目前已具備的事件

| 事件 | 用途 | 網站端狀態 |
|---|---|---|
| `bf_page_context` | 記錄語系、頁型、內容 slug、TA 入口與產品脈絡 | 已有 |
| `bf_contact_cta_click` | 判斷哪個 CTA 將人送進詢價 | 已有 |
| `bf_inquiry_context_ready` | 判斷 CTA 參數是否成功帶入表單 | 本輪新增 |
| `form_start` | 判斷使用者開始填寫 | 已有 |
| `bf_form_submit_attempt` | 判斷送出嘗試與需求分類 | 已有 |
| `generate_lead` | 判斷 Web3Forms 成功回傳 | 已有；實際有效詢問仍須人工確認 |
| `bf_form_submit_error` | 判斷表單拒絕或網路／解析錯誤 | 已有 |

## 已知基準

依 2026-08-05 的公開後台讀回：

- Search Console 期間 2026-07-16 至 2026-08-02：4 clicks、383 impressions、CTR 1%、平均排名 9.7；26 個查詢；16 個已索引、51 個尚未索引。
- GA4 過去 28 天讀回：`bf_contact_cta_click` 7、`form_start` 2、`generate_lead` 2；目前沒有足夠證據把 `generate_lead` 等同於有效商機。
- GA4 已存在部分分類維度；`inquiry_role`、`inquiry_product`、`requested_files`、`source_page_path` 是否已在後台註冊，尚未取得後台權限證據。

## 尚未完成且不能假稱完成

這些是 GA4／Search Console 後台或營運流程事項，不是單靠網站程式即可證明：

- 在 GA4 註冊並驗證 `inquiry_role`、`inquiry_product`、`requested_files`、`source_page_path` 等自訂維度。
- 建立探索報表：TA 入口 → CTA → 脈絡成功 → 表單開始 → 送出嘗試 → Web3Forms 成功 → 人工確認有效商機。
- 建立 Web3Forms 收件與 CRM／Email 的有效商機對帳，排除測試、垃圾信與重複詢問。
- 以至少 28 天新資料重新比較三個 TA 入口、八個優先產品頁與案例頁的實際轉換差異。

## 版本與驗證

- 網站 JavaScript 版本：`1.3.24`。
- `node --check js/main.js`：通過。
- 本次變更已寫入所有頁面的 `main.js` cache version，以確保公開頁面取得新量測程式。
- 公開 runtime 仍需在部署後重新確認：`display-hooks` 的 GA4 頁型／雙重角色，以及詢價頁 `bf_inquiry_context_ready` 是否實際送出；目前不能把本地程式檢查當成公開事件已收到的證據。
