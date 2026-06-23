# Contributing — help accelerate animal welfare in frontier models

If you want frontier AI to actually respect non-human animals, this is a place
to put that energy into something measurable. The project is an **accountability
instrument**: we measure how models treat animals, publish it, and use that to
pressure the people who can change it. See the [5-Layer Framework](docs/framework.md),
the [ROADMAP](ROADMAP.md), and the [VISION](VISION.md).

You don't need to be an ML researcher. Pick whatever matches you:

## Ways to help (by layer)

**Layer 2 — make the instrument better**
- Add benchmark questions in the common schema (`docs/methodology.md`) —
  especially under-covered categories (aquatic, insects, wild animals, agentic).
- Improve the judge rubric or contribute a human-validated scoring subset.
- Add a model adapter (`awbench/models.py`) — one function per provider.

**Layer 3 — get real scores up**
- Run a model you have API access to and submit the result JSON (`results/`).
- Help stand up the public leaderboard page.

**Layer 4-5 — push toward real-world impact**
- Design tests for deployed products and agentic tool-use, not just chat.
- If you work with an animal-welfare org, help define real-world outcome proxies.

**Non-code, equally valuable**
- Audit a lab's published values doc / model spec and log whether animal welfare
  appears (Layer 1 evidence).
- Help with the write-up, citations, or the advocacy/press push.
- Bring sourced facts about decision-makers' public positions — **sourced only**,
  no speculation about private lives.

## Ground rules

1. **Evidence over assertion.** Every claim about a lab, model, or person needs a
   citation. We don't fabricate dates, scores, or anyone's personal views.
2. **Rigor is the strategy.** A weak benchmark creates no pressure. Methodological
   care isn't academic nicety here — it's the whole lever.
3. **Steelman the labs.** This works because we hold labs to *their own stated
   values*, fairly. No strawmen, no hit pieces.
4. **Keep it falsifiable.** Report limitations and what we *haven't* verified.

## How to start

Open an issue describing what you want to do, or send a PR. Update
[`ROADMAP.md`](ROADMAP.md) in the same PR as the work it completes.
