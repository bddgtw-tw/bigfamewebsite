# Applications 案例數量一致性修正｜2026-08-05

## 發現

公開 `/tw/applications` 頁面原本在 Hero 與摘要列顯示 `09`，但頁面實際列出 11 個精選案例。這會讓訪客對案例資料的完整性產生疑問，也不符合「案例可驗證」的內容原則。

## 修正

- `tw/applications.html`：Hero 與 `SELECTED CASES` 改為 `11`
- `en/applications.html`：Hero 與 `SELECTED CASES` 改為 `11`
- `jp/applications.html`：Hero 與 `SELECTED CASES` 改為 `11`
- Commit：`7de9ef0 Align applications case count`
- 已同步：`main`、`draft`、`release/draft`

## 驗證

- 本地三語頁面均為 `11`
- 公開快取更新後，以 `https://www.bigfame.co/tw/applications?release=7de9ef0` 驗證：`count11=2`、`count09=0`、`h1=1`
- 不帶查詢參數的公開網址短時間內仍可能讀到舊快取；canonical 仍維持不帶查詢參數的正式網址，查詢參數只用於驗證版本。

## 邊界

這次修正只調整與實際案例數一致的顯示數字，沒有因此宣稱每一個案例都具備完整可公開的客戶名稱、數量或成果數據。
