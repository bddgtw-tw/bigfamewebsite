"""Inventory Big Fame source media without copying or publishing files."""

from pathlib import Path
from collections import Counter
import json


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "網站營運素材" / "02_Big_Fame_Raw_Data"
OUTPUT = ROOT / "templates" / "big-fame-source-media-inventory.json"
EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".mp4", ".mov", ".webm", ".pdf", ".ai", ".psd", ".tif", ".tiff"}

if not SOURCE.exists():
    raise SystemExit(f"Source folder not found: {SOURCE}")

top = []
for folder in sorted(SOURCE.iterdir()):
    if not folder.is_dir():
        continue
    files = [p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in EXTENSIONS]
    counts = Counter(p.suffix.lower().lstrip(".") for p in files)
    top.append({
        "folder": folder.name,
        "media_count": len(files),
        "by_extension": dict(sorted(counts.items())),
    })

report = {
    "source_root": str(SOURCE),
    "scope": "Big Fame raw website and marketing media source; no files copied or published",
    "total_media_files": sum(item["media_count"] for item in top),
    "top_level": sorted(top, key=lambda item: item["media_count"], reverse=True),
}
OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"total_media_files={report['total_media_files']}")
print(f"output={OUTPUT.relative_to(ROOT)}")
