"""Audit that each public case page covers evidence fields and boundaries."""
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.hrefs = []

    def handle_data(self, data):
        self.text.append(data)

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.hrefs.append(href)


CHECKS = {
    "problem": r"客戶問題|客戶需求|客戶課題|顧客の課題|顧客の要望|Documented Need|Client Problem|Client Need|Project Evidence|What was the problem|需求討論|案件",
    "store_type": r"店型|店面|店舗|零售|Retail|Store|Space|店舗タイプ",
    "products": r"展示產品|使用產品|產品|產品方向|展示|展示櫃|掛勾|家具|Product|Display|Fixture|System|製品|什器",
    "materials": r"材料|材質|素材|Material|Materials|Wood|Metal|Glass|Acrylic",
    "scope": r"實際承擔範圍|Big Fame 做了什麼|Big Fame 公開範圍|Big Fameの対応|Big Fameの範囲|What Big Fame|Big Fame.?s contractual scope|Scope|Actual scope|対応範囲|公開範圍",
    "quantity": r"數量|数量|Quantity",
    "lead_time": r"交期|納期|文件交期|Lead time|timing",
    "delivery": r"交付地|目的地|交付先|納品地|納入地|納品先|配送先|Delivery|Destination|交貨地",
    "public_boundary": r"公開程度|公開範圍|匿名|授權|公開可否|Public|Anonymous|Evidence|公開範囲",
    "faq": r"FAQPage",
}

failures = []
pages = 0
for language in ("tw", "en", "jp"):
    flat_pages = sorted((ROOT / language).glob("case-*.html"))
    clean_pages = [path.parent / path.stem / "index.html" for path in flat_pages if (path.parent / path.stem / "index.html").exists()]
    for path in flat_pages + clean_pages:
        pages += 1
        source = path.read_text(encoding="utf-8")
        parser = TextParser()
        parser.feed(source)
        visible = " ".join(parser.text)
        missing = [name for name, pattern in CHECKS.items() if not re.search(pattern, visible + " " + source, re.I)]
        if not any(re.search(r"(?:^|/)contact(?:\.html)?\?", href) and "category=" in href for href in parser.hrefs):
            missing.append("contextual_cta")
        if missing:
            failures.append((str(path.relative_to(ROOT)), missing))

print(f"CASE_CONTRACT_PAGES={pages}")
print(f"CASE_CONTRACT_FAILURES={len(failures)}")
for path, missing in failures:
    print(f"{path}: {', '.join(missing)}")
if failures:
    raise SystemExit(1)
