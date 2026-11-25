# AntV Infographic vs mechanism-specific custom SVG — v12 evaluation

**Status: PARTIAL / experimental.** Three custom diagrams rendered locally; three AntV infographic DSL candidates and a CDN-backed preview page were authored, **but could not be rendered locally** because npm registry access returned DNS error `EAI_AGAIN` and the headless-browser CDN attempt timed out. It would be misleading to announce a visual quality winner between both engines at this stage.

## Evaluated subjects

| Subject | AntV candidate | Offline custom SVG | Mechanism details that must survive |
|---|---|---|---|
| PostgreSQL LEFT JOIN | `relation-dagre-flow-tb-simple-circle-node` | Row-by-row input/output tables | Ada has 2 matches; Ben 1; Cleo survives with NULLs; 4 output rows |
| Transformer attention | `sequence-ascending-steps` | Vector, scores, weights, weighted sum | q=[1,0], k1=[1,0], k2=[0,1], d_k=2; scores [0.7071,0], softmax [0.6698,0.3302]; output [6.70,6.60] |
| Decision outputs | `compare-binary-horizontal-simple-fold` | Two-column logit and probability comparison | Softmax [0.7856,0.1753,0.0391] sums to 1; sigmoids [0.9526,0.8176,0.0759] need not sum to 1 |

## Results actually observed

- Custom SVGs: **3/3** parsed as SVG and rendered to PNG using CairoSVG. Original images were visually inspected. Minor math-font issue was corrected and re-rendered.
- Technical fixture: PostgreSQL row multiplication/null preservation, attention numerical values, and softmax/sigmoid invariants were checked with assertions, all passed.
- AntV DSL: **3/3** passed minimal local DSL-shape checks (valid candidate template families, `data` and `theme` blocks). **Not validated against the AntV renderer**; actual template registration, DSL field compatibility, typography, geometry, SVG export and mobile layout remain unknown.
- Existing v11 skill regression tests: **8/8 passed**.
- Browser visual comparison: **blocked**. Chromium external-CDN attempt stalled; the offline custom diagrams were instead verified via CairoSVG PNG renders.
- Public repo: verified official `@antv/infographic` package, MIT license, declarative syntax, bundled templates and skills. Official README: https://github.com/antvis/Infographic ; official creator skill: https://github.com/antvis/Infographic/tree/main/skills/infographic-creator .

## Preliminary engineering decision

Adopt **AntV as an optional, preferred renderer for broad sequences, comparisons and architecture overviews**, subject to successful pinned local install and rendered tests. Keep **custom SVG as mandatory escape hatch** for detailed rows, tensor operations, token-level flow, exact math, or other mechanisms inadequately represented by AntV templates.

**Do not make AntV the default for all figures yet.** There is insufficient local rendering evidence. The same is true for claims of speed, output fidelity, mobile compatibility or cross-run consistency.

## How to complete the AntV visual experiment on a connected machine

1. Install `@antv/infographic@0.2.20` in a clean Node project using `npm install --save-exact @antv/infographic@0.2.20`.
2. Open `examples/visual-comparison/index.html` with network access, or replace the pinned CDN script with a local UMD build and inspect the 3 live AntV panels.
3. For each figure, confirm rendered structure, label fit, accuracy, text contrast and mobile 375px screenshot. Use the `Export AntV SVG` button to obtain a static artifact and test it offline.
4. Compare rendered diagrams against custom SVG at both desktop and mobile sizes; reject cases where visual simplicity hides row multiplicity, score derivation, or other core mechanism.
5. Check the installed AntV release's actual template names and schema before treating the DSL candidate as tested.
6. Record results and screenshots in this report; only then consider AntV the default renderer for the supported diagram categories.

## Scope and provenance

Examples, numbers and figures are original/synthetic explanatory content. No diagrams or images were copied from TheLion.AI. They do not establish any proprietary Jev internals or measured performance. The AntV project is MIT licensed; our bundle **links to it but does not vendor its source code**.
