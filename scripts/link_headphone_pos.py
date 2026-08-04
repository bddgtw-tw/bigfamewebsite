"""Link the headphone display engineering record to POS display pages."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPLACEMENTS = {
    "tw": [
        ('<a href="display-hooks">展示掛勾</a> · <a href="modular-fixtures">模組化展示架</a> · <a href="applications">應用案例</a>', '<a href="display-hooks">展示掛勾</a> · <a href="modular-fixtures">模組化展示架</a> · <a href="pos-displays">POS 展示架</a> · <a href="applications">應用案例</a>'),
        ('<a href="../display-hooks">展示掛勾</a> · <a href="../modular-fixtures">模組化展示架</a> · <a href="../applications">應用案例</a>', '<a href="../display-hooks">展示掛勾</a> · <a href="../modular-fixtures">模組化展示架</a> · <a href="../pos-displays">POS 展示架</a> · <a href="../applications">應用案例</a>'),
    ],
    "en": [
        ('<a href="display-hooks">Display hooks</a> · <a href="modular-fixtures">Modular fixtures</a> · <a href="applications">Applications</a>', '<a href="display-hooks">Display hooks</a> · <a href="modular-fixtures">Modular fixtures</a> · <a href="pos-displays">POS displays</a> · <a href="applications">Applications</a>'),
        ('<a href="../display-hooks">Display hooks</a> · <a href="../modular-fixtures">Modular fixtures</a> · <a href="../applications">Applications</a>', '<a href="../display-hooks">Display hooks</a> · <a href="../modular-fixtures">Modular fixtures</a> · <a href="../pos-displays">POS displays</a> · <a href="../applications">Applications</a>'),
    ],
    "jp": [
        ('<a href="display-hooks">展示フック</a> · <a href="modular-fixtures">モジュール什器</a> · <a href="applications">事例</a>', '<a href="display-hooks">展示フック</a> · <a href="modular-fixtures">モジュール什器</a> · <a href="pos-displays">POS什器</a> · <a href="applications">事例</a>'),
        ('<a href="../display-hooks">展示フック</a> · <a href="../modular-fixtures">モジュール什器</a> · <a href="../applications">事例</a>', '<a href="../display-hooks">展示フック</a> · <a href="../modular-fixtures">モジュール什器</a> · <a href="../pos-displays">POS什器</a> · <a href="../applications">事例</a>'),
    ],
}


for language, pairs in REPLACEMENTS.items():
    for path in (
        ROOT / language / "case-headphone-display-set.html",
        ROOT / language / "case-headphone-display-set" / "index.html",
    ):
        source = path.read_text(encoding="utf-8")
        if 'pos-displays' in source:
            continue
        for old, new in pairs:
            if old in source:
                path.write_text(source.replace(old, new, 1), encoding="utf-8")
                print(f"UPDATED {path.relative_to(ROOT)}")
                break
        else:
            raise RuntimeError(f"Expected capability links not found: {path}")
