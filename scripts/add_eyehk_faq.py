"""Expose the drawing-backed EYEHK questions in visible FAQ and FAQPage JSON-LD."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = {
    "tw": [
        ("2025 洞洞板圖面有哪些尺寸？", "圖面可見 160、175、150.93、128 與 25.4 mm 等尺寸；這些是圖面版本證據，正式 SKU 與目前版本需用最新圖面和樣品確認。"),
        ("2018 鎖螺絲版本有哪些材料與表面處理備註？", "圖面註記 t2.0 鐵板、橫向 4.0 鐵線、黑色粉體烤漆、尾端倒角與約 2° 上仰；正式材質牌號與表面處理仍依最新 SKU 確認。"),
    ],
    "en": [
        ("What dimensions are shown in the 2025 pegboard drawing?", "The drawing shows 160, 175, 150.93, 128 and 25.4 mm dimensions. These are drawing-version evidence; confirm the current SKU and revision against the latest drawing and sample."),
        ("What material and finish notes appear in the 2018 screw-on drawing?", "The drawing notes a t2.0 iron plate, 4.0 mm horizontal iron wire, black powder coating, chamfered ends and an approximately 2° upward angle. Confirm the formal material grade and finish by the current SKU."),
    ],
    "jp": [
        ("2025年の有孔ボード用図面にはどの寸法がありますか？", "図面には 160、175、150.93、128、25.4 mm などの寸法があります。図面版の根拠であり、現行 SKU と改訂版は最新図面とサンプルで確認します。"),
        ("2018年のねじ固定図面にはどの材質・仕上げの注記がありますか？", "t2.0 鉄板、横方向 4.0 mm 鉄線、ブラック粉体塗装、端部面取り、約 2° の上向き角度が記録されています。正式な材質グレードと仕上げは現行 SKU で確認します。"),
    ],
}


def add_json_ld(text: str, items: list[tuple[str, str]]) -> str:
    pattern = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)

    def replace(match: re.Match[str]) -> str:
        raw = match.group(1)
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return match.group(0)
        if data.get("@type") != "FAQPage":
            return match.group(0)
        known = {entry.get("name") for entry in data.get("mainEntity", [])}
        for question, answer in items:
            if question not in known:
                data.setdefault("mainEntity", []).append({
                    "@type": "Question",
                    "name": question,
                    "acceptedAnswer": {"@type": "Answer", "text": answer},
                })
        return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>"

    return pattern.sub(replace, text, count=0)


for lang, items in DATA.items():
    visible = ''.join(f'<article class="location-card reveal"><h3>{q}</h3><p>{a}</p></article>' for q, a in items)
    for rel in (f"{lang}/optical-hooks.html", f"{lang}/optical-hooks/index.html"):
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        if items[0][0] not in text:
            text = add_json_ld(text, items)
            anchor = '</div></div></section><section class="section section-light" data-bf-ta-links="1">'
            if anchor not in text:
                raise SystemExit(f"FAQ closing anchor not found: {path}")
            text = text.replace(anchor, visible + anchor, 1)
            path.write_text(text, encoding="utf-8", newline="")
