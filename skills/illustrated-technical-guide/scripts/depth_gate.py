#!/usr/bin/env python3
"""Fail-closed structural audit of mechanism traces. This is not a factual-accuracy judge."""
import json,argparse,sys
from pathlib import Path

def check(folder):
    file=Path(folder)/'mechanism_traces.json'
    if not file.exists():return [f'MISSING {file.name}']
    try:d=json.loads(file.read_text(encoding='utf8'))
    except Exception as exc:return [f'INVALID JSON: {exc}']
    traces=d.get('chapters') if isinstance(d,dict) else None
    if not isinstance(traces,list) or not traces:return ['No chapters in mechanism_traces.json']
    errors=[];seen=set()
    fields=['objective','starting_input','operations','intermediate_states','invariant','worked_check','variation','failure_mode','figure','sources','evidence_status']
    for t in traces:
        ch=t.get('chapter','<unnamed>')
        if ch in seen:errors.append(f'DUPLICATE chapter {ch}')
        seen.add(ch)
        if not t.get('core_concept',False):continue
        for f in fields:
            v=t.get(f)
            if not v or v in ['todo','unknown','none','n/a','pending']:
                errors.append(f'{ch}: missing {f}')
        if not isinstance(t.get('operations'),list) or len(t.get('operations',[]))<2:
            errors.append(f'{ch}: expected an ordered list of at least two operations')
        if not isinstance(t.get('intermediate_states'),list) or not t.get('intermediate_states'):
            errors.append(f'{ch}: intermediate state list missing')
        if t.get('evidence_status') not in ('tested','source-traced','partially-verified','unverified'):
            errors.append(f'{ch}: evidence_status must declare limits explicitly')
    return errors
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--guide',required=True);a=ap.parse_args();errs=check(a.guide)
    print(json.dumps({'status':'FAIL' if errs else 'STRUCTURAL PASS — semantic review still required','findings':errs},indent=2))
    sys.exit(bool(errs))
