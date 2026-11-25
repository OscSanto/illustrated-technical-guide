---
name: illustrated-technical-guide
description: Research, write, illustrate, implement, test, and publish substantial original standalone HTML technical textbooks with a dynamic nested contents menu. Invoke when user asks for a comprehensive illustrated guide, detailed mathematical reconstruction, or technical learning microsite.
---
# Illustrated Technical Guide v8 — research-to-publication

## Invocation
Explicit in Claude Code: `/illustrated-technical-guide <topic>`. Implicit selection is possible when the description matches. The skill creates `index.html`, a source ledger, runnable examples, and a validation report. It must not deliver a skeletal overview as a completed textbook.

## Seven required phases, with gates
1. **Research:** Collect original papers, primary product documentation, reproducible repositories, and benchmark reports. Record URLs and exact claims in `sources.md`. Separate published, independently measured, self-reported, inferred, and illustrative claims. Never invent measurements, papers, or unpublished model internals. If browsing is unavailable, explicitly limit claims.
2. **Outline:** Define audience and outcomes; build a dependency graph of concepts. Create as many chapters as needed to explain the subject (not a fixed count), and a recurring example. For every concept, record prerequisites, equations, figures, implementation, and test.
3. **Teach:** Each major algorithm gets problem → intuition → formal definitions and shapes → derivation with intermediate steps → numerical trace → pseudocode → executable implementation → verification → failure modes. Include comparisons with alternatives and explain *why* design choices exist. No undefined symbols, placeholders, or compressed derivations.
4. **Illustrate:** Original vector diagrams answer concrete questions. Use workflows for sequences, tensor/matrix diagrams for computation, parallel views for comparisons, curves for sourced experiments, and feedback loops for training. Every figure must have meaningful alt text, numbered caption, and explanatory paragraph. Do not draw invented data as measured.
5. **Implement:** Ship runnable minimal examples and unit tests. Record environment, inputs, expected outputs, and known differences from proprietary systems. Use small, CPU-friendly demonstrations where possible.
6. **Validate:** Run static HTML audit, execute every standalone code block or extracted lab, verify numerical examples, check citations and claims, test heading links, and inspect rendered desktop/mobile screenshots when a browser is available. Record what could not be tested. Fix errors before delivery.
7. **Publish:** Deliver standalone HTML plus ZIP with skill, source ledger, lab, and QA report. Do not claim the page is as complete as a reference unless evidence supports it.

## Depth and editorial quality gate
- No chapter may be only a few sentences of summary. Each chapter must materially advance the reconstruction and carry its own detailed example, derivation, procedure, experiment, or evidence.
- For quantitative claims: identify provenance, hardware, sample size, and uncertainty. For synthetic charts: label illustrative in caption and text.
- When relevant, show one forward pass and one backward update, with hand-calculated intermediate values and assertions.
- When a diagram represents a simplified conceptual mechanism, say what it omits.
- Provide meaningful evaluation protocols: train/validation/test separation, baselines, calibration, latency, option-order robustness, adversarial cases, and safe fallback.
- Reserve source citations for verified claims; distinguish a public API from a hypothetical reconstruction.

## HTML and navigation requirements
Use `template.html` as the design starting point. Generate a self-contained HTML page with accessible semantic sections, restrained editorial styling, responsive figures, printable layout, sticky desktop TOC and mobile TOC. Generate TOC from actual h2/h3 headings, preserve unique IDs and working anchors, show progress and active section. The number of chapters follows the subject, not the template. Keep useful links when JS is disabled.

## Test commands
`python scripts/validate_guide.py examples/jev-guide.html`
`python scripts/test_lab.py`
Check `QA_REPORT.md` for test scope and limitations.

## Reference example
`examples/jev-guide.html` is an original Jev-like engineering textbook example. It is NOT a reconstruction of proprietary TypeSafe model weights or internal training procedure. Use it to inspect visual composition, explanation density, math, and source distinctions; do not copy its subject-specific content into unrelated guides.

## Optional source-faithful reconstruction mode (v5)
**Preserve the general illustrated textbook workflow above.** Enable this mode when the user supplies a reference URL/document or asks to audit/reproduce a specific technical project. Do not activate for generic subject explanations unless requested.

1. **Source inventory gate:** Retrieve and read the entire primary reference, its linked official code/model cards where accessible, and record each section, numerical claim, table, dataset, hyperparameter, implementation detail, example, license, and limitation in `source_coverage.csv`. Never imply that a linked source was checked if it wasn't.
2. **Coverage map:** For each source claim, assign an ID, source URL/section, exact numeric value, provenance (developer-reported / independently verified / inference / illustration), destination guide heading, and status (covered, partially covered, absent, unverifiable). Preserve negative findings and caveats.
3. **Technical reconstruction:** Distinguish literal documented implementation from pedagogical NumPy/PyTorch demonstrations. Include published configurations and hyperparameters, input/output contracts, mathematical derivations, datasets and splits, evaluation definitions, full comparison tables where useful, and failure modes. Never present synthetic values as benchmark measurements.
4. **No silent source drift:** Compare tables and values against the primary page. Flag discrepancies within the source (e.g. category counts not summing to reported totals) rather than repairing them silently. Do not substitute plausible model internals for documented details.
5. **Audit gate:** Run a coverage checker on the ledger, execute runnable examples, verify table rows and navigation, record whether actual model weights/benchmarks and rendered browser screenshots were tested. Require 100% disposition of *critical* source claims; unresolved claims must be labeled, not quietly dropped.
6. **Deliverables:** The HTML, source ledger, coverage report, executable lab, QA report, and complete skill ZIP. The skill remains general-purpose; this mode is an opt-in extension.

Invocation: `/illustrated-technical-guide Reconstruct <URL> in source-audit mode, with a claim-by-claim coverage report.`


## Illustration art direction — v6 (mandatory for both modes)
The reference's strength is **editorial information design**, not generic flowchart boxes. Adopt the following *transferable visual principles* without copying the site's proprietary images, mascots, illustrations, or branding:

1. **Figure storyboard before drawing.** For each conceptual bottleneck write: question the figure answers, one-sentence insight, components, labels, data provenance, and why text alone is insufficient. Omit ornamental images.
2. **Editorial hierarchy.** Build an intentional figure with a short eyebrow/number, descriptive title, optional italic deck, 2–4 clearly composed visual regions, annotated mechanism, concise takeaway, and caption. Avoid anonymous chains of equal-sized rectangles.
3. **Restrained illustrated palette.** Warm ivory paper, ink-dark typography, muted sage/teal for computation, dusty coral for warnings/outcomes, slate blue for comparisons, sand for inputs. Consistent color meaning across all figures. Never use color as the only distinction.
4. **Visual craft.** Thin purposeful connectors, generous whitespace, subtle card borders, editorial serif headlines with clean sans labels and monospaced tensor/logit values; occasional hatched backgrounds and numbered circles. Avoid gradients, shiny dashboard cards, arbitrary icons, excessive rounded rectangles, or stock images.
5. **Concrete detail.** Draw actual example inputs, option text, selected logits, tensor shapes, equations, percentages, and the before/after state. When comparing approaches, align their corresponding stages so the contrast is visible. Use tables/plots for sourced measurements; show axes, units, denominators and provenance.
6. **Source integrity.** Every numerical annotation must be either directly sourced with a citation or explicitly labeled illustrative. Verify every number, equation, arrow, ordering, and clinical assertion against the source ledger. Never let an image generator invent benchmark results, temperatures, logit values, or scientific diagrams without review.
7. **SVG-first for technical fidelity.** Prefer hand-authored SVG/HTML diagrams for equations, arrows, precise labels and accessibility. Image generation may be used for non-quantitative artistic illustrations or visual references, but verify and redraw all technical annotations. All images need useful alt text, captions, and mobile legibility.
8. **Illustration diversity.** Choose the visual grammar for the question: annotated document, split-screen comparison, stepwise mechanism, mathematical geometry, tensor view, experiment plot, decision tree, failure-case comic, or real input/output trace. Do not use a repeated pipeline for every concept.
9. **Figure-level QA.** At desktop and mobile widths inspect for clipping, legibility, incorrect labels, misplaced arrows, and accessibility. Maintain an illustration manifest with each figure's instructional role, provenance, and validation status. Flag untested browser rendering.
10. **Density follows complexity.** Major conceptual transitions deserve figures; trivial paragraphs do not. Require explanation of *what to notice* before/after every figure.

### Figure acceptance test
A figure fails if its content can be replaced by “Input → Model → Output” without losing information. A figure passes when a reader can answer a specific question from it that the surrounding paragraph would otherwise leave ambiguous.


## Mathematical typography — v7 mandatory gate
- Never typeset display equations as plain Unicode approximations (e.g. `Σⱼ₌₁ᴷ` or inline slash fractions). Author equations in valid LaTeX with explicit grouping and defined variables.
- For standalone offline HTML, pre-render LaTeX into self-contained MathJax SVG using `scripts/render_math.cjs` or equivalent. SVG must have an accessible text label and the original LaTeX in `data-tex`. Do not rely on a CDN.
- Keep mathematical expressions selectable through their source labels where possible. Long display math must scroll horizontally on small screens rather than overflow the layout.
- Verify LaTeX compiles, the SVG is present, and no raw TeX control sequences or malformed Unicode math are visible. Confirm equations mathematically match nearby prose and numerical walkthroughs.
- Run `python scripts/test_math.py examples/meddecider-guide.html` as a release gate.


## v8 — enforceable publication contract (BOTH modes)

**Preserve both modes:** (A) general, topic-independent illustrated textbook, and (B) opt-in source-faithful reconstruction. A source URL does not make the entire skill subject-specific. Use the same research, figure, teaching, and QA gates for both, with reference-specific claims only for mode B.

### Required artifacts before writing
1. `research_inventory.json`: each primary/secondary source with URL, title, accessed/verified status, evidence excerpts or exact section, provenance; each factual claim has a unique ID, importance, verification status, destination anchor and precise evidence. No invented citation. For general mode, build the inventory from researched sources; if unavailable, mark unverified and avoid factual specificity.
2. `chapter_matrix.json`: each major algorithm/concept, its prerequisite, problem, intuition, diagram, variables and tensor shapes, derivation, numerical trace, runnable implementation, tests, limitations, and corresponding HTML anchor. Record actual DOM anchors, not just intentions. Mark `not_applicable` with a reason only when genuinely inappropriate (e.g., code for a historical survey).
3. `figure_storyboard.json`: every figure has a unique ID, linked HTML figure ID, the precise question it answers, the answer, visual grammar, specific mechanisms/labels/values, numeric provenance, adjacent explanation anchor, caption, mobile legibility check, and review status. Reject generic 'input → model → output' diagrams that do not reveal a meaningful mechanism.
4. `source_coverage.csv` in source-audit mode: extract a comprehensive reference inventory first (all sections, key numeric claims, tables, training settings, datasets, results, licenses, limitations), not merely 20 cherry-picked claims. Map every entry to a source locator and destination. Report omissions as FAIL; do not silently infer.

### Mandatory automated and human-reviewed release gate
- Run `python scripts/publication_gate.py --root . --html examples/<guide>.html` after generating artifacts. This checks schema, required fields, unique IDs, HTML links, claim destinations, source evidence, chapter depth coverage, figure questions/answers, and source ledger dispositions. It emits `PUBLICATION_REPORT.json` and `PUBLICATION_REPORT.md` and exits nonzero on blocking issues.
- `review_status=approved` requires an actual review; do not mark it approved based only on automated validation. Figure mobile/desktop reviews require screenshots inspected at two widths. If browser tooling is unavailable, mark `not_tested` and fail the visual gate; do not claim visual QA passed.
- Code verification requires real execution; `tests_run=true` only after executing the lab. Equations require real math rendering and independent numerical checks. A textual claim of passing is insufficient.
- **No automatic promotion from draft to publishable.** If any blocker remains, deliver as a clearly labeled DRAFT with a precise defect report, or fix and rerun until clean. Do not weaken the gate to make an example pass.
- Quality is about coverage, clarity, accuracy and evidence, not arbitrary figure/chapter counts. Avoid artificial padding.

### Suggested workflow
`research → evidence inventory → concept coverage matrix → figure storyboard → write → build diagrams → math typeset → run labs → inspect screenshots → publication_gate → revise → publication_gate → deliver`

See `schemas/` for example JSON manifests. `scripts/publication_gate.py` is a working checker, not a guarantee of semantic correctness. Human review and independent source checking remain essential.
