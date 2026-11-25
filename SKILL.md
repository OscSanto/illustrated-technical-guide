---
name: illustrated-technical-guide
description: Create original, deeply explained, research-grounded standalone illustrated HTML textbooks on any topic, with adaptive chapters, auto-generated table of contents, stepwise math, diagrams, runnable implementations, exercises, and automated quality checks. Use for illustrated technical guides, educational microsites, comprehensive explainers, or reproducible tutorials. Do not invoke for brief answers or generic landing pages.
---
# Illustrated Technical Guide — v3 (depth-first)

## Invocation
- Claude Code explicit: `/illustrated-technical-guide <topic and desired depth>`.
- Claude Code implicit: Claude may select this skill when its description matches; not guaranteed.
- Claude.ai: install as a custom skill where supported, then request it by name or describe the guide.
- Output: complete standalone `index.html` in requested location, plus optional reproducible examples.

## Core contract
Build a *new* original teaching page inspired by the educational organization (not copyrighted content or branding) of TheLion.AI's decision-model guide. Use `template.html` as a visual starting point, never as unedited final content. Do not claim to reproduce proprietary internals without evidence. Distinguish **verified**, **inferred**, **illustrative**, and **measured** material. Never fabricate citations, metrics, or source quotations.

## Planning phase (mandatory)
1. Define audience, prerequisite knowledge, outcome, and scope; choose 6–16 substantive chapters as appropriate, never a fixed count.
2. Build a dependency-ordered outline: motivation → prerequisite concepts → architecture/mechanisms → derivation → reconstruction → training/operation → validation → failure modes → applications → sources.
3. Select a recurring worked example where appropriate; carry its exact variables and inputs across chapters.
4. Write a **concept inventory**: each major mechanism gets its own instructional unit and visual if relationships, sequence, or computation are nontrivial.
5. Create a **claim ledger**: assertion, source URL, date/section if available, confidence class (verified/inferred/illustrative), and planned citation location. If research tools are unavailable, state the limitation and omit unsupported claims.
6. For technical subjects, set an explicit reproduction target and testable acceptance criteria (e.g., matching numerical output, loss decreasing, unit tests passing).

## Depth gate — EACH major algorithm/mechanism
A section is NOT complete unless it contains all applicable items:
1. **Problem:** concrete question or failure of prior approach.
2. **Intuition:** plain-language explanation with explicit assumptions.
3. **Architecture:** original labeled diagram showing direction, interfaces, and shapes where relevant.
4. **Formalization:** equation(s), with every symbol, dimension, domain, and convention defined; avoid decorative equations.
5. **Worked example:** actual small inputs; perform each transformation, show intermediate values and final result. Verify arithmetic with code if possible.
6. **Reconstruction:** pseudocode then runnable minimal code (standard Python or clearly pinned dependencies), including complete input and expected output.
7. **Verification:** executable assertion, unit test, invariant, or a hand-check; show failure case and how to debug it.
8. **Trade-offs:** complexity, memory/latency implications where grounded, assumptions, alternatives, and limitations.
If a field is inapplicable (e.g., equations for a historical account), substitute appropriate evidence/procedure and explicitly avoid forcing mathematics. No empty chapter shells or TODO placeholders.

## Visual grammar: image choice and placement
- Workflow/problem → flowchart immediately after the concrete scenario.
- Architecture → component diagram at first introduction of interacting parts.
- Mathematical transform → annotated matrices/tensors and numerical steps directly beside equation.
- Algorithm/process → numbered flow with loop/feedback edges.
- Comparison → aligned side-by-side schematic sharing scale and terminology.
- Experimental claim → chart with data source, units, axes, sample size if available; never depict invented data as measured.
- Spatial subject → exploded view, section drawing, timeline, or map as appropriate.
- Figure rule: every original SVG/HTML illustration has `figure`, meaningful accessible name/alt, numbered `figcaption`, and is cited in nearby prose. Each answers a specific reader question. No arbitrary image quota, no decorative stock images, no copied website figures.
- Use diagrams for difficult transitions; avoid replacing essential explanation with illustrations alone.

## Composition and layout
- Quiet editorial look: cream/off-white canvas, dark body text, restrained accents, serif headline, sans-serif body, monospace code.
- Hero with descriptive title, scope, audience, estimated reading level, guide metadata, and original overview visual if helpful.
- Main reading column ~720px; wider technical figures; generous whitespace, accessible contrast, captions, callouts for assumptions and caveats.
- Desktop sticky TOC; mobile disclosure navigation; print layout; responsive wide tables/code.
- Semantic h1–h3, section ids, figures/captions, accessible links and focus states, reduced-motion support.
- Full article: prerequisite checklist, chapters, key terms, exercises, references, and summary of what reader can reproduce.

## TOC contract (must pass)
- Generate desktop and mobile contents from actual headings, including nested h3 subsections; no fixed list of chapter names.
- Preserve unique stable IDs and working anchors, active-section indicator, reading progress, mobile collapse behavior.
- Provide useful navigation without JS (pre-render TOC at build time when possible). JS enhancement may update highlights/progress.
- Run `scripts/validate_guide.py index.html` and fix errors before delivering.

## Technical fidelity
- Define symbols and tensor shapes *before* using them in equations; distinguish loss, training objective, optimizer, and inference procedure.
- Show a trace for one complete forward pass and, where relevant, one backward/optimization step.
- Include minimal reproducible environment and dependencies; code blocks must be executable, not pseudocode disguised as code.
- Compare baseline and proposed method with the same dataset and metrics; explain sources of confounding.
- Label synthetic values **illustrative** in chart captions and nearby text. Do not make invented benchmark claims.
- Proprietary systems: present public interface as verified, candidate implementation as inferred, and state exactly what cannot be reproduced.

## Build and verification sequence
1. Research original/primary sources when available and write claim ledger.
2. Outline and write full prose and examples before decorating.
3. Build original diagrams from the explanations, not the reverse.
4. Produce complete offline `index.html` with embedded CSS, JS, and SVG; no CDN or server required.
5. Execute sample code/tests when possible; check numeric examples and diagram labels.
6. Run `python scripts/validate_guide.py path/to/index.html` (requires Python and BeautifulSoup). Fix all reported errors; manually test browser responsiveness and JS behavior if browser automation is available.
7. Audit each major mechanism against eight-point depth gate. State any incomplete areas honestly; do not call a shallow outline a full reproduction.
8. Report chapter count, figure count, references, tested code, and remaining limitations.

## Source material
- `template.html`: visual/behavior reference; replace all sample prose, figures, citations, metadata.
- `examples/jev-guide.html`: earlier short Jev guide demonstrating layout; intentionally **not** a passing depth benchmark for every chapter.
- `scripts/validate_guide.py`: deterministic static checks, not a substitute for visual browser QA or factual review.

## Example
`/illustrated-technical-guide Build a full guide to transformer attention: derive QKV, trace a 3-token example, implement multi-head attention in PyTorch, verify against a manual calculation, and compare causal and bidirectional masks.`
