#!/usr/bin/env python3
"""Fail-closed editorial publication gate. No network or browser needed for structural checks."""
import argparse,csv,json,re,sys
from pathlib import Path
from html.parser import HTMLParser
class Parser(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.links=[];self.figures=[];self.headings=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a' and a.get('href','').startswith('#'):self.links.append(a['href'][1:])
  if tag=='figure':self.figures.append(a.get('id',''))
  if tag in ('h2','h3'):self.headings.append(a.get('id',''))
def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--html',required=True);args=p.parse_args()
 root=Path(args.root);errors=[];warnings=[];metrics={}
 def readj(name):
  try:return json.loads((root/name).read_text())
  except Exception as e:errors.append(f'{name}: unreadable ({e})');return {}
 hpath=root/args.html
 try: h=hpath.read_text();parser=Parser();parser.feed(h)
 except Exception as e:errors.append(f'HTML unreadable: {e}');parser=Parser()
 idset=set(parser.ids);metrics.update({'html_ids':len(parser.ids),'figures_in_html':len(parser.figures),'headings':len(parser.headings)})
 if len(parser.ids)!=len(idset):errors.append('Duplicate HTML IDs')
 for x in parser.links:
  if x and x not in idset:errors.append(f'Broken anchor #{x}')
 for x in parser.headings:
  if not x:errors.append('Heading missing id')
 inv=readj('research_inventory.json');sources={s.get('id') for s in inv.get('sources',[])}
 if not inv.get('sources'):errors.append('No research sources')
 for s in inv.get('sources',[]):
  if not s.get('url') or not s.get('title'):errors.append('Source missing URL/title')
  if s.get('verified') is not True:warnings.append(f"Source {s.get('id')} not independently verified")
 for c in inv.get('claims',[]):
  ident=c.get('id','?')
  if c.get('source_id') not in sources:errors.append(f'{ident}: unknown source')
  if not c.get('source_locator'):errors.append(f'{ident}: missing source locator')
  if c.get('verification')!='verified':errors.append(f'{ident}: claim not verified')
  if c.get('status')!='covered':errors.append(f'{ident}: not fully covered')
  if not c.get('destination_anchor') or c.get('destination_anchor') not in idset:errors.append(f'{ident}: missing/invalid HTML destination')
 if not inv.get('claims'):errors.append('No claim inventory')
 matrix=readj('chapter_matrix.json');chapters=matrix.get('chapters',[])
 if not chapters:errors.append('No chapter coverage matrix')
 required=['prerequisites','problem','intuition','diagram_figure_id','variables_and_shapes','derivation','numerical_trace','implementation','tests','limitations']
 for c in chapters:
  ident=c.get('id','?')
  if not c.get('html_anchor') or c['html_anchor'] not in idset:errors.append(f'{ident}: missing HTML anchor')
  for field in required:
   v=c.get(field)
   if not v or (isinstance(v,str) and len(v.strip())<8):errors.append(f'{ident}: missing {field}')
  if c.get('tests_run') is not True:errors.append(f'{ident}: code/tests not executed')
  if c.get('review_status')!='approved':errors.append(f'{ident}: educational review pending')
 story=readj('figure_storyboard.json');figures=story.get('figures',[])
 if not figures:errors.append('No figure storyboard')
 for f in figures:
  ident=f.get('id','?');fid=f.get('html_figure_id','')
  if not fid or fid not in idset:errors.append(f'{ident}: figure not linked to HTML ID')
  for field in ['question','answer','visual_grammar','data_provenance','adjacent_explanation_anchor','caption']:
   if not f.get(field):errors.append(f'{ident}: missing {field}')
  if not f.get('technical_labels'):errors.append(f'{ident}: missing technical labels')
  if f.get('desktop_review')!='passed' or f.get('mobile_review')!='passed':errors.append(f'{ident}: desktop/mobile screenshot review incomplete')
  if f.get('review_status')!='approved':errors.append(f'{ident}: figure instructional review pending')
 if inv.get('mode')=='source_audit':
  f=root/'source_coverage.csv'
  if not f.exists():errors.append('Missing source_coverage.csv')
  else:
   rows=list(csv.DictReader(f.open()));metrics['source_ledger_rows']=len(rows)
   if not rows:errors.append('Empty source coverage ledger')
   for r in rows:
    if r.get('status')!='covered':errors.append(f"{r.get('claim_id')}: source ledger not covered")
    if not r.get('source_url') or not r.get('evidence'):errors.append(f"{r.get('claim_id')}: missing provenance")
 # v10: independent provenance and source-fidelity structural audit.
 try:
  from source_fidelity_gate import audit as fidelity_audit
  fidelity=fidelity_audit(root,args.html)
  metrics['provenance_artifacts']=fidelity['metrics'].get('artifacts',0)
  errors.extend('Provenance: '+e for e in fidelity['blockers'])
 except Exception as e:
  errors.append(f'Provenance gate could not run: {e}')
 report={'status':'PASS' if not errors else 'FAIL','metrics':metrics,'blockers':errors,'warnings':warnings,'scope':'Static checks plus self-reported review fields. Independent fact-check and screenshot inspection required.'}
 (root/'PUBLICATION_REPORT.json').write_text(json.dumps(report,indent=2))
 (root/'PUBLICATION_REPORT.md').write_text('# Publication gate: '+report['status']+'\n\n'+'\n'.join('- '+e for e in errors)+'\n\n## Warnings\n'+'\n'.join('- '+e for e in warnings)+'\n')
 print(f"{report['status']}: {len(errors)} blockers, {len(warnings)} warnings; report at {root/'PUBLICATION_REPORT.md'}")
 for e in errors[:12]:print(' -',e)
 return int(bool(errors))
if __name__=='__main__':sys.exit(main())
