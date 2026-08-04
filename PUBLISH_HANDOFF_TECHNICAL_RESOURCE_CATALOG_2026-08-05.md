# Technical Resources 資料分流發布讀回｜2026-08-05

## 變更

- Commit：`763b1e2 Add technical resource request catalog`
- `main` 與 `draft` 已同步。
- 三語 Technical Resources 新增四類資料索取分流：尺寸圖／規格摘要、CAD 檔案、材質／表面處理、打樣可行性。
- 每個入口保留 `role` 與 `requested_files`，不直接公開未核准的 CAD、MOQ、交期或測試資料。

## 公開讀回

| URL | HTTP | H1 | 資料目錄 | 尺寸圖 | CAD | 材質 | 打樣 | FAQPage | hreflang |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `/tw/technical-resources` | 200 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 |
| `/en/technical-resources` | 200 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 |
| `/jp/technical-resources` | 200 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 |

## 判讀

Technical Resources 現在從單一「索取資料」入口，變成可依採購／設計任務選擇資料類型的詢問目錄。這證明路徑與上下文已公開，不代表實際檔案已自動提供，也不代表已產生 lead。
