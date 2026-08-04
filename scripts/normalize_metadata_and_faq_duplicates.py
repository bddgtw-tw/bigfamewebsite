"""Remove duplicate Open Graph descriptions and redundant technical FAQs."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def keep_first_og_description(text: str) -> str:
    seen = False

    def replace(match: re.Match[str]) -> str:
        nonlocal seen
        if seen:
            return ""
        seen = True
        return match.group(0)

    return re.sub(r'<meta\s+property="og:description"[^>]*>', replace, text, flags=re.I)


def remove_visible_faq(text: str, question: str) -> str:
    pattern = rf'<article class="location-card reveal"><h3>{re.escape(question)}</h3><p>.*?</p></article>'
    return re.sub(pattern, "", text, count=1, flags=re.S)


def remove_jsonld_faq(text: str, question: str) -> str:
    pattern = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)

    def replace(match: re.Match[str]) -> str:
        try:
            data = json.loads(match.group(2))
        except json.JSONDecodeError:
            return match.group(0)
        if data.get("@type") != "FAQPage":
            return match.group(0)
        before = data.get("mainEntity", [])
        after = [item for item in before if item.get("name") != question]
        if len(after) == len(before):
            return match.group(0)
        data["mainEntity"] = after
        return match.group(1) + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + match.group(3)

    return pattern.sub(replace, text)


def main() -> None:
    changed = []
    for path in ROOT.rglob("*.html"):
        if "node_modules" in path.parts:
            continue
        original = path.read_text(encoding="utf-8")
        updated = keep_first_og_description(original)
        if path.as_posix().endswith("/en/technical-resources.html"):
            updated = remove_visible_faq(updated, "Does Big Fame support CAD sampling?")
            updated = remove_jsonld_faq(updated, "Does Big Fame support CAD sampling?")
        if path.as_posix().endswith("/jp/technical-resources.html"):
            updated = remove_visible_faq(updated, "Big Fame はCAD試作に対応できますか？")
            updated = remove_jsonld_faq(updated, "Big Fame はCAD試作に対応できますか？")
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="")
            changed.append(path.relative_to(ROOT).as_posix())
    print("Updated:", ", ".join(changed))


if __name__ == "__main__":
    main()
