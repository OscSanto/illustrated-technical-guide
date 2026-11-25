# Illustrated Technical Guide (v11)

**An evidence-aware Claude Code skill for creating deeply explained, illustrated computer-science textbooks and hand-holding technical tutorials.**

Two modes, independently usable:

- **Generate:** write an original illustrated guide for any CS topic, choosing the best teaching profile (hands-on, conceptual, mathematical, or mixed).
- **Reconstruct (opt-in):** faithfully explain and audit a named source article/paper while tracking every substantive claim, equation, algorithm, dataset, measurement and omission.

## Install

```bash
mkdir -p .claude/skills
cp -R skills/illustrated-technical-guide .claude/skills/
```

See [installation](docs/installation.md). Usage examples:

```text
/illustrated-technical-guide Beginner PostgreSQL with VS Code, joins, GROUP BY, and EXPLAIN ANALYZE; build one working dataset throughout.
/illustrated-technical-guide Teach transformer attention with tensor shapes, hand-computed softmax, diagrams, and a tested NumPy example.
/illustrated-technical-guide Reconstruct <source URL> in source-audit mode, with claim-by-claim coverage and labeled original pseudocode.
```

## Why it is different

- Teaching profiles chosen per goal instead of mandatory identical chapter templates.
- First-success ladder for practical subjects, with expected outputs and troubleshooting.
- Technical, mechanism-specific illustrated SVG diagrams rather than ornamental generic flows.
- Source provenance on code, diagrams, math, API examples and benchmark figures.
- Fail-closed deterministic checks; no false claims about executed code or published metrics.
- Eight-topic regression protocol designed to measure quality and variation across runs.

## Run checks

```bash
python -m unittest discover -s tests -v
python evals/evaluate.py --suite evals/cases.json --root evals/fixtures
python skills/illustrated-technical-guide/scripts/quality_gate.py --guide evals/fixtures/pass
```

The included `pass` fixture passes **structural** checks only, not independent scientific fact-checking. See [limitations](docs/limitations.md) and [evaluation methodology](evals/README.md).

## Status
**v11: developer preview.** The validators and pedagogical router are implemented; reliable generation quality across different agent runs is *not yet established*. Legacy Jev/PostgreSQL examples under `examples/` are intentionally labeled drafts and are not v11 golden outputs. Actual model-run benchmark results will be added only after repeated executions and human review.

## License
MIT (see `LICENSE`). Copyright/license of any external papers, code, diagrams, or documentation remains with their respective owners.
