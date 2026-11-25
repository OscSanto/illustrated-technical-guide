import json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'skills/illustrated-technical-guide/scripts'))
from quality_gate import validate
ROOT=Path(__file__).resolve().parents[1]
class QualityTests(unittest.TestCase):
    def test_structural_fixture_passes(self):
        result=validate(ROOT/'evals/fixtures/pass')
        self.assertEqual(result['status'],'PASS',result['blockers'])
    def test_profile_mismatch_is_rejected(self):
        result=validate(ROOT/'evals/fixtures/fail')
        self.assertEqual(result['status'],'FAIL')
        self.assertTrue(any('hands-on' in s or 'milestone' in s for s in result['blockers']))
    def test_missing_provenance_rejected(self):
        import shutil
        with tempfile.TemporaryDirectory() as d:
            shutil.copytree(ROOT/'evals/fixtures/pass',Path(d)/'case')
            (Path(d)/'case/artifact_provenance.json').unlink()
            result=validate(Path(d)/'case')
            self.assertEqual(result['status'],'FAIL')
            self.assertTrue(any('Provenance:' in b for b in result['blockers']))
    def test_critical_claim_unverified(self):
        import shutil
        with tempfile.TemporaryDirectory() as d:
            shutil.copytree(ROOT/'evals/fixtures/pass',Path(d)/'case')
            f=Path(d)/'case/research_inventory.json';obj=json.loads(f.read_text());obj['claims'][0]['critical']=True;obj['claims'][0]['status']='unverified';f.write_text(json.dumps(obj))
            self.assertTrue(any('Critical claim' in b for b in validate(Path(d)/'case')['blockers']))
    def test_source_audit_missing_coverage(self):
        import shutil
        with tempfile.TemporaryDirectory() as d:
            shutil.copytree(ROOT/'evals/fixtures/pass',Path(d)/'case')
            f=Path(d)/'case/guide_manifest.json';obj=json.loads(f.read_text());obj['mode']='source_audit';f.write_text(json.dumps(obj))
            self.assertTrue(any('source_coverage.csv' in b for b in validate(Path(d)/'case')['blockers']))
if __name__=='__main__':unittest.main()
