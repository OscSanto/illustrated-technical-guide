# Source and evidence ledger — Jev example

- [TheLion.AI Visual Guide](https://www.thelion.ai/guide-to-decision-models/): benchmark for editorial breadth and published 15-chapter/44-illustration/70-source counts. Design inspiration only; figures and explanatory text in our example are original.
- [TypeSafe Jev documentation mirrored in public GitHub repository](https://github.com/jevmodel/typesafe-jev): documented shared state, Choice, Score, Noul, output types and API behavior. Source claims in the example are limited to public interface descriptions.
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762): standard scaled dot-product attention and transformer background.
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599): temperature scaling and calibration background.

## Evidence boundaries
- **Published/documented:** Typed decision questions, shared state, returned probabilities and structured outputs.
- **Inferred/educational reconstruction:** Shared-prefix architecture, particular attention masks, option-embedding readouts, distillation training objective, internal optimizer and serving strategies.
- **Illustrative:** All small logits, distributions, thresholds, diagrams and numerical examples in this guide.
- **Measured:** Only locally executed arithmetic assertions and static HTML checks; no proprietary Jev accuracy or latency benchmark was performed.
