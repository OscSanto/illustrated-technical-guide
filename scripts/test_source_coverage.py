from pathlib import Path
from bs4 import BeautifulSoup
import csv, subprocess, sys
root=Path(__file__).resolve().parents[1]
s=BeautifulSoup((root/'examples/meddecider-guide.html').read_text(), 'html.parser')
ledger=list(csv.DictReader((root/'source_coverage.csv').open()))
ids={x.get('id') for x in s.find_all(id=True)}
missing=[a.get('href') for a in s.select('a[href^="#"]') if a.get('href')[1:] not in ids]
assert not missing,missing
assert len(s.select('.chapter'))==14
assert len(s.select('figure'))>=10
assert all(x['status']=='covered' for x in ledger if x['critical']=='yes')
for x in ledger:
 assert x['evidence'] in s.get_text(' ',strip=True), x['claim_id']
assert len(ledger)>=15
subprocess.run([sys.executable,str(root/'examples/reproduction_demo.py')],check=True)
print(f'PASS: {len(ledger)} source claims accounted for; {len(s.select(".chapter"))} chapters; {len(s.select("figure"))} figures; all anchors; numerical lab')
