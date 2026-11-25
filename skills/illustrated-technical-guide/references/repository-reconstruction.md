# Repository Reconstruction — source-faithful learning workflow (v15)

## Activation
A named GitHub/code repository plus an explanation, architecture, learning, walkthrough or component-specific request activates repository reconstruction. This is an OPTIONAL mode; the default general-purpose illustrated textbook generator remains unchanged.

## Evidence first
1. Record repository URL, exact commit SHA, branch and access date. Pin links to commit, not moving main.
2. Enumerate entry points, files, imports, settings, database schemas, commands, tests and evaluation artifacts. Read relevant functions in full. Source comments are evidence of developer intent, not proof of measured behavior.
3. Build a code-path index: trigger → function → transformation → persistence → reader → output. Each major mechanism must link to exact repository files/functions. Do not invent chunking, multiprocessing, API endpoints, cache behavior or optimizer results.
4. For databases: distinguish FTS indexes from ordinary storage, row IDs from vector IDs, temporary tables from persistent tables, and checkpoints from completion markers. Validate a synthetic schema fixture separately from actual integration tests.
5. For data ingestion: distinguish byte-buffered parsing, splitting articles into semantic chunks, batching for inference, and batching for DB commits. They are separate mechanisms.
6. For concurrency: identify threads, locks, asyncio tasks, processes, native-library thread pools, and queues separately. Trace lock scope. Do not assume core count scales throughput.
7. For resource analysis: keep source-reported numbers separate from measured and derived memory arithmetic. No synthetic hardware results labeled as observations.
8. Label excerpts precisely: `Source excerpt`, `Adapted source excerpt` (identify edits), `Our runnable fixture`, `Our pseudocode`, `Our derived calculation`, `Proposed experiment`. Architectures reconstructed from code must say `Source-derived diagram, independently drawn`.
9. Create specific figures for schema, id mapping, entry decomposition, embedding pooling, resume state, query ranking, concurrency and benchmark plan if these are important in the repository. Avoid generic layer diagrams in place of mechanisms.
10. Create SOURCE_COVERAGE.csv mapping each guide chapter and figure to code path/function and verification status. Mark missing pieces and inconsistencies, never silently reconcile.

## Verification gates
- Run syntax/structural tests, source-reference audit, executable fixtures, independent math checks, SVG-render tests and Chromium desktop/mobile screenshots where possible.
- Separate synthetic SQLite fixture tests from actual application/ZIM/ONNX/Raspberry Pi integration. Mark runtime absent as a publication blocker when the guide claims integration verification.
- Build a benchmark protocol with fixed commits/datasets/model hashes, CPU cores, memory, batch size, thread settings, page cache, and observed p50/p95/RSS/throughput/quality. Never supply invented measurements.
- Log every command, result and missing dependency in RUN_LOG.json. Incomplete tests produce DRAFT, not PASS.

## Deliverables
index.html, editable SVGs, source commit manifest, SOURCE_COVERAGE.csv, diagnostic labs, benchmark protocol, browser captures, QA report, and a repair log if findings remain.
