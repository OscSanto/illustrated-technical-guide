import json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'evals'))
from evaluate import aggregate
ROOT=Path(__file__).resolve().parents[1]
class EvaluationTests(unittest.TestCase):
    def test_empty_runs_incomplete(self):
        suite=json.loads((ROOT/'evals/cases.json').read_text())
        with tempfile.TemporaryDirectory() as d:
            result=aggregate(suite,Path(d))
            self.assertEqual(result['status'],'INCOMPLETE')
            self.assertEqual(result['completed_cases'],0)
    def test_three_independent_runs_aggregate(self):
        case={'id':'foo','runs_required':3}
        with tempfile.TemporaryDirectory() as d:
            for i,n in enumerate([2,3,4],1):
                folder=Path(d)/'foo'/f'run-{i}';folder.mkdir(parents=True)
                (folder/'result.json').write_text(json.dumps({'case_id':'foo','run_id':f'run-{i}','guide_dir':'/actual/directory','review_notes':'Reviewer examined output', 'reviewer_scores':{k:n for k in ('beginner_success','technical_accuracy','illustration_mechanism','provenance','reproducibility')}}))
            result=aggregate([case],Path(d))
            self.assertEqual(result['status'],'COMPLETE')
            self.assertEqual(result['cases'][0]['scores']['technical_accuracy']['mean'],3)
            self.assertEqual(result['cases'][0]['scores']['technical_accuracy']['stdev'],0.82)
    def test_missing_score_not_accepted(self):
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d)/'foo'/'r1';folder.mkdir(parents=True)
            (folder/'result.json').write_text(json.dumps({'case_id':'foo','run_id':'r1','guide_dir':'path','review_notes':'reviewed','reviewer_scores':{'beginner_success':4}}))
            result=aggregate([{'id':'foo','runs_required':1}],Path(d))
            self.assertEqual(result['status'],'INCOMPLETE')
if __name__=='__main__':unittest.main()
