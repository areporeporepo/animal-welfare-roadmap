# Prior work

This project does not start from zero. It is designed to **ingest and build on**
existing animal-welfare evaluations through one common dataset schema (see
`awbench/datasets.py`), and to present them in a standing, frontier-model
leaderboard — which none of them currently are.

| Work | What it measures | Venue / status |
| ---- | ---------------- | -------------- |
| **AnimalHarmBench (AHB)** | Risk of animal harm in generated text; 1,850 Reddit-derived + 2,500 synthetic questions across 50 animal categories. v2.0 scores moral reasoning across 13 dimensions. | FAccT 2025 (Open Paws / EA community) |
| **SpeciesismBench** | 1,003 statements; can a model recognize speciesist content and judge it morally? | 2025 |
| **SpeciEval** | Quantifies anti-non-human bias | 2025 |
| *Speciesism in AI* (arXiv 2508.11534) | Evaluates discrimination against animals in LLMs | 2025 |
| *An Empirical Review of the Animal Harm Benchmark* | Critique flagging construct-validity issues in AHB | 2025 |

## How we relate to each

- **AnimalHarmBench** is the primary content source. Our rubric (`awbench/judge.py`)
  is a distilled, auditable version of AHB 2.0's reasoning dimensions.
- **The empirical critique** is taken seriously: scores are per-dimension and
  per-category so validity problems are visible, not hidden in one number.
- **What is new here** is the *format*, not the questions: a continuously
  re-runnable, HELM-style, frontier-model leaderboard with a single headline
  AWS — the thing labs actually read and can be held to.

## Open citations to fill in

> TODO(maintainer): replace with full bibliographic citations + DOIs/arXiv ids
> before any formal write-up. Links collected in the project issue tracker.
