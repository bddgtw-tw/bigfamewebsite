"""Link the procurement TA entry to the evidence-backed procurement case."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPLACEMENTS = {
    "tw/procurement.html": (
        '<a href="case-eyewear-2016">眼鏡零售展示案例</a>；也可查看',
        '<a href="case-eyewear-2016">眼鏡零售展示案例</a>、<a href="case-retail-fixture-procurement-integration">匿名零售店面採購整合紀錄</a>；也可查看',
    ),
    "en/procurement.html": (
        '<a href="case-eyewear-2016">eyewear retail display case</a> or the',
        '<a href="case-eyewear-2016">eyewear retail display case</a>, the <a href="case-retail-fixture-procurement-integration">anonymous retail fixture procurement record</a> or the',
    ),
    "jp/procurement.html": (
        '<a href="case-eyewear-2016">アイウェア店舗ディスプレイ事例</a>、<a href="case-japanese-wine-bar">ワインバー展示事例</a>',
        '<a href="case-eyewear-2016">アイウェア店舗ディスプレイ事例</a>、<a href="case-retail-fixture-procurement-integration">匿名の店舗什器調達統合記録</a>、<a href="case-japanese-wine-bar">ワインバー展示事例</a>',
    ),
}

for relative, (old, new) in REPLACEMENTS.items():
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    if new in text:
        continue
    if old not in text:
        raise SystemExit(f"Expected procurement case phrase not found: {relative}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="")

print("Linked the procurement evidence case from all three procurement pages.")
