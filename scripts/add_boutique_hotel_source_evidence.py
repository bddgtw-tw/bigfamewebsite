"""Add source-file provenance to the multilingual boutique-hotel case pages."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COPY = {
    "tw": {
        "heading": "來源文件與判讀",
        "source_label": "可追溯來源",
        "boundary_label": "證據邊界",
        "body": "本頁可回溯至「Bespoke_Hotel_Room_Furniture／長敘述 250字體.docx」與同內容的「Delighting Bespoked Hotel Room Furniture／長敘述 250字體.docx」。文件直接記錄台北市中心 28 房精品旅宿、六層樓概念、衣櫃、飲料迷你吧、書桌、邊桌、床頭板與床架，以及 expanded mesh 搭配 wood、pipe、lighting、pattern 的方向。",
        "boundary": "文件描述的是專案設計與家具發展內容；正式客戶授權、Big Fame 合約分工、數量、價格、交付地、交期與最終成果未在來源中核准，因此本頁不把它寫成完整交付數據。",
        "link_text": "索取旅宿家具技術／CAD 資料",
    },
    "en": {
        "heading": "Source files and interpretation",
        "source_label": "Traceable sources",
        "boundary_label": "Evidence boundary",
        "body": "This page can be traced to “Bespoke_Hotel_Room_Furniture / 長敘述 250字體.docx” and the same brief under “Delighting Bespoked Hotel Room Furniture / 長敘述 250字體.docx”. The documents directly record a 28-room boutique hotel in central Taipei, a six-floor concept, wardrobe, beverage minibar, writing desk, side table, bed headboard and bedframe, plus expanded mesh combined with wood, pipe, lighting and pattern.",
        "boundary": "The documents describe project design and furniture development content. Client authorization, Big Fame contract scope, quantity, price, destination, lead time and final outcomes are not approved in the source, so this page does not present them as completed-delivery data.",
        "link_text": "Request hospitality furniture technical / CAD information",
    },
    "jp": {
        "heading": "資料と判読範囲",
        "source_label": "追跡できる資料",
        "boundary_label": "証拠の範囲",
        "body": "本ページは「Bespoke_Hotel_Room_Furniture／長敘述 250字體.docx」と、同じ内容の「Delighting Bespoked Hotel Room Furniture／長敘述 250字體.docx」に基づきます。資料には台北中心部の28室のブティックホテル、6階層のコンセプト、ワードローブ、ミニバー、デスク、サイドテーブル、ヘッドボード、ベッドフレーム、さらにexpanded meshと木・パイプ・照明・パターンの組合せが記録されています。",
        "boundary": "資料はプロジェクトのデザインと家具開発内容を記録しています。顧客許諾、Big Fameの契約範囲、数量、価格、納品先、納期、最終成果は承認されていないため、完成納品データとして表示しません。",
        "link_text": "ホテル家具の技術資料・CADを相談する",
    },
}


def main() -> None:
    changed = 0
    for language, copy in COPY.items():
        for relative in (
            f"{language}/case-boutique-hotel-furniture.html",
            f"{language}/case-boutique-hotel-furniture/index.html",
        ):
            path = ROOT / relative
            text = path.read_text(encoding="utf-8")
            if "Bespoke_Hotel_Room_Furniture" in text:
                continue
            marker = '<section class="section section-light" data-bf-faq="1">'
            if marker not in text:
                raise SystemExit(f"FAQ marker not found: {relative}")
            section = (
                '<section class="section section-light"><div class="container"><div class="section-heading reveal">'
                f'<span class="section-subtitle">SOURCE RECORD</span><h2 class="section-title">{copy["heading"]}</h2></div>'
                f'<div class="grid-2"><article class="location-card reveal"><h3>{copy["source_label"]}</h3><p>{copy["body"]}</p></article>'
                f'<article class="location-card reveal"><h3>{copy["boundary_label"]}</h3><p>{copy["boundary"]}</p></article></div>'
                f'<p class="section-note reveal"><a href="../technical-resources">{copy["link_text"]}</a> · <a href="../contact?role=designer&category=system_fixtures">開始類似需求討論</a></p></div></section>'
            )
            if language == "en":
                section = section.replace("開始類似需求討論", "Discuss a similar requirement")
            elif language == "jp":
                section = section.replace("開始類似需求討論", "類似要件を相談する")
            text = text.replace(marker, section + marker, 1)
            path.write_text(text, encoding="utf-8", newline="")
            changed += 1
    print(f"Updated {changed} boutique-hotel pages with source provenance.")


if __name__ == "__main__":
    main()
