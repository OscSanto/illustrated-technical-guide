# Illustrated Technical Guide — v12 experimental AntV integration

Generate deeply explained, illustrated, testable, introductory-to-advanced computer-science HTML textbooks. This is a developer preview, **not a proven consistent release**.

## Two main modes (retained)

- **Generate:** a general-purpose illustrated, hands-on technical guide from a learning-outcome request.
- **Reconstruct (optional):** source-faithful reconstruction of a specified paper, article or repository, with provenance and omission checks. Original instructional diagrams and synthetic examples must be labeled.

## New v12 feature: optional AntV Infographic rendering

See [`references/antv-illustration-engine.md`](skills/illustrated-technical-guide/references/antv-illustration-engine.md). The skill now routes broad narrative/comparison/overview diagrams toward AntV, while retaining precise custom SVG for detailed mechanisms. It uses a stable visual palette and semantic color registry, with editable source and eventual static SVG export.

**Current verification:** 3 custom figures rendered to PNG and passed numerical and XML tests; 3 AntV DSL candidates were authored but AntV couldn't be installed or rendered here (network blocked). See [`reports/COMPARISON_REPORT.md`](reports/COMPARISON_REPORT.md). Do not represent v12 as a full AntV integration test.

## Open the experiment

[`examples/visual-comparison/index.html`](examples/visual-comparison/index.html): PostgreSQL LEFT JOIN, transformer attention, and softmax vs sigmoid. Left panels use pinned `@antv/infographic@0.2.20` via CDN when reachable. Right panels are offline SVGs. Use the assets directory for PNG previews, DSL, and SVG sources.

## Install skill in Claude Code

Copy `skills/illustrated-technical-guide` into `.claude/skills/illustrated-technical-guide` in your project. Its entry point is [`SKILL.md`](skills/illustrated-technical-guide/SKILL.md). The existing validator and provenance scripts remain installed. This experimental package does not include AntV runtime files. The HTML figure preview uses a pinned CDN and must be exported to SVG for offline final textbooks.

## Tests

```bash
python scripts/build_visual_comparison.py
python scripts/test_visual_comparison.py
python -m unittest discover -s tests -v
```

See [`reports/COMPARISON_REPORT.md`](reports/COMPARISON_REPORT.md) for measured outcomes and unresolved blockers.

## License

Original skill content retains its existing LICENSE. AntV Infographic is a separate MIT-licensed project: https://github.com/antvis/Infographic . We reference its API, DSL and package but have **not copied its source code into this repo**.


### v13 mobile illustration experiment
See `examples/jev-v13/` for twelve illustrated figures, accessible 1280px pan/zoom dialogs and browser test evidence. AntV runtime remains unavailable in the benchmark environment; this is not source-fidelity publication approval.
