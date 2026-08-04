# 服飾案例與店型入口 clean route 發布交接

日期：2026-08-05

## 本次完成

- 補上三語服飾照片紀錄 clean route：
  - `/tw/case-apparel-2016`
  - `/en/case-apparel-2016`
  - `/jp/case-apparel-2016`
- 補上三語服飾店展示設備與店面規劃 clean route：
  - `/tw/apparel-store-fixtures`
  - `/en/apparel-store-fixtures`
  - `/jp/apparel-store-fixtures`
- clean route 以既有 flat page 為唯一內容來源同步，保留三語 canonical、hreflang、FAQPage、BreadcrumbList 與既有 CTA。
- 服飾照片紀錄補上 `data-bf-source-record="1"` 與 `data-bf-case-contract="1"`，使來源紀錄與證據邊界可被稽核。

## 內容證據邊界

服飾案例目前是匿名照片證據紀錄。來源可支援：中島展示、壁面陳列、吊掛系統、桌面配件與鞋類展示情境，以及店型與展示條件討論；目前不能證明客戶名稱、Big Fame 實際承擔範圍、正式規格、數量、MOQ、交期、交付地或成果數據。

## 發布前本機驗收

- `audit_case_page_contract.py`：36 頁，0 failures。
- `audit_product_page_quality.py`：24 頁，0 failures。
- 全站 HTML：173 個；內部 `.html` href：0。
- JSON-LD 可解析錯誤：0。
- 既有 `overview.html` 與 `contact-us.html` 沒有 H1，屬已知 legacy 例外，未在本次範圍處理。

## 尚未證明

- 本文件建立的是發布交接紀錄；尚未代表 GitHub push、Cloudflare Pages deploy 或公開網址 runtime 已完成。
- 發布後仍需逐一驗證六個 clean URL HTTP 200、H1、FAQ、canonical、hreflang、圖片與 CTA。
- 服飾照片公開授權、專案角色與正式案例說法仍需逐案確認。
