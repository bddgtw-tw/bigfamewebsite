# 首頁 Technical Resources 入口發布交接

> 變更日期：2026-08-05（Asia/Taipei）  
> commit：`5dfdb2e Add technical resources entry to homepages`

## 變更內容

三語首頁新增 Technical Resources 區塊，將高意圖的技術資料需求直接連到：

`technical-resources`

入口文案依語言說明尺寸圖、CAD、材質／表面處理與打樣評估，並保留「依產品代號、圖面、數量與專案條件確認」的證據邊界。不在首頁新增未核准的 MOQ、交期、材質牌號或客戶成果主張。

## 本地驗收

- `tw/index.html`：H1=1、Technical Resources 連結=1
- `en/index.html`：H1=1、Technical Resources 連結=1
- `jp/index.html`：H1=1、Technical Resources 連結=1
- `git diff --check`：通過
- `main` 與 `draft`：已同步至 `5dfdb2e`
- `origin/main` 與 `origin/draft`：已同步至 `5dfdb2e`

## 公開網址讀回

使用 cache-busting query 讀回：

| 公開網址 | HTTP | H1 | Technical Resources 連結 | canonical |
|---|---:|---:|---:|---|
| `https://www.bigfame.co/tw/?v=5dfdb2e` | 200 | 1 | 1 | `https://www.bigfame.co/tw/` |
| `https://www.bigfame.co/en/?v=5dfdb2e` | 200 | 1 | 1 | `https://www.bigfame.co/en/` |
| `https://www.bigfame.co/jp/?v=5dfdb2e` | 200 | 1 | 1 | `https://www.bigfame.co/jp/` |

## 尚未宣稱

- 尚未由 Search Console 證明首頁新增入口已產生曝光或點擊。
- 尚未由 GA4 證明該入口已產生 `form_start` 或 `generate_lead`。
- 本次未提交公開詢問表單；只驗證公開 HTML 與導向入口。

## 後續量測

在 28 天觀察窗內，檢查首頁到 Technical Resources 的曝光、點擊、CTA 點擊與詢問分流，並比較採購、設計與展示配件三類入口的行為差異。
