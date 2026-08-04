# P0 Publish Handoff｜網站資產版本統一

## 1. 目的

統一三語網站所有 HTML 頁面對 `main.js` 與 `style.css` 的版本引用，避免部分頁面因瀏覽器或 CDN 快取而載入舊版互動、表單脈絡或結構化資料邏輯。

## 2. 本地完成證據

- Commit：`fc56eff`
- 修改範圍：`tw`、`en`、`jp` 三語共 162 個 HTML 頁面
- `main.js`：統一為 `?v=1.3.16`
- `style.css`：統一為 `?v=20260805-p0`
- 版本完整性稽核：162／162 頁面符合
- `node --check js/main.js`：通過
- `python scripts/audit_product_page_quality.py`：24 頁、0 failures
- `python scripts/audit_case_page_contract.py`：36 頁、0 failures

## 3. 公開發布

- `main` 已推送至 `origin/main`
- `main` 已同步至 `origin/draft`
- 本地 `main`、`draft`、`origin/main`、`origin/draft` 均指向 `fc56eff`
- 公開站：`https://www.bigfame.co`

首次發布後立即讀取仍看到舊資產版本；等待部署／快取更新後再次讀取，公開首頁已回應：

- `https://www.bigfame.co/js/main.js?v=1.3.16`
- `https://www.bigfame.co/css/style.css?v=20260805-p0`

因此本次公開狀態以第二次延遲讀回為準，不把第一次舊快取讀值誤判為失敗或完成。

## 4. 公開 runtime 驗收

### 首頁

- 中文首頁 H1：1
- Hero 影片：正常載入
- VM CTA 仍存在：`contact?role=vm&category=display_hardware`

### 產品頁

公開 `/tw/optical-hooks`：

- H1：1
- Product JSON-LD：1
- JS 版本：`1.3.16`

### 聯絡頁脈絡

以設計師、展示五金、尺寸圖面的唯讀 URL 讀取 `/tw/contact`，實際欄位為：

| 欄位 | 讀值 |
|---|---|
| `buyer_role` | `store_design_engineering` |
| `inquiry_type` | `quote` |
| `product_category` | `display_hardware` |
| `requested_files` | `dimension_drawing` |
| `source_category` | `display_hardware` |
| `source_role` | `designer` |

本次沒有送出表單，也沒有產生外部寄送副作用。

## 5. 尚未因此完成的事項

資產版本統一只解決「公開頁是否穩定拿到最新前端資產」；不代表：

- 已有合格商機；
- 所有案例已具備正式交期、交付與授權證據；
- 非品牌 SEO 已經穩定成長；
- 產品的 MOQ、交期或 SKU 已被正式核准公開。

後續仍需依 28 天量測追蹤 GA4、Search Console 與案例證據補強。
