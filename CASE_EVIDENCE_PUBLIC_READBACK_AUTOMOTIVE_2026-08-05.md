# Automotive Parts Display Rack｜公開案例證據讀回

## 1. 本次目標

將汽車零件展示架案例從單純匿名工程敘述，提升為「證據狀態清楚」的 B2B 案例頁：訪客可以分辨客戶問題、產品與工程範圍、材料／改善、數量線索、交期／交付地狀態與公開邊界。

本次沒有把 shipping mark 當成獨立出貨或簽收證明，也沒有公開客戶名稱、PO、目的地或未核准的交付主張。

## 2. 修改範圍

- Commit：`890a210`
- 三語 clean route 與 legacy HTML 共 6 個頁面：
  - `/tw/case-automotive-parts-rack`
  - `/en/case-automotive-parts-rack`
  - `/jp/case-automotive-parts-rack`
  - 以及三個對應 `.html` 檔
- 新增區塊：`data-bf-case-evidence="1"`
- 內容涵蓋：客戶問題、使用產品與工程範圍、材料與改善、數量線索、交期與交付地、公開狀態。

## 3. 原始證據邊界

依內部 `CASE_EVIDENCE_READBACK_ON_TIME_AUTO_PARTS_2026-08-04.md`：

- 來源往返文件支持 4-side peg board rack 相容性、POP／Sign Holder 固定方式與 Big Fame 設計回覆。
- 設計文件支持 auto clip rotating rack、4-way peg board rack、hook shelf、POP／Sign Holder、多次圖面迭代、缺陷改善與組裝文件。
- 可視讀的 shipping mark 記錄兩種架型各 1 set；它是包裝／運輸標示線索，不是獨立訂單、提單或簽收證明。
- 目前沒有可公開的正式交期；目的地線索不在公開頁揭露，也未以獨立運輸文件完成驗證。

## 4. 公開 runtime readback

讀取日期：2026-08-05。方式：公開網址唯讀讀取，未提交表單。

| 語系 | H1 | 證據狀態區塊 | CTA | 語言 |
|---|---:|---:|---:|---|
| `/tw/case-automotive-parts-rack` | 1 | 1 | 3 | `zh-Hant-TW` |
| `/en/case-automotive-parts-rack` | 1 | 1 | 3 | `en` |
| `/jp/case-automotive-parts-rack` | 1 | 1 | 3 | `ja` |

中文頁公開 DOM 另確認：

- 可讀到「兩種架型各 1 set」的數量線索。
- 可讀到「目前來源未形成可公開的正式交期」的證據限制。
- 相關產品連結共 4 個：展示掛勾、槽板／洞洞板配件、模組化展示架、客製金屬零件。
- 詢價 CTA 共 3 個，導向設計師／系統展示／尺寸圖面脈絡。
- 公開頁載入 `main.js?v=1.3.16`。

## 5. 完成判定

本次完成的是「可驗證的匿名工程／交付準備案例頁」，不是「正式完整交付案例」。

尚未完成的完整案例條件：

- 客戶公開授權；
- 正式合約分工；
- 可公開的正式交期；
- 可由獨立文件驗證的交付結果；
- 可公開的客戶／目的地與現場成果。

下一步仍應在取得核准文件後，才考慮升格為完整交付案例；在此之前維持目前證據邊界。
