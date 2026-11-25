# Version 4 test report

## Comparison target
TheLion.AI's original guide reports 15 chapters, 44 illustrations, and 70 cited sources. This original reproduction test has 14 substantive chapters and 12 figures. It remains less comprehensive than the reference, especially on open-model comparisons and independent empirical benchmarking.

## Validated
- HTML heading/anchor consistency and static structural audit.
- Pre-rendered, nested desktop/mobile TOC links plus JavaScript enhancement.
- Original SVG figures with accessibility labels and captions.
- Six numerical invariants in the standalone Python lab (softmax, loss reduction, score expectation, permutation TV, and decision threshold).
- No CDN, external JS, or stylesheet required for offline HTML display.

## Not validated
- No pixel-level desktop/mobile browser screenshot comparison was run.
- No external Jev model inference or latency benchmark was run.
- Proprietary model internals are not available and are not reproduced.
- Editorial content is substantially expanded, but not an exhaustive recreation of the reference's 70-source research coverage.
