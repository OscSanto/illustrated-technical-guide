# Zimantic v16 — Depth-first revision benchmark

## Scope
Reconstructed from GitHub `OscSanto/zimantic` commit `40c404f6dd409dc0e1d80fb89f9212b99a8542f3`.
This is an **educational rewrite**, not a new hardware experiment, a scientific paper, or an exhaustive source audit.

## Changes from v15
- Expanded ZIM extraction, SQLite schema, embedding, build-resume, FAISS, search fusion, concurrency, and hardware sections.
- Introduced step-by-step toy input transformations, intermediate values, numerical checks, counterexamples and operational consequences.
- Added 8 mechanism-specific diagrams (total 18); preserved the original 10 architectural figures.
- Added rendered, offline vector mathematics for masked pooling, IVF cluster sizing, RRF and activation memory.
- Added 34 subheadings and nested desktop TOC navigation; made detailed tables scroll independently on narrow screens.
- Moved repetitive evidence statements into source references, figure captions and structured manifest fields.

## Depth observations
- Overall visible page text: 8382 words (including code, captions, navigation).
- Core chapter word counts: entry=1012, schema=967, embed=959, build=888, faiss=921, search=951, concurrency=881, hardware=760.
- These word counts are descriptive, not success criteria.

## Executed checks
- Python standard-library/SQLite lab `labs/depth_checks.py`: **PASS** (masked mean, normalization, RRF, FAISS cluster formula, tensor memory, FTS5 indexed-column semantics).
- Existing Zimantic v15 lab `labs/verify_concepts.py`: **PASS**.
- New `depth_gate.py`: **STRUCTURAL PASS**, not an educational correctness certification.
- v16 skill regression tests (`pytest tests`): **8 passed**.
- Provenance gate: **PASS** for figure provenance metadata and visible labels.
- New and old SVGs rendered with CairoSVG; 18 rasterized previews were embedded for a controlled Chromium rendering test.
- Chromium desktop 1440×1000 and mobile 390×844: no document horizontal overflow, all 18 preview images loaded, modal figure opens/closes and preserves 1,100 px image width.

## Publication gate
**FAIL — 39 remaining findings.** Principally pending independent technical/educational/source comparison reviews and individual figure editorial approvals. Automated image loading and viewer behavior do not constitute full human figure review.

## Not executed
- Real `.zim` archive indexing
- Real int8 ONNX E5 model inference and tokenization against model files
- Real FAISS build and retrieval benchmarks
- Raspberry Pi Zero 2 W / Pi 5 core-count and RAM profiling
- Independent repeated model generations

## Browser qualification
The environment blocked navigation to local file and localhost URLs. The browser test used `set_content` with **rasterized previews** embedded as `data:` images, while the distributable HTML references original local SVG assets. This validates composition, viewport behavior and figure controls, not a normal file:// deployment path or the raw SVG load path in Chromium.

## Test artifacts
`CHAPTER_DEPTH_AUDIT.csv`, `mechanism_traces.json`, `reports/browser_checks.json`, `reports/DEPTH_GATE.json`, `reports/DEPTH_TESTS.txt`, `QUALITY_REPORT.md`, `FIDELITY_REPORT.md`.
