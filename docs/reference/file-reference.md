# File Reference

## Top Level

| File | Purpose |
|---|---|
| `README.md` | Project summary, quickstart, and doc links |
| `AGENTS.md` | Agent entry point and repo conventions |
| `CLAUDE.md` | Claude-specific pointer to agent conventions |
| `pyproject.toml` | Package metadata and tool configuration |
| `uv.lock` | Locked dependency graph |
| `.python-version` | Python version for local tooling |
| `.gitignore` | Local artifacts excluded from git |
| `LICENSE` | MIT license |

## Package

| File | Purpose |
|---|---|
| `src/research_template/__init__.py` | Public package exports |
| `src/research_template/types.py` | `Probability`, `PositiveCount`, and parse/refinement helpers |
| `src/research_template/experiment.py` | `ExperimentConfig` and split helper |
| `src/research_template/metrics.py` | Weight normalization and weighted mean helpers |
| `src/research_template/cli.py` | Minimal installed CLI entry point |
| `src/research_template/py.typed` | Marks the package as typed |

## Tests

| File | Purpose |
|---|---|
| `tests/test_types.py` | Phantom type and config refinement tests |
| `tests/test_metrics.py` | Metric invariant and property tests |

## Docs

| Path | Purpose |
|---|---|
| `docs/README.md` | Documentation index |
| `docs/onboarding/` | Setup and day-to-day workflows |
| `docs/development/` | Correctness and testing guidance |
| `docs/pipelines/` | Research workflow templates |
| `docs/reference/` | Architecture, configuration, and file map |

## CI

| File | Purpose |
|---|---|
| `.github/workflows/ci.yml` | Runs `ruff`, `ty`, and `pytest` on pushes and pull requests |
