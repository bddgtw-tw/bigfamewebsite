# Big Fame 網站升級發布交接

更新日期：2026-08-03

## 目前已確認的兩個網站狀態

### 本地／Git draft

- 位置：本專案 `draft` 分支
- 內容：三語靜態網站，包含首頁、關於、產品、服務、店型與聯絡頁
- 本輪升級：TA 決策入口、證據導向區塊、保守化服務敘事、內容證據登錄表、案例候選登錄
- Git remote：`https://github.com/bddgtw-tw/bigfamewebsite.git`
- `main` 與 `draft` 分支目前存在，README 定義 `draft -> main` 為發布流程

### 公開 `bigfame.co`

- 公開搜尋可讀到的路由為 `/overview`、`/contact-us` 等 HubSpot／HubSnacks 頁面
- 公開首頁內容與本地 Git 靜態網站的路由、頁面結構不同
- 因此目前不能把本地 draft 的更新說成已經更新到 `bigfame.co`

## 發布前必須確認

1. Big Fame 要正式維護哪一套網站：HubSpot／HubSnacks，或本 Git 靜態網站。
2. 若採用 Git 靜態網站，確認 DNS、主機／CDN、部署方式與 `/tw`、`/en`、`/jp` 路由是否要取代目前公開路由。
3. 確認 `1988`、據點、馬來西亞、倉儲、測試方法與客戶成果等主張的正式來源與可公開措辭。
4. 從 `CONTENT_EVIDENCE_REGISTER.md` 的候選案例中完成至少一案的日期、角色、授權、素材來源與可公開文案核准。
5. 安裝依賴後完成 CSS 建置、瀏覽器渲染、表單送達、公開 URL 與 canonical／sitemap 檢查。
6. 確認通過後才將 `draft` 合併到 `main` 並執行正式發布。

## 本輪不能宣稱的事項

- 本地 draft 已發布到 `bigfame.co`
- 公開站已採用新的三語 TA 入口
- 候選案例已取得公開授權
- 未核對的測試數據、客戶名稱、所有權或市場地位已獲證明
