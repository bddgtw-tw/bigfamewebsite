# VM／展示陳列首頁入口發布交接

> 變更與讀回日期：2026-08-05（Asia/Taipei）  
> commit：`a406e41 Preserve VM inquiry context from homepage`

## 變更內容

三語首頁新增「VM／展示陳列團隊」入口，針對商品陳列、展示密度、掛勾、背板系統、尺寸、數量與補貨條件說明其工作情境。

首頁 CTA 直接使用：

`contact?role=vm&category=display_hardware`

這樣不會先進入固定 CTA 的展示掛勾頁而遺失 VM 角色脈絡。

## 本地驗收

- `tw/index.html`：VM CTA=1、H1=1
- `en/index.html`：VM CTA=1、H1=1
- `jp/index.html`：VM CTA=1、H1=1
- `git diff --check`：通過
- `main`、`draft`、`origin/main`、`origin/draft`：已同步至 `a406e41`

## 公開 HTML 讀回

三語首頁均為 HTTP 200，且公開 HTML 可讀到 `contact?role=vm&category=display_hardware`：

- `https://www.bigfame.co/tw/?v=a406e41-r4`
- `https://www.bigfame.co/en/?v=a406e41-r4`
- `https://www.bigfame.co/jp/?v=a406e41-r4`

## 三語表單 runtime 讀回

未提交表單，只讀取公開頁面載入後欄位值：

| 語言 | role | inquiry type | product category | source role | source category |
|---|---|---|---|---|---|
| `tw` | `visual_merchandising` | `quote` | `display_hardware` | `vm` | `display_hardware` |
| `en` | `visual_merchandising` | `quote` | `display_hardware` | `vm` | `display_hardware` |
| `jp` | `visual_merchandising` | `quote` | `display_hardware` | `vm` | `display_hardware` |

## 尚未宣稱

- 尚未由 GA4 證明 VM 入口已產生真實 CTA、`form_start` 或 `generate_lead`。
- 未提交 Web3Forms 真實表單，因此沒有新增 lead 或外部訊息。
- Search Console 尚未證明該入口已取得非品牌曝光。

## 後續量測

在 28 天觀察窗內，將 VM 入口與採購、設計支援、展示掛勾入口分開觀察，確認哪一類角色最常進入產品頁、技術資源頁與詢問表單。
