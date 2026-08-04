import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PROCUREMENT_QUESTIONS = {
    "tw": [
        ("展示設備可以做 OEM 製造與量產嗎？", "可以先從圖面、數量、材料、表面處理、包裝與交貨地整理製造協作範圍；OEM 與量產條件不作一律承諾，仍以核准圖面與專案條件確認。"),
        ("店面展示設備量產時，如何兼顧成本與效率？", "可先整理零件共通化、模組化、材料利用、包裝、組裝方式、數量與補貨週期，再依產品、數量、規格與交付條件確認正式成本。"),
    ],
    "en": [
        ("Can retail display equipment be reviewed for OEM production and volume orders?", "Yes. Start with drawings, quantity, material, finish, packaging and destination so the manufacturing coordination scope can be reviewed. OEM and volume conditions are confirmed against approved drawings and project terms."),
        ("How can retail fixtures balance cost and efficiency in volume production?", "Review part commonality, modularity, material use, packaging, assembly method, quantity and replenishment cycle first. Formal cost depends on the product, specification, quantity and delivery conditions."),
    ],
    "jp": [
        ("陳列什器のOEM製造・量産体制を相談できますか？", "相談できます。図面、数量、材料、仕上げ、梱包、納入先を確認し、製造協力の範囲を個別に整理します。OEMや量産条件を一律に約束せず、承認図面と案件条件で確認します。"),
        ("店舗什器を量産するとき、コストと効率をどう確認しますか？", "部品の共通化、モジュール化、材料利用、梱包、組立方法、数量、補充周期を先に整理します。正式なコストは製品、仕様、数量、納品条件ごとに確認します。"),
    ],
}

SLATWALL_QUESTION = (
    "Can these accessories be reviewed for a retail shelving system?",
    "Yes. Share the shelving or backing system, slot pitch, board thickness, mounting direction, displayed product and photos so compatibility can be reviewed. Formal specifications require the matching drawing and sample.",
)


def update_faq(path: Path, questions: list[tuple[str, str]]) -> bool:
    source = path.read_text(encoding="utf-8")
    faq_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', source, re.S)
    faq_script = None
    for match in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', source, re.S):
        try:
            data = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue
        if data.get("@type") == "FAQPage":
            faq_match = match
            faq_script = data
            break
    if faq_match is None or faq_script is None:
        raise RuntimeError(f"FAQPage schema not found: {path}")

    existing = {item.get("name") for item in faq_script.get("mainEntity", [])}
    new_questions = [item for item in questions if item[0] not in existing]
    for question, answer in new_questions:
        faq_script["mainEntity"].append({"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}})
    if new_questions:
        replacement = f'<script type="application/ld+json">{json.dumps(faq_script, ensure_ascii=False, separators=(",", ":"))}</script>'
        source = source[:faq_match.start()] + replacement + source[faq_match.end():]

    faq_section = re.search(r'<section\b[^>]*data-bf-faq="1"[^>]*>.*?</section>', source, re.S | re.I)
    if faq_section is None:
        raise RuntimeError(f"FAQ section not found: {path}")
    block = faq_section.group(0)
    cards = "".join(
        f'<article class="location-card reveal"><h3>{question}</h3><p>{answer}</p></article>'
        for question, answer in new_questions
        if f">{question}</h3>" not in block
    )
    if cards:
        insertion = block.rfind("</div></div></section>")
        if insertion == -1:
            raise RuntimeError(f"Unexpected FAQ section structure: {path}")
        block = block[:insertion] + cards + block[insertion:]
        source = source[:faq_section.start()] + block + source[faq_section.end():]

    if source != path.read_text(encoding="utf-8"):
        path.write_text(source, encoding="utf-8")
        return True
    return False


def main() -> None:
    for language, questions in PROCUREMENT_QUESTIONS.items():
        path = ROOT / language / "procurement.html"
        if update_faq(path, questions):
            print(f"UPDATED {path.relative_to(ROOT)}")

    path = ROOT / "en" / "slatwall-pegboard-accessories.html"
    source = path.read_text(encoding="utf-8")
    source = source.replace(
        "<title>Slatwall / Pegboard Accessories | Big Fame</title>",
        "<title>Slatwall / Pegboard Accessories for Retail Shelving Systems | Big Fame</title>",
    )
    source = source.replace(
        '<meta property="og:title" content="Slatwall / Pegboard Accessories | Big Fame">',
        '<meta property="og:title" content="Slatwall / Pegboard Accessories for Retail Shelving Systems | Big Fame">',
    )
    source = source.replace(
        "<h1>Slatwall / Pegboard Accessories</h1>",
        "<h1>Slatwall / Pegboard Accessories for Retail Shelving Systems</h1>",
    )
    if SLATWALL_QUESTION[0] not in source:
        update_faq(path, [SLATWALL_QUESTION])
        source = path.read_text(encoding="utf-8")
        source = source.replace(
            "<title>Slatwall / Pegboard Accessories | Big Fame</title>",
            "<title>Slatwall / Pegboard Accessories for Retail Shelving Systems | Big Fame</title>",
        ).replace(
            '<meta property="og:title" content="Slatwall / Pegboard Accessories | Big Fame">',
            '<meta property="og:title" content="Slatwall / Pegboard Accessories for Retail Shelving Systems | Big Fame">',
        ).replace(
            "<h1>Slatwall / Pegboard Accessories</h1>",
            "<h1>Slatwall / Pegboard Accessories for Retail Shelving Systems</h1>",
        )
        path.write_text(source, encoding="utf-8")
        print(f"UPDATED {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
