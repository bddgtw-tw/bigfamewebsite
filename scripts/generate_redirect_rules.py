"""Generate explicit clean-route rewrites for static-host compatibility."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
lines = [
    "/overview /en/about 301",
    "/overview/ /en/about 301",
    "/contact-us /en/contact 301",
    "/contact-us/ /en/contact 301",
    "/tw/overview /tw/about 301",
    "/tw/overview/ /tw/about 301",
    "/tw/contact-us /tw/contact 301",
    "/tw/contact-us/ /tw/contact 301",
    "/en/overview /en/about 301",
    "/en/overview/ /en/about 301",
    "/en/contact-us /en/contact 301",
    "/en/contact-us/ /en/contact 301",
    "/jp/overview /jp/about 301",
    "/jp/overview/ /jp/about 301",
    "/jp/contact-us /jp/contact 301",
    "/jp/contact-us/ /jp/contact 301",
    "/thank-you-page /en/contact 301",
    "/thank-you-page/ /en/contact 301",
    "/our-works /en/applications 301",
    "/our-works/ /en/applications 301",
    "/know-how /en/services 301",
    "/know-how/ /en/services 301",
    "/blog /en/applications 301",
    "/blog/ /en/applications 301",
    "/blog/author/benny /en/about 301",
    "/blog/author/benny/ /en/about 301",
    "/blog/retail-fixture-blog /en/display-hooks 301",
    "/blog/retail-fixture-blog/ /en/display-hooks 301",
]
(ROOT / "_redirects").write_text("\n".join(lines) + "\n", encoding="utf-8")
