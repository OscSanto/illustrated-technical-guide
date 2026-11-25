---
name: illustrated-technical-guide
description: Research, write, illustrate, implement, test, and publish substantial original standalone HTML technical textbooks with a dynamic nested contents menu. Invoke when user asks for a comprehensive illustrated guide, detailed mathematical reconstruction, or technical learning microsite.
---
# Illustrated Technical Guide v4 — research-to-publication

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
