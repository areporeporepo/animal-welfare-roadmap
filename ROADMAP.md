# Roadmap & Progress

Organized by the [5-Layer Framework](docs/framework.md) and by time horizon —
each horizon drives verification one layer deeper down the stack, the way a
hardware roadmap ships one architecture per generation.

**Legend:** ✅ done · 🟡 in progress · ⬜ not started

## Progress at a glance

| Layer | What it proves | Status |
| ----- | -------------- | ------ |
| 1 — Declared | labs *say* it | ✅ audited (Anthropic yes, OpenAI no) |
| 2 — Instrument | we can *measure* it | 🟡 harness runs; rigor in progress |
| 3 — Score | how models *actually* do | ⬜ needs live runs |
| 4 — Industry | holds in *deployed* products | ⬜ future |
| 5 — IRL | reduces real *suffering* | ⬜ north star |

---

## Horizon 1 — "Instrument" (now → 2026 H2) · Layers 1-2
Goal: a credible, runnable instrument and a documented gap.

- [x] Audit Layer 1: cite Claude's Constitution verbatim + provenance ([docs/constitution.md](docs/constitution.md))
- [x] Document the gap: value declared but unmeasured ([docs/the-gap.md](docs/the-gap.md))
- [x] Build the harness: dataset schema, model adapters, judge, leaderboard
- [x] Pipeline runs end-to-end offline (CI-verified)
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

## Horizon 5 — "IRL" (2028+) · Layer 5
Goal: connect scores to real-world animal outcomes.

- [ ] Define outcome proxies (decisions changed, harm avoided)
- [ ] Partner with animal-welfare orgs for field measurement
- [ ] Report the north-star: did any of this reduce real suffering?

---

*Update this file in the same PR as the work it tracks. A roadmap that lags the
code is just a wish list.*
