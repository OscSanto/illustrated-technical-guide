# Publication gate: FAIL

- C1: claim not verified
- C2: claim not verified
- C3: claim not verified
- C4: claim not verified
- C5: claim not verified
- C6: claim not verified
- C7: claim not verified
- C8: claim not verified
- C9: claim not verified
- C10: claim not verified
- C11: claim not verified
- C12: claim not verified
- start: code/tests not executed
- start: educational review pending
- install: code/tests not executed
- install: educational review pending
- vscode: code/tests not executed
- vscode: educational review pending
- schema: code/tests not executed
- schema: educational review pending
- data: code/tests not executed
- data: educational review pending
- queries: code/tests not executed
- queries: educational review pending
- group: code/tests not executed
- group: educational review pending
- joins: code/tests not executed
- joins: educational review pending
- analysis: code/tests not executed
- analysis: educational review pending
- performance: code/tests not executed
- performance: educational review pending
- diagnose: code/tests not executed
- diagnose: educational review pending
- production: code/tests not executed
- production: educational review pending
- fig-start: desktop/mobile screenshot review incomplete
- fig-start: figure instructional review pending
- fig-install: desktop/mobile screenshot review incomplete
- fig-install: figure instructional review pending
- fig-vscode: desktop/mobile screenshot review incomplete
- fig-vscode: figure instructional review pending
- fig-schema: desktop/mobile screenshot review incomplete
- fig-schema: figure instructional review pending
- fig-data: desktop/mobile screenshot review incomplete
- fig-data: figure instructional review pending
- fig-queries: desktop/mobile screenshot review incomplete
- fig-queries: figure instructional review pending
- fig-group: desktop/mobile screenshot review incomplete
- fig-group: figure instructional review pending
- fig-joins: desktop/mobile screenshot review incomplete
- fig-joins: figure instructional review pending
- fig-analysis: desktop/mobile screenshot review incomplete
- fig-analysis: figure instructional review pending
- fig-performance: desktop/mobile screenshot review incomplete
- fig-performance: figure instructional review pending
- fig-diagnose: desktop/mobile screenshot review incomplete
- fig-diagnose: figure instructional review pending
- fig-production: desktop/mobile screenshot review incomplete
- fig-production: figure instructional review pending
- Target-engine SQL execution unverified
- Independent figure-by-figure visual review unverified

## Evidence
{
  "engine": "PostgreSQL",
  "execution": "UNVERIFIED",
  "reason": "postgres/psql not installed; apt installation timed out; no actual server query execution",
  "commands": [
    {
      "command": "command -v psql",
      "result": "not found"
    },
    {
      "command": "apt-get update && apt-get install postgresql",
      "result": "timed out"
    }
  ],
  "screenshots": [
    "assets/desktop.png",
    "assets/mobile.png"
  ],
  "visual_review": "UNVERIFIED"
}
