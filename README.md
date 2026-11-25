# Illustrated Technical Guide v5

Two modes in one Claude Code skill:

- **General illustrated textbook**: `/illustrated-technical-guide Explain transformer attention from first principles`.
- **Source-audited reconstruction**: `/illustrated-technical-guide Reconstruct https://www.thelion.ai/projects/meddecider/ in source-audit mode`.

The second mode does not replace the first. Install this directory as `.claude/skills/illustrated-technical-guide/`. Open `examples/meddecider-guide.html` directly in a browser. `scripts/upgrade_meddecider.py` documents the deterministic enrichment of the prior test page.

Use `python scripts/test_source_coverage.py` and `python examples/reproduction_demo.py` to check the package.


## v6 visual direction
The skill now includes a source-safe editorial illustration system: warm paper, annotated multi-panel figures, visual grammar selection, SVG-first technical diagrams, and figure-level QA. The MedDecider example upgrades the hero and first three figures with substantial original explanatory art. Other figures retain their content with improved styling and figure headings; this is not a complete 13-figure redraw.
