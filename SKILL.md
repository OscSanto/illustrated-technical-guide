---
name: illustrated-technical-guide
description: Generate a complete, original, deeply researched, visually taught standalone HTML guide on ANY subject, with automatically generated clickable table of contents, equations when appropriate, diagrams, worked examples, and practical exercises. Use when asked for a visual guide, illustrated textbook, deep dive, educational microsite, or TheLion-style long-form explanation. Do not use for a short answer or ordinary web page.
---
# Illustrated Technical Guide — Reusable Claude Skill (v2)

## Activation
- **Explicit:** User says `/illustrated-technical-guide TOPIC` (when installed as a Claude Code skill), or asks to "use the illustrated-technical-guide skill".
- **Implicit:** Activate when the user's request matches the description and the skill is available. Never imply that implicit activation is guaranteed: Claude chooses whether to load it.
- **Default deliverable:** Write a complete, standalone `index.html` to the current project directory (or user-specified path), then report its location.
- If the user supplies no subject, ask for the subject. Otherwise proceed without unnecessary questions; use sensible defaults.

## Mission
Create an ORIGINAL long-form educational page inspired by the *editorial structure and instructional logic* of https://www.thelion.ai/guide-to-decision-models/. Do not copy the source site's text, branding, illustrations, logos, or distinctive creative assets. Make the guide useful for any topic: ML, mathematics, engineering, economics, biology, history, law, crafts, etc.

## Content planning: adaptive, not fixed
1. Identify target audience, scope, learning objectives, prerequisites, and whether the subject needs formal mathematics or procedural instructions.
2. Draft a coherent outline **before** HTML. Use as many chapters as the subject genuinely needs (often 6–16, not always 15). Include sections/subsections where helpful. Do not invent filler chapters.
3. Select one running example or case study when it improves continuity; adapt examples to the domain.
4. Develop the narrative from motivation → foundations → mechanisms → worked examples → implementation/application → evaluation/evidence → limitations → references.
5. Every chapter must contain meaningful original teaching content. No TODOs, "chapter slots," or single-sentence placeholders. If the request is too broad, narrow scope transparently or divide into a series.
6. Separate established fact, measured evidence, inference, illustrative example, and speculation. Never invent papers, quotations, benchmark results, or citations.

## When to use images (purpose-driven)
- **Problem/workflow:** flowchart immediately after explaining the real-world task.
- **Architecture/structure:** labeled component diagram when relationships or dependencies first become complex.
- **Comparison:** side-by-side panels when alternatives differ in steps, data flow, assumptions, or outputs.
- **Procedure:** numbered steps and feedback arrows when sequence matters.
- **Mathematics:** matrices, annotated vectors, shapes, and a fully worked numerical calculation beside each difficult equation (only where relevant).
- **Evidence:** chart ONLY with real sourced measurements; explicitly mark any synthetic numbers as illustrative.
- **Spatial/physical subject:** labeled cross-section, map, exploded view, timeline, or process sketch, as relevant.
- **Trade-offs:** table after prose; do not replace all prose with tables.
- Do NOT add images at arbitrary intervals. Each figure must answer a specific question, have a numbered caption, meaningful alt text, and be placed adjacent to the explanation it clarifies.
- Use original inline SVG, accessible HTML/CSS diagrams, or user-authorized assets. No hotlinked stock images or copied figures.

## Deep explanation recipe
For each nontrivial mechanism, adapt the sequence: concrete situation → why current method fails → intuition → diagram → formal explanation (define every variable) → numerical or real-world worked example → procedural steps/pseudocode/code when appropriate → verification → failure modes and trade-offs.
Avoid forcing equations into non-mathematical topics. For code examples, use executable snippets with dependencies, inputs, outputs, and test/checkpoints. For historical or social topics, prioritize source analysis, timelines, evidence, and competing interpretations.

## Visual and structural style
- Quiet editorial design: warm off-white background, near-black text, understated accent colors, serif display headings, sans-serif body, monospace code.
- Hero: eyebrow, descriptive title, one-paragraph deck, dynamic chapter/figure metadata, original overview illustration if genuinely useful.
- Readable main column (~700–760px) with wider figures (~900px), generous whitespace, restrained borders, captions immediately below illustrations.
- Desktop sticky left sidebar; mobile expandable contents; responsive tables, accessible focus indicators, sensible print stylesheet.
- Use semantic HTML: `<main>`, `<article>`, `<section>`, `<nav>`, `<h1>`–`<h3>`, `<figure>`, `<figcaption>`, `<pre>`, `<table>`. Exactly one h1.
- Include a "How to read" section, chapter sections, sources/references, and a coherent conclusion.

## Dynamic table of contents: REQUIRED
- The actual chapter count is determined by the content, not by a fixed template.
- Derive TOC entries from the actual DOM: each `article.content > section` with `h2`, plus nested `h3` subsections. Include the introduction and references.
- Give each section a stable unique id; generate unique slug ids for h3 if missing.
- Generate clickable links in BOTH desktop and mobile TOCs from those headings; never manually hardcode chapter links.
- Highlight the currently read section, show reading progress, and close mobile TOC after navigation.
- Anchor links must work with JavaScript enabled; provide an accessible no-JS fallback (e.g. server-generated static TOC when building, or clear in-document headings and navigation). In a self-contained file, prefer generating TOC links at build time if a generator is available; progressive enhancement can add active tracking.
- Verify all anchors exist, no duplicates, chapter numbers are correct, and TOC automatically adapts when chapters are added/removed.

## HTML implementation
- Output a complete self-contained `index.html` with embedded CSS, JS, and original SVGs; do not require a CDN, framework, server, or build step.
- Use `index.html` from this skill directory as a **styling and behavior reference**, not as immutable content. Replace ALL sample subject-specific prose and figures.
- Update hero/title, cover, running example, figure numbering, chapters, and citations for the new topic.
- Avoid untrusted HTML injection; if building HTML programmatically, escape user-supplied text.
- Make links keyboard-accessible; support reduced motion; ensure color contrast, mobile overflow, and print behavior.

## Research and citation integrity
- If browsing is available, prefer primary research, official docs, and reliable domain references. Link references at point of claim and in a numbered bibliography.
- If browsing is unavailable, do not fabricate citations; disclose that references require verification.
- Attribute quoted or adapted source material, respect copyright, and clearly identify hypothetical examples.

## Completion checks
1. Standalone file opens locally without network.
2. Outline fits the topic; all chapters are substantive and complete.
3. Both TOCs match actual chapters/subsections; every anchor works.
4. Active TOC and progress indicator work; mobile TOC collapses.
5. Every image is original, necessary, captioned, accessible, and adjacent to relevant text.
6. Every equation is explained and every claimed measurement sourced or labeled illustrative.
7. Code samples and numeric calculations checked when feasible.
8. No fixed 15-chapter assumption, placeholders, dead links, copyright copying, or horizontal overflow.
9. Provide the generated HTML file and a concise summary of chapters/figures.

## Example requests
- `/illustrated-technical-guide Explain transformer attention from dot products through multi-head attention, with tensor shapes and PyTorch`.
- `Use the illustrated-technical-guide skill to teach concrete mold making, with diagrams and safety notes.`
- `Create an illustrated 10-chapter guide to Bayesian statistics with worked problems and source references.`
