# PAGE 藥妝桌上展示詢問上下文發布交接

日期：2026-08-05  
版本：`8e1f09a`

## 本次變更

三語 PAGE 桌上型化妝品收納展示產品頁與資料紀錄頁的詢問 CTA 加入：

- `product=cosmetic-organizers`
- `requested_files=dimension_drawing`

產品 flat／clean 版本與三語資料紀錄頁均已同步。

## 證據內容

頁面保留來源文件支持的：

- W250 × D120 × H240 mm
- 透明壓克力／邊緣拋光／實木
- 1 SET／CTN
- 樣品約 15–25 天
- 量產約 25–35 天的來源方向

MOQ、正式 SKU、訂單數量、交付地、客戶名稱與公開授權仍維持按專案確認，不作通用承諾。

## 本地驗收

- `node --check js/main.js`：通過
- `audit_product_page_quality.py`：24／24 通過
- `audit_case_page_contract.py`：36／36 通過
- 9 個頁面均無內部 `.html` href

## 公開驗收

六個 clean URL 均 HTTP 200、單一 H1、canonical 正確，且全部讀回產品與尺寸圖詢問參數：

- `/tw/en/jp/cosmetic-organizers`
- `/tw/en/jp/case-page-cosmetic-organizer`

## 狀態

已發布並公開讀回；本次未提交表單，因此不宣稱新的 `generate_lead`。
