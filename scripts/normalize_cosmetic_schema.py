"""Keep one FAQPage and one BreadcrumbList for each cosmetic organizer page."""

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
LABELS = {
    "tw": "桌上型化妝品收納展示器",
    "en": "Tabletop Cosmetic Organizer",
    "jp": "卓上化粧品オーガナイザー",
}
SCRIPT_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL)


for lang, label in LABELS.items():
    for path in [ROOT / lang / "cosmetic-organizers.html", ROOT / lang / "cosmetic-organizers" / "index.html"]:
        text = path.read_text(encoding="utf-8")
        seen_faq = False

        def normalize(match: re.Match[str]) -> str:
            try:
                data = json.loads(match.group(1))
            except json.JSONDecodeError:
                return match.group(0)
            if data.get("@type") == "FAQPage":
                if state[0]:
                    return ""
                state[0] = True
            return match.group(0)

        state = [False]
        text = SCRIPT_RE.sub(normalize, text)
        if '"@type": "BreadcrumbList"' not in text and '"@type":"BreadcrumbList"' not in text:
            canonical = f"https://www.bigfame.co/{lang}/cosmetic-organizers"
            crumb = json.dumps({
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Big Fame", "item": f"https://www.bigfame.co/{lang}/"},
                    {"@type": "ListItem", "position": 2, "name": "Products", "item": f"https://www.bigfame.co/{lang}/products"},
                    {"@type": "ListItem", "position": 3, "name": label, "item": canonical},
                ],
            }, ensure_ascii=False)
            text = text.replace("</head>", f'<script type="application/ld+json">{crumb}</script></head>', 1)
        path.write_text(text, encoding="utf-8")
