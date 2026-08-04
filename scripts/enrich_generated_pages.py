"""Add shared evidence-safe FAQ, breadcrumbs and product visuals to generated pages."""
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = {
    "display-hooks": ("展示掛鉤", "Display Hooks", "ディスプレイフック", "product_hooks.jpg"),
    "optical-hooks": ("眼鏡展示掛鉤", "Optical Display Hooks", "メガネディスプレイフック", "product_hooks.jpg"),
    "anti-theft-hooks": ("防盜展示掛鉤", "Anti-theft Display Hooks", "防犯ディスプレイフック", "product_hooks.jpg"),
    "slatwall-pegboard-accessories": ("槽板／洞洞板配件", "Slatwall and Pegboard Accessories", "スラットウォール・有孔ボード用金具", "product_hooks.jpg"),
    "price-tag-holders": ("價格條與標示配件", "Price Tag Holders and Signage Accessories", "プライスレール・表示金具", "product_hooks.jpg"),
    "pos-displays": ("POS 展示架", "POS Displays", "POSディスプレイ", "product_pos.jpg"),
    "modular-fixtures": ("模組化展示架", "Modular Retail Display Fixtures", "モジュール什器", "product_fixtures.jpg"),
    "custom-metal-parts": ("客製金屬零件", "Custom Metal Parts for Retail Display", "店舗什器向けカスタム金属部品", "product_parts.jpg"),
}
ENTRY_SLUGS = {"procurement", "design-support", "display-hooks"}


def faq_for(lang: str, product: bool):
    if lang == "zh-Hant-TW":
        return [("可以從 CAD 或照片開始嗎？", "可以。可先提供 PDF、DWG、DXF、STEP、照片或概念需求，再依產品與專案確認。"), ("MOQ 與交期是多少？", "客製五金通常由 500 pcs 起討論；整體展示專案通常由 50 sets 起討論。打樣約 2–3 週、首批約 6–8 週、重複訂單約 4–6 週，仍以專案確認為準。")]
    if lang == "ja":
        return [("CADや写真から相談できますか？", "はい。PDF、DWG、DXF、STEP、写真、概念資料から相談し、製品と案件条件で確認します。"), ("MOQと納期は？", "カスタム金具は通常500個から、什器案件は通常50セットから相談。試作約2–3週間、初回約6–8週間、リピート約4–6週間を目安に案件ごとに確認します。")]
    return [("Can we start with CAD files or a photo?", "Yes. Share a PDF, DWG, DXF, STEP file, photo or concept brief, then confirm the product and project conditions."), ("What are the MOQ and lead time?", "Custom hardware is usually discussed from 500 pcs and a full fixture project from 50 sets. Sampling is about 2–3 weeks, first batch about 6–8 weeks and repeat orders about 4–6 weeks, subject to confirmation.")]


def enrich(path: Path):
    text = path.read_text(encoding="utf-8")
    if "data-bf-enriched=\"1\"" in text:
        return
    lang = re.search(r'<html lang="([^"]+)', text).group(1)
    slug = path.stem
    is_product = slug in PRODUCTS
    if not (is_product or slug in ENTRY_SLUGS or slug == "case-eyewear-2016"):
        return
    questions = faq_for(lang, is_product)
    faq_entities = [{"@type":"Question", "name": q, "acceptedAnswer": {"@type":"Answer", "text": a}} for q, a in questions]
    current_url = re.search(r'<link rel="canonical" href="([^"]+)"', text).group(1)
    breadcrumb = {"@context":"https://schema.org", "@type":"BreadcrumbList", "itemListElement":[{"@type":"ListItem","position":1,"name":"Big Fame","item":"https://www.bigfame.co/"},{"@type":"ListItem","position":2,"name":"Products" if is_product else "Applications","item":"https://www.bigfame.co/" + (path.parent.name + "/products" if is_product else path.parent.name + "/applications")},{"@type":"ListItem","position":3,"name":slug,"item":current_url}]}
    faq_schema = {"@context":"https://schema.org", "@type":"FAQPage", "mainEntity":faq_entities}
    text = text.replace("</head>", f'<script type="application/ld+json">{json.dumps(breadcrumb, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script></head>', 1)
    faq_html = '<section class="section section-light" data-bf-enriched="1"><div class="container"><div class="section-heading reveal"><span class="section-subtitle">FAQ</span><h2 class="section-title">Frequently asked questions</h2></div><div class="grid-2">' + ''.join(f'<article class="location-card reveal"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>' for q, a in questions) + '</div></div></section>'
    text = text.replace('<section class="section section-dark">', faq_html + '<section class="section section-dark">', 1)
    if is_product:
        zh, en, ja, image = PRODUCTS[slug]
        names = f'<p class="product-names reveal"><strong>產品名稱：</strong>{html.escape(zh)} · {html.escape(en)} · {html.escape(ja)}</p>'
        visual = f'<div class="product-visual reveal"><img src="../images/{image}" alt="{html.escape(en, quote=True)}" loading="lazy"></div>'
        text = text.replace('</div></section><section class="section section-light">', names + visual + '</div></section><section class="section section-light">', 1)
    path.write_text(text.replace('<html ', '<html data-bf-enriched="1" ', 1), encoding="utf-8")


for folder in ("tw", "en", "jp"):
    for path in (ROOT / folder).glob("*.html"):
        enrich(path)
