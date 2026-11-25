---
name: illustrated-technical-guide
description: Create original deeply explained, illustrated, testable CS learning guides and HTML textbooks; optionally reconstruct a supplied technical article or paper faithfully with claim-level provenance. Use for hands-on tutorials, mathematical walkthroughs, architecture explainers, and source-audited reconstructions.
---
# Illustrated Technical Guide v11

## Two independent capabilities
- **Generate (default):** research and author an original, approachable, illustrated technical textbook from a topic. Do not require a reference article.
- **Reconstruct (opt-in):** source-faithful educational reconstruction of a supplied article/paper/repository. Apply all common requirements PLUS the source fidelity workflow. Never infer proprietary internals.

## Start here — choose teaching profile
Read `profiles/hands-on.md`, `profiles/conceptual.md`, `profiles/mathematical.md`, or `profiles/source-audit.md` based on the **learner's goal**, not an arbitrary topic category. Mix profiles by chapter as needed. Use `references/pedagogy.md` for learning objectives and prerequisite ordering. Do **not** require a derivation in a setup chapter or an installation walkthrough in a theory chapter. A guide can combine tutorial, explanation, how-to and reference, but label these purposes.

## Working agreement (mandatory)
1. State intended learner and starting knowledge. Choose a recurring, minimally sized but authentic example. Write measurable learning objectives and a dependency-ordered outline.
2. **Research responsibly.** Read `references/research.md`. Use primary technical sources when possible and track claims in `research_inventory.json`. Unbrowsed URLs are unverified. Never fabricate citations, measurements, APIs, or tests.
3. **Storyboard instructional figures.** Read `references/illustrations.md`. Illustrations must reveal a real operation, trace, state change, or tradeoff. Use original accessible SVG/HTML by default. Do not use unverified numbers as measurements.
4. **Implement exercises and verification.** Read `references/execution.md`. In hands-on chapters, every milestone yields observable results plus troubleshooting. Distinguish executable/tested, executable/untested and pseudocode; always identify what code was created by us vs. adapted from a source.
5. **Make every artifact traceable.** Read `references/source-fidelity.md`. Visible origin labels for code, pseudocode, equations, datasets, architecture diagrams, tables and benchmarks, with machine-readable metadata. In reconstruct mode, claim-by-claim coverage and uncertainty are mandatory.
6. **Publish responsive standalone HTML.** Use `templates/standalone.html` as a starting point, with generated nested TOC, accessible headings, offline-readable formulas, labeled diagrams, downloadable labs, mobile layout, and source links. Original authoring files may be modular; the final HTML export should be portable.
7. **Gate and repair.** Run `python scripts/quality_gate.py --guide <guide-directory>`. Run actual code tests and inspect real browser screenshots when available. Resolve blockers in up to 3 repair cycles, writing `REPAIR_LOG.md` with evidence. If unverified, publish clearly as DRAFT; never flip evidence fields merely to pass.
8. **Evaluate transfer.** Refer to `../../../evals/README.md` in the repository and run multiple unrelated prompt cases across repeated independent generations. CI-only structural PASS is not an LLM consistency score.

## Output contract
Produce: `index.html`, `guide_manifest.json`, `artifact_provenance.json`, `research_inventory.json`, `figure_storyboard.json`, runnable labs as appropriate, `RUN_LOG.json` with real commands/results, and `QUALITY_REPORT.json`/`.md`. Add `source_coverage.csv` in reconstruct mode. Each critical omitted item remains a blocker. Cite docs in the guide where a fact is used.

## Safety / source fidelity
Source-reported ≠ independently reproduced; plausible architecture ≠ documented internals; mathematical validity ≠ evidence of actual implementation; synthetic ≠ observed benchmark. Source adaptations need locators and change notes. Rephrase copyrighted sources instead of copying long passages or their diagrams. When browser, runtime, or source access is missing, state what is unverified and do not claim a PASS.

## Compatibility
Original v10 provenance validator and v10 publication validator are retained under `scripts/` for legacy manifests. `quality_gate.py` is the v11 profile-aware entry point. Do not let legacy universal chapter-field requirements force irrelevant content into a chapter.
