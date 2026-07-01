#!/usr/bin/env python3
"""本地预览：强制 UTF-8 Content-Type，避免中文乱码。"""
import http.server
import socketserver
from pathlib import Path

PORT = 8766
ROOT = Path(__file__).resolve().parent


class Utf8Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".html": "text/html; charset=utf-8",
        ".css": "text/css; charset=utf-8",
        ".js": "application/javascript; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".md": "text/markdown; charset=utf-8",
    }


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Utf8Handler) as httpd:
        print(f"Serving UTF-8 at http://127.0.0.1:{PORT}/")
        print(f"Root: {ROOT}")
        httpd.serve_forever()
