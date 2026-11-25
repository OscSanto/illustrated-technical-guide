from bs4 import BeautifulSoup
from pathlib import Path
import sys
p=Path(sys.argv[1]);s=BeautifulSoup(p.read_text(),"html.parser")
e=s.select(".equation")
assert len(e)>=4, "Expected display equations"
for i,x in enumerate(e,1):
 assert x.get("data-tex") and x.find("svg") and x.find("mjx-container"),f"Equation {i} missing rendered SVG or source"
 assert x.get("aria-label"),f"Equation {i} missing accessibility label"
 assert "<svg" in str(x),f"Equation {i} not typeset"
print(f"PASS: {len(e)} embedded, accessible, offline vector equations")
