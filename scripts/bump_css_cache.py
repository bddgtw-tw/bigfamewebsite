from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
old = "style.css?v=20260805-p1"
new = "style.css?v=20260805-p2"
changed = 0
for path in ROOT.rglob("*.html"):
    text = path.read_text(encoding="utf-8")
    updated = text.replace(old, new)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        changed += 1
print(f"changed={changed}")
