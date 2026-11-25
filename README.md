# Illustrated Technical Guide v5

Two modes in one Claude Code skill:

- **General illustrated textbook**: `/illustrated-technical-guide Explain transformer attention from first principles`.
- **Source-audited reconstruction**: `/illustrated-technical-guide Reconstruct https://www.thelion.ai/projects/meddecider/ in source-audit mode`.

The second mode does not replace the first. Install this directory as `.claude/skills/illustrated-technical-guide/`. Open `examples/meddecider-guide.html` directly in a browser. `scripts/upgrade_meddecider.py` documents the deterministic enrichment of the prior test page.

Use `python scripts/test_source_coverage.py` and `python examples/reproduction_demo.py` to check the package.


## v6 visual direction
The skill now includes a source-safe editorial illustration system: warm paper, annotated multi-panel figures, visual grammar selection, SVG-first technical diagrams, and figure-level QA. The MedDecider example upgrades the hero and first three figures with substantial original explanatory art. Other figures retain their content with improved styling and figure headings; this is not a complete 13-figure redraw.

Version 7: display equations are pre-rendered as embedded MathJax SVG for offline, correctly typeset mathematical notation. See scripts/test_math.py.


## Version 8: enforceable editorial gates
General textbook mode and optional source-audit mode remain separate. New research_inventory.json, chapter_matrix.json, figure_storyboard.json and scripts/publication_gate.py require evidence, explanatory depth, technical illustration storyboards and actual desktop/mobile reviews. Run `python scripts/publication_gate.py --root . --html examples/meddecider-guide.html`. The bundled MedDecider v7 example is intentionally marked **DRAFT** until gaps are closed; failing the gate is the intended behavior. See PUBLICATION_REPORT.md.
