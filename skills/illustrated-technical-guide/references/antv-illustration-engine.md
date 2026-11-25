# Experimental AntV illustration engine

This is an **optional rendering subsystem** for the general illustrated textbook generator. It does not replace pedagogy, provenance, chapter tests, or source reconstruction. No external renderer may assert that a diagram is technically correct.

## Renderer selection (required)

1. Write the figure's **one technical question** and its required evidence: exact rows, coordinates, data flow, equations, or states.
2. Try **AntV Infographic** for broad structures: `sequence-*` for steps, `compare-*` for comparisons, `relation-*` for connectivity, `chart-*` for simple statistics. Choose the specific template according to the actual data schema.
3. Use **custom SVG** instead if every row, tensor cell, token, attention mask, math symbol, precise alignment, or trace must be individually visible and a stock template would lose the mechanism.
4. Do not turn a precise mechanism into a generic diagram just to use AntV. Prefer a hybrid chapter where a broad AntV overview is followed by a detailed SVG trace.
5. Keep figures original. Source reproduction/adaptation in audit mode requires source locator, explicit adaptations, and copyright awareness.

## Stable visual grammar

- Canvas `#f8f9fb`, ink `#3a424a`, border `#cbd0d5`, connectors `#535a62`.
- Primary semantic accents: blue `#2d92d5`, green `#2e9e52`, orange `#ee8517`, pink `#d82f79`; reserve neutral gray for secondary elements.
- Use Inter/Source Sans 3/Arial for titles and interface text; ui-monospace/Consolas for identifiers, logits, sample rows and code; embed fonts only when licensing permits.
- Agree on a **book-wide color registry** before illustrating (a color mapping is stable within any multi-figure example). Color never carries information alone.
- White/light-gray cards, 8–14px corner radii, 1.5–2.5px dark borders, 16–24px typical padding; minimum readable font size at actual mobile display. Avoid gradients, glow, over-decoration, crowded legends, and gratuitous icons.
- Present actual intermediate values and explain provenance: source-reported, independently reproduced, derived, synthetic, hypothetical, or unverified.

## AntV candidate workflow

1. From a storyboard, pick an installed **valid registered template**, then generate DSL using the appropriate data field: `nodes`/`relations`, `sequences`, `compares`, or `values`. Keep source DSL as an editable artifact.
2. Pin an explicit tested dependency version (experiment uses `@antv/infographic@0.2.20`); never use `@latest` for released books.
3. Render in a browser with that version. Export **static SVG**, preserving editable DSL/source; final exported HTML should embed the SVG and work offline. Avoid CDN runtime dependencies in final artifacts.
4. Validate browser rendering, overflow, font legibility, text-to-mark associations, geometry, mobile view, metadata, caption, and factual fidelity. Do not pass based on syntax checks only.
5. If the package, browser, or external assets are unavailable, label AntV as **untested**, retain DSL, and ship a genuinely offline custom-SVG fallback instead.

## Custom SVG fallback

Use semantic shapes and real example records, exact numeric calculations, aligned callouts, and captions. Make paths inspectable and editing possible. Run an XML parser and PNG rendering check. No performance values without measured test logs.

## Decision criteria for accepting AntV as default

Across PostgreSQL joins, transformer attention, and decision-model output comparisons: must preserve mechanism-level information; render and export successfully without unpinned packages; readable at 375px width; correct values; consistent styling; license attribution. If any fails, make AntV conditional, not required.

## Evidence and licensing

Official AntV project: https://github.com/antvis/Infographic (MIT license). Official skills: `skills/infographic-creator` and `skills/infographic-syntax-creator`. Its README reports declarative DSL, approximately 200 templates/components/layouts, SVG rendering, theme and editor support. **Neither an npm install nor AntV visual rendering was verified in this environment for the initial experiment.**
