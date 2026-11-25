# v14 Cross-topic illustrated guide benchmark

**Scope:** Two independently specified *topic fixtures*, PostgreSQL LEFT JOIN and 2D scaled dot-product attention. Not three independent LLM runs and not a complete textbook acceptance test.

## Verified results
- **2/2 topic figures** render in Chromium with the original SVG bytes embedded as data URLs via `page.set_content` (local navigation blocked by browser policy).
- **4/4 desktop/mobile page checks** have no document-level horizontal overflow.
- **4/4 figure viewer checks** open, preserve native 1120 px width, close with Escape, and restore button focus. Mobile viewer is horizontally pannable.
- **Attention numerical implementation:** executed Python; predicted weights `[0.6698, 0.3302]`, output `[6.6976, 6.6048]`.
- **PostgreSQL LEFT JOIN:** SQL executed against **SQLite only** with 4 matching expected rows. No PostgreSQL runtime execution is claimed.
- **Existing suite:** `pytest`: return code 0, output `........                                                                 [100%]
8 passed in 0.06s`; infographic fixture tests: return code 0.

## Not established
- AntV rendering and SVG export **NOT EXECUTED**; registry access failed (`EAI_AGAIN`). No visual A/B evidence with AntV exists. Direct browser URL navigation was blocked by policy; the screenshots test equivalent document content with inlined SVG assets, not hosting, file-path resolution, or network loading.
- **Cross-run skill reliability NOT MEASURED:** this test uses authored deterministic fixtures, not independent AI generations.
- Educational usefulness: no learner study or blind expert assessment.
- Full Jev source fidelity: out of scope for this visual transfer test.
- Static SVG labels are still shrunk in inline mobile preview; users must select **Open readable figure** to read them at native size.

## Verdict
**PASS for cross-topic browser, responsive figure viewer, and arithmetic fixtures; NOT READY to promote AntV or claim generative consistency.** Keep AntV optional until a real render/export benchmark succeeds.

Evidence: `BROWSER_RESULTS.json`, `SCORECARD.csv`, `postgresql-desktop.png, postgresql-mobile.png, attention-desktop.png, attention-mobile.png` and per-viewport viewer screenshots.

Re-run with `python scripts/run_cross_topic_benchmark.py` from the repository root. Requires Chromium, Playwright, beautifulsoup4, pytest.
