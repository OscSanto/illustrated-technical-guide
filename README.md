# Illustrated Technical Guide — Claude / Claude Code Skill v2

A reusable instruction skill for generating **original, standalone illustrated HTML guides about any subject**, using adaptive chapter counts and a dynamically built table of contents. `index.html` is a working **decision-model demo**, not the content that will be repeated for every topic.

## Install in Claude Code (personal)

Extract the ZIP and copy the folder `illustrated-technical-guide/` into:

- macOS/Linux: `~/.claude/skills/illustrated-technical-guide/`
- Windows: `%USERPROFILE%\.claude\skills\illustrated-technical-guide\`

The file `SKILL.md` must be directly inside that folder. For a project-only skill, use `.claude/skills/illustrated-technical-guide/` in the project root instead.

## Invoke

**Explicit (recommended for reliability):**

`/illustrated-technical-guide Explain transformer attention from scratch, with math, diagrams, and PyTorch.`

**Implicit:**

`Create a comprehensive illustrated HTML textbook explaining Bayesian inference, with a clickable table of contents and worked examples.`

Claude Code can select the skill automatically based on the description, but auto-selection is not guaranteed. If the slash command is not discovered, restart the session and check the folder and YAML frontmatter. You can also say `Use the illustrated-technical-guide skill to ...`.

## Claude.ai (web/app)

Skill support and installation depend on the Claude environment and account. If custom Skills are available, upload the ZIP through the relevant Skills settings and enable it. Explicitly ask Claude to use the skill; implicit selection may occur but is not guaranteed. If custom Skills are not available, attach `SKILL.md` and the HTML reference and ask Claude to follow them. A Claude Project's instructions are an alternative, but not the same as a registered skill.

## What's improved in v2

- Content-driven outline; chapter count varies by topic.
- Desktop and mobile TOC generated from the actual headings (including h3 subsections).
- Active-section highlighting and reading progress.
- Automatic mobile TOC collapse after a selection.
- Topic-specific diagram decision rules, citation integrity, complete-chapter quality gate.
- Clear explicit and implicit invocation instructions.

## Files

- `SKILL.md`: the reusable agent instructions.
- `index.html`: self-contained HTML demo with adaptive TOC behavior.
- `README.md`: installation and invocation.

This skill reproduces an *educational design approach*, not the original TheLion.AI copyrighted page.
