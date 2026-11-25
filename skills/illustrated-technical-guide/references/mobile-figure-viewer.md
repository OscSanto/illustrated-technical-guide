# Responsive technical figure viewer (v13)

A wide technical figure must not silently scale its labels to unreadable mobile sizes. Every important figure must expose a discoverable, keyboard-accessible **Open readable figure** action.

- Preserve the original SVG viewBox and its semantic text (aim >=13 SVG-unit labels at a 1280-unit figure width).
- On phone screens, open a dialog that displays the SVG at >= its source display width, allowing two-dimensional swipe/scroll/pan. Add obvious Close, Escape, and focus return.
- Responsive single-column/native mobile redraws are better when feasible, but a true-scale pan/zoom fallback is required for dense precision figures.
- Test viewer behavior in a real browser at 390 px and 1440 px; verify `img` loads, there is no document-level overflow, enlarged figure scrolls on mobile, and controls open/close.
- Never claim readability merely because the page avoids horizontal overflow. In-page preview may be tiny; disclose the zoom mechanism.
- Store figures as separately editable original SVGs with caption and provenance. Technical numbers must have numerical checks, and source claims must have evidence.
- AntV renders only count as tested if the AntV library actually ran locally. A DSL candidate alone is not an AntV-rendered illustration.
