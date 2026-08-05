"""Create a compact inventory of public image and video assets."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "templates" / "media-library.json"
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".mp4", ".webm", ".mov"}

items = []
for folder_name in ("images", "videos"):
    folder = ROOT / folder_name
    for path in sorted(folder.glob("*")):
        if path.is_file() and path.suffix.lower() in EXTENSIONS:
            role = "video" if folder_name == "videos" else (
                "case" if path.name.lower().startswith("case") else
                "factory" if path.name.lower().startswith("factory") else
                "hero" if path.name.lower().startswith("hero") else "product"
            )
            items.append({
                "file": f"{folder_name}/{path.name}",
                "role": role,
                "bytes": path.stat().st_size,
            })

OUTPUT.write_text(json.dumps({"generated_from": "images/ and videos/", "items": items}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"media_items={len(items)}")
print(f"output={OUTPUT.relative_to(ROOT)}")
