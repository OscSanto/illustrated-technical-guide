# Illustrated Technical Guide v14 — Cross-topic visual benchmark (development build)

This is the v13 skill plus a **cross-topic transfer test**. It demonstrates the same figure design and zoom/pan controls for a PostgreSQL LEFT JOIN and a transformer attention numerical example.

## Open the examples
- `examples/cross-topic-benchmark/postgresql/index.html`
- `examples/cross-topic-benchmark/attention/index.html`
- `reports/BENCHMARK_REPORT.md` (results and limitations)
- `reports/BROWSER_RESULTS.json`, `reports/SCORECARD.csv` (machine-readable evidence)

## Claims and boundaries
- The custom SVGs render and the figure viewer works in desktop and mobile Chromium **using inlined SVG contents via page.set_content**; direct local and HTTP navigation are prohibited in this test runtime.
- The Python attention example was executed. The SQL join result was cross-checked in SQLite only, **not PostgreSQL**.
- The v13 pytest suite passes. AntV rendering did **not** run because registry access is blocked.
- These are authored topic fixtures, **not independent model generations**. Neither cross-run reliability nor full Jev content accuracy is certified.

The two independent skill capabilities remain unchanged: original educational guides and optional source-faithful reconstruction.

## Installation
Copy `skills/illustrated-technical-guide` into your project's `.claude/skills` directory, including all referenced files, or retain this repository for tests and examples.
