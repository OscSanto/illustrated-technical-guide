# Depth-first teaching standard (v16)

## Core rule
**Do not stop when a concept has been introduced; stop when its mechanism can be reconstructed.** A page that lists component names, summarizes a diagram, or supplies a formula without tracing intermediate states is not a finished technical chapter.

### Three levels, with different budgets
1. **Orientation** (short): purpose, inputs/outputs, prerequisites, global map, and why the learner should care. Do not expand every topic prematurely.
2. **Mechanism** (primary): trace **one authentic or clearly labeled synthetic input** from a specific entry point to a verifiable output. At each consequential transform, explain shape/type/representation, a concrete intermediate state, the rule changing it, why the rule exists, and which later subsystem consumes it. Use a mechanism-specific diagram **in addition to**, not instead of, the prose.
3. **Implementation and diagnosis**: point to exact source function/lines or verified docs, unpack nontrivial code, show calculations and a test, and explain failure modes, tradeoffs, and parameter consequences. Teach how to predict behavior under variations.

### Choose depth by conceptual density, not a universal quota
Allow short chapters for orientation, recaps, or simple utilities. For a chapter with multiple difficult transformations (e.g., tokenization + pooling + normalization + indexing), expect several substantial subsections, often 800–1500+ explanation words where warranted; this is a planning heuristic, **not** a PASS threshold. Complex topics can exceed it. A small formula can be concise when a short worked example fully teaches it.

### The mechanism-trace worksheet (required per core concept)
| Field | Evidence required |
|---|---|
| Learner goal | What the reader can reconstruct without the guide |
| Starting state | Exact or labeled hypothetical data, types, and assumptions |
| Transition trace | Ordered operations; function/code locations; intermediate values or shapes |
| Invariants | What IDs, units, constraints, or data identities stay consistent |
| Derived check | Computed output with repeatable calculation or actual runtime test |
| Counterexample | At least one change of input or parameter and predicted outcome |
| Failure/tradeoff | Operational limit, diagnostic signal, or design alternative |
| Visual memory | A figure that reveals a **specific** transformation and coordinates with prose |

**Do not accept generic answers** such as “the vector is normalized” without specifying input shape, operation, calculated example, and why it matters. Equally, don't fill pages with repetitive history, meta-instructions, evidence labels or generic overview prose.

### Avoid prose pollution from provenance
Keep provenance **accurate and discoverable** in captions, source anchors, expandable notes, a bibliography or coverage ledger. A source-reported number can be described naturally once in the narrative. Repeat caveats only when an inference could otherwise be mistaken for an observation. Pseudocode and hypothetical architectures still require **visible** origin labels, but they need not interrupt every paragraph.

### Publication checks
A deterministic script can validate the existence of worksheets, examples, figures, citations and test artifacts; it cannot guarantee true understanding or correctness. Source review, numerical execution and learner testing remain distinct gates. If a chapter can't reconstruct its main operation in the trace worksheet, mark it incomplete even if its length and figure count are large.
