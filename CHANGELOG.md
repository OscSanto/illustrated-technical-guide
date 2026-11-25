# v16 — Depth-first teaching

- Required mechanism traces with intermediate states, invariants, derivations, parameter variations and failure modes.
- Reduced repetitive audit language in instructional prose while preserving provenance.
- Added `depth_gate.py` (structural only) and teaching reference.
- Expanded Zimantic exemplar with eight trace-level diagrams and detailed walkthroughs.

# Changelog

## v17 (2026-11-25) Reading design, claim badges, animated figures
- New `references/reading-design.md`: chapter ledes, short paragraphs, bridging tables, numbered citations, claim badges (published, measured, inferred, self-reported, our lab) and a cover illustration under the hero deck.
- `templates/standalone.html`: keeps the v16 page design. The page title and chapter titles use Times New Roman; the front-matter title and H3 use Archivo 800 (typography from TheLion.AI), embedded offline via `scripts/embed_header_fonts.py` (OFL licence in `templates/fonts/`). Adds badge, citation, callout and cover styles and a built-in readable-figure viewer.
- `profiles/conceptual.md`: "start from the familiar, change one assumption at a time".
- New `references/animated-flow-figures.md`: the four signs for animation, an `animate` decision per figure, optional dashmotion integration, hand-written SMIL for queues, batches and measured timing.
- `quality_gate.py`: blocks badges that cite unknown claims or show the wrong evidence type, and critical claims left unbadged once a guide uses badges; warns on missing or long chapter ledes and missing `animate` decisions. Five new tests.
- `source_fidelity_gate.py` / `quality_gate.py`: read files as UTF-8 (fixes the Windows cp1252 crash).

## v15 — Zimantic source reconstruction
- Added pinned-commit repository analysis and data lineage workflow.
- Explained code-level SQLite/FAISS identity, extraction, checkpoints, E5 embeddings, fusion, locks and hardware profiling.
- Added 11-chapter illustrated example with ten SVG figures, mobile dialog viewer, synthetic executable fixtures, and explicit DRAFT status.
- Preserved original general-purpose teaching and optional source audit modes.
