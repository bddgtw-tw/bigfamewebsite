# hreflang 與 x-default 全站修正｜2026-08-05

## 發現

全站 171 個語言頁面都有 canonical，但其中部分產品、案例與 TA 入口頁只有 `zh-TW`、`en`、`ja` 三組 alternate，沒有同頁的 `x-default` fallback；部分舊有內容頁的 `x-default` 甚至指向首頁，與該頁內容不對應。

## 修正

- 168 個非首頁語言頁補上 `x-default`。
- `x-default` 統一指向同一內容的英文 clean URL，例如 `/tw/procurement` 與 `/jp/procurement` 都指向 `/en/procurement`。
- 三個語言首頁保留 `x-default=https://www.bigfame.co/`，作為語言選擇入口。
- 沒有更改 canonical 的正式網址，也沒有把 `.html` 放回內部連結。

## 驗證

- 語言頁總數：171
- hreflang 問題：0
- 每頁均有 `zh-TW`、`en`、`ja`、`x-default`
- 產品頁品質檢查：48 頁、0 failures
- 案例頁合約檢查：72 頁、0 failures
- `git diff --check`：通過

## 邊界

這項修正只改善搜尋引擎的語言替代訊號；不等同於 Search Console 已重新處理所有網址，也不等同於排名或曝光已經提升。
