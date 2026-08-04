"""Add source-file provenance to the multilingual Urban Warehouse case pages."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COPY = {
    "tw": ("來源文件與判讀", "可追溯來源", "證據邊界", "本頁可回溯至「Urban Warehouse Self Storage／來源_UrbanWarehouse／長敘述.docx」。文件直接記錄城市儲物需求、可複製的迷你儲物單元、超過 50 個元件、約 3.4 m³ 標準單元、鋼板／鋼管／鋼線、客製粉體塗裝、K/D 結構、帶門單元與雙層儲物櫃；原文並記錄空間已開放使用與可複製到其他城市。", "這些內容是原始專案敘述可支持的設計、系統與使用結果；客戶授權、Big Fame 正式合約分工、最終數量、交期、交付地、包裝與公開成果數據未被核准，因此不在此頁推定。", "索取模組化儲物／金屬結構資料"),
    "en": ("Source files and interpretation", "Traceable source", "Evidence boundary", "This page can be traced to “Urban Warehouse Self Storage / 來源_UrbanWarehouse / 長敘述.docx”. The source directly records urban storage demand, repeatable mini-storage units, more than 50 components, an approximately 3.4 m³ standard unit, steel plate / tube / wire, custom powder-coat direction, knock-down structure, lockable units and double-layer storage cabinets; it also records that the space was opened for use and could be replicated in other cities.", "These are design, system and use-result details supported by the source brief. Client authorization, Big Fame contract scope, final quantity, lead time, destination, packing and public performance data are not approved, so they are not inferred here.", "Request modular storage / metal-structure information"),
    "jp": ("資料と判読範囲", "追跡できる資料", "証拠の範囲", "本ページは「Urban Warehouse Self Storage／來源_UrbanWarehouse／長敘述.docx」に基づきます。資料には都市型収納の需要、複製可能なミニ収納ユニット、50を超える部品、約3.4 m³の標準ユニット、鋼板・鋼管・鋼線、カスタム粉体塗装、K/D構造、扉付きユニット、二層収納が記録されています。また、空間が利用開始され、他都市へ複製できる方向も記録されています。", "これらは資料が支持する設計・システム・利用結果です。顧客許諾、Big Fameの正式な契約範囲、最終数量、納期、納品先、梱包、公開成果数値は承認されていないため推測しません。", "モジュール収納・金属構造資料を相談する"),
}


def main() -> None:
    changed = 0
    for language, (heading, source_label, boundary_label, body, boundary, link_text) in COPY.items():
        for relative in (f"{language}/case-urban-storage.html", f"{language}/case-urban-storage/index.html"):
            path = ROOT / relative
            text = path.read_text(encoding="utf-8")
            if "Urban Warehouse Self Storage／來源_UrbanWarehouse" in text:
                continue
            marker = '<section class="section section-light" data-bf-faq="1">'
            if marker not in text:
                raise SystemExit(f"FAQ marker not found: {relative}")
            section = (
                '<section class="section section-light"><div class="container"><div class="section-heading reveal">'
                f'<span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">{heading}</h2></div>'
                f'<div class="grid-2"><article class="location-card reveal"><h3>{source_label}</h3><p>{body}</p></article>'
                f'<article class="location-card reveal"><h3>{boundary_label}</h3><p>{boundary}</p></article></div>'
                f'<p class="section-note reveal"><a href="../technical-resources">{link_text}</a> · <a href="../contact?role=designer&category=system_fixtures">開始類似需求討論</a></p></div></section>'
            )
            if language == "en":
                section = section.replace("開始類似需求討論", "Discuss a similar requirement")
            elif language == "jp":
                section = section.replace("開始類似需求討論", "類似要件を相談する")
            text = text.replace(marker, section + marker, 1)
            path.write_text(text, encoding="utf-8", newline="")
            changed += 1
    print(f"Updated {changed} Urban Warehouse pages with source provenance.")


if __name__ == "__main__":
    main()
