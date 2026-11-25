# MedDecider source-audit retest — November 23, 2026

Reference: https://www.thelion.ai/projects/meddecider/

## Executed checks
- 20 critical source claims tracked in `source_coverage.csv`, each matched to guide text; no missing critical ledger items.
- 14 chapters and 13 original figures; all internal links resolve.
- NumPy scoring lab passed normalization, non-negativity, reversal remapping and cross-entropy checks.
- Expanded the earlier guide with model configuration, training mix, exact reported hyperparameters, calibration settings, clinical use cases, full family benchmark matrix, confidence interval, prompt-injection results, licensing and limitations.
- Noted a source-level arithmetic discrepancy: displayed 4B dataset components sum to 118,600 versus reported 119,034.

## Limits
- The 20-claim ledger is a prioritized coverage audit, **not an exhaustive sentence-by-sentence verification** of every claim on the source page.
- Reported benchmarks, latency and clinical use-case probabilities have not been independently reproduced. Model weights were not downloaded; no full LoRA training was performed.
- No headless browser screenshots or mobile visual comparison were executed. HTML was parsed and anchors validated, but rendering is not certified.
- Clinical applications are research examples only and are not validated for patient care.

### v7 mathematics correction
Replaced four plain-Unicode display equations with offline MathJax-rendered SVG; verified the original LaTeX, accessible labels and SVG markup. Browser screenshot testing not completed.
