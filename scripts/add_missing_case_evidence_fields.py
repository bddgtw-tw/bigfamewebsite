"""Add explicit boundary cards for case fields not already stated on the page."""
from html.parser import HTMLParser
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parents[1]


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)


CHECKS = {
    "problem": r"客戶問題|客戶需求|客戶課題|顧客の課題|顧客の要望|Documented Need|Client Problem|Client Need|Project Evidence|What was the problem|需求討論|案件",
    "store_type": r"店型|店面|店舗|零售|Retail|Store|Space|店舗タイプ",
    "products": r"展示產品|使用產品|產品|產品方向|展示|展示櫃|掛勾|家具|Product|Display|Fixture|System|製品|什器",
    "materials": r"材料|材質|素材|Material|Materials|Wood|Metal|Glass|Acrylic",
    "scope": r"實際承擔範圍|Big Fame 做了什麼|Big Fame 公開範圍|Big Fameの対応|Big Fameの範囲|What Big Fame|Big Fame.?s contractual scope|Scope|Actual scope|対応範囲|公開範圍",
    "quantity": r"數量|数量|Quantity",
    "lead_time": r"交期|納期|文件交期|Lead time|timing",
    "delivery": r"交付地|目的地|交付先|納品地|Delivery|Destination|交貨地",
}

LABELS = {
    "tw": {
        "title": "案例證據欄位狀態",
        "problem": ("客戶問題／來源狀態", "本頁未呈現可完整核對的客戶問題；不由照片或版面推定，請在新案中以需求文件確認。"),
        "store_type": ("店型／空間分類", "來源未提供可完整核對的店型分類；請依新案的空間用途與平面確認。"),
        "products": ("使用產品／系統", "來源未提供正式產品或 SKU 名稱；請依圖面、樣品與產品頁逐案確認。"),
        "materials": ("材質／製程", "正式材質牌號、板厚、線徑或製程未由本頁來源核准；請依圖面與樣品確認。"),
        "scope": ("Big Fame 實際承擔範圍", "公開來源未完整核准 Big Fame 的合約分工；本頁不把照片或概念稿推定為交付範圍。"),
        "quantity": ("數量", "來源未提供或未核准數量；不可由照片推算。"),
        "lead_time": ("交期", "來源未提供或未核准交期；需依數量、版本、排程與交貨地確認。"),
        "delivery": ("交付地／目的地", "來源未提供或未核准最終交付地；需依新案確認。"),
    },
    "en": {
        "title": "Case evidence field status",
        "problem": ("Client problem / source status", "The source does not state the client problem in enough detail to verify it here. Do not infer it from photos or layout; confirm it in the new brief."),
        "store_type": ("Store type / space classification", "The source does not provide a fully verifiable store classification. Confirm the space use and plan for a new project."),
        "products": ("Products / system", "The source does not provide an approved product or SKU name. Confirm it against drawings, samples and the product page."),
        "materials": ("Materials / process", "Formal material grades, thickness, wire diameter or process are not approved by this source. Confirm them against drawings and samples."),
        "scope": ("Big Fame actual scope", "The public source does not fully approve Big Fame's contractual scope. Do not turn photos or concepts into a delivery claim."),
        "quantity": ("Quantity", "The source does not provide or approve a quantity. Do not estimate it from photos."),
        "lead_time": ("Lead time", "The source does not provide or approve a lead time. Confirm it against quantity, version, schedule and destination."),
        "delivery": ("Delivery location / destination", "The source does not provide or approve the final delivery location. Confirm it for the new project."),
    },
    "jp": {
        "title": "事例証拠項目の状態",
        "problem": ("顧客課題／資料の状態", "資料から顧客課題を十分に確認できません。写真やレイアウトから推測せず、新案件の要件資料で確認してください。"),
        "store_type": ("店舗タイプ／空間分類", "資料から店舗分類を十分に確認できません。新案件の用途と平面で確認してください。"),
        "products": ("使用製品／システム", "正式な製品名や SKU は資料で確認できません。図面、サンプル、製品ページで確認してください。"),
        "materials": ("素材／加工", "正式な材質、板厚、線径、加工条件は資料で承認されていません。図面とサンプルで確認してください。"),
        "scope": ("Big Fame の実際の対応範囲", "公開資料では契約上の対応範囲を十分に確認できません。写真やコンセプトを納品実績とはみなしません。"),
        "quantity": ("数量", "資料に数量の記載または承認がありません。写真から推定しません。"),
        "lead_time": ("納期", "資料に納期の記載または承認がありません。数量、仕様、日程、納入地で確認します。"),
        "delivery": ("納入地／配送先", "最終納入地の記載または承認がありません。新案件で確認します。"),
    },
}

for language in ("tw", "en", "jp"):
    for path in sorted((ROOT / language).glob("case-*.html")):
        source = path.read_text(encoding="utf-8")
        if 'data-bf-case-contract="1"' in source:
            continue
        parser = TextParser()
        parser.feed(source)
        visible = " ".join(parser.text)
        missing = [name for name, pattern in CHECKS.items() if not re.search(pattern, visible + " " + source, re.I)]
        if not missing:
            continue
        cards = "".join(
            f'<article class="location-card reveal"><h3>{html.escape(LABELS[language][field][0])}</h3><p>{html.escape(LABELS[language][field][1])}</p></article>'
            for field in missing
        )
        section = f'<section class="section section-light" data-bf-case-contract="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">EVIDENCE STATUS</span><h2 class="section-title">{html.escape(LABELS[language]["title"])}</h2></div><div class="grid-3">{cards}</div></div></section>'
        faq_match = re.search(r'<section\b[^>]*>(?:(?!</section>).)*(?:FAQ|常見問題|よくある質問)', source, re.S | re.I)
        if not faq_match:
            raise SystemExit(f"FAQ section not found: {path}")
        source = source[:faq_match.start()] + section + source[faq_match.start():]
        path.write_text(source, encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}: {', '.join(missing)}")
