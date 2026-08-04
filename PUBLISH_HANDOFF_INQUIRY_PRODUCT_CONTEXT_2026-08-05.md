# 發布交接：詢價流程保留具體產品脈絡｜2026-08-05

## 變更

- 產品頁 CTA 會自動加入 `product=<slug>`。
- 聯絡頁新增隱藏欄位 `source_product`。
- 表單初始化會保存：產品 slug、產品類別、角色與同站來源頁。
- `bf_contact_cta_click`、`form_start`、`bf_form_submit_attempt`、`generate_lead` 事件新增 `inquiry_product`。
- 版本：`main.js?v=1.3.20`

## 公開 runtime readback

測試頁：`/tw/display-hooks`

從產品頁 Hero CTA 實際導向：

`/tw/contact?category=display_hardware&role=buyer&product=display-hooks`

聯絡頁讀回：

| 欄位 | 值 |
|---|---|
| `source_product` | `display-hooks` |
| `source_category` | `display_hardware` |
| `source_role` | `buyer` |
| `source_page` | `https://www.bigfame.co/tw/display-hooks?verify=0c02ea8b` |

同頁公開驗收：HTTP 200、`main.js 1.3.20`、產品頁 CTA 4 個均帶 product slug。

驗收時間：2026-08-05（Asia/Taipei）。未填寫姓名、Email，也未提交真實表單。

## 發布狀態

- commit：`0c02ea8`
- `main`、`draft`、`origin/main`、`origin/draft` 已同步。
- 這項變更只保存需求脈絡，不代表已取得有效商機；`generate_lead` 仍需真實詢問與後續商機品質判斷。
