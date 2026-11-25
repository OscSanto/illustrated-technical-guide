# Illustrated Technical Guide v15 — Source-faithful repository reconstruction

This preview preserves the v14 generic textbook generator and optional source reconstruction while adding `references/repository-reconstruction.md` for real codebases.

## New example
Open `examples/zimantic/index.html` to study the [OscSanto/zimantic](https://github.com/OscSanto/zimantic) repository at commit `40c404f6dd409dc0e1d80fb89f9212b99a8542f3`.

The 11-chapter HTML guide contains 10 original offline SVGs, SQL/algorithm educational fixtures, a benchmark plan, source coverage, provenance and a mobile zoom viewer. It is DRAFT because real ZIM/ONNX and Raspberry Pi benchmarks were not executed here.

## Install
Copy `skills/illustrated-technical-guide/` into your Claude Code skills directory. The `SKILL.md` is the entry point; its `references/` and other files must remain alongside it.

## Run educational verification
`python examples/zimantic/labs/verify_concepts.py`

Existing v14 regression tests and evaluation suite are retained. New source reconstruction instructions live in `skills/illustrated-technical-guide/references/repository-reconstruction.md`.
