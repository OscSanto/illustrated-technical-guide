# Provenance standard

## In brief
- Every visible figure, math derivation, code or pseudocode block, data table, API example and reported metric is labeled as source reproduction or adaptation, independent verification, our derivation or implementation, hypothetical, or unverified.
- "Our implementation · Pseudocode" is never passed off as the source's code.
- An official API example needs a verified version, endpoint, fields and docs URL. A benchmark number needs provenance and a recorded test environment.
- In source-audit mode, every critical source item gets an explicit coverage disposition and a faithful comparison.
- The provenance gate is structural: it detects missing or unsupported metadata, but it cannot do a factual peer review.

## Mandatory source fidelity and provenance contract

**Applies to both modes.** In general mode, label all original pedagogical artifacts. In source-audit mode, additionally inventory the primary article in full and map its specific systems, reported results, algorithms, and caveats. Do not merge distinct implementations into a generic architecture.

### Mandatory artifact provenance labels (visible in HTML)
Every code/pseudocode block, equation, figure, architecture, table, dataset, API example, and benchmark must have a visible label and an `artifact_provenance.json` entry linked to an HTML ID. Use these exact origin categories:
- `source_reproduction`: verbatim or direct reproduction, with precise source and rights/quotation review.
- `source_adaptation`: based on source, with precise locator and explicit change log.
- `independent_verification`: verified independently, with exact evidence.
- `our_derivation`: mathematically derived here; assumptions and steps documented.
- `our_implementation`: written by us; not source code unless explicitly established.
- `hypothetical_example`: synthetic teaching example; not real system behavior or data.
- `unverified`: not established; never present as fact.

Use human-readable labels like **Our implementation · Pseudocode · Not tested**, **Source adaptation · Redrawn from §4**, **Source-reported benchmark · Not independently reproduced**, **Our derivation**, **Hypothetical conceptual architecture · Not confirmed internals**. Always label executable/tested separately from executable/untested and pseudocode. Do not call pseudocode executable. Source-derived pseudocode must distinguish *quoted original*, *adapted from original*, and *our own reconstruction*.

### Distinctions that must not be blurred
1. Documented external behavior ≠ documented internal mechanism ≠ plausible architecture. Proprietary internals require an explicit uncertainty label. If source describes a conceptual model, preserve that qualification.
2. Official API syntax ≠ schematic JSON. Only call an API example verified when its endpoint, API version, fields, model identifier, docs URL and validation evidence are recorded; otherwise mark **Hypothetical/unverified API example — do not copy as production code**.
3. Source-reported benchmark ≠ independently reproduced benchmark ≠ synthetic illustration. Record hardware, dataset, units, sample size, conditions, and evidence when available. Do not manufacture missing metrics.
4. Source equations ≠ our derivations. Preserve symbols and assumptions when adapting equations; show transformation steps and numerical checks. Label all added calculations.
5. Source figure ≠ redrawn source adaptation ≠ original conceptual diagram. Original SVGs must not imply unconfirmed internal details.
6. Multiple implementations must retain distinct names, approaches, limitations and evidence. Record disagreements and source inconsistencies rather than resolving them silently.
7. Faithful coverage is **substantive**, not word-for-word copying: cite and paraphrase with care; reproduce only brief permitted excerpts, and create original figures instead of copying protected artwork.

### Source Fidelity Gate (blocking)
Before drafting in source-audit mode, inventory *all material* article sections, algorithms, equations, code samples, datasets, configurations, comparative systems, tables, results, caveats and linked primary sources. In `artifact_provenance.json`, record `source_coverage` entries with source locator, topic, disposition (`covered`, `partial`, `omitted`, `unverifiable`, `contradicted`) and criticality. Do not call an inventory exhaustive until it is independently checked. Critical omissions, contradictions, unsupported source attribution, unverified official API examples, unlabeled pseudocode, and benchmark conflation block publication.

Run `python scripts/source_fidelity_gate.py --root <guide-dir> --html index.html` and `python scripts/publication_gate.py --root <guide-dir> --html index.html`. Both must pass before declaring publication ready. The source fidelity gate performs **structural** checks; its PASS is not proof that source claims are true. A human/independent semantic comparison and actual code execution remain separate mandatory reviews. If evidence is unavailable, publish **DRAFT / FAIL** with honest gaps.

`examples/provenance-fixture/` demonstrates a structurally passing provenance manifest with clearly labeled hypothetical examples; it is not a Jev fidelity validation. `examples/jev-source-audit/` remains intentionally failing until full source inventory and article-by-article comparison are performed.
