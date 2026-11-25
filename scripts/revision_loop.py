#!/usr/bin/env python3
"""Evidence-aware publication gate wrapper; does not fabricate approvals."""
import argparse,subprocess,json,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--html',default='index.html');a=p.parse_args();root=Path(a.root).resolve()
gate=Path(__file__).with_name('publication_gate.py')
r=subprocess.run([sys.executable,str(gate),'--root',str(root),'--html',a.html],capture_output=True,text=True)
report=json.loads((root/'PUBLICATION_REPORT.json').read_text())
runlog=root/'RUN_LOG.json'
if not runlog.exists():runlog.write_text(json.dumps({'engine':'PostgreSQL','execution':'UNVERIFIED','reason':'No PostgreSQL server confirmed in build environment','commands':[],'screenshots':[],'visual_review':'UNVERIFIED'},indent=2))
log=json.loads(runlog.read_text());extra=[]
if log.get('execution')!='PASSED':extra.append('Target-engine SQL execution unverified')
if log.get('visual_review')!='PASSED':extra.append('Independent figure-by-figure visual review unverified')
report['blockers']+=extra
report['status']='FAIL' if report['blockers'] else 'PASS'
report['evidence_contract']=log
(root/'PUBLICATION_REPORT.json').write_text(json.dumps(report,indent=2))
(root/'PUBLICATION_REPORT.md').write_text('# Publication gate: '+report['status']+'\n\n'+ '\n'.join('- '+x for x in report['blockers'])+'\n\n## Evidence\n'+json.dumps(log,indent=2)+'\n')
print(report['status'],len(report['blockers']),'blockers; no automatic approvals')
sys.exit(0 if report['status']=='PASS' else 1)
