#!/usr/bin/env python3
"""Aggregate real (or explicitly fixture) agent-run scores. Does not invoke an LLM."""
import argparse,json,statistics
from pathlib import Path
DIMENSIONS=('beginner_success','technical_accuracy','illustration_mechanism','provenance','reproducibility')
def aggregate(suite,root):
    result=[]
    for case in suite:
        path=root/case['id']; records=[];invalid=[]
        if path.exists():
            for p in sorted(path.glob('*/result.json')):
                try:
                    d=json.loads(p.read_text());score=d['reviewer_scores']
                    if d['case_id']!=case['id'] or not d.get('run_id') or not d.get('guide_dir') or not d.get('review_notes'):
                        invalid.append(str(p));continue
                    if any(score.get(k) is None or not isinstance(score.get(k),(int,float)) or not 0<=score[k]<=4 for k in DIMENSIONS):
                        invalid.append(str(p));continue
                    records.append(d)
                except (ValueError,KeyError,OSError,TypeError):invalid.append(str(p))
        unique={d['run_id']:d for d in records}
        required=case.get('runs_required',3)
        scores={k:{'mean':round(statistics.mean([d['reviewer_scores'][k] for d in unique.values()]),2),'min':min(d['reviewer_scores'][k] for d in unique.values()),'max':max(d['reviewer_scores'][k] for d in unique.values()),'stdev':round(statistics.pstdev([d['reviewer_scores'][k] for d in unique.values()]),2)} for k in DIMENSIONS} if unique else {}
        result.append({'case_id':case['id'],'status':'COMPLETE' if len(unique)>=required and not invalid else 'INCOMPLETE','runs':len(unique),'required':required,'invalid':invalid,'scores':scores})
    return {'status':'COMPLETE' if all(x['status']=='COMPLETE' for x in result) else 'INCOMPLETE','cases':result,'completed_cases':sum(x['status']=='COMPLETE' for x in result),'total_cases':len(result),'note':'Only supplied reviewed run files were counted. This script never executes model generations.'}
def main():
    p=argparse.ArgumentParser();p.add_argument('--suite',required=True);p.add_argument('--root',required=True);p.add_argument('--out',default=None);a=p.parse_args()
    data=aggregate(json.loads(Path(a.suite).read_text()),Path(a.root))
    if a.out:Path(a.out).write_text(json.dumps(data,indent=2)+'\n')
    print(f"{data['status']}: {data['completed_cases']}/{data['total_cases']} cases have required independently reviewed runs")
    for c in data['cases']:print(f"- {c['case_id']}: {c['runs']}/{c['required']} {c['status']}")
    return 0 if data['status']=='COMPLETE' else 2
if __name__=='__main__':raise SystemExit(main())
