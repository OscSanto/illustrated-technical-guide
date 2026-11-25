# Installation

Clone or download this repository, then copy `skills/illustrated-technical-guide/` to your Claude Code project at `.claude/skills/illustrated-technical-guide/` (or your supported user-level skill directory). Keep `SKILL.md`, `profiles/`, `references/`, `templates/`, and `scripts/` together.

Example:

```bash
mkdir -p .claude/skills
cp -R skills/illustrated-technical-guide .claude/skills/
```

Invoke `/illustrated-technical-guide Build a beginner PostgreSQL guide using VS Code and a small commerce dataset` or request `Reconstruct <article URL> in source-audit mode`. Features depend on the agent's web/browser/runtime access. A local validator does not run an AI model.
