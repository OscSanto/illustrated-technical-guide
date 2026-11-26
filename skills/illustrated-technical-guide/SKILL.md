---
name: illustrated-technical-guide
description: Writes deep, illustrated, tested explanations of how a technical system works
  (models, algorithms, databases, protocols, code repositories) as one offline HTML guide
  with labs, figures and cited claims. Use when someone asks how something works
  "in depth", "mechanically" or "step by step", or asks to explain a repository or paper.
---
# Illustrated Technical Guide — depth-first illustrated technical teaching

## Two independent capabilities
- **Generate (default):** research and author an original, approachable, illustrated technical textbook from a topic. Do not require a reference article.
- **Reconstruct (opt-in):** source-faithful educational reconstruction of a supplied article/paper/repository. For code repositories, read `references/repository-reconstruction.md` first. Apply all common requirements PLUS the source fidelity workflow. Never infer proprietary internals.

## Repository fidelity rule
When a user links a code repository and requests how it works, activate source-audited repository reconstruction even if they never explicitly say “illustrated guide.” Inspect entry points and implementation rather than relying only on README. Produce actual data-lineage, storage, execution, concurrency and hardware-evidence maps when relevant. Preserve original code semantics and call out gaps.

## Depth-first mechanism gate (mandatory)
Read `references/depth-first-teaching.md` before outlining or drafting. Use concise orientation and deep mechanisms. For each dense technical chapter, trace one input through actual intermediate states, calculations, code, and outputs. Explain why transformations happen and what changes under alternate inputs. Depth follows conceptual complexity, not a universal word count. Keep provenance visible but quiet in captions/ledger so the narrative teaches instead of repeating audit caveats.

## Start here — choose teaching profile
Read `profiles/hands-on.md`, `profiles/conceptual.md`, `profiles/mathematical.md`, or `profiles/source-audit.md` based on the **learner's goal**, not an arbitrary topic category. Mix profiles by chapter as needed. Use `references/pedagogy.md` for learning objectives and prerequisite ordering. Do **not** require a derivation in a setup chapter or an installation walkthrough in a theory chapter. A guide can combine tutorial, explanation, how-to and reference, but label these purposes.

## Working agreement (mandatory)
1. State intended learner and starting knowledge. Choose a recurring, minimally sized but authentic example. Write measurable learning objectives and a dependency-ordered outline.
2. **Research responsibly.** Read `references/research.md`. Use primary technical sources when possible and track claims in `research_inventory.json`. Unbrowsed URLs are unverified. Never fabricate citations, measurements, APIs, or tests.
3. **Storyboard instructional figures.** Read `references/illustrations.md`. Illustrations must reveal a real operation, trace, state change, or tradeoff. Use `references/antv-illustration-engine.md` to choose optional AntV infographics or mechanism-specific custom SVG. Use original accessible SVG/HTML by default. For every figure, decide whether it needs animation by testing it against the four signs in `references/animated-flow-figures.md`: order, waiting, repetition, merging or splitting. Record the decision and the signs as `animate` in `figure_storyboard.json`. Animated figures use the optional `dashmotion` skill for topology plus journeys when it is installed, and hand-written SVG otherwise. Hand-written SVG is also required for queues, batches and measured timing. Do not use unverified numbers as measurements.
4. **Implement exercises and verification.** Read `references/execution.md`. In hands-on chapters, every milestone yields observable results plus troubleshooting. Distinguish executable/tested, executable/untested and pseudocode; always identify what code was created by us vs. adapted from a source.
5. **Write for reading.** Read `references/reading-design.md` and build the page from `templates/standalone.html` (page design with TheLion.AI header typography, fonts embedded). Every chapter opens with a one- or two-sentence lede. Keep paragraphs short. Use bridging tables for half-known ideas, numbered citations for facts, and claim badges (`published`, `measured`, `inferred`, `self-reported`, `our lab`) tied to claim ids in `research_inventory.json`.
6. **Make every artifact traceable.** Read `references/provenance.md`. Visible origin labels for code, pseudocode, equations, datasets, architecture diagrams, tables and benchmarks, with machine-readable metadata. In reconstruct mode, claim-by-claim coverage and uncertainty are mandatory.
7. **Publish responsive standalone HTML.** Use `templates/standalone.html` (see step 5), with generated nested TOC, accessible headings, offline-readable formulas (`scripts/render_math.cjs`, see `profiles/mathematical.md`), labeled diagrams, per-figure zoom/pan for dense SVGs, downloadable labs, mobile layout, and source links. Original authoring files may be modular; the final HTML export should be portable.
8. **Cross-topic figure gate.** For any new illustration engine or style, test at least two unrelated topic mechanisms (for example database joins and attention). Use numeric or relational assertions, desktop and mobile rendered screenshots, visible provenance, functional keyboard/zoom controls, and report whether any external renderer was actually executed. Distinguish hand-built fixtures from independent model generations.
9. **Depth audit.** Prepare `mechanism_traces.json` with per-chapter evidence for input, ordered operations, intermediate states, computed or tested outcome, parameter variation, failure modes, and source locators. Run `python scripts/depth_gate.py --guide <guide-directory>`. Structural results are only a minimum; semantically review major chapters.
10. **Gate and repair.** Run `python scripts/quality_gate.py --guide <guide-directory>`. Run actual code tests and inspect real browser screenshots when available. Resolve blockers in up to 3 repair cycles, writing `REPAIR_LOG.md` with evidence. If unverified, publish clearly as DRAFT; never flip evidence fields merely to pass.
11. **Evaluate transfer.** Refer to `../../evals/README.md` (the repository's `evals/` folder) and run multiple unrelated prompt cases across repeated independent generations. CI-only structural PASS is not an LLM consistency score.

## Output contract
Produce: `index.html`, `guide_manifest.json`, `artifact_provenance.json`, `research_inventory.json`, `figure_storyboard.json`, `mechanism_traces.json`, runnable labs as appropriate, `RUN_LOG.json` with real commands/results, and `QUALITY_REPORT.json`/`.md`. Add `source_coverage.csv` in reconstruct mode. Each critical omitted item remains a blocker. Cite docs in the guide where a fact is used.

## Safety / source fidelity
Source-reported ≠ independently reproduced; plausible architecture ≠ documented internals; mathematical validity ≠ evidence of actual implementation; synthetic ≠ observed benchmark. Source adaptations need locators and change notes. Rephrase copyrighted sources instead of copying long passages or their diagrams. When browser, runtime, or source access is missing, state what is unverified and do not claim a PASS.

## Compatibility
`source_fidelity_gate.py` and `publication_gate.py` are retained under `scripts/` for older manifests. `quality_gate.py` is the main, profile-aware entry point. Do not let legacy universal chapter-field requirements force irrelevant content into a chapter.
