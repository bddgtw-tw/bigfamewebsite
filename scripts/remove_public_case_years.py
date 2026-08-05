from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
YEAR = re.compile(r"(?<![A-Za-z0-9])(?:19|20)\d{2}(?:年)?(?:\s*Q[1-4])?(?![A-Za-z0-9])")
ATTR = re.compile(r"(?P<open>\b(?:href|src|action|poster|data-src)=\s*[\"'])(?P<value>.*?)(?P<close>[\"'])", re.I)


def files():
    result = []
    for language in ("tw", "en", "jp"):
        folder = ROOT / language
        result.append(folder / "applications.html")
        result.extend(folder.glob("case-*.html"))
        result.extend(folder.glob("case-*/index.html"))
    return sorted(set(result))


def clean(text: str) -> str:
    protected = []

    def hold(match):
        protected.append(match.group(0))
        return f"__BF_PROTECTED_{len(protected) - 1}__"

    text = ATTR.sub(hold, text)
    text = YEAR.sub("", text)
    text = text.replace("> · ", ">")
    text = text.replace(" · </", "</")
    text = re.sub(r"(<(?:title|h[1-3])[^>]*>)\s+", r"\1", text, flags=re.I)
    text = text.replace("  ", " ")
    text = re.sub(r"(?<=>) {2,}(?=[^<]*<)", " ", text)
    for index, value in enumerate(protected):
        text = text.replace(f"__BF_PROTECTED_{index}__", value)
    return text


changed = 0
for path in files():
    original = path.read_text(encoding="utf-8")
    updated = clean(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        changed += 1
        print(path.relative_to(ROOT))

print(f"changed={changed}")
