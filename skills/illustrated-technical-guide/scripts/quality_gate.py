#!/usr/bin/env python3
"""v11 profile-aware quality gate. Structural evidence validation, NOT a fact checker.
No third-party dependencies. Generates QUALITY_REPORT.json/QUALITY_REPORT.md.
"""
import argparse, json, csv, re, sys
from pathlib import Path
from html.parser import HTMLParser

class Structure(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[];self.anchors=[];self.figures=[];self.headers=[];self.artifacts=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='a' and a.get('href','').startswith('#'):self.anchors.append(a['href'][1:])
        if tag in ('h2','h3'):self.headers.append(a.get('id'))
        if tag=='figure':self.figures.append(a.get('id'))
        if 'data-artifact-type' in a:self.artifacts.append(a.get('id'))

BADGE_EVIDENCE={'b-pub':'published','b-meas':'measured','b-inf':'inferred','b-self':'self_reported','b-lab':'our_lab'}

def check_claim_badges(html,claims,blockers,warnings):
    """Claim badges (references/reading-design.md): each badge names a real claim whose evidence matches."""
    by_id={c.get('id'):c for c in claims}
    badged=set()
    for m in re.finditer(r'<span\b[^>]*\bclass="([^"]*\bbadge\b[^"]*)"[^>]*>',html):
        tag,classes=m.group(0),m.group(1).split()
        if 'badge' not in classes:continue
        kind=next((c for c in classes if c in BADGE_EVIDENCE),None)
        if 'data-legend' in tag:continue  # badge key or legend entry, not a claim
        cm=re.search(r'\bdata-claim="([^"]+)"',tag)
        if not cm:
            warnings.append(f'Badge without data-claim: {tag}');continue
        cid=cm.group(1)
        if kind is None:blockers.append(f'Badge for claim {cid}: unknown badge class');continue
        claim=by_id.get(cid)
        if claim is None:blockers.append(f'Badge cites unknown claim {cid}');continue
        if claim.get('evidence')!=BADGE_EVIDENCE[kind]:
            blockers.append(f"Badge for claim {cid}: shows {BADGE_EVIDENCE[kind]} but research_inventory says {claim.get('evidence')}")
        badged.add(cid)
    if badged:
        for c in claims:
            if c.get('critical') and c.get('id') not in badged:
                blockers.append(f"Critical claim {c.get('id')}: no badge in the HTML (the guide uses claim badges)")

def check_ledes(html,warnings):
    """Each chapter should open with a short lede paragraph right after its title."""
    for m in re.finditer(r'<section\b[^>]*\bclass="[^"]*\bchapter\b[^"]*"[^>]*\bid="([^"]+)"[^>]*>(.*?)</section>',html,re.S):
        sid,body=m.group(1),m.group(2)
        if sid=='references' or 'refs' in m.group(0)[:200]:continue
        lm=re.search(r'</h2>\s*<p\b[^>]*>(.*?)</p>',body,re.S)
        if not lm:warnings.append(f'Chapter {sid}: no lede paragraph directly after the title');continue
        words=len(re.sub(r'<[^>]+>',' ',lm.group(1)).split())
        if words>60:warnings.append(f'Chapter {sid}: lede is {words} words; keep it to one or two sentences')

def validate(guide):
    guide=Path(guide); blockers=[];warnings=[]; metrics={}
    def require_json(fname):
        path=guide/fname
        try: return json.loads(path.read_text(encoding='utf-8'))
        except (OSError,ValueError) as e:
            blockers.append(f'{fname}: missing/unreadable: {e}'); return {}
    manifest=require_json('guide_manifest.json')
    try:
        html=(guide/'index.html').read_text(encoding='utf-8')
        parser=Structure();parser.feed(html)
    except (OSError,ValueError) as e:
        blockers.append(f'index.html: missing/unreadable: {e}');parser=Structure();html=''
    ids=set(parser.ids)
    if len(parser.ids)!=len(ids):blockers.append('Duplicate HTML IDs')
    for h in parser.headers:
        if not h:blockers.append('Heading missing id')
    for a in parser.anchors:
        if a and a not in ids:blockers.append(f'Broken anchor #{a}')
    title=manifest.get('title')
    if not title:blockers.append('Missing title')
    mode=manifest.get('mode')
    if mode not in ('general','source_audit'):blockers.append('mode must be general or source_audit')
    if not manifest.get('audience'):blockers.append('Missing learner audience')
    objectives=manifest.get('learning_objectives',[])
    if not objectives:blockers.append('No learning objectives')
    chapters=manifest.get('chapters',[])
    if not isinstance(chapters,list):
        blockers.append('guide_manifest.json: chapters must be a list of chapter records, not a count')
        chapters=[]
    if not chapters:blockers.append('No chapters')
    allowed={'hands-on','conceptual','mathematical','source-audit'}
    used=set()
    for c in chapters:
        cid=c.get('id','?');profile=c.get('profile')
        if profile not in allowed:blockers.append(f'{cid}: unsupported teaching profile {profile}')
        used.add(profile)
        if c.get('html_anchor') not in ids:blockers.append(f'{cid}: missing HTML section anchor')
        if not c.get('learning_objective'):blockers.append(f'{cid}: missing chapter learning objective')
        if not c.get('learner_check'):blockers.append(f'{cid}: missing learner checkpoint')
        if profile=='hands-on':
            for field in ('milestones','setup','troubleshooting'):
                if not c.get(field):blockers.append(f'{cid}: hands-on chapter missing {field}')
            for i,m in enumerate(c.get('milestones',[]),1):
                for key in ('action','expected_output','verification','failure_recovery'):
                    if not m.get(key):blockers.append(f'{cid} milestone {i}: missing {key}')
                if m.get('execution_status')!='tested':blockers.append(f'{cid} milestone {i}: execution not verified')
        elif profile=='mathematical':
            for field in ('definitions','worked_example','numerical_check','edge_cases'):
                if not c.get(field):blockers.append(f'{cid}: mathematical chapter missing {field}')
        elif profile=='conceptual':
            for field in ('mechanism_trace','tradeoffs','limitations'):
                if not c.get(field):blockers.append(f'{cid}: conceptual chapter missing {field}')
        elif profile=='source-audit':
            for field in ('source_claim_ids','distinctions','caveats'):
                if not c.get(field):blockers.append(f'{cid}: source-audit chapter missing {field}')
    if mode=='source_audit' and 'source-audit' not in used:
        warnings.append('Source-audit mode has no explicit source-audit chapter; can be valid if source coverage is mapped elsewhere')
    sources=require_json('research_inventory.json')
    if not sources.get('sources'):blockers.append('No research sources')
    for s in sources.get('sources',[]):
        if not s.get('url') or not s.get('locator'):blockers.append(f"Source {s.get('id','?')}: missing URL/locator")
        if s.get('verification')!='verified':warnings.append(f"Source {s.get('id','?')}: not verified")
    for claim in sources.get('claims',[]):
        if claim.get('critical') and claim.get('status')!='verified':blockers.append(f"Critical claim {claim.get('id')}: not verified")
        if claim.get('destination_anchor') not in ids:blockers.append(f"Claim {claim.get('id')}: invalid destination")
    check_claim_badges(html,sources.get('claims',[]),blockers,warnings)
    check_ledes(html,warnings)
    storyboard=require_json('figure_storyboard.json')
    storyboard_ids=set()
    for f in storyboard.get('figures',[]):
        fid=f.get('html_id');storyboard_ids.add(fid)
        if fid not in ids or fid not in parser.figures:blockers.append(f'Figure {fid}: not present as HTML figure')
        for field in ('question','mechanism','caption','provenance'):
            if not f.get(field):blockers.append(f'Figure {fid}: missing {field}')
        if f.get('review_status')!='approved':blockers.append(f'Figure {fid}: technical review pending')
        if f.get('desktop_review')!='passed' or f.get('mobile_review')!='passed':blockers.append(f'Figure {fid}: desktop/mobile review pending')
        if 'animate' not in f:warnings.append(f'Figure {fid}: no animate decision recorded (see references/animated-flow-figures.md)')
    if not parser.figures:blockers.append('No instructional figures in HTML')
    for fid in parser.figures:
        if fid not in storyboard_ids:blockers.append(f'Figure {fid}: missing storyboard entry')
        if fid not in parser.artifacts:blockers.append(f'Figure {fid}: missing data-artifact-type and provenance annotation')
    runlog=require_json('RUN_LOG.json')
    for entry in runlog.get('runs',[]):
        for field in ('command','environment','exit_code','evidence_file'):
            if field not in entry or entry[field] in ('',None):blockers.append(f'Run log missing {field}')
        if 'evidence_file' in entry and not (guide/entry['evidence_file']).exists():blockers.append(f"Run log evidence file missing: {entry['evidence_file']}")
        if entry.get('exit_code')!=0:blockers.append(f"Run command failed: {entry.get('command')}")
    for c in chapters:
        if c.get('profile')=='hands-on' and not runlog.get('runs'):
            blockers.append('Hands-on guide has no executed run log');break
    if manifest.get('review',{}).get('educational')!='approved':blockers.append('Educational review pending')
    if manifest.get('review',{}).get('source_factcheck')!='approved':blockers.append('Source fact-check pending')
    # Always run the existing provenance validator; do not replace it with metadata-only optimism.
    try:
        sys.path.insert(0,str(Path(__file__).resolve().parent))
        from source_fidelity_gate import audit
        provenance=audit(guide,'index.html')
        blockers.extend('Provenance: '+msg for msg in provenance['blockers'])
        declared={a.get('html_id') for a in (json.loads((guide/'artifact_provenance.json').read_text(encoding='utf-8')).get('artifacts',[]))}
        for fid in parser.figures:
            if fid not in declared:blockers.append(f'Figure {fid}: missing provenance manifest entry')
    except Exception as e:blockers.append(f'Could not execute provenance checker: {e}')
    if mode=='source_audit':
        coverage=guide/'source_coverage.csv'
        if not coverage.exists():blockers.append('Missing source_coverage.csv')
        else:
            with coverage.open(newline='',encoding='utf-8') as file:rows=list(csv.DictReader(file))
            if not rows:blockers.append('Empty source coverage')
            for item in rows:
                if not item.get('source_locator') or not item.get('evidence'):blockers.append(f"Source item {item.get('claim_id')}: missing locator/evidence")
                if item.get('critical','').lower()=='true' and item.get('disposition')!='covered':blockers.append(f"Critical source item {item.get('claim_id')}: {item.get('disposition')}")
        if manifest.get('review',{}).get('source_comparison')!='approved':blockers.append('Source-by-source comparison pending')
    metrics.update({'chapters':len(chapters),'html_figures':len(parser.figures),'sources':len(sources.get('sources',[])),'blockers':len(blockers)})
    report={'status':'PASS' if not blockers else 'FAIL','blockers':blockers,'warnings':warnings,'metrics':metrics,'scope':'Structural and recorded-evidence gate. Review flags are declarations, not independent proof of factual accuracy or visual quality.'}
    return report

def main():
    p=argparse.ArgumentParser();p.add_argument('--guide',required=True);args=p.parse_args()
    root=Path(args.guide);result=validate(root)
    root.mkdir(exist_ok=True,parents=True)
    (root/'QUALITY_REPORT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    lines=[f"# Quality gate: {result['status']}", '', '## Blockers']+['- '+v for v in result['blockers']]+['','## Warnings']+['- '+v for v in result['warnings']]
    (root/'QUALITY_REPORT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f"{result['status']}: {len(result['blockers'])} blockers, {len(result['warnings'])} warnings")
    return 0 if result['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
