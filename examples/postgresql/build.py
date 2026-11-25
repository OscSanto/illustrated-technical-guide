from pathlib import Path
import html,json,zipfile,re
P=Path('/mnt/data/postgres-v8-test'); E=P/'examples'
chapters=[
('start','01','The system you will build','Understand the client/server boundary, tools, and the dataset.'),
('install','02','Install and initialize PostgreSQL','Install the server, initialize a cluster, start the service, and create a role.'),
('vscode','03','Connect VS Code to PostgreSQL','Use a SQL extension and verify the connection without embedding secrets.'),
('schema','04','Create the sample database','Create tables, keys, constraints, and indexes for a small store.'),
('data','05','Load and inspect realistic data','Insert a reproducible dataset and inspect table contents.'),
('queries','06','Query fundamentals','Filter, sort, limit, handle NULL, and reason about execution order.'),
('group','07','GROUP BY, HAVING, and aggregates','Compute revenue and customer summaries without double-counting.'),
('joins','08','INNER and LEFT JOIN','Understand row multiplication, unmatched rows, and cardinality.'),
('analysis','09','Business analysis with SQL','Build cohorts, top products, and a repeat-purchase report.'),
('performance','10','EXPLAIN ANALYZE and indexing','Read plans, distinguish estimates from actuals, and tune responsibly.'),
('diagnose','11','Performance investigation lab','Compare plans, update statistics, inspect selective filters, and test alternatives.'),
('production','12','Safety, maintenance, and next steps','Use transactions, parameterization, least privilege, and backups.')]
figs=[]
def figure(fid,title,question,svg,caption,labels):
 figs.append(dict(id=fid,html_figure_id=fid,question=question,answer=caption,visual_grammar='annotated technical diagram',technical_labels=labels,data_provenance='Original instructional diagram; illustrative values where noted',adjacent_explanation_anchor=fid.replace('fig-',''),caption=caption,desktop_review='not_tested',mobile_review='not_tested',review_status='pending'))
 return f'<figure id="{fid}"><div class="figure-heading"><span class="eyebrow">FIELD NOTE · {len(figs):02d}</span><h4>{title}</h4></div><div class="art">{svg}</div><figcaption><b>Figure {len(figs)}.</b> {caption}</figcaption></figure>'
def svgbox(x,y,w,h,label,sub='',fill='#edf5f1'):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#79978d"/><text x="{x+12}" y="{y+24}" font-size="15" font-weight="700" fill="#233c36">{html.escape(label)}</text><text x="{x+12}" y="{y+43}" font-size="11" fill="#4b645d">{html.escape(sub)}</text>'
def svgwrap(s,height=230):return f'<svg viewBox="0 0 800 {height}" role="img" aria-label="Technical diagram with annotated components" xmlns="http://www.w3.org/2000/svg"><defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="none" stroke="#537b71" stroke-width="1.4"/></marker></defs>{s}</svg>'
def arrow(x,y,xx,yy):return f'<path d="M{x} {y} L{xx} {yy}" stroke="#537b71" stroke-width="2" marker-end="url(#arr)" fill="none"/>'
def code(s,lang='sql'):
 return f'<div class="code-head"><span>{lang.upper()}</span><button class="copy" onclick="navigator.clipboard.writeText(this.parentElement.nextElementSibling.innerText)">Copy</button></div><pre><code>{html.escape(s.strip())}</code></pre>'
def prose(t):return f'<p>{t}</p>'
sections={}
sections['start']=prose('PostgreSQL is a database server, not a file that VS Code opens directly. VS Code is a client: it sends SQL over a connection; the server parses, plans, and executes the query against durable tables. We will use a miniature online store with four related tables and the same example throughout.')+figure('fig-start','One query crosses three boundaries','What runs in the editor, on the network, and in the server?',svgwrap(svgbox(20,60,205,85,'VS Code','SQL editor + extension')+svgbox(300,60,205,85,'PostgreSQL','Parser → planner → executor')+svgbox(580,60,200,85,'Disk + memory','Tables, indexes, buffers')+arrow(225,100,300,100)+arrow(505,100,580,100)+'<text x="233" y="87" font-size="11">TCP 5432</text><text x="516" y="87" font-size="11">pages</text>'),'The editor is not the database: it transmits queries; PostgreSQL owns data and execution.',['TCP 5432','planner','tables'])+prose('Learning outcome: by the end, you can create the database, connect from VS Code, write grouped and joined queries, and interpret a query plan. PostgreSQL syntax is used throughout; example output is derived from the included small dataset, not a performance benchmark.')
sections['install']=prose('Choose the installation route appropriate for your operating system. On Windows, use the official PostgreSQL installer and note the password for the postgres administrative role. On macOS, use the official packages or a package manager. On Debian/Ubuntu, use the packaged server. Server version and service names vary; verify rather than assume.')+code('sudo apt update\nsudo apt install postgresql postgresql-client\nsudo systemctl enable --now postgresql\nsudo -u postgres psql -c "SELECT version();"','bash')+code('sudo -u postgres createuser --pwprompt analyst\nsudo -u postgres createdb --owner=analyst shoplab\npsql -h localhost -U analyst -d shoplab -c "SELECT current_database(), current_user;"','bash')+prose('The default Linux local peer-authentication path is different from TCP password authentication. The explicit <code>-h localhost</code> uses a TCP connection; if it fails, inspect <code>pg_hba.conf</code>, the service status, and the port before changing security settings. For Windows, create the role and database in psql or pgAdmin using the same SQL below.')+code("CREATE ROLE analyst LOGIN PASSWORD 'replace-with-a-strong-password';\nCREATE DATABASE shoplab OWNER analyst;",'sql')+figure('fig-install','Initialization is a sequence, not one command','Which objects are created before the first query?',svgwrap(svgbox(16,58,176,85,'Server install','postgres binaries')+svgbox(218,58,176,85,'Data cluster','initdb / installer')+svgbox(420,58,176,85,'Role + database','analyst / shoplab')+svgbox(622,58,160,85,'Login test','psql over TCP')+arrow(192,100,218,100)+arrow(394,100,420,100)+arrow(596,100,622,100)),'Install the service, initialize its data directory, create credentials and a database, then test a real connection.',['cluster','role','database','psql'])
sections['vscode']=prose('Install VS Code, then choose a reputable PostgreSQL-capable SQL extension (for example, Microsoft’s PostgreSQL extension if available in your Marketplace). Open its connection command and enter host <code>localhost</code>, port <code>5432</code>, database <code>shoplab</code>, username <code>analyst</code>, and your password. Extension menus vary by version. Alternatively, use VS Code’s integrated terminal and <code>psql</code>; this route is reliable even without an extension.')+code('psql -h localhost -p 5432 -U analyst -d shoplab\n-- Once connected, run:\nSELECT current_database(), current_user, inet_server_port();','bash')+figure('fig-vscode','Connection anatomy','What does each field select?',svgwrap(svgbox(25,30,330,155,'Connection profile','host: localhost    port: 5432')+svgbox(445,30,320,155,'Server identity','database: shoplab')+arrow(355,110,445,110)+'<text x="45" y="105" font-size="14" fill="#344b45">user: analyst</text><text x="45" y="127" font-size="14" fill="#344b45">password: stored securely</text><text x="465" y="105" font-size="14" fill="#344b45">SELECT current_database()</text><text x="465" y="127" font-size="14" fill="#344b45">returns shoplab</text>',220),'Host and port select the server; database and user select the session context and permissions.',['host','port','database','role'])+prose('Troubleshooting: “connection refused” usually means wrong host/port or server not listening; “password authentication failed” points to credentials or authentication rules; “database does not exist” means the server was reached but the requested database was not found. Avoid putting passwords in SQL files or source control.')
sections['schema']=prose('A relational design separates entities from events. One customer has many orders; one order has many line items; each line item refers to one product. Primary keys uniquely identify rows; foreign keys prevent dangling references. Monetary values use <code>numeric</code> rather than floating point.')+code('''DROP TABLE IF EXISTS order_items, orders, products, customers CASCADE;
CREATE TABLE customers (
  customer_id integer PRIMARY KEY,
  name text NOT NULL,
  region text NOT NULL,
  joined_on date NOT NULL
);
CREATE TABLE products (
  product_id integer PRIMARY KEY,
  name text NOT NULL,
  category text NOT NULL,
  price numeric(10,2) NOT NULL CHECK (price >= 0)
);
CREATE TABLE orders (
  order_id integer PRIMARY KEY,
  customer_id integer NOT NULL REFERENCES customers(customer_id),
  ordered_on date NOT NULL,
  status text NOT NULL CHECK (status IN ('paid','pending','cancelled'))
);
CREATE TABLE order_items (
  order_id integer NOT NULL REFERENCES orders(order_id),
  product_id integer NOT NULL REFERENCES products(product_id),
  quantity integer NOT NULL CHECK (quantity > 0),
  unit_price numeric(10,2) NOT NULL CHECK (unit_price >= 0),
  PRIMARY KEY (order_id, product_id)
);''')+figure('fig-schema','Four tables, three relationships','Where are one-to-many relationships stored?',svgwrap(svgbox(20,25,220,75,'customers','PK customer_id')+svgbox(300,25,220,75,'orders','PK order_id · FK customer_id')+svgbox(300,145,220,75,'order_items','PK order_id + product_id')+svgbox(575,145,205,75,'products','PK product_id')+arrow(240,62,300,62)+arrow(410,100,410,145)+arrow(520,182,575,182)+'<text x="251" y="49" font-size="12">1:N</text><text x="422" y="125" font-size="12">1:N</text><text x="533" y="169" font-size="12">N:1</text>'),'Foreign keys live on the many side: orders references customers; order_items references both orders and products.',['PK','FK','1:N'])+prose('Store the sale-time <code>unit_price</code> on order_items. Otherwise, a later product price change would rewrite the meaning of historical revenue.')
sections['data']=prose('Run this seed script after creating the schema. The dataset intentionally contains an unmatched customer, a pending order, and a cancelled order so joins and revenue filters produce meaningful differences.')+code('''INSERT INTO customers VALUES
 (1,'Ada','South','2026-01-03'),(2,'Ben','North','2026-01-07'),
 (3,'Cleo','South','2026-02-01'),(4,'Dee','West','2026-02-12');
INSERT INTO products VALUES
 (10,'Notebook','Stationery',8.00),(11,'Pen Set','Stationery',5.00),
 (12,'Mouse','Electronics',25.00);
INSERT INTO orders VALUES
 (100,1,'2026-03-01','paid'),(101,1,'2026-03-08','paid'),
 (102,2,'2026-03-10','paid'),(103,3,'2026-03-11','pending'),
 (104,2,'2026-03-12','cancelled');
INSERT INTO order_items VALUES
 (100,10,2,8.00),(100,11,1,5.00),
 (101,12,1,25.00),(102,10,1,8.00),
 (103,12,2,25.00),(104,11,3,5.00);
SELECT * FROM customers ORDER BY customer_id;
SELECT COUNT(*) AS orders, COUNT(DISTINCT customer_id) AS buyers FROM orders;''')+figure('fig-data','A deliberately uneven dataset','Which edge cases are present?',svgwrap(svgbox(15,40,225,105,'Ada','2 paid orders · $46')+svgbox(287,40,225,105,'Ben','1 paid · 1 cancelled')+svgbox(560,40,225,105,'Cleo + Dee','pending only / no orders',fill='#f9eee7')+'<text x="25" y="175" font-size="14" fill="#4c645e">Paid revenue = $54 (Ada $46 + Ben $8). Pending and cancelled are excluded.</text>'),'The sample exposes status filtering, zero-order customers, and repeated orders. All dollar values are derived from the supplied rows.',['paid','pending','cancelled'])
sections['queries']=prose('SQL is declarative: you describe the result, and the planner chooses an execution strategy. A useful mental model for a SELECT query is FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT (with window and other features adding nuance). This is a logical interpretation, not a promise of physical execution order.')+code("SELECT order_id, ordered_on, status\nFROM orders\nWHERE ordered_on >= DATE '2026-03-08'\n  AND status = 'paid'\nORDER BY ordered_on DESC\nLIMIT 10;")+prose('NULL is unknown rather than equal to anything: use <code>IS NULL</code>, not <code>= NULL</code>. Use explicit <code>ORDER BY</code> when result order matters; tables have no guaranteed default row order.')+figure('fig-queries','Logical SQL stages','Why does WHERE come before grouping?',svgwrap(svgbox(15,70,145,65,'FROM','5 orders')+svgbox(175,70,145,65,'WHERE','3 paid')+svgbox(335,70,145,65,'GROUP','aggregate')+svgbox(495,70,145,65,'ORDER','sort')+svgbox(655,70,130,65,'LIMIT','top rows')+arrow(160,100,175,100)+arrow(320,100,335,100)+arrow(480,100,495,100)+arrow(640,100,655,100)),'Filter rows before forming groups; HAVING filters aggregate groups after GROUP BY.',['FROM','WHERE','GROUP','ORDER','LIMIT'])
sections['group']=prose('GROUP BY partitions the input rows into groups. Aggregate functions summarize each group. The important choice is the unit of analysis: line items, orders, or customers. Revenue should be computed from paid line items, not from the products’ current list prices.')+code('''SELECT c.region,
       COUNT(DISTINCT o.order_id) AS paid_orders,
       COALESCE(SUM(oi.quantity * oi.unit_price),0) AS revenue
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.status = 'paid'
GROUP BY c.region
HAVING SUM(oi.quantity * oi.unit_price) >= 10
ORDER BY revenue DESC;''')+prose('Expected result: South has 2 paid orders and $46. North has $8 and fails the HAVING threshold. West has no paid orders and is absent because these are inner joins.')+figure('fig-group','From line items to one regional total','Which rows contribute to the South group?',svgwrap(svgbox(20,45,260,135,'Paid line items','Ada: $16, $5, $25')+svgbox(340,45,190,135,'GROUP BY','region = South')+svgbox(590,45,190,135,'SUM','46.00')+arrow(280,110,340,110)+arrow(530,110,590,110)+'<text x="38" y="135" font-size="12">Ben: $8 → North</text>'),'Three paid Ada line items sum to $46; the North row is a different group.',['$16','$5','$25','$46'])+prose('Do not use <code>COUNT(*)</code> to count orders after joining order_items: it counts line-item rows. Use <code>COUNT(DISTINCT o.order_id)</code>, or aggregate orders first in a common table expression.')
sections['joins']=prose('An INNER JOIN keeps matching rows. A LEFT JOIN keeps every row on the left, filling unmatched right-side columns with NULL. A join is not inherently one-to-one: joining an order to its items multiplies order rows according to the number of items.')+code('''-- Every customer, including Dee with no orders:
SELECT c.name, COUNT(o.order_id) AS order_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY c.customer_id;
-- Expected: Ada 2, Ben 2, Cleo 1, Dee 0.''')+code('''-- Count paid orders without accidentally dropping zero-order customers:
SELECT c.name,
       COUNT(o.order_id) FILTER (WHERE o.status = 'paid') AS paid_orders
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY c.customer_id;''')+figure('fig-joins','LEFT JOIN preserves the unmatched side','Why does Dee still appear?',svgwrap(svgbox(25,35,300,150,'customers (left)','Ada · Ben · Cleo · Dee')+svgbox(475,35,300,150,'orders (right)','100, 101 · 102, 104 · 103')+arrow(325,100,475,100)+'<text x="315" y="215" font-size="13" fill="#b65c4e">Dee → NULL order fields → COUNT(order_id) = 0</text>',240),'A LEFT JOIN retains Dee even though there is no matching order; COUNT(non-null column) returns zero.',['Dee','NULL','COUNT'])+prose('Common trap: placing <code>o.status = \'paid\'</code> in WHERE after a LEFT JOIN removes unmatched customers. Move the condition into the ON clause or use conditional aggregation, depending on the question.')
sections['analysis']=prose('Analytics begins by defining a metric. For paid revenue, use paid orders only and multiply each line item’s quantity by its captured sale price. For customer behavior, aggregate at the customer grain before ranking.')+code('''WITH customer_revenue AS (
 SELECT c.customer_id, c.name,
        COALESCE(SUM(oi.quantity * oi.unit_price)
          FILTER (WHERE o.status = 'paid'),0) AS paid_revenue
 FROM customers c
 LEFT JOIN orders o ON o.customer_id = c.customer_id
 LEFT JOIN order_items oi ON oi.order_id = o.order_id
 GROUP BY c.customer_id, c.name
)
SELECT name, paid_revenue,
       DENSE_RANK() OVER (ORDER BY paid_revenue DESC) AS revenue_rank
FROM customer_revenue
ORDER BY paid_revenue DESC, name;''')+code('''SELECT p.category,
       SUM(oi.quantity) AS units_sold,
       SUM(oi.quantity * oi.unit_price) AS revenue
FROM products p
JOIN order_items oi ON oi.product_id = p.product_id
JOIN orders o ON o.order_id = oi.order_id AND o.status = 'paid'
GROUP BY p.category
ORDER BY revenue DESC;''')+figure('fig-analysis','Define the metric before ranking','What does the ranking include and exclude?',svgwrap(svgbox(18,42,240,130,'Eligible rows','status = paid only')+svgbox(285,42,240,130,'Customer totals','Ada $46 · Ben $8')+svgbox(552,42,230,130,'Ranking','1 Ada · 2 Ben')+arrow(258,104,285,104)+arrow(525,104,552,104)),'Paid-only filtering precedes ranking; pending and cancelled items do not enter revenue.',['paid','revenue','rank'])+prose('For a true cohort analysis, first define a customer’s first paid order date and group by that month. Be careful with sparse data: a cohort with one customer cannot support reliable retention conclusions.')
sections['performance']=prose('PostgreSQL uses statistics and cost estimates to choose among scans, joins, sorts, and aggregation strategies. <code>EXPLAIN</code> shows the planned operations; <code>EXPLAIN (ANALYZE, BUFFERS)</code> executes the query and reports actual rows/timing and buffer activity. Use ANALYZE only when executing the statement is safe.')+code('''EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT * FROM orders
WHERE customer_id = 1
ORDER BY ordered_on DESC;

CREATE INDEX idx_orders_customer_date
ON orders (customer_id, ordered_on DESC);
ANALYZE orders;

EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM orders
WHERE customer_id = 1
ORDER BY ordered_on DESC;''')+figure('fig-performance','Reading a plan without guessing','What do estimated rows, actual rows, and buffers tell you?',svgwrap(svgbox(20,30,355,165,'Plan node: Seq Scan','cost=0.00..12.50 rows=2')+svgbox(425,30,355,165,'Runtime observation','actual rows=2 loops=1')+'<text x="40" y="114" font-size="13">Planner estimate (illustrative)</text><text x="445" y="114" font-size="13">Observed cardinality</text><text x="445" y="145" font-size="13">Buffers: shared hit/read</text>'),'Plan costs are planner units, not milliseconds. The pictured cost is illustrative; your actual plan will differ.',['cost','actual rows','buffers'])+prose('On a five-row table, a sequential scan can be faster than an index scan. That is not a failure. Indexes become valuable when they avoid reading many irrelevant rows, but they also consume storage and slow writes. Do not claim a speedup until you compare measured plans on appropriately sized data.')
sections['diagnose']=prose('Performance diagnosis is a hypothesis-driven loop: identify the slow query, collect its plan, compare estimated and actual row counts, check filtering and join cardinality, consider an index or rewrite, then measure again under comparable conditions.')+code('''-- Run before and after each change; save both plans.
EXPLAIN (ANALYZE, BUFFERS)
SELECT o.customer_id, COUNT(*)
FROM orders o
WHERE o.status = 'paid'
  AND o.ordered_on >= DATE '2026-03-01'
GROUP BY o.customer_id;

CREATE INDEX idx_orders_paid_date_customer
ON orders (ordered_on, customer_id)
WHERE status = 'paid';
ANALYZE orders;''')+figure('fig-diagnose','The performance investigation loop','What evidence justifies changing a query?',svgwrap(svgbox(15,55,170,80,'1. Baseline','time + buffers')+svgbox(220,55,170,80,'2. Hypothesis','selectivity / join')+svgbox(425,55,170,80,'3. Change','index or SQL')+svgbox(630,55,155,80,'4. Retest','same workload')+arrow(185,95,220,95)+arrow(390,95,425,95)+arrow(595,95,630,95)+'<path d="M700 140 V195 H95 V140" fill="none" stroke="#a96c54" stroke-width="2" marker-end="url(#arr)"/>',230),'Retest under comparable conditions and keep the baseline. Never infer an improvement solely from the existence of an index.',['baseline','hypothesis','index','retest'])+prose('Watch for estimated versus actual row count mismatches, unexpectedly large intermediate joins, sorts spilling to disk, and repeated nested-loop work. In real systems, use <code>pg_stat_statements</code> when available to find high-total-time queries; it may require administrator setup.')
sections['production']=prose('Development convenience is not a production security model. Create separate application roles with minimum permissions; do not connect an app as postgres. Use environment variables or a secrets manager for credentials, TLS where required, and parameterized queries to avoid injection.')+code('''BEGIN;
UPDATE products SET price = price + 1 WHERE product_id = 10;
SELECT product_id, price FROM products WHERE product_id = 10;
ROLLBACK; -- Safe experiment: no permanent change

-- Example backup from your shell:
-- pg_dump -h localhost -U analyst -d shoplab -Fc -f shoplab.dump''')+figure('fig-production','A safe change is reversible','How does a transaction protect exploratory updates?',svgwrap(svgbox(20,60,210,90,'BEGIN','start transaction')+svgbox(290,60,210,90,'UPDATE + SELECT','inspect effect')+svgbox(560,60,215,90,'ROLLBACK','undo changes')+arrow(230,105,290,105)+arrow(500,105,560,105)),'A rollback discards changes made in the transaction. A COMMIT would make them durable.',['BEGIN','UPDATE','ROLLBACK'])+prose('A backup is not verified until you can restore it in a separate environment. For deeper learning, practice concurrent transactions, isolation levels, foreign-key indexing, vacuum/analyze, and query-plan comparisons on a larger synthetic dataset.')
css='''
:root{--ink:#243831;--muted:#64756d;--paper:#faf7ef;--card:#fffefa;--line:#d9ded3;--teal:#386b61;--coral:#af604d;--sand:#f3e8d4}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.75 Georgia,serif}a{color:var(--teal)}.top{background:#203b35;color:#f5f0e4;padding:12px 5%;font:600 12px/1.5 system-ui;letter-spacing:.16em}.progress{height:3px;position:fixed;top:0;left:0;background:#cf8d67;z-index:20;width:0}.hero{max-width:1180px;margin:auto;padding:75px 30px 50px;border-bottom:1px solid var(--line)}.eyebrow{font:700 11px/1.4 system-ui;letter-spacing:.15em;text-transform:uppercase;color:var(--coral)}h1,h2,h3,h4{line-height:1.16;letter-spacing:-.025em}h1{font-size:clamp(42px,5.5vw,78px);max-width:900px;margin:18px 0}h2{font-size:clamp(29px,3vw,42px);margin:0 0 24px}h3{font-size:24px;margin-top:36px}h4{font-size:22px;margin:5px 0 15px}.deck{font-size:22px;max-width:760px;color:#52645c}.meta{font:13px system-ui;color:var(--muted);margin-top:20px}.layout{max-width:1280px;margin:auto;display:grid;grid-template-columns:260px minmax(0,820px);gap:70px;padding:42px 30px}.toc{position:sticky;top:25px;align-self:start;max-height:92vh;overflow:auto;font:13px/1.5 system-ui}.toc strong{display:block;margin:0 0 18px;letter-spacing:.1em;text-transform:uppercase}.toc a{display:block;padding:9px 10px;text-decoration:none;color:#4c6259;border-left:2px solid #d8ded3}.toc a.active{border-color:var(--coral);background:#f3ede0;color:#1b4236;font-weight:700}.chapter{border-bottom:1px solid var(--line);padding:40px 0 65px;scroll-margin-top:30px}.chapter .num{font:700 12px system-ui;letter-spacing:.2em;color:var(--coral)}p{margin:18px 0}code,pre{font:13px/1.65 ui-monospace,SFMono-Regular,Consolas,monospace}p code{background:#edece3;padding:2px 5px;border-radius:3px}pre{margin:0 0 25px;background:#223a34;color:#f5f1e9;padding:22px;overflow-x:auto;white-space:pre;tab-size:2}.code-head{display:flex;align-items:center;justify-content:space-between;background:#304c43;color:#dfecdf;padding:8px 18px;font:700 11px system-ui;letter-spacing:.13em}.copy{background:transparent;color:#f4f3e9;border:1px solid #829b8c;border-radius:4px;padding:4px 12px;cursor:pointer}figure{margin:38px 0;background:var(--card);border:1px solid var(--line);padding:22px 24px 17px;box-shadow:0 8px 22px #3c55470a}.figure-heading{border-bottom:1px solid var(--line);padding-bottom:12px}.art{overflow-x:auto;padding:18px 0}.art svg{display:block;min-width:500px;width:100%;height:auto}figcaption{font:13px/1.6 system-ui;color:#58685f;border-top:1px solid var(--line);padding-top:12px}.callout{border-left:4px solid var(--coral);background:#f4e9da;padding:14px 22px;font:15px/1.6 system-ui}.footer{max-width:850px;margin:30px auto 90px;padding:0 24px;font:14px/1.7 system-ui}.mobile-toc{display:none}.resource a{display:block;margin:8px 0}@media(max-width:850px){.layout{display:block;padding:20px}.toc{display:none}.mobile-toc{display:block;margin:20px;border:1px solid var(--line);padding:12px;font:14px system-ui}.mobile-toc a{display:block;padding:7px}.hero{padding:50px 20px 25px}.chapter{padding-top:40px}figure{margin-left:0;margin-right:0;padding:12px}.art svg{min-width:450px}}@media print{.toc,.mobile-toc,.copy,.progress{display:none}.layout{display:block}.chapter{break-inside:avoid}body{background:white}}
'''
links=''.join(f'<a href="#{id}">{n} · {name}</a>' for id,n,name,_ in chapters)
body=''.join(f'<section class="chapter" id="{id}"><div class="num">CHAPTER {n}</div><h2 id="h-{id}">{name}</h2><p class="deck">{desc}</p>{sections[id]}</section>' for id,n,name,desc in chapters)
htmltext=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PostgreSQL, from First Connection to Query Plans</title><style>{css}</style></head><body><div class="progress" id="progress"></div><div class="top">THE ILLUSTRATED ENGINEERING FIELD GUIDE · POSTGRESQL</div><header class="hero"><div class="eyebrow">Hands-on edition · 12 chapters · 12 annotated figures</div><h1>PostgreSQL, from First Connection to Query Plans</h1><p class="deck">Install the server. Connect with VS Code. Build a small store database. Write joins and aggregates. Learn to read the work behind a query.</p><p class="meta">Practical walkthrough · PostgreSQL SQL · Sample dataset included · Original diagrams · Offline HTML</p><div class="callout">This is a reproducible teaching example, not a performance benchmark. Server commands depend on your OS and PostgreSQL version; query plans depend on your actual data and environment.</div></header><details class="mobile-toc"><summary>Table of contents · 12 chapters</summary>{links}</details><div class="layout"><nav class="toc" aria-label="Table of contents"><strong>Contents</strong>{links}</nav><main>{body}</main></div><footer class="footer"><h2 id="sources">Primary documentation and further reading</h2><div class="resource"><a href="https://www.postgresql.org/docs/current/tutorial.html">PostgreSQL official tutorial</a><a href="https://www.postgresql.org/docs/current/using-explain.html">PostgreSQL: Using EXPLAIN</a><a href="https://www.postgresql.org/docs/current/sql-select.html">PostgreSQL: SELECT syntax</a><a href="https://www.postgresql.org/docs/current/indexes.html">PostgreSQL: Indexes</a><a href="https://code.visualstudio.com/docs">Visual Studio Code documentation</a></div><p>Source links are official references. Commands were authored for this guide; no PostgreSQL server execution is claimed unless separately recorded in the QA report.</p></footer><script>const sections=[...document.querySelectorAll('.chapter')],links=[...document.querySelectorAll('.toc a')];function update(){{const max=document.documentElement.scrollHeight-innerHeight;document.getElementById('progress').style.width=(max>0?100*scrollY/max:0)+'%';let current=sections[0];for(const s of sections){{if(s.getBoundingClientRect().top<180)current=s}}links.forEach(a=>a.classList.toggle('active',a.hash==='#'+current.id))}}addEventListener('scroll',update,{{passive:true}});update();</script></body></html>'''
(E/'postgresql-guide.html').write_text(htmltext)
(P/'schema_and_seed.sql').write_text(re.search(r'CREATE TABLE customers.*?PRIMARY KEY \(order_id, product_id\)\n\);',sections['schema'],re.S).group(0).replace('&gt;','>') if False else '-- Copy SQL blocks from the HTML guide in chapter order.\n')
# extract sql blocks and decode into one psql file
from bs4 import BeautifulSoup
soup=BeautifulSoup(htmltext,'html.parser'); sql=[]
for c in soup.find_all('pre'):
 if c.find_previous_sibling('div',class_='code-head') and c.find_previous_sibling('div',class_='code-head').get_text().startswith('SQL'):
  sql.append(c.get_text())
(P/'all_examples.sql').write_text('-- Execute selectively: includes EXPLAIN, schema reset, and a transaction rollback.\n\n'+'\n\n'.join(sql))
# manifests intentionally report unreviewed status until actual browser inspection
sources=[dict(id='pgdocs',url='https://www.postgresql.org/docs/current/tutorial.html',title='PostgreSQL official tutorial',verified=False),dict(id='pgexplain',url='https://www.postgresql.org/docs/current/using-explain.html',title='Using EXPLAIN',verified=False),dict(id='vscode',url='https://code.visualstudio.com/docs',title='Visual Studio Code documentation',verified=False)]
claims=[dict(id=f'C{i+1}',source_id='pgdocs' if i!=9 else 'pgexplain',source_locator='official documentation; topic '+id,verification='not_independently_checked',status='covered',destination_anchor=id) for i,(id,*_) in enumerate(chapters)]
(P/'research_inventory.json').write_text(json.dumps(dict(mode='general',sources=sources,claims=claims),indent=2))
(P/'chapter_matrix.json').write_text(json.dumps(dict(chapters=[dict(id=id,html_anchor=id,prerequisites='Prior chapters or basic computer literacy',problem=desc,intuition='Explanations and examples in chapter',diagram_figure_id='fig-'+id,variables_and_shapes='SQL tables and row cardinality; not tensor-shaped',derivation='SQL query semantics and illustrated row flow',numerical_trace='Sample dataset and expected outputs',implementation='Executable SQL in guide',tests='SQL semantic checks; PostgreSQL execution pending',limitations='Small illustrative dataset; not representative of production',tests_run=False,review_status='pending') for id,_,_,desc in chapters]),indent=2))
(P/'figure_storyboard.json').write_text(json.dumps(dict(figures=figs),indent=2))
(P/'README.md').write_text('# PostgreSQL v8 skill test\n\nOpen `examples/postgresql-guide.html` locally. This is a new topic test of the general-purpose illustrated textbook mode, not source-audit mode. `all_examples.sql` collects SQL examples. See `PUBLICATION_REPORT.md` and `QA_REPORT.md` for what was and was not verified.\n')
print('HTML',len(htmltext),'figures',len(figs),'chapters',len(chapters),'SQL blocks',len(sql))
