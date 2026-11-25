#!/usr/bin/env python3
import copy,json,tempfile,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from source_fidelity_gate import audit
source=Path(__file__).resolve().parents[1]/'examples/provenance-fixture'
assert audit(source,'index.html')['status']=='PASS'
with tempfile.TemporaryDirectory() as td:
 d=Path(td);(d/'index.html').write_text((source/'index.html').read_text())
 obj=json.loads((source/'artifact_provenance.json').read_text());obj['artifacts'][0]['origin']='source_reproduction'
 (d/'artifact_provenance.json').write_text(json.dumps(obj))
 assert audit(d,'index.html')['status']=='FAIL','Misattribution must fail'
 obj=json.loads((source/'artifact_provenance.json').read_text());obj['artifacts'][0]['visible_label']='Imaginary label'
 (d/'artifact_provenance.json').write_text(json.dumps(obj))
 assert audit(d,'index.html')['status']=='FAIL','Missing visible label must fail'
 obj=json.loads((source/'artifact_provenance.json').read_text());obj['artifacts'][0]['type']='api_example';obj['artifacts'][0]['verification_status']='verified'
 (d/'artifact_provenance.json').write_text(json.dumps(obj))
 assert audit(d,'index.html')['status']=='FAIL','Unverified API spec must fail'
print('PASS: fixture and three negative provenance tests')
