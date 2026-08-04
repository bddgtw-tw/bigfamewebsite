# Big Fame Website 發布交接：TA 入口連結至證據案例

日期：2026-08-05  
版本：`b2e1c6e`  
公開網址：<https://www.bigfame.co>

## 本次已完成

將 Urban Warehouse 城市儲物空間模組化案例，加入三語 TA 入口頁的可見導引：

- `tw/en/jp/procurement`
- `tw/en/jp/design-support`
- `tw/en/jp/display-hooks`
- `tw/en/jp/modular-fixtures`
- `tw/en/jp/applications`

每頁皆加入 `data-bf-evidence-route="1"` 的證據案例區塊，連往同語系相對路徑 `case-urban-storage`。

## 本地驗收

- `git diff --check`：通過
- `python scripts/audit_case_page_contract.py`：`CASE_CONTRACT_PAGES=36`、`CASE_CONTRACT_FAILURES=0`
- 15 個入口頁：每頁 `Route=1`、`Urban>=1`、`H1=1`

## 公開驗收

以 `https://www.bigfame.co/{locale}/{path}` 逐頁讀取 15 個入口頁：

- 全部 HTTP 200
- 全部包含 1 個證據案例入口
- 全部包含 `case-urban-storage`
- 全部保有單一 H1
- 瀏覽器 DOM 另驗證 `tw/procurement`、`en/design-support`、`jp/applications`：各為 `h1=1`、`route=1`、`urban=1`

## 證據邊界

此發布只改善「被看見、被理解、被找到案例證據」的路徑，不代表已取得客戶公開授權，也不補造正式合約分工、訂單數量、完整交期、交貨地或商業成效。這些欄位仍需以原始專案文件與授權確認。

## 後續觀察

1. 觀察 Search Console 是否出現與 Urban Warehouse、modular storage、self-storage、K/D display／storage 等非品牌查詢的曝光。
2. 觀察 GA4 是否出現從 TA 入口進入案例頁，再進入詢問表的路徑。
3. 若取得授權與正式交付證據，再逐欄補強案例 Brief，不以目前公開文案推導未證實數字。
