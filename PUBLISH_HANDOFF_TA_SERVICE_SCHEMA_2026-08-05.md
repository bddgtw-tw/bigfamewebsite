# TA 入口 Service schema 發布交接

> 變更與讀回日期：2026-08-05（Asia/Taipei）  
> commit：`8504864 Version TA entry JavaScript assets`

## 變更內容

三語三類 TA 入口共九頁，透過共用 `js/main.js` 在 runtime 注入對應的 `schema.org/Service` JSON-LD：

- 台灣店面展示設備採購／Taiwan Retail Display Hardware Procurement／台湾の店舗什器・ディスプレイ金具の購買
- 零售空間展示系統與設計支援／Retail Display Systems and Design Support／店舗什器・ディスプレイシステム設計支援
- 展示掛勾與陳列五金／Display Hooks & Retail Display Hardware／ディスプレイフック・店舗什器金物

每個 Service entity 都包含：

- `@type=Service`
- 對應 clean URL 的 `@id`
- 語言對應的 `name` 與 `description`
- `serviceType`
- `provider=@id https://www.bigfame.co/#organization`

## 快取與版本驗收

為避免正式頁面沿用舊版共用腳本，九個 TA 頁面的 script 引用已改為：

`js/main.js?v=1.3.14`

公開 HTML 讀回三個抽樣頁均為 HTTP 200，且包含版本化 script：

- `/tw/procurement?v=8504864`
- `/en/design-support?v=8504864`
- `/jp/display-hooks?v=8504864`

## 公開 runtime 讀回

九頁逐一讀取公開 DOM，結果全部為 `present=true`、`type=Service`，且 `@id`、名稱與 provider 均與頁面語言／clean URL 對應：

| 語言 | TA 入口數 | Service schema |
|---|---:|---:|
| `tw` | 3 | 3／3 |
| `en` | 3 | 3／3 |
| `jp` | 3 | 3／3 |

## 證據邊界

- 本次證明的是公開頁面 runtime DOM 已出現 Service schema，不宣稱 Google 已立即採用、建立索引或產生 AI 引用。
- Service schema 描述的是可提供的 B2B 服務入口，不新增未核准的客戶、數量、MOQ、交期、測試標準或所有權主張。
- GA4 與 Search Console 成效仍需在 28 天觀察窗中另行量測。
