# Jev v13 — full illustration benchmark

**Scope:** All twelve existing Jev figure positions; six preserved from v12 and six completely redesigned. No independent LLM-generation repeatability study was performed.

## Verified
- **12/12 figures** have original editable SVG assets, provenance captions, and accessible image descriptions.
- **12/12 figures** have an explicit **Open readable figure** control that opens the same SVG at 1280 CSS px, with horizontal panning on narrow screens.
- **Chromium browser interaction verified** at 1440×900 (desktop) and 390×844 (mobile), using a test-only HTML with inlined SVG assets to bypass sandbox navigation restrictions. Viewer opened and closed and mobile horizontal panning was confirmed.
- **No document-level horizontal overflow** detected at either tested viewport width.
- Numerical checks passed for a two-token attention example, multiclass loss and gradients, and the hypothetical cost threshold.
- **All 12 SVG figures render through CairoSVG**; six additional PNG previews generated. Earlier six SVGs were already rendered in v12.

## Remaining limitations
- Original figures are intentionally still **shrunk on the in-page mobile overview**; readers use the prominent zoom/pan viewer for labels at their designed size. This is an accessibility improvement but not a native stacked mobile redraw.
- No actual AntV rendering comparison was possible: npm registry lookup returned `EAI_AGAIN` and no local dependency was found. Finished figures use custom SVG. AntV remains an unverified candidate.
- This benchmark does **not** validate TypeSafe Jev's proprietary architecture, reproduce benchmarks, or complete all source claims from TheLion.AI.
- Layout and numerical validation are not a user comprehension study; screen-reader quality was not tested by a human.

## Automated checks
- attention_weight: **True**
- attention_output: **True**
- softmax: **True**
- loss: **True**
- gradient: **True**
- threshold: **True**
- twelve_svg: **True**
- twelve_toolbar: **True**
- browser_desktop: **True**
- browser_mobile: **True**

## Browser measurements

| Metric | Desktop | Mobile |
|---|---:|---:|
| Figure slots | 12 | 12 |
| Zoom controls | 12 | 12 |
| Enlarged SVG displayed width | 1280 px | 1280 px |
| Viewer viewport width | 1416 px | 366 px |
| Scrollable for detail | False | True |
| Document overflow | False | False |

**Verdict: visual redesign coverage PASS (12/12); mobile zoom/pan behavior PASS; AntV comparison NOT VERIFIED; full source-fidelity publication gate remains FAIL/NOT RE-RUN.**
