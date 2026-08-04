"""Add the anonymous automotive rack record to the case and product navigation."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "case-automotive-parts-rack"

APPLICATION_CARD = {
    "tw": '<article class="case-library-card reveal"><div class="case-library-card-body"><div class="case-meta">2011 · Display Fixture Engineering · 匿名工程／交付紀錄</div><h3><a href="case-automotive-parts-rack">汽車零件展示架工程紀錄</a></h3><p>從洞洞板與旋轉架相容性、POP 掛牌，到結構補強、表面保護、組裝與包裝改善，整理可核對的工程證據。</p><a class="btn btn-secondary" href="case-automotive-parts-rack">查看工程證據與公開邊界</a></div></article>',
    "en": '<article class="case-library-card reveal"><div class="case-library-card-body"><div class="case-meta">2011 · Display Fixture Engineering · Anonymous engineering record</div><h3><a href="case-automotive-parts-rack">Automotive Parts Display Rack</a></h3><p>An engineering record covering pegboard and rotating-rack compatibility, POP hardware, structural reinforcement, surface protection, assembly and packing.</p><a class="btn btn-secondary" href="case-automotive-parts-rack">View evidence and boundaries</a></div></article>',
    "jp": '<article class="case-library-card reveal"><div class="case-library-card-body"><div class="case-meta">2011 · Display Fixture Engineering · 匿名エンジニアリング記録</div><h3><a href="case-automotive-parts-rack">自動車部品ディスプレイラック</a></h3><p>有孔ボードと回転ラックの互換性、POP金具、構造補強、表面保護、組立てと梱包改善を整理しています。</p><a class="btn btn-secondary" href="case-automotive-parts-rack">証拠と公開範囲を見る</a></div></article>',
}

for locale, card in APPLICATION_CARD.items():
    for path in [ROOT / locale / "applications.html", ROOT / locale / "applications" / "index.html"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if SLUG in text:
            continue
        marker = "\n      </div>\n    </div>\n  </section>\n\n  <!-- Audience & Store Type Navigation -->"
        if marker not in text:
            raise SystemExit(f"applications grid marker missing: {path}")
        text = text.replace(marker, f"\n        {card}{marker}", 1)
        text = text.replace("<strong>07</strong>", "<strong>08</strong>", 1)
        path.write_text(text, encoding="utf-8")

for locale in ["tw", "en", "jp"]:
    for path in [ROOT / locale / "modular-fixtures.html", ROOT / locale / "modular-fixtures" / "index.html", ROOT / locale / "display-hooks.html", ROOT / locale / "display-hooks" / "index.html"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if SLUG in text:
            continue
        link = f'<a href="{("../" if path.parent.name in {"modular-fixtures", "display-hooks"} else "")}{SLUG}">' + ("汽車零件展示架工程紀錄" if locale == "tw" else "Automotive parts display rack record" if locale == "en" else "自動車部品ラック記録") + "</a>"
        marker = "</p></div></section>"
        if marker not in text:
            raise SystemExit(f"product link marker missing: {path}")
        text = text.replace(marker, f" · {link}</p></div></section>", 1)
        path.write_text(text, encoding="utf-8")
