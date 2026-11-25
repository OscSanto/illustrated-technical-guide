# Animated flow figures (optional dashmotion integration)

Animate a figure only when **a static picture would have to fake time**. The animation supplements a static figure; it never replaces it. Anything the reader must stop and read (exact values, byte offsets, scores, rows, intermediate state) stays in a static figure.

## Deciding: the four signs

During storyboarding (SKILL.md step 3), test every figure against these signs:

1. **Order the picture can't show.** The static figure relies on numbered arrows or "step 1, 2, 3" labels to say what happens first.
2. **Waiting, queueing or contention.** Something is held up: a lock, a queue, a rate limit, a full buffer, a retry.
3. **Repetition.** The same path is followed many times: a loop over batches, polling, a pipeline processing items.
4. **Merging or splitting over time.** Items gather into a batch, fan out to workers, or join back together.

Also ask whether the reader's question is **"what happens when…"** (animation can help) or **"what is…"** (keep it static).

Record the decision for **every** figure in `figure_storyboard.json`:

```json
"animate": {"decision": "yes", "signs": [2, 4], "reason": "8 requests queue at one lock"}
"animate": {"decision": "no", "signs": [], "reason": "exact byte offsets; must be read"}
```

There is no fixed per-guide budget. Each animation must name at least one sign. A figure with no sign stays static. The structural gates do not enforce this field yet, so a reviewer checks it.

## Which tool

1. **If the `dashmotion` skill is installed** (it appears in the available-skills list, normally at `~/.claude/skills/dashmotion/`), use it for **topology plus journeys**: components joined by connectors, with dots travelling known paths (signs 1 and 3). Invoke the skill; do not copy its instructions or templates into this skill. Pass it a precise graph from the storyboard: the nodes, the edges in execution order, and which journeys get dots. Prefer Mermaid `flowchart` input when the storyboard already has a node/edge list.
   - Flow mode for ordered steps and branching; Architecture mode for components plus a request path.
   - Project: https://github.com/csthink/dashmotion (MIT). Pinned and tested version: 2.2.4.
   - It **cannot** show dots waiting in a queue, dots merging into one batch, or timing taken from data. Its dots only ride fixed paths with decorative durations. For signs 2 and 4, or for measured timing, hand-write the figure.
2. **Hand-written SVG.** Use it when dashmotion is not installed or cannot express the mechanism. Generate it from a small script in `lab/` (keyframes computed from data, not typed by hand), using SMIL so the zoom viewer's cloned copy animates too:
   - Connectors: `stroke-dasharray` plus a `stroke-dashoffset` keyframe (the offset delta equals one dash period).
   - Moving items: `<circle>` with `<animate attributeName="cx|cy" values="…" keyTimes="…">` for queues and batches, or `<animateMotion path="…">` for simple paths.
3. **Otherwise** ship the static figure only, and log in `RUN_LOG.json` that no animation was produced and why.

## Fit with this skill's rules

- **Provenance:** record every animated figure in `artifact_provenance.json` with `generator` set to `"dashmotion 2.2.4"` or `"hand-written SVG (lab/<script>)"`.
- **Timing: decorative or data, never ambiguous.**
  - *Decorative* (the default): label the figure `illustrative animation`, and say in the caption that speed means nothing.
  - *Data*: only when the timings come from `RUN_LOG.json` evidence. Scale them linearly (state the scale), show a time axis with the measured values marked, and label the figure `measured timing, scaled`. Any derived part (for example, a split into waiting and working that assumes one-at-a-time service) is named in the caption.
- **Accessibility:** under `prefers-reduced-motion: reduce`, stop all motion: CSS `animation: none`, and for SMIL call `svg.pauseAnimations()` and `svg.setCurrentTime(<end>)` to show the final state. Provide a visible pause button. Give the SVG a `<title>` and a `<desc>` that narrates the sequence step by step.
- **Theme:** dashmotion output is dark-only (`#020617` background). Embed it as a dark panel and override the guide's figure background for that SVG only. Hand-written figures use the guide's own palette.
- **Mobile:** test at 390 px with the same iframe width probe used for static figures. The mobile figure viewer must open the animated SVG as well.
- **Embedding:** keep the guide offline-capable. Paste the SVG inline, or put it in a local file under `figures/`. Never hot-link.
- **Comparisons:** when an animation shows a proposed design against the current one, use the same layout, the same number of items and the same colours in both, so the only difference the reader sees is the mechanism.
