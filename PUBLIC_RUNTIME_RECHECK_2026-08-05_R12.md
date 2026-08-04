# Big Fame 公開網站 runtime 複核｜2026-08-05 R12

本次複核只記錄公開網站可直接觀察到的狀態，不把本地檔案或部署意圖當成公開成果。

## 公開頁面

| 頁面 | 結果 | 可觀察證據 |
|---|---|---|
| `https://www.bigfame.co/tw/procurement` | 通過 | 正常載入；頁面標題為「台灣店面展示設備採購｜Big Fame」；H1 為「台灣店面展示設備採購」；canonical 指向同一 clean URL；未設定 `noindex`。 |
| `https://www.bigfame.co/tw/contact?...` | 通過 | 由展示掛勾產品頁帶入採購角色與圖面需求後，`source_category`、`source_role`、`source_product`、`requested_files`、`source_page`、`buyer_role`、`inquiry_type` 與 `product_category` 均正確預填。 |

## 邊界

- 這次沒有送出真實聯絡表單，因此 Web3Forms 實際收件、GA4 `generate_lead` 後台資料與有效詢價仍未證明。
- 公開頁面已載入 GA4 與網站主程式的 script 標記；本次不把第三方分析服務是否成功入帳誤判為已驗證。
- Search Console 的索引要求仍需在具備權限的帳戶中由使用者確認後提交；目前 Sitemap 與網站端可索引條件已完成，但新 TA 頁面是否已被 Google 個別收錄仍未證明。

## 判定

網站端的 URL、TA 入口、產品頁、案例頁與詢價上下文已具備可公開驗收的基礎；目前真正未閉環的是外部平台權限、真實送單收件、GA4 後台歸因，以及 Google 個別索引與非品牌搜尋成效。
