"""Build a Pages comparison site from two checkouts. No repository documents are published."""
import argparse
import html
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from posixpath import normpath

ATTR = re.compile(r'\b(href|src|action)\s*=\s*(["\'])(.*?)\2', re.I)
WEB_DIRS = ("jp", "en", "tw", "css", "js", "images", "videos")
ASSET_SUFFIXES = {".css", ".js", ".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".ico", ".mp4", ".woff", ".woff2", ".ttf", ".pdf"}

def local_link(value, source, root, prefix):
    decoded = html.unescape(value)
    u = urlsplit(decoded)
    if u.scheme or u.netloc or not u.path:
        return value
    if u.path.startswith("/"):
        candidate = u.path.lstrip("/")
    else:
        candidate = normpath(str(source.parent / u.path))
    if candidate.startswith("../"):
        return value
    if (root / (candidate + ".html")).is_file():
        candidate += ".html"
    elif (root / candidate).is_dir() and (root / candidate / "index.html").is_file():
        candidate = candidate.rstrip("/") + "/"
    elif not (root / candidate).is_file():
        return value
    return html.escape(urlunsplit(("", "", prefix + candidate, u.query, u.fragment)), quote=True)

def export(root, out, prefix):
    pages = []
    for directory in WEB_DIRS:
        folder = root / directory
        if not folder.is_dir():
            continue
        for source in folder.rglob("*"):
            if not source.is_file() or source.is_symlink():
                continue
            rel = source.relative_to(root)
            if any(part.startswith(".") for part in rel.parts):
                continue
            if source.suffix.lower() == ".html" and directory in ("jp", "en", "tw"):
                target = out / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                text = source.read_text(encoding="utf-8")
                text = ATTR.sub(lambda m: m[1] + "=" + m[2] + local_link(m[3], rel, root, prefix) + m[2], text)
                text = re.sub(r'<meta\s+[^>]*name=["\']robots["\'][^>]*>', "", text, flags=re.I)
                text = re.sub(r'</head>', '<meta name="robots" content="noindex,nofollow">\n</head>', text, count=1, flags=re.I)
                target.write_text(text, encoding="utf-8")
                pages.append(rel.as_posix())
            elif source.suffix.lower() in ASSET_SUFFIXES:
                target = out / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
    for locale in ("jp", "en", "tw"):
        if not (out / locale / "index.html").is_file():
            raise ValueError("Missing locale homepage: " + locale)
    (out / "index.html").write_text('<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><title>BIG FAME</title><a href="jp/">日本語</a> <a href="en/">English</a> <a href="tw/">繁體中文</a>', encoding="utf-8")
    return pages

def build(main, preview, output, base="/bigfamewebsite/"):
    if not re.fullmatch(r"/[A-Za-z0-9_/-]*/", base):
        raise ValueError("Invalid Pages base path")
    output.mkdir(parents=True, exist_ok=True)
    export(main, output, base)
    export(preview, output / "preview/jp-taste", base + "preview/jp-taste/")
    (output / ".nojekyll").touch()
    (output / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    (output / "compare").mkdir(exist_ok=True)
    (output / "compare/index.html").write_text("""<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>BIG FAME 版本比較</title>
<style>body{margin:0;background:#F7F6F2;color:#1A1A1A;font:16px/1.68 system-ui,sans-serif}main{max-width:960px;margin:auto;padding:100px 24px}h1{font-size:clamp(28px,5vw,48px);line-height:1.25}a{display:block;padding:24px 0;color:inherit;border-bottom:1px solid #d4d2c9}a:focus-visible{outline:2px solid #1A1A1A}p{color:#55544f}</style></head>
<body><main><h1>BIG FAME 版本比較</h1><p>選擇版本後，可在瀏覽器分頁並排檢視。</p><a href="../jp/">日文首頁：main 正式版快照</a><a href="../preview/jp-taste/jp/">日文首頁：改善分支預覽</a></main></body></html>""", encoding="utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--main", type=Path, required=True)
    parser.add_argument("--preview", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--base", default="/bigfamewebsite/")
    args = parser.parse_args()
    build(args.main, args.preview, args.output, args.base)
