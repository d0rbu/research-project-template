# Testing

## Default Suite

```bash
uv run pytest
```

The default suite includes unit tests, property tests, and coverage.

## Focused Runs

```bash
uv run pytest tests/test_types.py
uv run pytest tests/test_metrics.py -k weighted_mean
uv run pytest -m property
```

## Coverage

Coverage is configured in `pyproject.toml` and currently fails below 95%.

Use coverage as a guardrail, not a substitute for meaningful assertions. The most useful
tests in this template check invariants: probabilities stay in range, weights normalize
to one, and invalid primitive values are rejected before they enter core code.
