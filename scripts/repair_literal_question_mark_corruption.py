from pathlib import Path


REPLACEMENTS = {
    Path("tw/display-hooks.html"): {
        '"name":"?????????"': '"name":"展示掛勾與陳列五金"',
    },
    Path("tw/design-support.html"): {
        '"name":"?????????????"': '"name":"零售空間展示系統與設計支援"',
    },
    Path("tw/procurement.html"): {
        '"name":"??????????"': '"name":"台灣店面展示設備採購"',
    },
    Path("jp/display-hooks.html"): {
        '"name":"????????????????"': '"name":"ディスプレイフック・店舗什器金物"',
        '"serviceType":"????????????????"': '"serviceType":"ディスプレイフック・店舗什器金物"',
    },
    Path("jp/design-support.html"): {
        '"name":"???????????????????"': '"name":"店舗什器・ディスプレイシステム設計支援"',
        '"serviceType":"???????????????????"': '"serviceType":"店舗什器・ディスプレイシステム設計支援"',
    },
    Path("jp/procurement.html"): {
        '"name":"?????????????????"': '"name":"台湾の店舗什器・ディスプレイ金具の購買"',
        '"serviceType":"??????????????????"': '"serviceType":"店舗什器・ディスプレイ金具の購買相談"',
    },
    Path("tw/case-ivy-modular-system.html"): {
        '<p class="section-note reveal">???????<a href="../modular-fixtures">??????</a> ? <a href="../custom-metal-parts">??????</a></p>': '<p class="section-note reveal">相關能力：<a href="../modular-fixtures">模組化展示架</a> · <a href="../custom-metal-parts">客製金屬零件</a></p>',
    },
    Path("tw/case-boutique-hotel-furniture.html"): {
        '<p class="section-note reveal">???????<a href="../custom-metal-parts">??????</a> ? <a href="../modular-fixtures">??????</a></p>': '<p class="section-note reveal">相關能力：<a href="../custom-metal-parts">客製金屬零件</a> · <a href="../modular-fixtures">模組化展示架</a></p>',
    },
    Path("jp/case-ivy-modular-system.html"): {
        '<p class="section-note reveal">????????<a href="../modular-fixtures">???????</a> ? <a href="../custom-metal-parts">????????</a></p>': '<p class="section-note reveal">関連する能力：<a href="../modular-fixtures">モジュール什器</a> · <a href="../custom-metal-parts">カスタム金属部品</a></p>',
    },
    Path("jp/case-boutique-hotel-furniture.html"): {
        '<p class="section-note reveal">?????????<a href="../custom-metal-parts">????????</a> ? <a href="../modular-fixtures">???????</a></p>': '<p class="section-note reveal">関連する能力：<a href="../custom-metal-parts">カスタム金属部品</a> · <a href="../modular-fixtures">モジュール什器</a></p>',
    },
    Path("tw/case-headphone-display-set.html"): {'href=""': 'href="./"'},
    Path("tw/case-hair-display-spinner-engineering.html"): {'href=""': 'href="./"'},
    Path("tw/case-retail-fixture-procurement-integration.html"): {'href=""': 'href="./"'},
    Path("tw/case-automotive-parts-rack.html"): {'href=""': 'href="./"'},
    Path("en/case-retail-fixture-procurement-integration.html"): {'href=""': 'href="./"'},
    Path("en/case-hair-display-spinner-engineering.html"): {'href=""': 'href="./"'},
    Path("en/case-headphone-display-set.html"): {'href=""': 'href="./"'},
    Path("en/case-automotive-parts-rack.html"): {'href=""': 'href="./"'},
    Path("jp/case-retail-fixture-procurement-integration.html"): {'href=""': 'href="./"'},
    Path("jp/case-hair-display-spinner-engineering.html"): {'href=""': 'href="./"'},
    Path("jp/case-headphone-display-set.html"): {'href=""': 'href="./"'},
    Path("jp/case-automotive-parts-rack.html"): {'href=""': 'href="./"'},
}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    changed = 0
    for relative_path, replacements in REPLACEMENTS.items():
        path = root / relative_path
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in replacements.items():
            count = text.count(old)
            expected = 1 if old != 'href=""' else 2
            if count not in (0, expected):
                raise RuntimeError(f"{relative_path}: expected {expected} matches, found {count}: {old}")
            if count:
                text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8", newline="")
            changed += 1
            print(relative_path)
    print(f"CHANGED_FILES={changed}")


if __name__ == "__main__":
    main()
