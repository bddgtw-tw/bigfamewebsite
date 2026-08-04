# Big Fame 核心內容結構化資料驗收

更新日期：2026-08-04

## 本輪範圍

針對繁中、英文、日文的關於、應用案例、產品總覽、服務，以及防盜展示掛勾、客製金屬零件、POS 展示架頁面，補齊 BreadcrumbList JSON-LD；共 30 個本地 HTML 檔案，涵蓋 flat source 與 clean URL 對應的 index 檔案。

首頁與聯絡表單頁不列入一般內容頁 Breadcrumb 缺口：首頁是階層根節點，聯絡頁以表單流程為主要任務。

## 驗收結果

- 30／30 頁已加入 BreadcrumbList。
- `MISSING_CONTENT_BREADCRUMBS=0`。
- Breadcrumb 的階層使用 Big Fame → 產品或應用／服務 → 目前頁面。
- 本輪沒有新增未核准的客戶名稱、產品規格、MOQ、交期、承重或成果數據。
- JSON-LD 欄位存在不等於搜尋引擎已採用；仍需以公開 HTML、Search Console 與實際查詢結果持續確認。
