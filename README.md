# Illustrated Technical Guide

A Claude Code skill that writes deeply explained, illustrated, testable learning guides as single portable HTML pages. It can also reconstruct a supplied article, paper or code repository faithfully, with claim-level provenance.

Each dense technical chapter traces one real input through the mechanism it teaches. Every figure, code block and factual claim is labelled with where it came from (published, measured, inferred, self-reported, or computed in the guide's own lab), and structural gates check those labels before a guide is called finished.

## Install
Copy `skills/illustrated-technical-guide/` into your Claude Code skills directory. `SKILL.md` is the entry point; its `references/` and other files must stay alongside it. This is the only thing you need to install.

**Optional companion skills.** The skill works fully without them and falls back to hand-written SVG:
- [dashmotion](https://github.com/csthink/dashmotion) (MIT). It adds animated flow figures (dots travelling through a system). Install it with `npx skills add csthink/dashmotion -a claude-code -g`. See `references/animated-flow-figures.md`.

## What's in the skill
- `SKILL.md`: the working agreement, step by step.
- `profiles/`: hands-on, conceptual, mathematical and source-audit chapter patterns.
- `references/`: depth-first teaching, reading design, repository reconstruction, provenance, illustrations and animation guidance.
- `templates/standalone.html`: the page template, with the header font embedded so guides work offline.
- `scripts/`: `quality_gate.py` (main gate), `depth_gate.py`, `source_fidelity_gate.py`.

## Example
`examples/zimantic/index.html` explains the [OscSanto/zimantic](https://github.com/OscSanto/zimantic) repository at commit `40c404f6dd409dc0e1d80fb89f9212b99a8542f3`. Run its concept checks with `python examples/zimantic/labs/verify_concepts.py`. The depth-first benchmark for that guide is in `docs/V16_BENCHMARK.md`.

## Tests
`make test` (or `python -m unittest discover -s tests -v`) runs the gate tests. `make fixture` runs the quality gate on the passing fixture. See `evals/` for the multi-topic evaluation harness.
