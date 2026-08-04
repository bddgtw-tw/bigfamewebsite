# 眼鏡案例詢問上下文發布交接

日期：2026-08-05  
版本：`a9235be`

## 本次變更

三語 `case-eyewear-2016` 的設計／採購 CTA 加入：

- `product=optical-hooks`
- `requested_files=dimension_drawing`

flat HTML 與 clean URL 的 `index.html` 均同步更新。

## 本地驗收

- `git diff --check`：通過
- `audit_case_page_contract.py`：36／36 通過
- 6 個頁面均無內部 `.html` href

## 公開驗收

三語 clean URL 均公開回應 HTTP 200，且各頁：

- 單一 H1
- canonical 正確
- CTA 讀回 `product=optical-hooks`
- CTA 讀回 `requested_files=dimension_drawing`

公開網址：

- `https://www.bigfame.co/tw/case-eyewear-2016`
- `https://www.bigfame.co/en/case-eyewear-2016`
- `https://www.bigfame.co/jp/case-eyewear-2016`

## 證據邊界

`case-eyewear-2016` 是匿名眼鏡門市照片／情境紀錄；`optical-hooks` 是另一組 EYEHK 圖面規格證據。這次只建立「案例需求 → 眼鏡展示掛勾 → 尺寸圖索取」的語意與詢問路徑，不宣稱兩者為同一筆客戶交付，也不新增客戶名稱、數量、交期、交付地或授權主張。

## 狀態

已發布並公開讀回；真實表單提交與 `generate_lead` 仍未在本次驗收中觸發。
