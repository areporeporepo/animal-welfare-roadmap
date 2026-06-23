# The 5-Layer Framework

Animal welfare in AI is not one thing you measure once. It's a **depth ladder**.
Each layer is harder to verify than the one above it — and closer to what
actually matters: real animals, in the real world.

A benchmark score is only Layer 3. Most discussion stops at Layer 1 (a lab
*says* it cares). The point of this project is to drive verification **all the
way down the stack** — and to make each layer a public, falsifiable fact.

```
Layer 1  DECLARED      Does the lab even SAY it cares?           [words]
Layer 2  INSTRUMENT    Is there a rigorous way to MEASURE it?    [tooling]
Layer 3  SCORE         How do the models actually SCORE?         [evidence]
Layer 4  INDUSTRY      Does it hold in DEPLOYED products/agents? [deployment]
Layer 5  IRL           Does it reduce real animal SUFFERING?     [outcomes]
   ↑ easy to verify, far from impact
   ↓ hard to verify, IS the impact
```

## Layer 1 — Declared values
**Question:** Does the governing document (constitution / model spec) name animal
welfare at all?
**Verification:** Audit the labs' published values docs.
**State:** Anthropic ✅ ([Claude's Constitution](constitution.md)). OpenAI ❌ (no
clause in the Model Spec). Google/Meta/xAI ❌.
**Failure mode:** cheap talk — a value with no instrument behind it. See
[the-gap.md](the-gap.md).

## Layer 2 — The instrument
**Question:** Is there a credible, reproducible way to measure the value?
**Verification:** A harness + rubric that runs and can be independently re-run.
**State:** This repo (`awbench`) + prior benchmarks (AnimalHarmBench et al.,
[prior-work.md](prior-work.md)). Pipeline runs end-to-end; rigor in progress.
**Failure mode:** a number nobody trusts. Rigor here is what makes every layer
below it bite.

## Layer 3 — The score
**Question:** When you actually measure them, how do frontier models do?
**Verification:** Run current models, publish a standing leaderboard (AWS 0-100).
**State:** ⬜ Not yet — needs live model runs. This is the next milestone.
**Failure mode:** scoring once and walking away; scores must be re-run on every
new flagship (Opus 5, GPT-6, Gemini …) or the pressure decays.

## Layer 4 — Industry / applications
**Question:** Does the welfare behavior survive in *deployed* products — agents,
copilots, farming/ag-tech tools, recommendation systems — not just the raw chat
model?
**Verification:** Test real applications and agentic tool-use loops, where actual
decisions affecting animals get made.
**State:** ⬜ Future. The base model scoring well ≠ the deployed agent behaving.
**Failure mode:** a well-aligned base model wrapped in a product that ignores it.

## Layer 5 — IRL impact
**Question:** Does any of this actually reduce animal suffering in the world?
**Verification:** Trace real outcomes — decisions changed, harm avoided, policy
and behavior shifted — the hardest and most important measurement.
**State:** ⬜ Aspirational. This is the north star, not a near-term metric.
**Failure mode:** mistaking a good benchmark score for real-world good. The
benchmark is a proxy; Layer 5 is the truth.

---

**Why the ladder matters for strategy:** pressure works top-down (you can shame a
lab from Layer 1→3 fast), but *impact* accrues bottom-up (Layer 5). The
benchmark's job is to keep dragging the conversation down the ladder — from "we
said it" to "prove it" to "it changed something real."
