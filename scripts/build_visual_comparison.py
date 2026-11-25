#!/usr/bin/env python3
"""Build three technically grounded, offline SVG illustrations plus AntV DSL/HTML candidates."""
from pathlib import Path
import html, json, math
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'examples/visual-comparison'; A=OUT/'assets'; A.mkdir(parents=True,exist_ok=True)
COL={'canvas':'#f8f9fb','ink':'#3a424a','line':'#535a62','blue':'#2d92d5','green':'#2e9e52','orange':'#ee8517','pink':'#d82f79','muted':'#76808c','gray':'#b8c0c9','cream':'#f6efe5','border':'#cbd0d5'}

def tx(x,y,s,size=15,weight=500,color=None,mono=False,anchor='start'):
 return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{color or COL["ink"]}" font-family="{ "ui-monospace, SFMono-Regular, Consolas, monospace" if mono else "Inter, Source Sans 3, Arial, sans-serif" }">{html.escape(str(s))}</text>'
def box(x,y,w,h,fill='white',stroke=None,rx=11,sw=2):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke or COL["line"]}" stroke-width="{sw}"/>'
def arrow(x1,y1,x2,y2,color=None):
 c=color or COL['line'];return f'<path d="M{x1} {y1} H{x2}" stroke="{c}" stroke-width="2.3" fill="none" marker-end="url(#arr)"/>' if y1==y2 else f'<path d="M{x1} {y1} V{y2} H{x2}" stroke="{c}" stroke-width="2.3" fill="none" marker-end="url(#arr)"/>'
def svg(body,w=1120,h=540):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img"><defs><marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9Z" fill="{COL['line']}"/></marker></defs><rect width="{w}" height="{h}" fill="{COL['canvas']}"/>{body}</svg>'''

def table(x,y,headers,rows,widths,rowh=43,accent=None,title=None):
 W=sum(widths); parts=[]
 if title: parts.append(tx(x,y-14,title,17,700))
 parts.append(box(x,y,W,(len(rows)+1)*rowh,rx=9,sw=1.8))
 parts.append(f'<rect x="{x+1}" y="{y+1}" width="{W-2}" height="{rowh-1}" rx="8" fill="#e7edf2"/>')
 for j,h in enumerate(headers):parts.append(tx(x+sum(widths[:j])+12,y+27,h,13,700))
 for i,row in enumerate(rows):
  yy=y+(i+1)*rowh
  if i%2==1:parts.append(f'<rect x="{x+1}" y="{yy}" width="{W-2}" height="{rowh}" fill="#f4f7fa"/>')
  parts.append(f'<path d="M{x} {yy} H{x+W}" stroke="#d0d7dd"/>')
  for j,s in enumerate(row):
   c=accent if (accent and j==0) else COL['ink']
   parts.append(tx(x+sum(widths[:j])+12,yy+27,s,13,600 if j==0 else 450,c,mono=j>0))
 for j in range(1,len(widths)):parts.append(f'<path d="M{x+sum(widths[:j])} {y} V{y+(len(rows)+1)*rowh}" stroke="#e0e5e9"/>')
 return ''.join(parts)

# database: exact input rows -> LEFT JOIN result shows duplicate matches and null-preserved row
p=[]
p+=[tx(34,46,'LEFT JOIN: follow each customer to its matching order rows',25,800),tx(34,79,'ON customers.id = orders.customer_id  •  an unmatched customer remains as a NULL-filled row',15,450,COL['muted'])]
p+=[table(35,147,['id','customer'],[['1','Ada'],['2','Ben'],['3','Cleo']],[67,145],title='customers (left table)',accent=COL['blue'])]
p+=[table(293,147,['id','customer_id','total'],[['101','1','$30'],['102','1','$22'],['103','2','$12']],[64,126,90],title='orders (right table)',accent=COL['orange'])]
p+=[table(718,129,['customer','order_id','total'],[['Ada','101','$30'],['Ada','102','$22'],['Ben','103','$12'],['Cleo','NULL','NULL']],[126,126,112],title='LEFT JOIN result (4 rows)',accent=COL['green'])]
p+=[arrow(248,264,282,264), arrow(576,265,694,265),tx(630,245,'match on id',12,600,COL['muted'],anchor='middle')]
p+=[box(34,364,620,108,fill='#f0f6fb',stroke='#bbd7ea',rx=12,sw=1.5),tx(54,396,'Why 4 result rows?',17,750,COL['blue']),tx(54,424,'Ada has 2 orders → 2 rows; Ben has 1 → 1 row.',15),tx(54,448,'Cleo has no orders → 1 preserved row with NULLs.',15)]
p+=[box(715,390,375,82,fill='#eef7ef',stroke='#b6d7bf',rx=12,sw=1.5),tx(734,418,'Mechanism, not an ER diagram',16,700,COL['green']),tx(734,445,'Shows row multiplication and NULL preservation.',13)]
(A/'postgres-custom.svg').write_text(svg(''.join(p),1120,510))

# attention: numeric derivation and weights explicit
s=1/math.sqrt(2); w1=math.exp(s)/(math.exp(s)+1);w2=1-w1
p=[]
p += [tx(32,46,'Scaled dot-product attention: one query, two keys',24,800),tx(32,78,'Toy calculation with dₖ = 2. Numbers are calculated, not measured.',15,450,COL['muted'])]
for x,label,values,color in [(34,'Query q','[1, 0]',COL['blue']),(260,'Key k₁','[1, 0]',COL['green']),(454,'Key k₂','[0, 1]',COL['orange'])]:
 p.extend([box(x,126,164,90,'white'),tx(x+16,159,label,17,700,color),tx(x+16,190,values,19,600,mono=True)])
p.extend([tx(35,261,'Step 1 · dot products, scaled by √dₖ',18,750),box(35,279,590,64,'#f7efe3',sw=1.5),tx(52,307,'scores = [q·k₁, q·k₂] / sqrt(2)',17,600,mono=True),tx(52,330,f'= [{s:.4f}, 0.0000]',15,550,mono=True)])
p.extend([tx(35,384,'Step 2 · softmax gives attention weights',18,750),box(35,400,590,65,'#eaf5e9',sw=1.5),tx(52,429,f'weights = [{w1:.4f}, {w2:.4f}]',18,650,mono=True),tx(52,453,'They sum to 1; each tells how much to read from a value.',12,450,COL['muted'])])
p.extend([tx(694,125,'Step 3 · weight the values',18,750),box(685,146,396,268,fill='white')])
p.extend([tx(708,184,'v₁ = [10, 0]',18,700,COL['green'],mono=True),tx(708,218,'v₂ = [0, 20]',18,700,COL['orange'],mono=True)])
p.extend([tx(708,267,'output = w₁ · v₁ + w₂ · v₂',15,600,mono=True),tx(708,305,f'= [{10*w1:.2f}, {20*w2:.2f}]',22,800,COL['blue'],mono=True)])
p.extend([tx(708,365,'Each dimension is a weighted SUM,',13,500),tx(708,384,'not a choice of just one value.',13,500)])
p.extend([tx(33,502,'Original teaching example · Simplified to a single-head, single-query calculation; not a full transformer architecture.',13,450,COL['muted'])])
(A/'attention-custom.svg').write_text(svg(''.join(p),1120,530))

# decision categorical logits and sigmoid distinctions, no source-specific architecture claimed
z=[2,.5,-1]; exp=[math.exp(t) for t in z]; prob=[v/sum(exp) for v in exp]; labels=['billing','tech','account']; colors=[COL['blue'],COL['gray'],COL['gray']]
p=[tx(32,47,'One-label decision versus independent labels',25,800),tx(32,79,'Synthetic logits demonstrate the output rules; these are not Jev measurements.',15,450,COL['muted'])]
p += [box(31,117,520,335,'white'),box(569,117,520,335,'white'),tx(51,154,'One label: softmax',20,800,COL['blue']),tx(589,154,'Several labels: sigmoid',20,800,COL['orange'])]
for i,(lab,zi,pr,c) in enumerate(zip(labels,z,prob,colors)):
 y=189+i*75
 p.extend([box(51,y,152,47,COL['cream'],sw=1.3),tx(63,y+29,f'{lab} {zi:+.1f}',13,650,mono=True),arrow(206,y+24,259,y+24),box(267,y+10,87,30,'#f6d9da',sw=1.2),tx(310,y+30,'joint',12,700,anchor='middle'),box(378,y+4,146,42,'white',sw=1.2),tx(392,y+29,f'{pr:.3f}',17,800,c,mono=True)])
for i,(lab,zi) in enumerate([('refund',3),('cancel',1.5),('legal',-2.5)]):
 y=189+i*75; pr=1/(1+math.exp(-zi))
 p.extend([box(588,y,152,47,COL['cream'],sw=1.3),tx(600,y+29,f'{lab} {zi:+.1f}',13,650,mono=True),arrow(743,y+24,794,y+24),box(803,y+10,86,30,'#fce7cf',sw=1.2),tx(845,y+30,'sigmoid',12,700,anchor='middle'),box(912,y+4,146,42,'white',sw=1.2),tx(923,y+29,f'{pr:.3f}',17,800,COL['orange'] if i==0 else COL['muted'],mono=True)])
p += [tx(266,180,'shared normalizer',11,700,COL['blue']),tx(53,431,'Σ probabilities = 1',16,750,COL['blue']),tx(589,431,'Σ probabilities ≈ 1.85 (not constrained to 1)',14,750,COL['orange']),tx(32,503,'Original comparison · illustrative scores; does not establish the internals of any proprietary decision model.',13,500,COL['muted'])]
(A/'decision-custom.svg').write_text(svg(''.join(p),1120,525))

# Valid, conservative AntV DSL candidates -- declared exactly as templates, no unsupported fields
specs={
 'postgres':'''infographic relation-dagre-flow-tb-simple-circle-node\ndata\n  title LEFT JOIN: input tables and output\n  desc A customer can match several order rows, or none\n  nodes\n    - id customers\n      label Customers: Ada, Ben, Cleo\n    - id orders\n      label Orders: 101→Ada, 102→Ada, 103→Ben\n    - id joined\n      label Joined rows: Ada×2, Ben×1, Cleo×NULL\n  relations\n    customers - match customer_id -> joined\n    orders - contribute matches -> joined\ntheme\n  palette #2d92d5 #2e9e52 #ee8517''',
 'attention':'''infographic sequence-ascending-steps\ndata\n  title Attention on a toy query\n  desc q=[1,0], k1=[1,0], k2=[0,1], d_k=2\n  sequences\n    - label Compute dot products\n      desc q·k1=1; q·k2=0\n      icon calculator\n    - label Scale scores by sqrt(2)\n      desc [0.7071, 0]\n      icon scale\n    - label Softmax scores\n      desc [0.6698, 0.3302]\n      icon chart bar\n    - label Weighted sum of values\n      desc v1=[10,0], v2=[0,20]; output=[6.70,6.60]\n      icon sum\ntheme\n  palette #2d92d5 #2e9e52 #ee8517''',
 'decision':'''infographic compare-binary-horizontal-simple-fold\ndata\n  title Softmax and sigmoid: different output semantics\n  compares\n    - label One-label decision\n      children\n        - label Softmax logits [2,0.5,-1]\n          desc Billing 0.786, tech 0.175, account 0.039; probabilities sum to 1\n          icon chart bar\n    - label Independent labels\n      children\n        - label Sigmoids [3,1.5,-2.5]\n          desc Refund 0.953, cancel 0.818, legal 0.076; sum need not be 1\n          icon chart bar\ntheme\n  palette #2d92d5 #2e9e52 #ee8517'''
}
for name,dsl in specs.items():(A/f'{name}-antv.infographic').write_text(dsl+'\n')

# Side-by-side browser page, pinned CDN; fallback clearly status, no deceptive 'rendered' claim.
css='''*{box-sizing:border-box}body{font-family:Inter,Source Sans 3,Arial,sans-serif;background:#f5f7fa;color:#303741;margin:0}header{padding:28px max(24px,4vw);background:#fff;border-bottom:1px solid #d4dae0}h1{margin:0 0 9px;font-size:1.9rem}p{line-height:1.55}main{padding:22px max(20px,3vw) 60px;max-width:1800px;margin:auto}.topic{margin-bottom:34px}.topic h2{font-size:1.35rem}.pair{display:grid;grid-template-columns:1fr 1fr;gap:17px}.panel{background:white;border:1px solid #cbd0d5;border-radius:13px;padding:14px;min-width:0;box-shadow:0 2px 8px #2222220a}.panel h3{margin:2px 0 10px;font-size:1rem}.panel img,.panel svg{max-width:100%;height:auto}.antv{min-height:320px;overflow:auto}.status{color:#73500b;font-size:.86rem}.meta{color:#65717d;font-size:.88rem}code,pre{font:12px/1.6 ui-monospace,Consolas,monospace}details{margin-top:8px}pre{overflow:auto;white-space:pre-wrap;overflow-wrap:anywhere;background:#f5f7fa;padding:12px;border-radius:7px}button{padding:8px 12px;border:1px solid #7e8994;background:white;border-radius:7px;cursor:pointer}a{color:#126db2}@media(max-width:950px){.pair{grid-template-columns:1fr}.antv{min-height:260px}}'''
htmlbits=[f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AntV vs Custom SVG — technical illustration experiment</title><style>{css}</style></head><body><header><h1>Technical Illustration Engine · v12 experiment</h1><p>Side-by-side comparison of <b>AntV Infographic candidates</b> and <b>tested static custom SVG</b>. AntV panels load a pinned external renderer when network access is available. If it fails, the source DSL remains accessible below. No figures here are attributed to TheLion.AI.</p><p class="meta">All numbers are synthetic teaching examples, not benchmark measurements. AntV templates are structurally plausible candidates; local runtime verification is pending.</p></header><main>''']
for name,title,subtitle in [('postgres','PostgreSQL: LEFT JOIN','AntV relationship overview versus exact row-level join trace'),('attention','Transformer attention','AntV process sequence versus numerically worked attention'),('decision','Decision-model outputs','AntV softmax/sigmoid comparison versus side-by-side calculated values')]:
 source=html.escape(specs[name]);htmlbits.append(f'''<section class="topic"><h2>{title}</h2><p class="meta">{subtitle}</p><div class="pair"><article class="panel"><h3>AntV Infographic · proposed template</h3><div class="antv" id="antv-{name}" aria-live="polite"><p class="status" id="status-{name}">Waiting for AntV renderer…</p></div><button type="button" onclick="saveAntv('{name}')">Export AntV SVG</button><details><summary>View AntV DSL</summary><pre>{source}</pre></details></article><article class="panel"><h3>Custom SVG · offline original</h3><img src="assets/{name}-custom.svg" alt="{title} illustrated with explicit technical details" loading="lazy"><p class="meta">Direct SVG rendering; legible offline and editable.</p><a href="assets/{name}-custom.svg" download>Download SVG</a></article></div></section>''')
htmlbits.append('''<p class="meta">Source: original teaching figures and calculated values. Generated for the skill evaluation. Neither engine verifies the scientific accuracy of its source inputs by itself.</p></main><script src="https://cdn.jsdelivr.net/npm/@antv/infographic@0.2.20/dist/infographic.min.js"></script><script>
const specs = '''+json.dumps(specs,ensure_ascii=False)+''';const instances = {};
function createAntv(){
 const C=window.AntVInfographic?.Infographic;
 for (const [name,spec] of Object.entries(specs)) {
  const out=document.getElementById('antv-'+name),status=document.getElementById('status-'+name);
  if(!C){status.textContent='Renderer unavailable offline or CDN blocked. DSL retained below; no AntV visual was verified.';continue;}
  try{const viz=new C({container:'#antv-'+name,width:'100%',height:'100%',editable:false});instances[name]=viz;Promise.resolve(viz.render(spec)).then(()=>{status.remove()}).catch(e=>{status.textContent='AntV render error: '+e.message});}
  catch(e){status.textContent='AntV initialization error: '+e.message;}
 }
}
async function saveAntv(name){const v=instances[name];if(!v){alert('AntV renderer unavailable. Use the offline custom SVG.');return;}try{const src=await v.toDataURL({type:'svg'});const a=document.createElement('a');a.href=src;a.download=name+'-antv.svg';a.click();}catch(e){alert('AntV export failed: '+e.message);}}
createAntv();
</script></body></html>''')
(OUT/'index.html').write_text(''.join(htmlbits))
(OUT/'figure_data.json').write_text(json.dumps({'postgres':{'customers':[['1','Ada'],['2','Ben'],['3','Cleo']],'orders':[['101','1','30'],['102','1','22'],['103','2','12']],'left_join_rows':[['Ada','101','30'],['Ada','102','22'],['Ben','103','12'],['Cleo',None,None]]},'attention':{'scaled_scores':[s,0],'weights':[w1,w2],'weighted_output':[10*w1,20*w2]},'decision':{'softmax_logits':z,'softmax_probabilities':prob,'sigmoid_logits':[3,1.5,-2.5],'sigmoid_probabilities':[1/(1+math.exp(-x)) for x in [3,1.5,-2.5]]}},indent=2))
print('generated',len(list(A.iterdir())),'assets, HTML')
