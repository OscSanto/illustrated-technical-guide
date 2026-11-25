---
name: illustrated-technical-guide
description: Create long-form, mathematically rigorous illustrated technical guides in standalone HTML using the editorial structure and pedagogical composition of TheLion.AI's Visual Guide to Jev-like Models.
---
# Illustrated Technical Guide — HTML Skill

## Goal
Create a responsive, self-contained HTML technical textbook page that closely follows the **information architecture, visual rhythm, and teaching methodology** of https://www.thelion.ai/guide-to-decision-models/ without copying its protected prose, branding, illustrations, or other creative assets. Use original content and diagrams.

## Page anatomy (in order)
1. Narrow announcement ribbon (optional).
2. Minimal editorial masthead: small brand, compact navigation, subtle bottom rule.
3. Hero: uppercase eyebrow, prominent serif headline, one-paragraph deck, concise metadata (free, chapters, figures, references).
4. Wide technical cover illustration that previews the entire system.
5. Compact "Contents" control and chapter index, ideally sticky on wide screens.
6. "How to read this guide": source-evidence labels, assumed prerequisites, recurring example, notation conventions.
7. Numbered long-form chapters, each with small chapter kicker, large serif heading, prose, subheads, diagrams, equations, tables, citations.
8. References and optional closing next steps.

## Composition rules
- Keep reading column ~700–760px; illustration can extend to 900–1000px.
- Cream/off-white page, near-black text, muted grays, restrained accent colors (e.g. coral for decision branches and blue for generation).
- Serif display headings; highly legible sans-serif body; monospace for code and mathematical symbols.
- Spacious margins, paragraph line-height ~1.7, meaningful vertical separation between figures and subsections.
- Diagrams are functional, not decorative. Avoid generic stock photos.
- Captions directly beneath figures: `Figure N. What the reader should notice. Illustration / measured / adapted from ...`.
- Provide meaningful alt text, keyboard focus, semantic headings, responsive figures and tables.
- If using third-party data or claims, cite primary sources near the claim and in References.
- Never imply an inferred architecture is an officially disclosed implementation.

## Pedagogical sequence
For each concept: (1) concrete problem, (2) current limitation, (3) plain-English mechanism, (4) diagram at the point of conceptual difficulty, (5) mathematical formalization with defined variables, (6) worked numerical example, (7) procedural pseudocode/PyTorch, (8) measurement, failure modes, trade-offs.
Use a **single running example** across chapters to minimize context switching. Show architectural progression as modifications to the same example.

## Illustration decision rules
- **Opening workflow:** use a left-to-right or top-to-bottom flowchart when defining the problem.
- **Architecture:** use component blocks and labeled arrows at first introduction of a mechanism.
- **Comparison:** use paired panels when contrasting generative versus discriminative computation or two training regimes.
- **Procedure:** use numbered pipeline and feedback arrows for training and inference.
- **Mathematics:** use matrices, shapes, highlighted entries, and one fully worked calculation adjacent to the equation.
- **Evidence:** use a chart only for real measured numbers with source, sample size and units; otherwise mark values illustrative.
- **Trade-offs:** use tables after prose to consolidate choices.
- **Complexity spike:** insert an image immediately after the explanation that would otherwise require the reader to imagine a data flow, matrix or multi-stage dependency.
- Do not place images at arbitrary fixed intervals or repeat prose as illustration.

## HTML implementation
- Produce a single `index.html` with embedded CSS and SVG diagrams; no required external runtime.
- Responsive CSS Grid for main reading column and sidebar TOC; collapse to one column on mobile.
- Use `position:sticky` for TOC on desktop, `details/summary` for mobile contents.
- Use CSS custom properties for palette, widths and spacing.
- Use `<figure><svg ... role="img" aria-label="..."></svg><figcaption>...</figcaption></figure>`.
- For equations, use accessible HTML and optional MathML; avoid reliance on a remote LaTeX service.
- Provide a print stylesheet with no navigation, no sticky behavior, and clean page breaks.
- Include a citation convention `[1]` with linked bibliography.
- Validate links, heading hierarchy, alt descriptions, and responsive behavior.

## Deliverables
1. `index.html`: ready-to-open standalone example page.
2. `SKILL.md`: this reusable generation specification.
3. `README.md`: customization and usage instructions.

## Quality gate
Before completion, check: all chapter links resolve; mobile navigation works; no horizontal overflow; each figure has a teaching purpose and caption; math variables are defined; numeric data is marked illustrative unless sourced; content is original; no copyrighted site assets are embedded.
