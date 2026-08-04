from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

for lang in ("tw", "en", "jp"):
    flat_path = ROOT / lang / "case-retail-fixture-procurement-integration.html"
    clean_path = ROOT / lang / "case-retail-fixture-procurement-integration" / "index.html"
    flat = flat_path.read_text(encoding="utf-8")
    required = (
        'data-bf-source-record="1"',
        'data-bf-case-contract="1"',
        'data-bf-faq="1"',
        "TA MUJI",
    )
    missing = [marker for marker in required if marker not in flat]
    if missing:
        raise RuntimeError(f"{lang} flat procurement case missing: {missing}")
    clean_path.write_text(flat, encoding="utf-8", newline="\n")

print("Synchronized procurement case flat and clean variants for tw/en/jp")
