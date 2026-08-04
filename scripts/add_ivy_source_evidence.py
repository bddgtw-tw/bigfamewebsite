"""Add source-file provenance to the multilingual IVY system record pages."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "tw": {
        "heading": "來源文件與判讀",
        "body": "本頁內容可回溯至「[25x40展示系統] 新增 Microsoft Word 文件.docx」與「[25x40展示系統] 2019.12.16 IVY 樣品.pdf」。前者記錄 IVY 壁面陳列系統的設計問題與製造／運輸／安裝／維護方向；後者記錄 25×40 系統、600 mm 組合尺寸、M6 組裝與元件圖面。",
        "boundary": "本頁的可核對成果是系統設計與樣品圖面紀錄，不是特定客戶已安裝、量產數量或最終交付證明；正式製作仍以最新核准圖面與專案條件為準。",
    },
    "en": {
        "heading": "Source files and interpretation",
        "body": "This page can be traced to “[25x40展示系統] 新增 Microsoft Word 文件.docx” and “[25x40展示系統] 2019.12.16 IVY 樣品.pdf”. The first records the IVY wall-display problem and the manufacturing, transport, installation and maintenance direction; the second records the 25×40 system, 600 mm module dimension, M6 assembly and component drawings.",
        "boundary": "The verifiable output here is a system-development and sample-drawing record—not proof of installation for a named client, production quantity or final delivery. Formal production remains subject to the latest approved drawings and project conditions.",
    },
    "jp": {
        "heading": "資料と判読範囲",
        "body": "本ページは「[25x40展示系統] 新增 Microsoft Word 文件.docx」と「[25x40展示系統] 2019.12.16 IVY 樣品.pdf」に基づきます。前者にはIVY壁面陳列システムの課題と製造・輸送・設置・メンテナンスの方向が、後者には25×40システム、600 mmの組合せ寸法、M6組立、各部品図面が記録されています。",
        "boundary": "確認できる成果はシステム開発とサンプル図面の記録であり、特定顧客への設置、量産数量、最終納品を証明するものではありません。正式な製作は最新承認図面と案件条件に基づきます。",
    },
}


def main() -> None:
    changed = 0
    for language, copy in PAGES.items():
        for relative in (
            f"{language}/case-ivy-modular-system.html",
            f"{language}/case-ivy-modular-system/index.html",
        ):
            path = ROOT / relative
            text = path.read_text(encoding="utf-8")
            if "Source files and interpretation" in text or "來源文件與判讀" in text or "資料と判読範囲" in text:
                continue
            marker = '<section class="section section-light" data-bf-faq="1">'
            if marker not in text:
                raise SystemExit(f"FAQ marker not found: {relative}")
            section = (
                '<section class="section section-light"><div class="container"><div class="section-heading reveal">'
                f'<span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">{copy["heading"]}</h2></div>'
                f'<div class="grid-2"><article class="location-card reveal"><h3>可追溯來源</h3><p>{copy["body"]}</p></article>'
                f'<article class="location-card reveal"><h3>證據邊界</h3><p>{copy["boundary"]}</p></article></div>'
                '<p class="section-note reveal"><a href="../technical-resources">索取技術／CAD 資料</a> · <a href="../contact?role=designer&category=system_fixtures">提出類似需求</a></p></div></section>'
            )
            if language == "en":
                section = section.replace('可追溯來源', 'Traceable sources').replace('證據邊界', 'Evidence boundary').replace('索取技術／CAD 資料', 'Request technical / CAD information').replace('提出類似需求', 'Discuss a similar requirement')
            elif language == "jp":
                section = section.replace('可追溯來源', '追跡できる資料').replace('證據邊界', '証拠の範囲').replace('索取技術／CAD 資料', '技術資料・CADを相談').replace('提出類似需求', '類似要件を相談する')
            text = text.replace(marker, section + marker, 1)
            path.write_text(text, encoding="utf-8", newline="")
            changed += 1
    print(f"Updated {changed} IVY pages with source provenance.")


if __name__ == "__main__":
    main()
