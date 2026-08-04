"""Link the design-support TA entries to the engineering evidence case."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPLACEMENTS = {
    "tw/design-support.html": (
        '<a href="case-eyewear-2016">眼鏡零售展示案例</a>與<a href="case-japanese-wine-bar">酒吧展示案例</a>',
        '<a href="case-eyewear-2016">眼鏡零售展示案例</a>、<a href="case-hair-display-spinner-engineering">美妝展示旋轉架工程紀錄</a>與<a href="case-japanese-wine-bar">酒吧展示案例</a>',
    ),
    "en/design-support.html": (
        'the <a href="case-eyewear-2016">eyewear retail display case</a> and the <a href="case-japanese-wine-bar">wine-bar display case</a>',
        'the <a href="case-eyewear-2016">eyewear retail display case</a>, the <a href="case-hair-display-spinner-engineering">hair-display engineering record</a> and the <a href="case-japanese-wine-bar">wine-bar display case</a>',
    ),
    "jp/design-support.html": (
        '<a href="case-eyewear-2016">アイウェア店舗ディスプレイ事例</a>と<a href="case-japanese-wine-bar">ワインバー展示事例</a>',
        '<a href="case-eyewear-2016">アイウェア店舗ディスプレイ事例</a>、<a href="case-hair-display-spinner-engineering">ヘアケア什器の設計記録</a>と<a href="case-japanese-wine-bar">ワインバー展示事例</a>',
    ),
}

for relative, (old, new) in REPLACEMENTS.items():
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    if new in text:
        continue
    if old not in text:
        raise SystemExit(f"Expected design-support case phrase not found: {relative}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="")

print("Linked the engineering evidence case from all three design-support pages.")
