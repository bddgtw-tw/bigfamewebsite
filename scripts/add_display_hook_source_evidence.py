"""Add evidence-bound display-hook dimensions from the raw Product Hook document."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = {
    "tw": {
        "anchor": "安裝系統",
        "title": "原始文件可核對的掛勾資料",
        "body": "Product Hook.docx 記錄 wire hook 方向、掛勾長度 50／75／100／150／200 mm 等級距，以及 Φ5.0／Φ6.0／Φ8.0／Φ10.0 線徑；這是原始文件的型式資料，不延伸推定所有目前 SKU。",
        "bar_title": "Crossbar 與展示系統方向",
        "bar_body": "文件另記錄 crossbar 長條 10×20、14×24、20×40、15×30 mm，並描述 pegboard、slatwall、wire shelving 等使用方向；正式相容性仍依背板、SKU、圖面與樣品確認。",
        "source": "來源：Product Hook.docx。正式材質牌號、表面處理、MOQ、交期與客製範圍仍依 SKU、圖面與專案確認。",
        "commercial": "原始文件可支持 wire hook 與上述尺寸方向；正式材質牌號、線徑、MOQ、交期、包裝與客製範圍，依 SKU、圖面與樣品確認。",
    },
    "en": {
        "anchor": "Mounting systems",
        "title": "Raw document hook data",
        "body": "Product Hook.docx records wire-hook directions, hook lengths of 50 / 75 / 100 / 150 / 200 mm and hook diameters of Φ5.0 / Φ6.0 / Φ8.0 / Φ10.0. These are raw document type ranges, not a blanket claim for every current SKU.",
        "bar_title": "Crossbar and fixture-system directions",
        "bar_body": "The document also records crossbar sizes of 10×20, 14×24, 20×40 and 15×30 mm, and describes pegboard, slatwall and wire-shelving directions. Confirm compatibility by backing system, SKU, drawing and sample.",
        "source": "Source: Product Hook.docx. Formal material grade, finish, MOQ, lead time and customization scope remain subject to SKU, drawing and project confirmation.",
        "commercial": "The raw document supports wire-hook and the dimension directions above; formal material grade, wire diameter, MOQ, lead time, packaging and customization scope require SKU, drawing and sample confirmation.",
    },
    "jp": {
        "anchor": "取付システム",
        "title": "原資料で確認できるフック情報",
        "body": "Product Hook.docx には wire hook の方向、フック長さ 50／75／100／150／200 mm、フック線径 Φ5.0／Φ6.0／Φ8.0／Φ10.0 が記録されています。原資料の型式範囲であり、すべての現行 SKU への一括適用ではありません。",
        "bar_title": "Crossbar と什器システムの方向",
        "bar_body": "資料には crossbar の 10×20、14×24、20×40、15×30 mm も記録され、pegboard、slatwall、wire shelving の方向が説明されています。適合性は背板、SKU、図面、サンプルで確認します。",
        "source": "出典：Product Hook.docx。正式な材質グレード、仕上げ、MOQ、納期、カスタム範囲は SKU、図面、案件で確認します。",
        "commercial": "原資料から wire hook と上記寸法の方向を確認できます。正式な材質グレード、線径、MOQ、納期、梱包、カスタム範囲は SKU、図面、サンプルで確認します。",
    },
}


def update(path: Path, cfg: dict) -> bool:
    text = path.read_text(encoding="utf-8")
    if cfg["title"] in text:
        return False
    anchor_re = re.compile(
        rf'(<article class="location-card reveal"><h3>{re.escape(cfg["anchor"])}</h3><p>.*?</p></article>)',
        re.S,
    )
    match = anchor_re.search(text)
    if not match:
        raise SystemExit(f"anchor not found: {path}")
    cards = (
        match.group(1)
        + f'<article class="location-card reveal"><h3>{cfg["title"]}</h3><p>{cfg["body"]}</p><p>{cfg["source"]}</p></article>'
        + f'<article class="location-card reveal"><h3>{cfg["bar_title"]}</h3><p>{cfg["bar_body"]}</p></article>'
    )
    text = text[: match.start()] + cards + text[match.end() :]
    old = {
        "tw": "材質、線徑、MOQ、交期、包裝與客製範圍，依 SKU、圖面與樣品確認。",
        "en": "Material, wire diameter, MOQ, lead time, packaging and customization are confirmed by SKU, drawing and sample.",
        "jp": "材質、線径、MOQ、納期、梱包、カスタム範囲は SKU・図面・サンプルで確認します。",
    }[next(lang for lang, item in DATA.items() if item is cfg)]
    text = text.replace(old, cfg["commercial"], 1)
    path.write_text(text, encoding="utf-8", newline="")
    return True


for lang, cfg in DATA.items():
    for rel in (f"{lang}/display-hooks.html", f"{lang}/display-hooks/index.html"):
        update(ROOT / rel, cfg)
