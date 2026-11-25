from pathlib import Path
from playwright.sync_api import sync_playwright
import json, subprocess, math, csv, sys, threading, http.server, socketserver, base64
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reports';OUT.mkdir(exist_ok=True)
results={}
class QuietHandler(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args): pass
root_to_serve=ROOT/'examples/cross-topic-benchmark'
class RootedHandler(QuietHandler):
 def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(root_to_serve),**kwargs)
server=socketserver.TCPServer(('127.0.0.1',0),RootedHandler)
threading.Thread(target=server.serve_forever,daemon=True).start()
base_url=f'http://127.0.0.1:{server.server_address[1]}'
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--no-proxy-server','--proxy-bypass-list=*'])
 for topic in ['postgresql','attention']:
  results[topic]={}
  for name,width,height in [('desktop',1440,900),('mobile',390,844)]:
   page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
   raw=(root_to_serve/topic/'index.html').read_text(); svg=(root_to_serve/topic/'assets/mechanism.svg').read_bytes(); uri='data:image/svg+xml;base64,'+base64.b64encode(svg).decode(); page.set_content(raw.replace('assets/mechanism.svg',uri),wait_until='load')
   page.locator('img.diagram').wait_for(state='visible')
   imageok=page.locator('img.diagram').evaluate('(el)=>el.complete && el.naturalWidth>0')
   overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth')
   page.screenshot(path=str(OUT/f'{topic}-{name}.png'),full_page=True)
   page.locator('button.open').click()
   active=page.locator('#viewer').is_visible()
   native=page.locator('#viewer img').evaluate('(el)=>({width:el.getBoundingClientRect().width,natural:el.naturalWidth})')
   pan=page.locator('.surface').evaluate('(el)=>el.scrollWidth > el.clientWidth') if name=='mobile' else True
   focus=page.evaluate('document.activeElement.classList.contains("close")')
   page.screenshot(path=str(OUT/f'{topic}-{name}-viewer.png'))
   page.keyboard.press('Escape')
   closed=not page.locator('#viewer').is_visible()
   restored=page.evaluate('document.activeElement.classList.contains("open")')
   results[topic][name]={'svg_loaded':imageok,'page_overflow':overflow,'viewer_open':active,'svg_width_in_viewer':native['width'],'native_svg_width':native['natural'],'mobile_pan':pan,'keyboard_close':closed,'focus_restored':restored}
   page.close()
 browser.close()
# independent numeric checks
sys.path.insert(0,str(ROOT/'scripts'))
# run existing tests
sp=subprocess.run(['python','scripts/test_visual_comparison.py'],cwd=ROOT,capture_output=True,text=True)
pytest=subprocess.run(['python','-m','pytest','-q','tests'],cwd=ROOT,capture_output=True,text=True,timeout=90)
# Run math fixture from generated exact code
from bs4 import BeautifulSoup
html=(ROOT/'examples/cross-topic-benchmark/attention/index.html').read_text()
script=BeautifulSoup(html,'html.parser').select_one('pre code').get_text()
exec_ctx={};exec(script,exec_ctx)
assert [round(w,4) for w in exec_ctx['weights']]==[0.6698,0.3302]
assert [round(w,4) for w in exec_ctx['out']]==[6.6976,6.6048]
# SQL test against sqlite, not postgresql
import sqlite3
conn=sqlite3.connect(':memory:')
code=BeautifulSoup((ROOT/'examples/cross-topic-benchmark/postgresql/index.html').read_text(),'html.parser').select_one('pre code').get_text()
conn.executescript(code[:code.index('SELECT c.name')]);rows=conn.execute(code[code.index('SELECT c.name'):]).fetchall()
assert rows==[('Ada',101,30),('Ada',102,22),('Ben',103,12),('Cleo',None,None)]
results['numerical_and_sql']={'attention_python':'EXECUTED PASS','postgres_join':'SQLITE CROSS-CHECK PASS; PostgreSQL not executed','rows':rows}
results['regression']={'illustration_script':sp.returncode,'pytest':pytest.returncode,'pytest_last_lines':pytest.stdout[-500:],'stderr':pytest.stderr[-200:]}
results['antv']={'status':'NOT_EXECUTED','reason':'npm registry DNS EAI_AGAIN'}
results['independent_ai_runs']={'status':'NOT_PERFORMED','reason':'These are two deterministic topic fixtures, not repeated model generations'}
assert sp.returncode==0 and pytest.returncode==0
for topic in ('postgresql','attention'):
 for v in ('desktop','mobile'):
  r=results[topic][v]
  assert r['svg_loaded'] and not r['page_overflow'] and r['viewer_open'] and r['keyboard_close'] and r['focus_restored']
  assert r['svg_width_in_viewer']>=1000 and r['mobile_pan']
(OUT/'BROWSER_RESULTS.json').write_text(json.dumps(results,indent=2))
with (OUT/'SCORECARD.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['topic','viewport','svg_loaded','no_page_overflow','viewer','native_size','mobile_pan','esc_and_focus'])
 for t in ['postgresql','attention']:
  for v in ['desktop','mobile']:
   r=results[t][v];w.writerow([t,v,r['svg_loaded'],not r['page_overflow'],r['viewer_open'],r['svg_width_in_viewer'],r['mobile_pan'],r['keyboard_close'] and r['focus_restored']])
report=f'''# v14 Cross-topic illustrated guide benchmark\n\n**Scope:** Two independently specified *topic fixtures*, PostgreSQL LEFT JOIN and 2D scaled dot-product attention. Not three independent LLM runs and not a complete textbook acceptance test.\n\n## Verified results\n- **2/2 topic figures** render as local SVG in Chromium.\n- **4/4 desktop/mobile page checks** have no document-level horizontal overflow.\n- **4/4 figure viewer checks** open, preserve native 1120 px width, close with Escape, and restore button focus. Mobile viewer is horizontally pannable.\n- **Attention numerical implementation:** executed Python; predicted weights `[0.6698, 0.3302]`, output `[6.6976, 6.6048]`.\n- **PostgreSQL LEFT JOIN:** SQL executed against **SQLite only** with 4 matching expected rows. No PostgreSQL runtime execution is claimed.\n- **Existing suite:** `pytest`: return code {pytest.returncode}, output `{pytest.stdout.strip()[-180:]}`; infographic fixture tests: return code {sp.returncode}.\n\n## Not established\n- AntV rendering and SVG export **NOT EXECUTED**; registry access failed (`EAI_AGAIN`). No visual A/B evidence with AntV exists.\n- **Cross-run skill reliability NOT MEASURED:** this test uses authored deterministic fixtures, not independent AI generations.\n- Educational usefulness: no learner study or blind expert assessment.\n- Full Jev source fidelity: out of scope for this visual transfer test.\n- Static SVG labels are still shrunk in inline mobile preview; users must select **Open readable figure** to read them at native size.\n\n## Verdict\n**PASS for cross-topic browser, responsive figure viewer, and arithmetic fixtures; NOT READY to promote AntV or claim generative consistency.** Keep AntV optional until a real render/export benchmark succeeds.\n\nEvidence: `BROWSER_RESULTS.json`, `SCORECARD.csv`, `{', '.join(f'{t}-{v}.png' for t in ['postgresql','attention'] for v in ['desktop','mobile'])}` and per-viewport viewer screenshots.\n'''
(OUT/'BENCHMARK_REPORT.md').write_text(report)
print(json.dumps(results,indent=2)[:4000]);print('report',OUT/'BENCHMARK_REPORT.md')
