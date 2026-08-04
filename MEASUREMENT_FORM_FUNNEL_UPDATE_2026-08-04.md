# 表單漏斗量測更新

更新日期：2026-08-04

## 新增事件

`js/main.js` 現在在表單送出時新增兩個不含個資的事件：

- `bf_form_submit_attempt`：使用者按下送出，記錄 inquiry type、產品類別、來源類別與角色。
- `bf_form_submit_error`：Web3Forms 拒絕，或發生網路／解析錯誤，記錄錯誤類型與非個資分類。

成功回傳仍使用既有 `generate_lead`，不改變成功條件，也不送出姓名、Email、電話、需求文字或圖面連結。

## 漏斗判讀

`bf_contact_cta_click` → `form_start` → `bf_form_submit_attempt` → `generate_lead`

若有 `bf_form_submit_attempt` 但沒有 `generate_lead`，可再用 `bf_form_submit_error` 判斷是 Web3Forms 拒絕或網路／解析問題；若兩者都沒有，則代表尚未完成送出或事件尚未被 GA4 讀回。

## 驗證界線

本次已完成本地 JavaScript 靜態讀回；未提交公開表單，因此沒有宣稱新的 `generate_lead` 已在 GA4 實際發生。公開站發布後需以 GA4 即時／事件報表確認事件是否收到。
