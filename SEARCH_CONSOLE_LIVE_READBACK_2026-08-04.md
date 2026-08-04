# Big Fame Search Console 實際讀回紀錄

讀取日期：2026-08-04（Asia/Taipei）  
Property：`sc-domain:bigfame.co`  
搜尋類型：網路  
Search Console 顯示資料區間：2026-07-16 至 2026-08-02  
介面最後更新：讀取時約 4 小時前

## 這次實際讀到的數據

| 指標 | 數值 |
|---|---:|
| 總點擊次數 | 4 |
| 曝光總數 | 383 |
| 平均點閱率 | 1% |
| 平均排序 | 9.7 |
| 查詢數 | 26 |
| 曝光頁數 | 24 |

以上是 Search Console 介面實際顯示值，不是推估，也不代表完整歷史累積表現。

## 實際查詢詞

### 有品牌或公司辨識意圖

| 查詢 | 點擊 | 曝光 |
|---|---:|---:|
| 碧豐實業有限公司 | 2 | 10 |
| fame | 0 | 105 |
| big fame | 0 | 94 |
| the big fame | 0 | 4 |
| fame export | 0 | 4 |
| bigfame | 0 | 3 |
| fame supplier | 0 | 2 |
| bigfangroup | 0 | 1 |
| bigfair | 0 | 1 |
| fame email address | 0 | 1 |
| f a m e | 0 | 1 |
| brightfame | 0 | 1 |

### 與展示設備、零售什器或供應商有關

| 查詢 | 點擊 | 曝光 |
|---|---:|---:|
| 陳列什器 製造 oem 体制 | 0 | 3 |
| 店舗什器 量産 コスト 効率 | 0 | 3 |
| 店舗什器 量産 コスト 最適化 | 0 | 1 |
| shelving system | 0 | 2 |
| round display panel manufacturer | 0 | 1 |
| 陳列架設計 | 0 | 1 |
| shopdesign | 0 | 1 |
| rolling metal racks | 0 | 1 |
| metal retail displays | 0 | 1 |
| warehouse rack manufacturers | 0 | 1 |
| hanger supplier | 0 | 1 |

### 不代表 TA 需求的雜訊或舊網址意圖

| 查詢 | 點擊 | 曝光 |
|---|---:|---:|
| in intitle:contact " * co" -india | 0 | 4 |
| email in intitle:contact " * co" -india | 0 | 2 |
| intitle:会社概要 | 0 | 2 |

## 實際曝光頁面

| 頁面 | 點擊 | 曝光 |
|---|---:|---:|
| `/` | 2 | 300 |
| `/tw/about` | 2 | 8 |
| `/tw/` | 0 | 51 |
| `/en/about` | 0 | 27 |
| `/contact-us` | 0 | 15 |
| `/tw/about.html` | 0 | 11 |
| `/en/contact.html` | 0 | 11 |
| `/en/` | 0 | 9 |
| `/en/applications.html` | 0 | 8 |
| `/en/products.html` | 0 | 8 |
| `/know-how` | 0 | 8 |
| `/jp/` | 0 | 7 |
| `/en/services.html` | 0 | 6 |
| `/overview` | 0 | 6 |
| `/en/about.html` | 0 | 6 |
| `/jp/applications` | 0 | 6 |
| `/privacy-policy` | 0 | 5 |
| `/jp/products` | 0 | 3 |
| `/en/contact` | 0 | 3 |
| `/jp/about.html` | 0 | 3 |
| `/en/services` | 0 | 2 |
| `/jp/services.html` | 0 | 2 |
| `/jp/about` | 0 | 2 |
| `/jp/contact` | 0 | 1 |

## 客觀判讀

1. 目前曝光仍高度集中在首頁與品牌／公司辨識詞；不能宣稱非品牌 TA 已大量找到 Big Fame。
2. 已出現可用的非品牌訊號，尤其是日文「店舗什器／量産／コスト」、中文「陳列什器 製造 OEM」、英文 `shelving system`、`metal retail displays` 與 `hanger supplier`。
3. Search Console 仍記錄 `.html`、`/overview`、`/contact-us`、`/know-how` 等舊網址曝光。這是遷移尾端的搜尋資料，不等於目前 sitemap 或 canonical 仍使用舊網址；現況仍需維持 301 與 canonical 驗收。
4. 本次前 24 頁清單沒有出現三個 TA 入口、產品頁或新案例頁。這只能表示它們尚未進入本次曝光頁前 24 名，不能推論為零曝光或沒有被索引。
5. 這批資料的結束日早於 2026-08-04 最新發布，因此不能用來判斷 `e329217` 之後的服飾案例卡片 CTA 成效。

## 下一輪應做的修正

- 以「OEM／量產成本／展示系統／掛勾供應」為已出現的搜尋語意，檢查三個 TA 入口與產品頁的 title、H1、首段與 FAQ 是否直接回答。
- 不因單次 1 次曝光就建立大量新頁；先觀察 28 天內相同語意是否重複出現。
- 持續觀察 `/tw/`、`/en/`、`/jp/` 及 clean URL 是否逐步取代舊 `.html` 與 legacy URL 的曝光。
- 將產品頁進入聯絡頁、`form_start`、`generate_lead` 與 TA 入口分開量測；Search Console 本身無法取代 GA4 的轉換數據。

## 證據限制

- 本紀錄來自登入後 Search Console 介面讀回，不是 Search Console API 匯出。
- 查詢與頁面表格依介面排序，未取得完整每一筆的平均排序與 CTR。
- 搜尋資料存在延遲；後續應以固定日期窗口重新讀取，不要直接與不同窗口的數值比較。
