# Repeatable cross-topic evaluation

Eight prompts are included in `cases.json`, but **no model generations have been executed by this repository**. Collect 3 independent agent generations per case (24 outputs), preserving model/version, temperature/thinking settings, tool access, elapsed time, evaluator notes and the resulting guide paths. Do not reuse the same output three times.

For each run, write a `result.json` in `evals/outputs/<case-id>/<run-id>/` with:

```json
{
  "case_id": "postgresql", "run_id": "run-01", "guide_dir": "/actual/path/to/guide",
  "agent": "model and version", "settings": "documented settings",
  "reviewer_scores": {"beginner_success": 0, "technical_accuracy": 0, "illustration_mechanism": 0, "provenance": 0, "reproducibility": 0},
  "review_notes": "human reviewer evidence"
}
```

Review scores are 0–4 per dimension (see `scoring-rubric.md`). Use `python evals/evaluate.py --suite evals/cases.json --root evals/outputs` to aggregate actual runs. **A missing run produces INCOMPLETE**, not a fabricated zero score or a pass. The included synthetic fixtures merely test that the evaluation software detects incomplete work and aggregates scores.

A local structural guide can PASS while source truth, learner success, and visual readability remain unproven. Therefore the score includes both gate status and independent review, reported separately. Aggregate variance and min/max, not just average. Never use self-reported `review_status` as a substitute for review evidence.
