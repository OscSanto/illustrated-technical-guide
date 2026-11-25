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
class ClaimBadgeTests(unittest.TestCase):
    """reading-design.md: badges must cite a real claim whose recorded evidence matches the badge."""
    def case(self,d,badge,evidence='measured',critical=False,extra_claim=None):
        import shutil
        shutil.copytree(ROOT/'evals/fixtures/pass',Path(d)/'case')
        f=Path(d)/'case/research_inventory.json';obj=json.loads(f.read_text())
        obj['claims'][0]['evidence']=evidence;obj['claims'][0]['critical']=critical
        if extra_claim:obj['claims'].append(extra_claim)
        f.write_text(json.dumps(obj))
        h=Path(d)/'case/index.html';html=h.read_text(encoding='utf-8')
        h.write_text(html.replace('no educational quality is claimed.','no educational quality is claimed. '+badge,1),encoding='utf-8')
        return validate(Path(d)/'case')
    def test_matching_badge_passes(self):
        with tempfile.TemporaryDirectory() as d:
            r=self.case(d,'<span class="badge b-meas" data-claim="c1">measured</span>')
            self.assertEqual(r['status'],'PASS',r['blockers'])
    def test_unknown_claim_blocked(self):
        with tempfile.TemporaryDirectory() as d:
            r=self.case(d,'<span class="badge b-meas" data-claim="c99">measured</span>')
            self.assertTrue(any('unknown claim c99' in b for b in r['blockers']))
    def test_mismatched_evidence_blocked(self):
        with tempfile.TemporaryDirectory() as d:
            r=self.case(d,'<span class="badge b-pub" data-claim="c1">published</span>',evidence='inferred')
            self.assertTrue(any('shows published' in b for b in r['blockers']))
    def test_critical_claim_without_badge_blocked_once_badges_used(self):
        with tempfile.TemporaryDirectory() as d:
            extra={'id':'c2','critical':True,'destination_anchor':'queue','status':'verified','evidence':'published'}
            r=self.case(d,'<span class="badge b-meas" data-claim="c1">measured</span>',extra_claim=extra)
            self.assertTrue(any('Critical claim c2: no badge' in b for b in r['blockers']))
    def test_no_badges_keeps_legacy_guides_valid(self):
        result=validate(ROOT/'evals/fixtures/pass')
        self.assertFalse(any('badge' in b for b in result['blockers']))
if __name__=='__main__':unittest.main()
