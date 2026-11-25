#!/usr/bin/env python3
"""Static audit for standalone illustrated guide HTML. Requires beautifulsoup4."""
import sys, re
from pathlib import Path
from collections import Counter
from bs4 import BeautifulSoup

def audit(path):
    raw=Path(path).read_text(encoding='utf-8')
    soup=BeautifulSoup(raw,'html.parser')
    problems=[]; warnings=[]
    ids=[x['id'] for x in soup.select('[id]')]
    for ident,count in Counter(ids).items():
        if count>1: problems.append(f'Duplicate id: {ident}')
    if len(soup.select('h1'))!=1: problems.append('Must have exactly one h1')
    sections=soup.select('article.content > section') or soup.select('article section')
    headings=soup.select('h2,h3')
    for h in headings:
        if not h.get('id') and not h.find_parent(id=True):
            warnings.append(f'Heading without anchor: {h.get_text(" ",strip=True)[:60]}')
    for link in soup.select('a[href^="#"]'):
        target=link['href'][1:]
        if target and target not in ids: problems.append(f'Broken anchor: #{target}')
    figs=soup.select('figure')
    for i,f in enumerate(figs,1):
        if not f.select_one('figcaption'): problems.append(f'Figure {i} missing caption')
        svg=f.select_one('svg')
        if svg and not (svg.get('aria-label') or svg.select_one('title')):
            warnings.append(f'Figure {i} SVG lacks accessible description')
    if re.search(r'\bTODO\b|lorem ipsum|chapter slot',soup.get_text(' ',strip=True),re.I):
        warnings.append('Potential placeholder text')
    if re.search(r'<(?:script|link)[^>]+(?:src|href)=["\']https?://',raw,re.I):
        warnings.append('External script or stylesheet dependency; not fully offline')
    print(f'Chapters/sections: {len(sections)} | h2/h3: {len(headings)} | figures: {len(figs)} | anchors: {len(ids)}')
    for p in problems: print('ERROR:',p)
    for w in warnings: print('WARN:',w)
    print('PASS static structure' if not problems else 'FAIL static structure')
    return int(bool(problems))

if __name__=='__main__':
    if len(sys.argv)!=2: print('Usage: validate_guide.py index.html'); sys.exit(2)
    sys.exit(audit(sys.argv[1]))
