"""Repair generated-page links and remove unapproved founding-year footer claims."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for folder in ("tw", "en", "jp"):
    for path in (ROOT / folder).glob("*.html"):
        text = path.read_text(encoding="utf-8")
        if 'data-bf-enriched="1"' not in text:
            continue
        text = text.replace("https://www.bigfame.co//tw/products", "https://www.bigfame.co/tw/products")
        text = text.replace("https://www.bigfame.co//en/products", "https://www.bigfame.co/en/products")
        text = text.replace("https://www.bigfame.co//jp/products", "https://www.bigfame.co/jp/products")
        text = text.replace("https://www.bigfame.co//tw/applications", "https://www.bigfame.co/tw/applications")
        text = text.replace("https://www.bigfame.co//en/applications", "https://www.bigfame.co/en/applications")
        text = text.replace("https://www.bigfame.co//jp/applications", "https://www.bigfame.co/jp/applications")
        text = text.replace('</a> · <a href="display-hooks">Display hardware overview</a>', '</a> · <a href="case-eyewear-2016">2016 eyewear retail case</a> · <a href="display-hooks">Display hardware overview</a>')
        if folder == "tw":
            text = text.replace("Frequently asked questions", "常見問題")
        elif folder == "jp":
            text = text.replace("Frequently asked questions", "よくある質問")
        text = text.replace("© 1988-2026 Big Fame IND. CORP.", "© Big Fame IND. CORP.")
        path.write_text(text, encoding="utf-8")
