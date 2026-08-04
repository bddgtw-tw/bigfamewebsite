# 詢價事件上下文複核｜2026-08-05 R13

## 本輪修正

前端版本由 `1.3.24` 更新為 `1.3.25`。`bf_form_submit_attempt`、`bf_form_submit_error`（Web3Forms rejected／network error）現在都傳送以下非個資欄位：

- `inquiry_category`
- `inquiry_role`
- `inquiry_product`
- `requested_files`
- `source_page_path`

這讓後續 GA4 可以區分：哪一類 TA、哪一種產品、從哪個頁面開始詢問，以及在哪個送出階段失敗。

## 靜態驗收

- `node --check js/main.js`：通過
- 三類事件上下文完整性：`attempt=True`、`rejected=True`、`network=True`
- 171 個 HTML 的 `main.js` cache version：全部為 `1.3.25`
- 8 類產品頁品質：48／48、0 failures
- 案例頁合約：72／72、0 failures
- 8 類產品三語頁的 90 個詢價連結：均具 `category` 與 `role`
- 三語 TA／技術資源入口的 57 個詢價連結：均具 `category` 與 `role`

## 公開 runtime 回讀

- 公開 `https://www.bigfame.co/js/main.js?v=1.3.25` 回應 HTTP 200，讀到 `SITE_VERSION = '1.3.25'`，並包含送出嘗試與完整上下文欄位。
- 公開繁中聯絡頁回應 HTTP 200，載入 `main.js?v=1.3.25`；以展示掛勾、採購角色、尺寸圖與 `/tw/display-hooks` 來源參數進入時，`buyer_role`、`inquiry_type`、`product_category`、`requested_files`、`source_category`、`source_role`、`source_product` 與 `source_page` 均正確預填。
- 公開瀏覽器 runtime 的錯誤／警告讀回為空；本次未提交表單。

## 尚未宣稱的事項

- 尚未取得 GA4 管理權限，因此尚未在 GA4 後台註冊或讀回所有自訂維度。
- 尚未送出真實表單，因此尚未證明 Web3Forms 收件或實際 `generate_lead`。
- 事件程式與靜態頁面完整，不等於 GA4 已有有效詢價資料。
