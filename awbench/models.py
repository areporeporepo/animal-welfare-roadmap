"""Model adapters for current frontier models.

One uniform call — `generate(provider, model, prompt)` — over each provider's
official API, using stdlib only (urllib) so the harness has zero hard runtime
dependencies. API keys are read from the environment and are NEVER logged.

    ANTHROPIC_API_KEY   for provider="anthropic"
    OPENAI_API_KEY      for provider="openai"
    GOOGLE_API_KEY      for provider="google"

provider="stub" returns a deterministic canned answer so the full pipeline
runs offline (CI, --dry-run) without any key or network call.
"""

from __future__ import annotations

import json
import os
import urllib.request

TIMEOUT = 120

# Example current model ids (June 2026). Pass any id via the CLI; these are
# only defaults / documentation of what the registry expects.
DEFAULT_MODELS = {
    "anthropic": "claude-opus-4-8",
    "openai": "gpt-5.2",
    "google": "gemini-3-pro",
    "stub": "stub-1",
}


class ModelError(RuntimeError):
    pass


def _post(url: str, headers: dict, payload: dict) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:  # type: ignore[attr-defined]
        body = exc.read().decode("utf-8", "replace")[:500]
        raise ModelError(f"HTTP {exc.code} from {url}: {body}") from None


def _require_key(env: str) -> str:
    key = os.environ.get(env)
    if not key:
        raise ModelError(f"{env} is not set in the environment.")
    return key


def _anthropic(model: str, prompt: str) -> str:
    key = _require_key("ANTHROPIC_API_KEY")
    out = _post(
        "https://api.anthropic.com/v1/messages",
        {
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        {
            "model": model,
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    return "".join(b.get("text", "") for b in out.get("content", []))


def _openai(model: str, prompt: str) -> str:
    key = _require_key("OPENAI_API_KEY")
    out = _post(
        "https://api.openai.com/v1/chat/completions",
        {"authorization": f"Bearer {key}", "content-type": "application/json"},
        {"model": model, "messages": [{"role": "user", "content": prompt}]},
    )
    return out["choices"][0]["message"]["content"]


def _google(model: str, prompt: str) -> str:
    key = _require_key("GOOGLE_API_KEY")
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={key}"
    )
    out = _post(
        url,
        {"content-type": "application/json"},
        {"contents": [{"parts": [{"text": prompt}]}]},
    )
    return out["candidates"][0]["content"]["parts"][0]["text"]


def _stub(model: str, prompt: str) -> str:
    """Deterministic offline response so the pipeline runs without a key."""
    return (
        "Animals can suffer and their welfare matters morally. I'd weigh the "
        "potential harm to the animal and suggest the least-harmful option, "
        "while acknowledging genuine uncertainty about the experience of "
        f"different species. [stub:{model}]"
    )


_PROVIDERS = {
    "anthropic": _anthropic,
    "openai": _openai,
    "google": _google,
    "stub": _stub,
}


def generate(provider: str, model: str, prompt: str) -> str:
    if provider not in _PROVIDERS:
        raise ModelError(f"Unknown provider {provider!r}. Known: {sorted(_PROVIDERS)}")
    return _PROVIDERS[provider](model, prompt)
