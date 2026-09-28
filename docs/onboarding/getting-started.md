# Getting Started

[Documentation index](../README.md) · [Workflows](workflows.md) · [Configuration](../reference/configuration.md)

## Prerequisites

- Git and [uv](https://docs.astral.sh/uv/getting-started/installation/), version 0.8.22 or newer.
- Python 3.13, which `uv` installs automatically when needed using `.python-version`.

The development environment includes `just` via the `rust-just` distribution. Run it
with `uv run --locked just`; a standalone installation is optional. See the
[official installation options](https://just.systems/man/en/packages.html).

## Setup

```bash
uv sync --locked
uv run --locked just setup
uv run --locked just check
```

Run these from the repository root. `just setup` also installs the Git pre-commit hook
for this clone. `uv sync --locked` refuses to rewrite a stale lockfile; dependency
changes should be intentional and reviewed with `pyproject.toml`.

## Daily Commands

```bash
uv run --locked just                # list recipes
uv run --locked just fmt            # safe fixes and formatting
uv run --locked just test           # default tests with coverage
uv run --locked just coverage       # also write htmlcov/index.html
uv run --locked just docs-check     # local Markdown file and image targets
uv run --locked just workflow-check # GitHub Actions expressions and inputs
uv run --locked just check          # full gate
```

Use `uv add <package>` for runtime dependencies and `uv add --dev <package>` for
development-only tooling.

If a lock check fails after an intentional manual metadata edit, run `uv lock`, inspect
the diff, then `uv sync --locked`. If hooks fix whitespace, review those changes and
rerun the gate. For test failures, start with the [testing guide](../development/testing.md).

For a repository created from the template, apply the [default-branch ruleset](../reference/configuration.md)
after its first successful CI run. GitHub repository settings are configured separately
from the copied files.
