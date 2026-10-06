# 🏭 Big Fame Industrial Corp - 官方網站專案

本專案為 **Big Fame Industrial Corp** 官方網站之前端程式碼與資源庫。

---

## 📌 專案架構與分支管理

本專案採用 **GitHub 雙分支管理機制**：

- **`draft` (預設開發分支)**：所有日常 HTML/CSS 修改、新增頁面或測試均在此分支進行。
- **`main` (正式發布分支)**：僅放已確認無誤、準備 publish 上線的穩定程式碼。

---

## 🚀 快速操作指南

### 1. 切換至開發分支並提交變更
```bash
git checkout draft
git add .
git commit -m "更新內容說明"
git push origin draft
```

### 2. 合併發布至正式版 (Publish)
```bash
git checkout main
git merge draft
git push origin main
git checkout draft
```

---

## 📂 素材與文案儲存位置
- 網站原始碼：本 GitHub 儲存庫
- 設計稿、原始高畫質圖檔、企劃文件：`Google 雲端硬碟 (F:\共用雲端硬碟)`


## JP 首頁設計基準（2026-10-06）

本次以 [taste-skill](https://github.com/Leonxlnx/taste-skill) 的 brief-first、audit-first 與局部改善原則為參考；未安裝外部 runtime，也未遷移框架。

- 品牌規範優先：Swiss 工程白皮書、Light Mode、#F7F6F2 / #1A1A1A / #B8860B。
- JP → EN → TW；本輪樣式僅作用於 `body.jp-dossier`。
- 原生 HTML/CSS；DESIGN_VARIANCE 5、MOTION_INTENSITY 2、VISUAL_DENSITY 3。
- 正文至少 16px、輔助文字至少 14px；正文行高 1.68、標題行高 1.25，主要區段留白 100–110px。
- 使用自有概念素材並標明非納品照片；禁止客戶名稱、未授權照片、虛構認證及無条件精度承諾。
- 簡化首屏、單一詢價用語、清楚鍵盤焦點、手機選單、無 JavaScript 可閱讀。
- 保留 URL、導覽標籤、SEO metadata、JSON-LD 及詢價 query parameters；不改表單欄位。
- 驗收需包含 375 / 390 / 768 / 1024 / 1440px、橫向溢出、選單開關、圖片與連結、無 JS、reduced motion。僅靜態檢查不能算實機或正式站驗收。
