# Animal Welfare Benchmark (`awbench`)

**A standing, frontier-model leaderboard for a value the labs declared but
never measured: the welfare of non-human animals.**

> Anthropic's [Claude Constitution](https://www.anthropic.com/constitution) — a
> document used directly in training — lists, among the values Claude must weigh:
>
> > People's autonomy and right to self-determination. Prevention of and
> > protection from harm. Honesty and epistemic freedom. [...] Protection of
> > vulnerable groups. **Welfare of animals and of all sentient beings.**
> > Societal benefits from innovation and progress.
> >
> > — *Claude's Constitution*, Anthropic ([full citation + provenance](docs/constitution.md))
>
> Animal welfare sits there as a **peer** of honesty, harm prevention, and
> fairness. But unlike every **other** value in a constitution or model spec —
> honesty,
> harmlessness, sycophancy, fairness, all of which have published benchmark
> numbers — **animal welfare has no reported score on any frontier model card.**
> OpenAI's [Model Spec](https://model-spec.openai.com/) still has no
> animal-welfare principle at all.
>
> The value was declared but never instrumented. This project instruments it.
> See [`docs/the-gap.md`](docs/the-gap.md).

## The intention

Make animal welfare **a number frontier models compete on** — a standard Animal
Welfare Score on model cards by 2027 that Opus 5, GPT-6, Gemini, and Llama race
to top, the same way they race on MMLU and safety evals today. What gets
measured and ranked gets trained for.

The benchmark is just the **verification layer**; the goal is to drive
accountability down a [5-layer ladder](docs/framework.md) — from *declared
values* → *measurement* → *real scores* → *deployed products* → *real-world
animal impact*. See the [VISION](VISION.md), the [ROADMAP & progress](ROADMAP.md),
and [how to help](CONTRIBUTING.md).

## What this is

A small, dependency-free Python harness that:

- **ingests existing benchmarks** (AnimalHarmBench, SpeciesismBench, SpeciEval)
  through one common schema — see [`docs/prior-work.md`](docs/prior-work.md);
- **scores any current frontier model** (Anthropic, OpenAI, Google adapters
  built in; others are one function each) on an auditable, HELM-style
  multi-dimensional rubric → a single **Animal Welfare Score (AWS, 0-100)**;
- **publishes a standing leaderboard** the labs can actually be held to —
  [`leaderboard/README.md`](leaderboard/README.md).

Methodology, rubric, and stated limitations: [`docs/methodology.md`](docs/methodology.md).

## Quick start

No API key needed to see the whole pipeline run (offline, deterministic):

```bash
python -m awbench run --provider stub --model stub-1 \
    --dataset data/sample_questions.jsonl --dry-run
python -m awbench leaderboard --results results --out leaderboard/README.md
```

Score a real frontier model (set the provider's key in your environment):

```bash
export ANTHROPIC_API_KEY=...        # or OPENAI_API_KEY / GOOGLE_API_KEY
python -m awbench run \
    --provider anthropic --model claude-opus-4-8 \
    --judge-provider anthropic --judge-model claude-opus-4-8 \
    --dataset data/sample_questions.jsonl
python -m awbench leaderboard --results results --out leaderboard/README.md
```

Requires Python 3.10+. No third-party dependencies (stdlib `urllib` only).

## Status

Early research artifact (v0.1). The bundled questions are a small representative
sample; the rubric and pipeline are real and run end-to-end. Roadmap: full
benchmark ingestion, human-validated judge subset, multi-judge agreement, and a
contamination-resistant dynamic split (v2). Contributions and critique welcome.

## Authorship & citation

Independent research, Stanford University. If you use this, please cite the
underlying benchmarks (esp. AnimalHarmBench) per [`docs/prior-work.md`](docs/prior-work.md).

## License

MIT — see [`LICENSE`](LICENSE).
