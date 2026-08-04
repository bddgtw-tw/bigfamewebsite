"""Add a small inline fallback for requested_files query prefill on contact pages."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
needle = "document.getElementById('source_role').value=r||'unspecified';"
replacement = needle + "var f=q.get('requested_files');if(f)document.getElementById('requested_files').value=f;"

for locale in ("tw", "en", "jp"):
    path = ROOT / locale / "contact.html"
    text = path.read_text(encoding="utf-8")
    if "q.get('requested_files')" in text:
        continue
    if needle not in text:
        raise SystemExit(f"contact context marker missing: {path}")
    path.write_text(text.replace(needle, replacement, 1), encoding="utf-8")
