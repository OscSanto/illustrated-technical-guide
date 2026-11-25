# Responsive technical figure viewer

A wide technical figure must not silently scale its labels to unreadable mobile sizes. Clicking or tapping any figure, illustration or animation opens it full size in a dialog; there is no separate button. Each figure is keyboard-accessible (focusable, opens on Enter or Space) and shows a small "Enlarge" hint on hover or focus, always faintly visible on touch screens. Clicks on controls inside a figure, such as an animation's pause button, do not open it.

- Preserve the original SVG viewBox and its semantic text (aim >=13 SVG-unit labels at a 1280-unit figure width).
- On phone screens, open a dialog that displays the SVG at >= its source display width, allowing two-dimensional swipe/scroll/pan. Add obvious Close, Escape, and focus return.
- Responsive single-column/native mobile redraws are better when feasible, but a true-scale pan/zoom fallback is required for dense precision figures.
- Test viewer behavior in a real browser at 390 px and 1440 px; verify `img` loads, there is no document-level overflow, enlarged figure scrolls on mobile, and clicking a figure opens it and Close/Escape closes it.
- Never claim readability merely because the page avoids horizontal overflow. In-page preview may be tiny; disclose the zoom mechanism.
- Store figures as separately editable original SVGs with caption and provenance. Technical numbers must have numerical checks, and source claims must have evidence.
- AntV renders only count as tested if the AntV library actually ran locally. A DSL candidate alone is not an AntV-rendered illustration.
