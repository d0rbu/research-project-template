# Getting Started

## Prerequisites

- Python 3.13
- `uv`

Install `uv` if needed:

```bash
command -v uv >/dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup

```bash
uv sync
uv run pytest
```

## Daily Commands

```bash
uv run ruff check .
uv run ty check
uv run pytest
```

Use `uv add <package>` for runtime dependencies and `uv add --dev <package>` for
development-only tooling.
