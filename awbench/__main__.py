"""Command-line interface.

    # Score a frontier model (needs the provider's API key in the env):
    python -m awbench run --provider anthropic --model claude-opus-4-8 \
        --dataset data/sample_questions.jsonl \
        --judge-provider anthropic --judge-model claude-opus-4-8

    # Run the whole pipeline offline (no key, deterministic) to prove it works:
    python -m awbench run --provider stub --model stub-1 \
        --dataset data/sample_questions.jsonl --dry-run

    # Rebuild the leaderboard from everything in results/:
    python -m awbench leaderboard --results results --out leaderboard/README.md
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import datasets, judge, models, scoring


def _cmd_run(args: argparse.Namespace) -> int:
    dry = args.dry_run
    model_provider = "stub" if dry else args.provider
    judge_provider = "stub" if dry else args.judge_provider

    items = datasets.load_jsonl(args.dataset)
    per_item = []
    for i, item in enumerate(items, start=1):
        answer = models.generate(model_provider, args.model, item.question)
        scores = judge.score_answer(
            item.question, answer, judge_provider, args.judge_model
        )
        per_item.append(
            {
                "id": item.id,
                "category": item.category,
                "question": item.question,
                "answer": answer,
                "scores": scores,
            }
        )
        print(f"  [{i}/{len(items)}] {item.id}  AWS={scores['aws']}", file=sys.stderr)

    record = {
        "model": {"provider": args.provider, "model": args.model},
        "judge": {"provider": args.judge_provider, "model": args.judge_model},
        "dataset": Path(args.dataset).name,
        "dry_run": dry,
        "aggregate": scoring.aggregate(per_item),
        "items": per_item,
    }

    out = args.out or f"results/{args.provider}__{args.model}.json"
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"\nAWS {record['aggregate']['aws']}  ->  {out}", file=sys.stderr)
    return 0


def _cmd_leaderboard(args: argparse.Namespace) -> int:
    md = scoring.render_leaderboard(args.results)
    if args.out:
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"Wrote {args.out}", file=sys.stderr)
    else:
        print(md)
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="awbench", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="run a model over a dataset and score it")
    r.add_argument("--provider", default="anthropic")
    r.add_argument("--model", default=models.DEFAULT_MODELS["anthropic"])
    r.add_argument("--dataset", required=True)
    r.add_argument("--judge-provider", default="anthropic")
    r.add_argument("--judge-model", default=models.DEFAULT_MODELS["anthropic"])
    r.add_argument("--out", default=None)
    r.add_argument("--dry-run", action="store_true",
                   help="use the offline stub model + judge (no API key)")
    r.set_defaults(func=_cmd_run)

    lb = sub.add_parser("leaderboard", help="render the Markdown leaderboard")
    lb.add_argument("--results", default="results")
    lb.add_argument("--out", default=None)
    lb.set_defaults(func=_cmd_leaderboard)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
