# TA Hub 內部連結補強與公開驗收｜2026-08-05

## 修正範圍

三語的下列 hub 頁面新增共同 TA 導覽區：

- `products`
- `applications`
- `services`

共 9 頁，每頁直接連往：

- `procurement`
- `design-support`
- `display-hooks`

## 修正目的

讓產品、店型／案例、服務三種內容不再只依賴首頁作為 TA 入口；訪客與搜尋引擎可以從任一主要 hub 直接進入採購、設計支援或展示配件路徑。

## 驗證

- 本地 TA block：9/9
- 本地三條入口連結：9/9 頁均具備
- 產品品質檢查：48 頁、0 failures
- 案例合約檢查：72 頁、0 failures
- 公開抽樣：
  - `/tw/products`：TA block 1、三條連結存在
  - `/en/applications`：TA block 1、三條連結存在
  - `/jp/services`：TA block 1、三條連結存在
- 三個公開抽樣頁均為單一 H1

## 發布

- Commit：`3eb7c2d Connect hub pages to TA entry routes`
- 已同步：`main`、`draft`、`release/draft`

這項補強改善內部導流與主題關係，但不等同於 Google 已經索引所有入口或已產生非品牌點擊。
