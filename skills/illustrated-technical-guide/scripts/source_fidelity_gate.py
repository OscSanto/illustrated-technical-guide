#!/usr/bin/env python3
"""Source fidelity and artifact provenance gate (v10). Fail closed on missing provenance.
Checks manifest-to-HTML links and declarations; does NOT fact-check source claims.
"""
import argparse, json, re, sys
from html.parser import HTMLParser
from pathlib import Path

KINDS={'source_reproduction','source_adaptation','independent_verification','our_derivation','our_implementation','hypothetical_example','unverified'}
TYPES={'code','pseudocode','equation','figure','architecture','benchmark','api_example','claim','table','dataset'}
STATUSES={'verified','tested','unverified','not_tested','reported','derived','illustrative'}
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.nodes={};self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):
   self.ids.append(a['id']);self.nodes[a['id']]={'tag':tag,'attrs':a}

def audit(root,html,manifest='artifact_provenance.json'):
 errors=[];warnings=[]
 try: data=json.loads((root/manifest).read_text(encoding='utf-8'))
 except Exception as e:return {'status':'FAIL','blockers':[f'Missing/unreadable provenance manifest: {e}'],'warnings':[],'metrics':{}}
 try:p=Parse();p.feed((root/html).read_text(encoding='utf-8'))
 except Exception as e:return {'status':'FAIL','blockers':[f'HTML unreadable: {e}'],'warnings':[],'metrics':{}}
 if len(p.ids)!=len(set(p.ids)):errors.append('Duplicate HTML IDs')
 arts=data.get('artifacts',[])
 if not arts:errors.append('No artifact provenance entries')
 seen=set();covered=set()
 for a in arts:
  ident=a.get('id','?');kind=a.get('origin');typ=a.get('type');status=a.get('verification_status')
  if ident in seen:errors.append(f'{ident}: duplicate manifest artifact ID')
  seen.add(ident)
  if kind not in KINDS:errors.append(f'{ident}: invalid/missing origin')
  if typ not in TYPES:errors.append(f'{ident}: invalid/missing artifact type')
  if status not in STATUSES:errors.append(f'{ident}: invalid/missing verification_status')
  anchor=a.get('html_id','')
  if anchor not in p.nodes:errors.append(f'{ident}: missing HTML artifact #{anchor}')
  else:
   covered.add(anchor);node=p.nodes[anchor]
   if node['attrs'].get('data-origin')!=kind:errors.append(f'{ident}: HTML data-origin disagrees with manifest')
   if node['attrs'].get('data-verification')!=status:errors.append(f'{ident}: HTML data-verification disagrees with manifest')
  if not a.get('visible_label') or not a.get('visible_label_in_html',False):errors.append(f'{ident}: missing visible origin label or evidence of label')
  # A text search is an additional guard against falsely declaring visible_label_in_html=true.
  if a.get('visible_label') and a['visible_label'] not in (root/html).read_text(encoding='utf-8'):errors.append(f'{ident}: declared visible label not present in HTML')
  if not a.get('explanation'):errors.append(f'{ident}: missing provenance explanation')
  if kind in {'source_reproduction','source_adaptation','independent_verification'}:
   if not a.get('source_url') or not a.get('source_locator'):errors.append(f'{ident}: source origin lacks precise URL/locator')
  if kind=='source_adaptation' and not a.get('adaptation_notes'):errors.append(f'{ident}: adaptation lacks change log')
  if kind in {'our_derivation','our_implementation','hypothetical_example'} and a.get('attributed_to_source') is True:errors.append(f'{ident}: original work incorrectly attributed to source')
  if kind=='unverified' and status in {'verified','tested'}:errors.append(f'{ident}: unverified origin marked verified/tested')
  if typ=='pseudocode' and not a.get('is_pseudocode',False):errors.append(f'{ident}: pseudocode not explicitly classified')
  if typ=='api_example':
   if status in {'verified','tested'}:
    if not all(a.get(k) for k in ('api_docs_url','api_version','endpoint','verification_evidence')):errors.append(f'{ident}: API marked verified without docs/version/endpoint/evidence')
   elif 'unverified' not in a.get('visible_label','').lower() and 'hypothetical' not in a.get('visible_label','').lower():errors.append(f'{ident}: unverified API lacks visible warning')
  if typ=='architecture' and a.get('system_is_proprietary') and not a.get('internal_mechanism_publicly_documented'):
   if kind in {'source_reproduction','independent_verification'}:errors.append(f'{ident}: proprietary internals claimed documented without evidence')
   if 'conceptual' not in a.get('visible_label','').lower() and 'hypothetical' not in a.get('visible_label','').lower():errors.append(f'{ident}: conceptual proprietary architecture needs explicit label')
  if typ=='benchmark':
   if a.get('result_kind') not in {'source_reported','independently_reproduced','synthetic'}:errors.append(f'{ident}: benchmark must distinguish reported/reproduced/synthetic')
   if a.get('result_kind')=='independently_reproduced' and not all(a.get(k) for k in ('run_log','environment','sample_size')):errors.append(f'{ident}: reproduced benchmark lacks run evidence')
   if a.get('result_kind')=='source_reported' and not a.get('source_url'):errors.append(f'{ident}: reported benchmark lacks source')
  if typ in {'code','pseudocode'} and status=='tested' and not a.get('run_log'):errors.append(f'{ident}: tested code missing run log')
 # Every annotated artifact in HTML must appear in the manifest; catch omissions.
 for anchor,node in p.nodes.items():
  if 'data-artifact-type' in node['attrs'] and anchor not in covered:errors.append(f'HTML artifact #{anchor} absent from provenance manifest')
 if data.get('mode')=='source_audit':
  inventory=data.get('source_coverage',[])
  if not inventory:errors.append('Source-audit mode requires explicit source_coverage entries')
  for item in inventory:
   if not all(item.get(k) for k in ('source_id','source_locator','topic','disposition')):errors.append('Incomplete source coverage entry')
   if item.get('disposition') not in {'covered','partial','omitted','unverifiable','contradicted'}:errors.append(f"{item.get('source_id')}: invalid coverage disposition")
   if item.get('critical') and item.get('disposition')!='covered':errors.append(f"{item.get('source_id')}: critical source content not faithfully covered")
  if not data.get('inventory_scope'):errors.append('Source audit lacks inventory scope statement')
 return {'status':'FAIL' if errors else 'PASS','blockers':errors,'warnings':warnings,'metrics':{'artifacts':len(arts),'source_topics':len(data.get('source_coverage',[]))},'scope':'Structural provenance validation only. Original source fidelity and semantic correctness require independent review.'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',default='.');ap.add_argument('--html',required=True);ap.add_argument('--manifest',default='artifact_provenance.json');args=ap.parse_args()
 root=Path(args.root);report=audit(root,args.html,args.manifest)
 (root/'FIDELITY_REPORT.json').write_text(json.dumps(report,indent=2))
 (root/'FIDELITY_REPORT.md').write_text('# Source fidelity gate: '+report['status']+'\n\n'+ '\n'.join('- '+x for x in report['blockers'])+'\n\n'+report['scope']+'\n')
 print(f"{report['status']}: {len(report['blockers'])} provenance blockers")
 return int(report['status']!='PASS')
if __name__=='__main__':sys.exit(main())
