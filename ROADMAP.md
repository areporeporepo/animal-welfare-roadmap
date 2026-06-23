# Roadmap & Progress

Organized by the [6-layer Accountability Stack](docs/framework.md) and by time
horizon — each horizon drives verification one layer deeper down the workflow,
the way a fabrication pipeline is qualified one stage at a time.

**Legend:** ✅ done · 🟡 in progress · ⬜ not started

## Progress at a glance

| Layer | What it proves | Status |
| ----- | -------------- | ------ |
| L1 — Declaration | labs *say* it | ✅ audited (Anthropic yes, OpenAI no) |
| L2 — Codification (legal) | it's *backed* by governance/law | 🟡 structure exists; not yet tied to the value |
| L3 — Instrumentation | we can *measure* it | 🟡 harness runs; rigor in progress |
| L4 — Measurement | how models *actually* score | ⬜ needs live runs |
| L5 — Deployment | holds in *shipped* products | ⬜ future |
| L6 — Veritas (IRL) | reduces real *suffering* (the truth) | ⬜ north star |

---

## Horizon 1 — "Instrument" (now → 2026 H2) · Layers L1-L3
Goal: a credible, runnable instrument, the legal/governance picture, and a
documented gap.

- [x] Audit L1: cite Claude's Constitution verbatim + provenance ([docs/constitution.md](docs/constitution.md))
- [x] Document the gap: value declared but unmeasured ([docs/the-gap.md](docs/the-gap.md))
- [x] Build the harness: dataset schema, model adapters, judge, leaderboard
- [x] Pipeline runs end-to-end offline (CI-verified)
- [ ] **L2 (legal):** map each lab's governance hooks (PBC charter, trust/board, disclosure norms) the welfare value could attach to
- [ ] **L2 (legal):** identify the realistic policy lever (mandated eval/disclosure, not legislating model content)
- [ ] Ingest a full public benchmark (AnimalHarmBench) in the common schema
- [ ] Rigor pass: human-validated judge subset + inter-rater agreement
- [ ] Multi-judge scoring to reduce judge bias

## Horizon 2 — "Score" (2026 H2 → 2027) · Layer 3
Goal: real frontier-model numbers on a standing, public board.

- [ ] First live run: Claude (Opus 4.8 / 5) → first real AWS on the board
- [ ] Add GPT-* and Gemini-* runs
- [ ] Add Llama / DeepSeek / open-weight models
- [ ] Publish the standing leaderboard publicly (stanford.edu or repo Pages)
- [ ] Re-run protocol: score every new flagship at release
- [ ] Contamination-resistant dynamic split (LiveBench-style refresh)

## Horizon 3 — "Adoption" (2027) · Layers 1→3 feedback
Goal: labs report the number themselves.

- [ ] Submit as a HELM-style scenario for independent distribution
- [ ] Formal write-up / paper with full citations
- [ ] Get at least one lab to report an animal-welfare score on a model card
- [ ] Press / advocacy push so the leaderboard creates competitive pressure

## Horizon 4 — "Industry" (2027 → 2028) · Layer 4
Goal: measure deployed products, not just base models.

- [ ] Benchmark agentic / tool-use settings (where real decisions get made)
- [ ] Test deployed ag-tech, assistant, and recommendation products
- [ ] Publish an "application-layer" leaderboard

## Horizon 5 — "Veritas / IRL" (2028+) · Layer L6
Goal: connect scores to real-world animal outcomes.

- [ ] Define outcome proxies (decisions changed, harm avoided)
- [ ] Partner with animal-welfare orgs for field measurement
- [ ] Report the north-star: did any of this reduce real suffering?

---

*Update this file in the same PR as the work it tracks. A roadmap that lags the
code is just a wish list.*
