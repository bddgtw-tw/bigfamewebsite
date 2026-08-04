"""Add direct drawing evidence for the EYEHK optical-hook page."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = {
    "tw": {
        "marker": "圖面可核對的變體",
        "heading": "圖面可核對的變體",
        "peg_title": "2025 洞洞板圖面",
        "peg_body": "Eyewear Display Hook (pegboard) 圖面可見 160、175、150.93、128 與 25.4 mm 等尺寸，並註記以雷射切割形成掛片，再焊接於面板背面；消水孔 Ø4 移至下方。這是圖面版本證據，不延伸推定所有 SKU。",
        "screw_title": "2018 鎖螺絲／溝槽板圖面",
        "screw_body": "圖面註記 t2.0 鐵板、橫向 4.0 鐵線、5.0 吊孔、黑色粉體烤漆、尾端倒角與約 2° 上仰；可見外包 145／175 mm 與 40 mm 安裝片尺寸。",
        "note": "圖面另有「估價數量 1000 支」備註；這不是已驗證的實際交付數量或通用 MOQ。正式 SKU、材質牌號、交期與目前可供應性，依最新圖面與樣品確認。",
    },
    "en": {
        "marker": "Documented drawing variants",
        "heading": "Documented drawing variants",
        "peg_title": "2025 pegboard drawing",
        "peg_body": "The Eyewear Display Hook (pegboard) drawing shows 160, 175, 150.93, 128 and 25.4 mm dimensions, and notes a laser-cut mounting tab welded to the back of the panel; the Ø4 drain hole is moved downward. This is drawing-version evidence, not a blanket claim for every SKU.",
        "screw_title": "2018 screw-on / slatwall drawing",
        "screw_body": "The drawing notes a t2.0 iron plate, 4.0 mm horizontal iron wire, a 5.0 mm hanging-hole position, black powder coating, chamfered ends and an approximately 2° upward angle; visible views include 145 / 175 mm outer dimensions and a 40 mm mounting plate.",
        "note": "The drawing also notes an estimated quotation quantity of 1,000 pieces; this is not verified delivery quantity or universal MOQ. Confirm the current SKU, material grade, lead time and availability against the latest drawing and sample.",
    },
    "jp": {
        "marker": "図面で確認できるバリエーション",
        "heading": "図面で確認できるバリエーション",
        "peg_title": "2025 有孔ボード用図面",
        "peg_body": "Eyewear Display Hook (pegboard) の図面には 160、175、150.93、128、25.4 mm などの寸法が見られ、レーザー切断した掛片をパネル背面に溶接する注記があります。消水孔 Ø4 は下方へ移動。図面版の根拠であり、すべての SKU への一括適用ではありません。",
        "screw_title": "2018 ねじ固定／スラットウォール用図面",
        "screw_body": "図面には t2.0 鉄板、横方向 4.0 mm 鉄線、5.0 mm 吊り孔、ブラック粉体塗装、端部面取り、約 2° の上向き角度が記録されています。外包 145／175 mm と 40 mm の取付プレート寸法も見られます。",
        "note": "図面には見積数量 1,000 本の注記もありますが、実際の納品数量や共通 MOQ ではありません。現行 SKU、材質グレード、納期、供給可否は最新図面とサンプルで確認します。",
    },
}


for lang, cfg in DATA.items():
    block = (
        f'<section class="section section-light"><div class="container"><div class="section-heading reveal">'
        f'<span class="section-subtitle">DRAWING VARIANTS</span><h2 class="section-title">{cfg["heading"]}</h2></div>'
        f'<div class="grid-2"><article class="location-card reveal"><h3>{cfg["peg_title"]}</h3><p>{cfg["peg_body"]}</p></article>'
        f'<article class="location-card reveal"><h3>{cfg["screw_title"]}</h3><p>{cfg["screw_body"]}</p></article></div>'
        f'<p class="section-note reveal">{cfg["note"]}</p></div></section>'
    )
    marker = {
        "tw": '<section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SPECIFICATION</span>',
        "en": '<section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SPECIFICATION</span>',
        "jp": '<section class="section section-light"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">SPECIFICATION</span>',
    }[lang]
    for rel in (f"{lang}/optical-hooks.html", f"{lang}/optical-hooks/index.html"):
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        if cfg["marker"] in text:
            continue
        if marker not in text:
            raise SystemExit(f"specification marker not found: {path}")
        text = text.replace(marker, block + marker, 1)
        path.write_text(text, encoding="utf-8", newline="")
