# Big Fame Search Console 實際基準

> 讀取日期：2026-08-04（Asia/Taipei）  
> 資源：`sc-domain:bigfame.co`  
> 來源：Google Search Console 網頁搜尋成效與網頁索引狀態介面  
> 性質：唯讀快照，不代表永久固定數據。

## 一、搜尋成效

Search Console 成效報表目前選取「3 個月」，圖表實際涵蓋 **2026-07-16 至 2026-08-02**；介面顯示上次更新約 3.5 小時前。

| 指標 | 實際讀值 |
|---|---:|
| 總點擊次數 | 4 |
| 曝光總數 | 383 |
| 平均點閱率 | 1% |
| 平均排序 | 9.7 |
| 查詢列數 | 26 |
| 網頁列數 | 24 |

### 目前可見的搜尋詞

以下是報表第一頁目前可見的 10 筆，不是完整 26 筆：

| 查詢 | 點擊 | 曝光 |
|---|---:|---:|
| 碧豐實業有限公司 | 2 | 10 |
| `fame` | 0 | 105 |
| `big fame` | 0 | 94 |
| `the big fame` | 0 | 4 |
| `fame export` | 0 | 4 |
| `in intitle:contact " * co" -india` | 0 | 4 |
| `bigfame` | 0 | 3 |
| `陳列什器 製造 oem 体制` | 0 | 3 |
| `店舗什器 量産 コスト 効率` | 0 | 3 |
| `shelving system` | 0 | 2 |

### 目前可見的熱門網頁

| 網頁 | 點擊 | 曝光 |
|---|---:|---:|
| `https://www.bigfame.co/` | 2 | 300 |
| `https://www.bigfame.co/tw/about` | 2 | 8 |
| `https://www.bigfame.co/tw/` | 0 | 51 |
| `https://www.bigfame.co/en/about` | 0 | 27 |
| `https://www.bigfame.co/contact-us` | 0 | 15 |
| `https://www.bigfame.co/tw/about.html` | 0 | 11 |
| `https://www.bigfame.co/en/contact.html` | 0 | 11 |
| `https://www.bigfame.co/en/` | 0 | 9 |
| `https://www.bigfame.co/en/applications.html` | 0 | 8 |
| `https://www.bigfame.co/en/products.html` | 0 | 8 |

## 二、索引狀態

索引報表介面標示上次更新日期為 **2026-07-24**：

| 狀態 | 網頁數 |
|---|---:|
| 已建立索引 | 16 |
| 未建立索引 | 51 |
| 已知頁面合計 | 67 |

未建立索引的 6 個原因：

| 原因 | 網頁數 | 目前判讀 |
|---|---:|---|
| 找不到網頁（404） | 17 | 需逐一確認是否為舊網址、錯誤網址或實際遺失頁面 |
| 頁面會重新導向 | 10 | 舊網址導向本身不應索引，但需確認導向目標一致 |
| 重複網頁；使用者未選取標準網頁 | 2 | 需查看 canonical 與 Google 選取的版本 |
| 替代頁面（有適當的標準標記） | 1 | 可能是語言／路由替代頁，暫不直接視為錯誤 |
| 已檢索，目前尚未建立索引 | 14 | 需觀察內容品質、內部連結與索引延遲 |
| 已找到，目前尚未建立索引 | 7 | 需觀察 sitemap、內部連結與 Google 排程 |

其他介面狀態：

- HTTPS：22 個良好、0 個非 HTTPS。
- Core Web Vitals：行動裝置與桌面皆顯示無資料，尚不能宣稱速度達標。
- 影片索引：3 個網頁的影片未編入索引、0 個已編入索引；首頁影片目前是背景影片，不應把影片索引當成主要 KPI。

## 三、客觀判讀

1. Big Fame 已開始出現非品牌搜尋訊號，但目前曝光仍高度集中在首頁與品牌相關查詢。
2. 日文零售什器查詢與英文 `shelving system` 已證明 TA 搜尋方向開始出現，但目前曝光量很小，不能宣稱 SEO 已形成穩定流量。
3. Google 報表仍保留 `/contact-us`、`.html` 與根網址等舊版本曝光，表示 URL 遷移尚在過渡期；這不等於目前網站導向失效。
4. 目前 4 次點擊中，2 次來自品牌公司名稱查詢；非品牌查詢尚未產生可確認的點擊。
5. 51 個未索引頁面是下一個 P0／P1 稽核對象，優先處理 17 個 404 與 10 個重新導向頁面的實際 URL 清單。

## 四、下一步執行

1. 在 Search Console 索引報表逐一讀取 17 個 404 URL，確認是否為可移除的舊 URL、應建立 301 的舊 URL，或真正遺失的公開頁面。
2. 讀取 10 個重新導向 URL，確認導向後是否落在正確語言與 clean URL。
3. 以目前非品牌詞建立 28 天觀察分組：`陳列什器`、`店舗什器`、`shelving system`、`display hooks`、`retail fixture`。
4. 將 GA4 的 `bf_contact_cta_click`、`form_start`、`generate_lead` 與 Search Console 的落地頁交叉觀察；目前尚未取得 GA4 實際事件數。
