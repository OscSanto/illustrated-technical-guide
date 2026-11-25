# Reading design: page, prose and claim labels

A guide must be pleasant to read for an hour. The page keeps the skill's original design; the header typography and the writing habits below come from studying TheLion.AI's "Visual guide to Jev-like models" (Nov 2026). All of it is built into `templates/standalone.html`, so start from the template; do not restyle it per guide.

## Page

- **Layout.** A 220 px sticky contents column (chapters plus their subsections, the current one highlighted) beside a 760 px reading column. Below 850 px the contents become a collapsible list at the top.
- **Body.** Inter or the system sans-serif, 16 px, line height 1.75, dark grey on warm paper (`#faf9f6`).
- **Blocks.** Blue primers for new concepts, green "Why it matters" boxes, dashed "Check yourself" boxes, a coral-edged running-example card, small uppercase table headers with row rules, and figures that bleed slightly wider than the text.

## Headers

| Element | Font | Weight | Size | Line height | Letter spacing |
|---|---|---|---|---|---|
| H1 (page title) | Times New Roman (`--times`) | normal | `clamp(48px, 7vw, 82px)` | 1.07 | −0.05em |
| H2 (chapter titles) | Times New Roman | normal | `clamp(34px, 4vw, 48px)` | 1.12 | −0.025em |
| H2 in the front matter ("Before you start") | Archivo (from TheLion.AI) | 800 | `clamp(1.7rem, 2.6vw, 2.3rem)` | 1.1 | −0.03em |
| H3 (section) | Archivo (from TheLion.AI) | 750 (renders 800) | 1.2rem | 1.75 | −0.02em |

Headers use colour `#14141c` and `text-wrap: balance`. Archivo 800 is embedded in the template as base64 (latin subset, Fontsource 5.3.0, SIL OFL 1.1; file and licence in `templates/fonts/`, re-embed with `python scripts/embed_header_fonts.py`), so guides stay offline. A metric-matched Arial fallback keeps the layout stable if the font fails.

## Cover illustration

Put one overview illustration right under the hero deck (`<figure class="figure cover" id="fig-cover">`). It must show the whole guide at a glance: the running example flowing through every major stage the guide teaches, each stage tagged with the chapter that explains it, using real values from the guide (not new numbers). Label it like any figure (provenance label, storyboard entry, `artifact_provenance.json`), and mark inferred parts as inferred inside the drawing.

## Prose

- **Every chapter opens with a lede:** one or two sentences, the first paragraph after the chapter title, that set up the chapter's question or scene. It is ordinary body text. It hooks; it does not summarise. Good: "A ticket arrives at 9:14 on a Monday, and before anyone replies, software must answer four small questions about it." Bad: "This chapter covers the interface."
- **Short paragraphs.** Aim for 30–60 words. One idea per paragraph. Split any paragraph over about 90 words.
- **Bridging tables.** When a new idea maps onto one the reader half-knows, use a two-column table ("In LLM work | In a decision model") instead of a paragraph of analogies.
- **One assumption at a time.** For a concept that grows out of a familiar one, change one assumption per step and say what each change buys (see `profiles/conceptual.md`).
- **Running example card.** The guide's single running example is a labelled card (`.ticket`). Show it once in full, then reuse the same card style when it returns in later chapters.
- **Front matter.** Open with two short callouts: "How to read this guide" (the badge key and what citations mean) and "What you should know already".
- **Cross-references** to other chapters use quiet links (`.xref`), not "click here".

## Claim labels (badges) and citations

Figures and code already carry provenance labels. Factual claims in the prose carry them too, right where the claim is made.

1. Every non-obvious factual claim gets a **numbered citation**: `<a class="cite" href="#ref-2">[2]</a>`. Reference ids (`ref-N`) map to `research_inventory.json` sources in order, and the reference list is the last chapter.
2. Claims that a reader could mistake for established fact also get a **badge** placed after the sentence, linked to a claim id in `research_inventory.json`:

   `<span class="badge b-meas" data-claim="C5">measured</span>`

   | Badge | Class | `evidence` value | Use when |
   |---|---|---|---|
   | published | `b-pub` | `published` | The vendor or official docs state it |
   | measured | `b-meas` | `measured` | An independent party measured it and published the data |
   | inferred | `b-inf` | `inferred` | A hypothesis that fits the evidence, not confirmed |
   | self-reported | `b-self` | `self_reported` | A project reports this about itself, on its own tests |
   | our lab | `b-lab` | `our_lab` | We computed or ran it; the run is in `RUN_LOG.json` |

3. Each claim in `research_inventory.json` records its `evidence` value. The quality gate blocks a badge whose `data-claim` does not exist or whose class does not match the claim's `evidence`. Once a guide uses badges, every critical claim needs at least one.
4. Badges in the badge key, or any other legend, carry `data-legend` instead of `data-claim`, so the gate skips them.
5. Explain the badge key once, in the "How to read this guide" callout. Do not over-badge: one badge per claim, on the sentence that makes it, not on every sentence that repeats it.
