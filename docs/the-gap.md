# The Gap: a declared value that was never instrumented

In late 2025, Anthropic's [Claude Constitution](https://www.anthropic.com/constitution)
became the first major frontier-lab guiding document to name **"the welfare of
animals and of all sentient beings"** as a value the model should weigh. The
constitution is used directly in training, so this is not a press release — it
shapes behavior.

Here is the problem. **Every other value in a constitution or model spec is
qualitative in the document but quantified somewhere** — in an eval, a
benchmark, a published model/system card number. Animal welfare is the
exception.

| Constitutional value | Quantified by | Reported by labs? |
| -------------------- | ------------- | ----------------- |
| Honesty / truthfulness | TruthfulQA and successors | Yes |
| Harmlessness / safety | HarmBench, safety evals | Yes |
| Sycophancy | sycophancy evals | Yes |
| Fairness (race / gender) | BBQ, bias benchmarks | Yes |
| **Animal welfare / sentient beings** | AnimalHarmBench exists, but… | **No lab reports a score** |

The value was **declared but never instrumented.** No frontier model card
reports an animal-welfare number. There is no standing leaderboard the labs
read. OpenAI's published [Model Spec](https://model-spec.openai.com/) still has
no animal-welfare principle at all.

## What this project does

Turn the declared value into a measured one:

1. Adopt the strongest existing benchmark content (AnimalHarmBench and peers).
2. Score it with an auditable, HELM-style multi-dimensional rubric → a single
   **Animal Welfare Score (AWS, 0-100)**.
3. Run it on current frontier models and publish a standing, citable
   leaderboard.

"They wrote it down. We measure whether they live up to it."
