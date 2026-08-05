# Big Fame 共用頁面骨架

這個資料夾是網站共用結構的維護入口。公開的 `tw/`、`en/`、`jp/` HTML 是產出物，不應把每一頁都當成 header、footer 的唯一來源。

## 維護邊界

- `css/style.css`：共用視覺、斷點、圖示尺寸與間距。
- `scripts/`：頁面產生器與批次修正工具。
- `templates/`：共用 shell 的規格與之後可抽出的片段。
- `tw/`、`en/`、`jp/`：公開產出的 HTML，只有單頁特殊內容才直接修改。

## 媒體素材

- `templates/media-library.json`：由 `scripts/audit_media_library.py` 產生的公開圖片／影片清單。
- 更換既有素材時，使用 `scripts/replace_media_reference.py OLD NEW`，先確認新檔案已放在 `images/` 或 `videos/`，再由工具同步 HTML、CSS、JS 與產生器中的引用。

## 修改順序

1. 先修改共用 shell 或 CSS。
2. 再由產生器輸出三語頁面。
3. 執行 HTML、canonical、hreflang、sitemap、手機版與公開網址驗收。
4. 確認回讀後才提交與部署。

## 目前採取的安全策略

現有網站仍有多種歷史頁面骨架，因此不一次重產全部 HTML。先讓共用 CSS 與媒體尺寸規則集中化，再逐批將首頁、TA 入口、產品頁、案例頁接到相同 shell，避免破壞既有 URL 與 SEO 結構。
