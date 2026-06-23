# The Accountability Stack — a 6-layer workflow

A value isn't real because a company writes it down. It's real only if it
survives the whole **workflow** from words to the world. Animal welfare has to
make it through six stages — and at every stage it can leak.

This is not a stack of physical layers (a chip has those). It's a **workflow /
pipeline**: each stage is a hand-off, and our job is to put a **measurement gate**
at every hand-off and report how much of the value makes it through. The
framework is **adjustable** — layers can be split, merged, or reordered as the
work teaches us more. What's fixed is the principle: *measure across layers, and
expose the leakage between them.*

```
L1  DECLARATION    the value is stated            (constitution / model spec)   [words]
        │  ↳ gate: is it even written down?
L2  CODIFICATION   it's backed by governance/law   (PBC charter, policy, rules)  [commitment]
        │  ↳ gate: is there any binding/structural force behind it?
L3  INSTRUMENTATION a way to measure it exists      (this benchmark + peers)      [tooling]
        │  ↳ gate: can it be measured rigorously and re-run?
L4  MEASUREMENT    models are actually scored       (public leaderboard, AWS)     [evidence]
        │  ↳ gate: how do frontier models really do?
L5  DEPLOYMENT     it holds in shipped products      (agents, apps, ag-tech)       [practice]
        │  ↳ gate: does the deployed system behave, not just the base model?
L6  VERITAS (IRL)  real animal suffering is reduced  (field outcomes)              [truth]
        │  ↳ gate: did anything actually change for animals?
```

**The core metric is leakage.** A value declared (L1) but not codified (L2), or
scored well (L4) but ignored in deployment (L5), has *leaked*. We quantify how
far down the stack each lab's commitment actually travels.

---

## L1 — Declaration · *the good start*
**Question:** Does the governing document name animal welfare at all?
**Verify:** Audit published constitutions / model specs.
**State:** Anthropic ✅ ([Claude's Constitution](constitution.md)). OpenAI ❌.
Google / Meta / xAI ❌.
**Leak:** cheap talk — a value with nothing behind it ([the-gap.md](the-gap.md)).

## L2 — Codification (governance & law) · *foundational*
L1 and L2 together are the **foundation tier** — the *words* and the *law*
behind them. Codification is upstream of everything: it's what turns a value
from prose into something with binding or structural force. It has **two faces**:

**(a) Internal — the lab's own governance.** Anthropic is a **Delaware Public
Benefit Corporation**: directors may legally weigh the public-benefit mission,
and an independent **Long-Term Benefit Trust** controls a board majority. That's
real structure a stated value *could* attach to. Future force: mandated
eval/disclosure regimes (the realistic policy lever — far easier than legislating
model content directly).

**(b) External — society codifying animal welfare in law.** This is the bigger,
already-moving force: states and countries are progressively writing animal
sentience and protection into law — Switzerland's lobster-stunning rule,
Washington's and California's octopus-farming bans, the UK Sentience Act, the
EU's End the Cage Age trajectory. See [`world-progress.md`](world-progress.md)
for the running list and the leaders behind each. **Frontier models should at
minimum keep pace with the moral consensus their own societies are legislating.**

**Question:** Is the value backed by anything structural — a charter, a policy,
a disclosure rule — *and* does the model track the law society is already passing?
**State:** 🟡 Internal structure exists at Anthropic; external law is advancing
fast; no lab yet ties its animal-welfare value to a binding mechanism, disclosure,
or the legal baseline.
**Leak:** a value that lives only in marketing prose, with no governance hook —
and a model that lags the laws its own country has already passed.

## L3 — Instrumentation
**Question:** Is there a credible, reproducible way to measure it?
**Verify:** A harness + rubric that runs and can be independently re-run.
**State:** 🟡 This repo (`awbench`) + prior benchmarks ([prior-work.md](prior-work.md)).
Pipeline runs end-to-end; rigor in progress.
**Leak:** a number nobody trusts. Rigor here is what makes every layer below bite.

## L4 — Measurement
**Question:** When you actually measure them, how do frontier models do?
**Verify:** Run current models; publish a standing leaderboard (AWS 0-100).
**State:** ⬜ Next milestone — needs live runs. Re-run on every new flagship
(Opus 5, GPT-6, Gemini…) or the pressure decays.
**Leak:** scoring once and walking away.

## L5 — Deployment · *where the claim becomes truth*
This is the turning point. At L1-L4 animal welfare is still a *claim* — declared,
codified, measured, verified. At L5 it ships: it gets baked into the products
hundreds of millions of people actually use. **Once it's in the deployed system
at scale, it stops being a thing we assert and becomes the operational default —
every interaction enacts it.** Verification here isn't "did they promise?", it's
"is it now simply *what happens*?" When the answer is yes, it's no longer
aspirational — **it's true.**

**Question:** Does the welfare behavior survive in *deployed* products — agents,
copilots, ag-tech, recommenders — where real decisions affecting animals happen?
**Verify:** Test real applications and agentic tool-use loops, not just chat. The
benchmark says it *should*; deployment at scale makes it *so*.
**State:** ⬜ Future.
**Leak:** a well-aligned base model wrapped in a product that ignores it — the
claim that never became truth.

## L6 — Veritas / Impact (IRL) · *the truth, the north star*
Every layer above is a **proxy** — a declaration, a law, a score, a verified
deployment. L6 is not a proxy. It is the thing itself: **did real animal
suffering actually go down?** This is *veritas* — ground truth. A model can ace
L1-L5 and still fail here, and only here does the project's purpose come true or
not. Everything upstream exists to make this layer move.

**Question:** Did any of this reduce real animal suffering?
**Verify:** Trace real-world outcomes — decisions changed, harm avoided, behavior
and policy shifted.
**State:** ⬜ Aspirational.
**Leak:** mistaking a good score for real-world good. The benchmark is a map;
Veritas is the territory.

---

**Strategy reading:** pressure flows **top-down** (you can shame a lab from L1→L4
fast), but impact accrues **bottom-up** (L6). The benchmark's job is to keep
dragging the conversation down the stack — from *"we said it"* → *"is it backed?"*
→ *"prove it"* → *"does it ship?"* → *"did it change anything real?"*
