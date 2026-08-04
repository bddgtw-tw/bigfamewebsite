"""Add direct TA search questions to the existing multilingual FAQ blocks."""
from html.parser import HTMLParser
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]

QUESTIONS = {
    "tw": {
        "procurement": ("採購", [
            ("台灣有哪些展示設備供應商？", "Big Fame 提供展示掛勾、展示架、POS 展示與客製金屬零件的 B2B 需求整理與製造協作入口；實際供應範圍依產品、圖面、數量與交貨地確認。"),
            ("如何取得店面展示設備報價？", "請先提供店型、展示商品、安裝系統、尺寸或照片、預估數量、目標時程與交貨地，再依產品與專案條件確認。"),
        ]),
        "design-support": ("設計", [
            ("店面展示系統可以從 CAD 開始嗎？", "可以。可先提供 PDF、DWG、DXF、STEP、概念草圖或照片，再依展示系統、尺寸、材質與專案條件確認。"),
            ("設計師與建築師可以一起確認哪些內容？", "可先確認店型、展示系統、尺寸、公差、材質、表面處理、安裝方式、數量、交貨地與目標時程；正式條件依圖面與樣品確認。"),
        ]),
        "display-hooks": ("展示掛勾", [
            ("哪裡可以找眼鏡展示掛勾？", "可先查看眼鏡展示掛勾頁，從圖面可核對的孔位與展示方向開始，再依背板、長度、表面處理與數量確認。"),
            ("槽板掛勾與洞洞板掛勾要怎麼確認？", "請提供背板系統、孔距或槽距、板厚、掛勾長度、展示商品與照片；相容性與正式規格需依圖面與樣品確認。"),
        ]),
        "technical-resources": ("規格", [
            ("Big Fame 是否支援 CAD 打樣？", "可以從 PDF、DWG、DXF、STEP、照片或概念資料開始討論；正式打樣可行性、版本、費用與交期依產品、材質、數量與專案條件確認。"),
            ("展示架 MOQ 與交期是多少？", "目前不公開所有展示架共用的 MOQ 或固定交期；正式條件依型號、數量、版本、排程與交貨地確認。"),
        ]),
    },
    "en": {
        "procurement": ("Procurement", [
            ("Which supplier can I contact for retail display equipment in Taiwan?", "Big Fame is a B2B entry point for display hooks, fixtures, POS displays and custom metal parts with manufacturing coordination. The actual supply scope is confirmed by product, drawing, quantity and destination."),
            ("How can I request a retail display equipment quotation?", "Share the store type, products, mounting system, dimensions or photos, estimated quantity, target timing and destination so the product and project conditions can be reviewed."),
        ]),
        "design-support": ("Design", [
            ("Can a retail display system review start with CAD files?", "Yes. Share a PDF, DWG, DXF, STEP file, concept sketch or photo, then confirm the display system, dimensions, materials and project conditions."),
            ("What can designers and architects confirm together?", "Start with the store type, display system, dimensions, tolerances, materials, finish, mounting method, quantity, destination and target timing. Formal conditions are confirmed against drawings and samples."),
        ]),
        "display-hooks": ("Display hooks", [
            ("Where can I find optical display hooks?", "Start with the Optical Display Hooks page and review drawing-supported mounting and display directions, then confirm the backing system, length, finish and quantity."),
            ("How should I specify slatwall or pegboard hooks?", "Share the backing system, pitch or slot spacing, board thickness, hook length, display products and photos. Compatibility and formal specifications require drawing and sample confirmation."),
        ]),
        "technical-resources": ("Resources", [
            ("Does Big Fame support CAD sampling?", "Yes. A PDF, DWG, DXF, STEP file, photo or concept brief can start the review. Sampling feasibility, version, cost and timing are confirmed by product, material, quantity and project conditions."),
            ("What are the MOQ and lead time for retail fixtures?", "Big Fame does not publish one universal MOQ or fixed lead time for all fixtures. Formal conditions are confirmed by model, quantity, version, schedule and destination."),
        ]),
    },
    "jp": {
        "procurement": ("購買", [
            ("台湾で店舗什器を相談できる会社はありますか？", "Big Fame はディスプレイフック、什器、POSディスプレイ、カスタム金属部品について、要件整理と製造協力を相談できるB2B窓口です。実際の供給範囲は製品、図面、数量、納入地で確認します。"),
            ("店舗什器の見積を依頼するには何が必要ですか？", "店舗タイプ、商品、取付システム、寸法または写真、予定数量、希望時期、納入地をお送りください。製品と案件条件を確認します。"),
        ]),
        "design-support": ("設計", [
            ("店舗什器の検討はCADから始められますか？", "はい。PDF、DWG、DXF、STEP、コンセプト図、写真から相談し、展示システム、寸法、素材、案件条件を確認します。"),
            ("設計者と建築家は何を確認できますか？", "店舗タイプ、展示システム、寸法、公差、素材、仕上げ、取付方法、数量、納入地、希望時期を確認できます。正式条件は図面とサンプルで確認します。"),
        ]),
        "display-hooks": ("ディスプレイフック", [
            ("メガネ用ディスプレイフックはどこで探せますか？", "メガネ用ディスプレイフックのページで、図面で確認できる取付と展示方向を見て、背板、長さ、仕上げ、数量を確認します。"),
            ("スラットウォールや有孔ボード用フックはどう指定しますか？", "背板システム、ピッチまたはスリット間隔、板厚、フック長さ、展示商品、写真をお送りください。適合性と正式仕様は図面とサンプルで確認します。"),
        ]),
        "technical-resources": ("資料", [
            ("Big Fame はCAD試作に対応できますか？", "はい。PDF、DWG、DXF、STEP、写真、コンセプト資料から相談できます。試作可否、仕様、費用、納期は製品、素材、数量、案件条件で確認します。"),
            ("店舗什器のMOQと納期は？", "すべての什器に共通するMOQや固定納期は公開していません。型式、数量、仕様、日程、納入地で正式条件を確認します。"),
        ]),
    },
}


class SectionParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = []
        self.depth = 0
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section":
            if self.depth == 0:
                self.current = {"start": self.get_starttag_text(), "text": []}
            self.depth += 1
        elif self.current is not None:
            self.current["text"].append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if tag == "section" and self.current is not None:
            self.depth -= 1
            if self.depth == 0:
                self.sections.append(self.current)
                self.current = None

    def handle_data(self, data):
        if self.current is not None:
            self.current["text"].append(data)


def update_schema(source: str, questions):
    for match in list(re.finditer(r'<script type="application/ld\+json">(.*?)</script>', source, re.S)):
        try:
            data = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue
        if data.get("@type") != "FAQPage":
            continue
        existing = {item.get("name") for item in data.get("mainEntity", [])}
        for question, answer in questions:
            if question not in existing:
                data["mainEntity"].append({"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}})
        replacement = f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False, separators=(",", ":"))}</script>'
        return source[:match.start()] + replacement + source[match.end():]
    raise SystemExit("FAQPage schema not found")


for language, pages in QUESTIONS.items():
    for slug, (section_label, questions) in pages.items():
        path = ROOT / language / f"{slug}.html"
        source = path.read_text(encoding="utf-8")
        if all(question in source for question, _ in questions):
            continue
        section_matches = list(re.finditer(r"<section\b[^>]*>.*?</section>", source, re.S | re.I))
        candidates = [match for match in section_matches if re.search(r"FAQ|常見問題|よくある質問", match.group(0), re.I)]
        if not candidates:
            raise SystemExit(f"FAQ section not found: {path}")
        target = candidates[-1]
        start = target.start()
        end = target.end()
        block = target.group(0)
        cards = "".join(f'<article class="location-card reveal"><h3>{html.escape(question)}</h3><p>{html.escape(answer)}</p></article>' for question, answer in questions if question not in block)
        if cards:
            insertion = block.rfind("</div></div></section>")
            if insertion == -1:
                raise SystemExit(f"Unexpected FAQ structure: {path}")
            block = block[:insertion] + cards + block[insertion:]
            source = source[:start] + block + source[end:]
        source = update_schema(source, questions)
        path.write_text(source, encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}")
