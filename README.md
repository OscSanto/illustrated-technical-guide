# Illustrated Technical Guide v5

Two modes in one Claude Code skill:

- **General illustrated textbook**: `/illustrated-technical-guide Explain transformer attention from first principles`.
- **Source-audited reconstruction**: `/illustrated-technical-guide Reconstruct https://www.thelion.ai/projects/meddecider/ in source-audit mode`.

The second mode does not replace the first. Install this directory as `.claude/skills/illustrated-technical-guide/`. Open `examples/meddecider-guide.html` directly in a browser. `scripts/upgrade_meddecider.py` documents the deterministic enrichment of the prior test page.

Use `python scripts/test_source_coverage.py` and `python examples/reproduction_demo.py` to check the package.
