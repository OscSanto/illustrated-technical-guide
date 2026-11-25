// Render TeX to standalone SVG with MathJax 3 (the mathjax-full npm package).
// Usage: echo '["a^2+b^2=c^2"]' | node render_math.cjs   -> JSON array of SVG strings on stdout
// Finds mathjax-full in: $MATHJAX_DIR, then normal Node resolution (local node_modules), then the global npm root.
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

function findMathJax() {
  const tries = [];
  if (process.env.MATHJAX_DIR) tries.push(process.env.MATHJAX_DIR);
  try { tries.push(path.dirname(require.resolve('mathjax-full/package.json', { paths: [process.cwd(), __dirname] }))); } catch (e) {}
  try { tries.push(path.join(execSync('npm root -g', { encoding: 'utf8' }).trim(), 'mathjax-full')); } catch (e) {}
  const hit = tries.find(d => fs.existsSync(path.join(d, 'js', 'mathjax.js')));
  if (!hit) {
    console.error('mathjax-full not found. Run "npm install mathjax-full@3" here or globally, or set MATHJAX_DIR.');
    process.exit(1);
  }
  return path.join(hit, 'js');
}

const base = findMathJax();
const { mathjax } = require(path.join(base, 'mathjax.js'));
const { TeX } = require(path.join(base, 'input', 'tex.js'));
const { AllPackages } = require(path.join(base, 'input', 'tex', 'AllPackages.js'));
const { SVG } = require(path.join(base, 'output', 'svg.js'));
const { liteAdaptor } = require(path.join(base, 'adaptors', 'liteAdaptor.js'));
const { RegisterHTMLHandler } = require(path.join(base, 'handlers', 'html.js'));

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const doc = mathjax.document('', { InputJax: new TeX({ packages: AllPackages }), OutputJax: new SVG({ fontCache: 'none' }) });
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
process.stdout.write(JSON.stringify(input.map(x => adaptor.outerHTML(doc.convert(x, { display: true })))));
