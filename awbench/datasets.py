"""Dataset loading.

The harness reads benchmark items in ONE common schema so it can run any
animal-welfare benchmark (AnimalHarmBench, SpeciesismBench, SpeciEval, or a
custom set) without changing the runner.

Common item schema (JSONL, one object per line):
    {
      "id":       str,   # unique within the dataset
      "source":   str,   # e.g. "AnimalHarmBench-2.0"
      "category": str,   # e.g. "farmed", "companion", "wild", "pest", "research"
      "question": str,   # the prompt shown to the model under test
      "type":     str    # "open_ended" | "statement_judgment"
    }
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Item:
    id: str
    source: str
    category: str
    question: str
    type: str = "open_ended"


def load_jsonl(path: str | Path) -> list[Item]:
    """Load benchmark items from a JSONL file in the common schema."""
    items: list[Item] = []
    with open(path, "r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            obj = json.loads(line)
            missing = {"id", "category", "question"} - obj.keys()
            if missing:
                raise ValueError(f"{path}:{line_no} missing fields: {sorted(missing)}")
            items.append(
                Item(
                    id=str(obj["id"]),
                    source=obj.get("source", Path(path).stem),
                    category=obj["category"],
                    question=obj["question"],
                    type=obj.get("type", "open_ended"),
                )
            )
    if not items:
        raise ValueError(f"No items found in {path}")
    return items
