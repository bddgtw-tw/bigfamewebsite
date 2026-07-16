#!/usr/bin/env python3
"""Serve the Big Fame site locally with Traditional Chinese clean URLs."""

from __future__ import annotations

import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent
TW_PAGES = {
    "index.html",
    "about.html",
    "products.html",
    "services.html",
    "applications.html",
    "contact.html",
}


class BigFameHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path: str) -> str:
        clean_path = unquote(urlsplit(path).path).lstrip("/")
        if clean_path in TW_PAGES and clean_path != "index.html":
            return str(ROOT / "tw" / clean_path)
        return super().translate_path(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8085)
    args = parser.parse_args()
    handler = lambda *values, **kwargs: BigFameHandler(*values, directory=str(ROOT), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    print(f"Big Fame local preview: http://localhost:{args.port}/about.html")
    server.serve_forever()


if __name__ == "__main__":
    main()
