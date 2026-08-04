# 總覽頁詢問上下文發布讀回｜2026-08-05

## 變更

- Commit：`37703a3 Preserve inquiry context on hub CTAs`
- `main` 與 `draft` 已同步至同一 commit。
- 三語首頁、Products、Applications、Services、About 的通用 CTA 改為帶入 `category=integration`。
- 產品與案例詳細頁既有的 `display_hardware`、`system_fixtures`、`pos_displays` 等細分類未被覆寫。

## 公開讀回

三語共 15 個總覽頁皆確認：

- HTTP 200
- H1 = 1
- canonical 指向對應 clean URL
- hreflang = 4（含 `x-default`）
- 至少一個帶有 `contact?category=integration` 的入口

舊網址也已確認 301：

- `/overview` → `/en/about`
- `/contact-us` → `/en/contact`
- 各語系 `/overview`、`/contact-us` → 對應語系 clean URL

## 邊界

- 本次證明詢問分類會被帶入網址，不代表真實表單已送出或已產生 lead。
- 真實詢問數、非品牌曝光與搜尋詞仍需由 Search Console／GA4 觀察確認。
