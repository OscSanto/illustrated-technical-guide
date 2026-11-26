# Backlog

Changes found while auditing the skill with its own method (the "How a skill is built" guide, November 2026). Agreed as worth doing, deferred for now.

## Scripts and gates
- **Move legacy scripts out of the skill folder.** Delete `scripts/validate_guide.py`, the original HTML checker. It needs BeautifulSoup, checks less than `quality_gate.py` and is referenced nowhere. Move `scripts/publication_gate.py` to a `legacy/` folder and `scripts/test_source_fidelity.py` to `tests/`. Then shorten the "Compatibility" paragraph in SKILL.md.
- **Give `references/provenance.md` the same gate commands as SKILL.md.** It still says to run `source_fidelity_gate.py` and `publication_gate.py` directly, while SKILL.md makes `quality_gate.py` the main entry point. `quality_gate.py` already calls the provenance gate.
- **Fix the `source_fidelity_gate.py` crash on an empty folder.** Its early returns have no `scope` field, so `main()` raises `KeyError: 'scope'`. It still exits non-zero, but only by accident.
- **Check shown code against tested code.** Add a `quality_gate.py` check that every code block on the page matches its lab file exactly. The skill guide's `lab/lab2_trace_request.py` already does this with `ast`. Changed code was one of 6 planted faults the gates missed.
- **Check origin labels per artifact.** If one copy of a label is removed but the same label appears elsewhere on the page, the gate still passes.

## SKILL.md and references
- **Trim step 3.** At 828 characters it is the longest line in SKILL.md. Move the details of when to animate into `references/animated-flow-figures.md` and leave one sentence in the step.
- **Merge the three small references.** `pedagogy.md`, `research.md` and `execution.md` are each under 1 KB. One file would mean fewer reads for the same content.
- **Reconsider step 8 (cross-topic figure gate).** It only applies when a new illustration engine is built.

## Evaluation
- **Run the evals.** `evals/cases.json` defines 8 cases × 3 runs; 0 of 24 have been run.
- **Rerun the trigger test with a longer turn cap.** Old and new descriptions each triggered on 3 of 9 Jev prompts that do not name the skill. The 2-turn cap cut most sessions off while they were still exploring, so the test could not separate the two descriptions. Try about 8 turns and 5 runs per prompt.

## Repository hygiene
- **Extend `.gitignore`.** Add `__pycache__/` and the `QUALITY_REPORT.*` files that tests write into `evals/fixtures/`.
