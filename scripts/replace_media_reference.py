"""Replace one public media filename across generated HTML and style files.

Usage:
    python scripts/replace_media_reference.py old.jpg new.jpg

The target file must already exist under images/ or videos/. The operation is
bounded to public page and style files, and reports every changed file.
"""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIRS = (ROOT / "tw", ROOT / "en", ROOT / "jp", ROOT / "css", ROOT / "js", ROOT / "scripts")
MEDIA_DIRS = (ROOT / "images", ROOT / "videos")


def usage() -> None:
    print("Usage: python scripts/replace_media_reference.py OLD_FILENAME NEW_FILENAME")


if len(sys.argv) != 3:
    usage()
    raise SystemExit(2)

old, new = sys.argv[1:]
if Path(old).name != old or Path(new).name != new:
    raise SystemExit("Only filenames are accepted; paths are not allowed.")
if not any((folder / new).is_file() for folder in MEDIA_DIRS):
    raise SystemExit(f"Target media file does not exist under images/ or videos/: {new}")

changed = []
for folder in PUBLIC_DIRS:
    if not folder.exists():
        continue
    for path in folder.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".html", ".css", ".js", ".py"}:
            continue
        text = path.read_text(encoding="utf-8")
        updated = text.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed.append(path.relative_to(ROOT).as_posix())

print(f"old={old}")
print(f"new={new}")
print(f"changed={len(changed)}")
for item in changed:
    print(item)
