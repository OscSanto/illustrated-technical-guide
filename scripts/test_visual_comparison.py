#!/usr/bin/env python3
"""Portable integrity and numerical tests for illustration candidates. Does not certify AntV rendering."""
from pathlib import Path
import json, math, re, sys
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/'examples/visual-comparison'; A=E/'assets'; results={}
for name in ['postgres','attention','decision']:
 p=A/f'{name}-custom.svg'; e=ET.parse(p).getroot(); assert e.tag.endswith('svg'); assert len(list(e))>5
 assert (A/f'{name}-antv.infographic').exists()
 d=(A/f'{name}-antv.infographic').read_text();assert d.startswith('infographic '); assert '\ndata\n' in d and '\ntheme\n' in d
 results[name]={'custom_svg_xml':'PASS','antv_dsl_structure':'PASS','antv_render':'NOT_TESTED (package unavailable)'}
x=json.loads((E/'figure_data.json').read_text()); p=x['postgres']
assert len(p['left_join_rows'])==4 and p['left_join_rows'][-1][1] is None
assert sum(1 for z in p['left_join_rows'] if z[0]=='Ada')==2
weights=x['attention']['weights'];assert abs(sum(weights)-1)<1e-12
assert abs(weights[0]- math.exp(1/math.sqrt(2))/(math.exp(1/math.sqrt(2))+1)) < 1e-12
assert abs(x['attention']['weighted_output'][0]-weights[0]*10)<1e-12
z=x['decision']; assert abs(sum(z['softmax_probabilities'])-1)<1e-12
assert all(abs(t-(1/(1+math.exp(-v))))<1e-12 for v,t in zip(z['sigmoid_logits'],z['sigmoid_probabilities']))
assert abs(sum(z['sigmoid_probabilities'])-1)>0.1
results['data_correctness']='PASS (seven arithmetic and relational invariants)'
ht=(E/'index.html').read_text();assert '0.2.20' in ht and '@latest' not in ht and 'renderer unavailable' in ht.lower()
results['html_version_and_fallback']='PASS (CDN pinned; offline message visible)'
(E/'TEST_RESULTS.json').write_text(json.dumps({'results':results,'overall':'PARTIAL: offline SVGs and fixtures pass; AntV not rendered'},indent=2))
print(json.dumps(results,indent=2))
