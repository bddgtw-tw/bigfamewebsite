"""Link existing product and design pages to the anonymous jewelry record."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {"tw": "珠寶展示配件紀錄", "en": "Jewelry display record", "jp": "ジュエリー展示記録"}

def add_after_anchor(path: Path, anchor: str, label: str, href: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if href in text:
        return False
    pos = text.find(anchor)
    if pos < 0:
        raise SystemExit(f"anchor not found: {path} / {anchor}")
    end = text.find("</a>", pos)
    if end < 0:
        raise SystemExit(f"closing anchor not found: {path}")
    end += len("</a>")
    text = text[:end] + f' · <a href="{href}">{label}</a>' + text[end:]
    path.write_text(text, encoding="utf-8")
    return True

changed = 0
for locale, label in LABELS.items():
    for slug in ("custom-metal-parts", "design-support"):
        for path in (ROOT / locale / f"{slug}.html", ROOT / locale / slug / "index.html"):
            href = "jewelry-display-accessories" if path.parent == ROOT / locale else "../jewelry-display-accessories"
            anchor = 'href="case-ivy-modular-system"' if slug == "custom-metal-parts" and path.parent == ROOT / locale else 'href="../case-ivy-modular-system"' if slug == "custom-metal-parts" else 'href="custom-metal-parts"' if path.parent == ROOT / locale else 'href="../custom-metal-parts"'
            if add_after_anchor(path, anchor, label, href):
                changed += 1
print(f"UPDATED_PAGES={changed}")
