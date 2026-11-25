.PHONY: test eval fixture

test:
	python -m unittest discover -s tests -v

eval:
	python evals/evaluate.py --suite evals/cases.json --root evals/outputs

fixture:
	python skills/illustrated-technical-guide/scripts/quality_gate.py --guide evals/fixtures/pass
