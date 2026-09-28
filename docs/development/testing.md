# Testing

[Documentation index](../README.md) · [Correctness](correctness.md) · [Configuration](../reference/configuration.md)

## Default Suite

```bash
uv run --locked python -m pytest
```

The default suite includes unit tests, bounded Hypothesis property tests, and coverage.
Unknown configuration options and markers are errors, warnings fail tests, and an
unexpected pass of an `xfail` test is a failure. Tests use importlib import mode so
test directories are not implicitly added to the import path.

Invoke pytest with `python -m pytest` so the repository's `scripts` module is importable
without installing a research package or changing `sys.path` inside tests.

Mark expensive tests with `@pytest.mark.slow`; the default suite excludes them. Run
them explicitly with `uv run --locked python -m pytest -m slow --no-cov`. Tests requiring network,
paid services, or GPUs should have explicit opt-in setup as those capabilities are added.

## Pre-Commit

Install hooks once per clone:

```bash
uv run --locked pre-commit install
```

Run the full configured gate manually:

```bash
uv run --locked pre-commit run --all-files
```

The hooks run the checks listed in the [configuration reference](../reference/configuration.md):
lock validation, Ruff lint and formatting, ty, Vulture, pytest with coverage, actionlint,
local Markdown targets, and file hygiene. CI invokes the same configuration.
`uv run --locked just check` is equivalent.

## Focused Runs

```bash
uv run --locked python -m pytest tests/test_correctness_tools.py
uv run --locked python -m pytest --no-cov -k weighted_mean
uv run --locked python -m pytest --no-cov -m property
uv run --locked just test --no-cov -k "weighted_mean or normalize_weights"
```

Use `--no-cov` for a subset because the 95% threshold applies to the whole configured
source. A focused pass does not replace the full gate. The `just test` recipe preserves
argument boundaries, including quoted expressions.

## What to Test

- Known results with an independent expected value, not a copy of the implementation.
- Invalid input at runtime boundaries: NaN/Inf, booleans, empty values, wrong dtype/rank,
  and mismatched dimensions.
- Invariants over generated data, including extreme finite magnitudes and subnormal floats.
- External behavior: rejected inputs, output type/shape, numerical tolerance, and input mutation.

Keep generated examples bounded. Preserve minimal failures as regression examples and
investigate a failure before increasing tolerances or disabling a health check. Hypothesis
stores local failures in `.hypothesis/`, which is ignored by Git.

`tests/test_markdown_links.py` checks real Markdown parsing and temporary Git repositories:
relative and root-relative paths, encoded filenames, images and reference links, code
examples, ignored/untracked/deleted files, and target renames that break unchanged docs.

## Coverage

Coverage is configured in `pyproject.toml` and currently fails below 95%.

Branch coverage is enabled. `tool.coverage.run.source = ["scripts", "tests"]` measures
the maintenance commands and executable scaffold examples. Once research modules exist,
include those modules and remove test code from the measured production source.
The bare `--cov` option reads that setting, so there is only one coverage target to update.

```bash
uv run --locked just coverage
```

Open `htmlcov/index.html` for a browsable report. Generated coverage files are ignored.

Use coverage as a guardrail, not a substitute for meaningful assertions. The most useful
tests in this scaffold check invariants: probabilities stay in range, weights normalize
to one, and invalid primitive values are rejected before they enter core code.
