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
