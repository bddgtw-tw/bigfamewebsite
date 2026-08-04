"""Create directory-index routes for clean URLs on static hosts."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
slugs = [
    "procurement", "design-support", "display-hooks", "case-eyewear-2016",
    "optical-hooks", "anti-theft-hooks", "slatwall-pegboard-accessories",
    "price-tag-holders", "pos-displays", "modular-fixtures", "custom-metal-parts",
]
for language in ("tw", "en", "jp"):
    for slug in slugs:
        source = ROOT / language / f"{slug}.html"
        target_dir = ROOT / language / slug
        target_dir.mkdir(exist_ok=True)
        text = source.read_text(encoding="utf-8")
        text = text.replace('href="../css/', 'href="../../css/')
        text = text.replace('src="../images/', 'src="../../images/')
        text = text.replace('src="../js/', 'src="../../js/')
        for name in ("products", "applications", "contact", "display-hooks", "case-eyewear-2016"):
            text = text.replace(f'href="{name}', f'href="../{name}')
        text = text.replace('href="./"', 'href="../"')
        (target_dir / "index.html").write_text(text, encoding="utf-8")
