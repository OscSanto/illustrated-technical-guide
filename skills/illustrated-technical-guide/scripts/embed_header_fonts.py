#!/usr/bin/env python3
"""Inline the header fonts (templates/fonts/*.woff2) into templates/standalone.html as base64 @font-face rules.

The guide must work offline, so fonts are embedded rather than hot-linked. Safe to re-run: it replaces the
previous embedded block. Fonts: Archivo 800, latin subset, Fontsource 5.3.0,
SIL Open Font License 1.1 (licence texts in templates/fonts/).
Usage: python scripts/embed_header_fonts.py
"""
import base64, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "standalone.html"
FONTS = [("Archivo", "normal", 800, "archivo-latin-800-normal.woff2")]
START, END = "/*@HEADER-FONTS-START@*/", "/*@HEADER-FONTS-END@*/"

rules = []
for family, style, weight, name in FONTS:
    data = base64.b64encode((ROOT / "templates" / "fonts" / name).read_bytes()).decode("ascii")
    rules.append(f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};font-display:swap;"
                 f"src:url(data:font/woff2;base64,{data}) format('woff2')}}")
block = START + "\n" + "\n".join(rules) + "\n" + END

html = TEMPLATE.read_text(encoding="utf-8")
if START in html:
    html = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, html, count=1, flags=re.S)
elif "/*@HEADER-FONTS@*/" in html:
    html = html.replace("/*@HEADER-FONTS@*/", block, 1)
else:
    raise SystemExit("no font placeholder in template")
TEMPLATE.write_text(html, encoding="utf-8")
print(f"embedded {len(FONTS)} fonts; template is now {len(html):,} bytes")
