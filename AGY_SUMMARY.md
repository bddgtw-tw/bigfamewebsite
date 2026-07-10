# Big Fame 網站 — 現狀總結（給 AGY）

## 專案路徑
```
C:\Users\bddgt\Documents\antigravity\wonderful-volta\bigfamewebsite\
├── index.html（語言選擇頁）
├── tw/index.html（繁體中文首頁）← 主要編輯檔案
├── en/index.html
├── jp/index.html
├── css/style.css
├── js/main.js
├── images/（9 張產品/工廠圖）
└── videos/hero_bg.mp4（23MB 背景影片）
```

## 品牌定位（從公司資料萃取）
- 碧豐不是展示架製造商，是**商業空間轉型專家**
- 核心差異：**一站式購足（One-Stop Shop）**— 從設計到全球交付，單一窗口
- 工藝高度：金屬・木質・壓克力・玻璃 異材質無縫整合
- 品牌承諾：**If you can name it, we can do it.**
- 客戶：日本眼鏡連鎖、歐美運動通路、便利商店巨頭、百貨精品

## 視覺概念：「支持的角色」
店面中不起眼的掛勾、桿子、五金，是支持商品/商店/品牌的重要角色。
網站設計本身要傳達這個理念——**低調、安靜、不搶眼，但沒有它一切都不成立。**

### 視覺語言規則
| 項目 | 規則 |
|------|------|
| 標題字體 | Shippori Mincho（明朝體）weight 400，letter-spacing 0.02em |
| 內文字體 | Outfit, weight 300 |
| 主色 | #111111（純黑） |
| 背景 | #ffffff（純白） |
| 區塊交替 | #f8f7f4（極淺暖灰） |
| 點綴色 | #9e8561（啞金）— 只能用於 section-subtitle、hover 底線、footer tagline |
| 按鈕 hover | 不反轉背景，只變邊框色為金色 |
| 圓角 | 全部 border-radius: 0 |
| 圖片 | 不強制固定高度，用 max-height + object-fit: cover |
| 區塊間隔 | 底部 shelf line（極細 border-bottom） |
| 行距 | 1.6 |
| section padding | 80px |

## 首頁架構（目前完成的）
1. **Header** — BIG FAME logo + 6 項導覽 + 電話 + 語言切換
2. **Hero** — 全螢幕影片背景 + 白色漸層 overlay + 標題 + 一句話描述 + 2 個 CTA
3. **Trust Badges** — 38+ 年 / 3 據點 / 日系品管
4. **Client Sectors** — 4 大產業客戶
5. **Gallery** — 4 項產品能力（左右交錯排列）
6. **Network** — 三地聯動（台北/彰化/吉隆坡）
7. **CTA** — 深色背景的 call-to-action
8. **Footer** — 4 欄資訊

## 已經完成的 CSS class
| Class | 用途 |
|-------|------|
| `.section` | 一般區塊，含底部 shelf line |
| `.section-alt` | 暖灰背景區塊 |
| `.section-cta-dark` | 深色 CTA 區塊 |
| `.section-accent` | 無頂部邊框的區塊 |
| `.gallery-section` | 產品展示區 |
| `.gallery-item` | 左右交錯排列 |
| `.gallery-img-holder` | 圖片容器 |
| `.gallery-content` | 文字區域 |
| `.gallery-number` | 編號（01/02/03...）|
| `.gallery-title` | 產品標題 |
| `.gallery-desc` | 產品簡述 |
| `.gallery-link` | 查看詳細連結 |
| `.trust-badges` | 信任數字 |
| `.badge-item` | 單項數字 |
| `.badge-number` | 數字（明朝體） |
| `.badge-title` | 數字標題 |
| `.client-sectors-wall` | 客戶產業牆 |
| `.sector-item` | 單項產業 |
| `.hero` | 全螢幕 hero |
| `.hero-overlay` | 白色漸層 |
| `.hero-title` | 主標題 |
| `.hero-title span` | 副標題（If you can name it...）|
| `.hero-tag` | 金色標籤 |
| `.hero-desc` | 描述文字 |
| `.header-phone-cta` | 電話按鈕 |
| `.tagline` | footer 金色 tagline |

## 待完成事項
1. **EN / JP 語系頁面** — 目前只有 TW 首頁完成，需要同步更新 en/ 和 jp/ 的 index.html
2. **內頁** — about.html / products.html / services.html / applications.html / contact.html 需要統一樣式
3. **圖片** — 目前 images/ 內的 9 張圖疑似為圖庫照片，需要替換為 Big Fame 真實產品/工廠照
4. **Hero 影片** — 23MB 的 hero_bg.mp4 需要確認是否為真實工廠 footage
5. **產品細節** — gallery 的「查看詳細」目前都連到 products.html，需要建立對應的產品頁面內容
6. **RWD 微調** — 768px 以下的 mobile 斷點需要測試

## 絕對不要做的事
- ❌ 不要加入任何飽和色（#ff6600 / #e60012 / #00a0e9）
- ❌ 不要用圓角（border-radius 保持 0）
- ❌ 不要讓按鈕 hover 時反轉背景色（只變邊框色）
- ❌ 不要用圖庫照片（Unsplash / Pexels / Shutterstock）
- ❌ 不要寫長文案（每區塊最多一句話，10-15 字）
- ❌ 不要加入動態效果（旋轉/跳動/飛入）