# Human scoring rubric (each dimension 0–4)
- 0: absent/incorrect, 1: substantial gaps, 2: partially effective, 3: meets stated learning objectives, 4: precise, clear and demonstrably successful.
- `beginner_success`: can a novice complete the first checkpoint with provided instructions and recover from common errors?
- `technical_accuracy`: equations, API facts, examples, and explanations checked against trustworthy evidence.
- `illustration_mechanism`: diagrams reveal actual state, values, relationships and edge cases, not generic boxes.
- `provenance`: all sourced, derived, illustrative and invented artifacts distinguished accurately.
- `reproducibility`: run logs, target runtime, versions, expected outputs and assertions sufficient.

A reviewer must link evidence; unreviewed dimensions should be null, not guessed. Report structural gate separately from quality scores. Recommended release threshold: mean >=3 on all dimensions, no dimension <2 for any accepted output, zero critical factual errors or unsupported attributions, and at least 3 independent runs per case. These are proposed criteria; not achieved metrics.
