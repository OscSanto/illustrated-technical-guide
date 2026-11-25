# Illustrated Technical Guide — v3

A topic-independent Claude / Claude Code skill for writing original, research-grounded standalone HTML teaching guides, inspired by the educational organization of TheLion.AI, not copied from its design assets.

## Installation
Extract this folder as `illustrated-technical-guide` under `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`) for personal use, or `<project>/.claude/skills/` for project-specific use. Ensure `SKILL.md` is directly inside that folder.

## Invoke
Explicit in Claude Code: `/illustrated-technical-guide Explain transformer attention, with full derivations and executable PyTorch.`
Implicit: `Create a comprehensive illustrated HTML guide to Bayesian inference.` Claude may select the skill if relevant, but selection is not guaranteed.

In Claude.ai, install/upload the skill through the Skills feature if available on your account; ask Claude to use it by name. This ZIP is for a Claude skill, not a deployed website.

## Files
- `SKILL.md` — generation requirements and depth/quality gates.
- `template.html` — standalone design reference.
- `examples/jev-guide.html` — earlier illustrative example; deliberately short of v3's full depth requirements.
- `scripts/validate_guide.py` — static checks (requires `beautifulsoup4`).

## What's new
Eight-part depth gate per major mechanism, numerical traces, reproducible code and tests, claim ledger, explicit proprietary/inferred distinctions, no-JS TOC requirement, and deterministic HTML audit. These requirements improve reliability but cannot guarantee that a generated guide is as extensive or visually polished as the reference website. Browser visual QA and factual source verification remain necessary.

## Test
`python scripts/validate_guide.py examples/jev-guide.html`
