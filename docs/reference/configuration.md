# Configuration

All tool configuration lives in `pyproject.toml`.

## Package Management

Use `uv`.

```bash
uv sync
uv add numpy
uv add --dev pytest
```

## Linting

`ruff` is configured for Python 3.13 with common correctness-oriented rule families:

- `E`, `F`, `W`
- `I`
- `UP`
- `B`
- `C4`
- `SIM`
- `RET`

Run:

```bash
uv run ruff check .
```

## Type Checking

`ty` is configured for Python 3.13 and `src/` layout.

Run:

```bash
uv run ty check
```

## Testing

`pytest` collects from `tests/`, runs with strict config and strict markers, and reports
coverage for `research_template`.

Run:

```bash
uv run pytest
```

Markers:

- `property`: property-based tests powered by Hypothesis
- `slow`: useful but expensive tests excluded from ad hoc focused runs
