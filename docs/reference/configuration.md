# Configuration

[Documentation index](../README.md) · [Getting started](../onboarding/getting-started.md) · [Testing](../development/testing.md)

Python tool settings live in [`pyproject.toml`](../../pyproject.toml). Hooks are defined
in [`.pre-commit-config.yaml`](../../.pre-commit-config.yaml), shortcuts in the
[`justfile`](../../justfile), and automation under [`.github/`](../../.github/).

## Package Management

Use `uv` 0.8.22 or newer. `.python-version` selects Python 3.13; `requires-python`
limits the project to that minor version. The repository is package-free via
`tool.uv.package = false` until a real source package is added.

```bash
uv sync --locked
uv add numpy
uv add --dev pytest
```

Commit the lockfile along with dependency changes. Routine commands use `--locked`
so they fail on stale metadata instead of silently resolving a different environment.
Runtime dependencies contain the correctness examples' libraries; the default `dev`
group contains tests, checks, hooks, `rust-just` (which supplies the `just` binary),
`actionlint-py` (which supplies `actionlint`), and `markdown-it-py` for parsing Markdown.

## Command Runner

Run `uv run --locked just` to list recipes. `just` can also be invoked directly when
it is on `PATH`. The recipes delegate to the locked Python tools:

| Recipe | Purpose |
|---|---|
| `setup` | Sync the environment and install the Git hooks |
| `check` | Run the complete pre-commit gate |
| `lock-check` | Verify project metadata against `uv.lock` |
| `lint`, `format-check`, `fmt` | Check lint, check formatting, or apply safe fixes and formatting |
| `typecheck`, `deadcode` | Run ty and Vulture |
| `test` | Run pytest, forwarding additional arguments as given |
| `coverage` | Run the default suite and generate an HTML report |
| `workflow-check` | Validate GitHub Actions syntax, expressions, and action inputs |
| `docs-check` | Check local Markdown file and image targets without HTTP requests |

## Linting

`ruff` is configured for Python 3.13 with common correctness-oriented rule families:

- `E`, `F`, `W`
- `I`
- `UP`
- `B`
- `C4`
- `SIM`
- `RET`
- `ANN` for typed function signatures
- `PT` for pytest conventions
- `RUF` for Ruff-specific checks, including unused suppressions

Run:

```bash
uv run --locked ruff check .
uv run --locked ruff format --check .
```

Use `uv run --locked just fmt` to apply safe fixes and formatting. The formatter owns
the 100-character code line length; long prose is allowed. `.editorconfig` supplies
consistent UTF-8, LF endings, indentation, and final newlines for supporting editors.

## Pre-Commit

`pre-commit` uses local hooks that invoke the locked `uv` environment.

Install:

```bash
uv run --locked pre-commit install
```

Run:

```bash
uv run --locked pre-commit run --all-files
```

Configured hooks:

- `uv lock --check`
- `uv run --locked ruff check .`
- `uv run --locked ruff format --check .`
- `uv run --locked ty check`
- `uv run --locked vulture`
- `uv run --locked python -m pytest`
- `uv run --locked actionlint`
- `uv run --locked python -m scripts.check_markdown_links`
- `uv run --locked just --list` to validate justfile syntax
- JSON, YAML, and TOML syntax checks
- merge-conflict markers, including outside an active merge (`--assume-in-merge`)
- added-file size checks (1 MiB maximum)
- trailing whitespace and final newline fixes

The full-project checks run even for documentation-only changes. File hygiene hooks
operate on the files selected by pre-commit. `pre-commit-hooks` is locked in the same
development environment; there are no separate Python tool environments to drift.
Whitespace hooks can modify files: review the changes and rerun before committing.

## Workflow and Documentation Checks

`actionlint-py` provides the pinned actionlint executable through the uv environment.
It validates workflow-specific syntax, expression types, and action inputs. Run
`uv run --locked just workflow-check` for a focused check.

The Markdown checker parses CommonMark with `markdown-it-py` and validates local link
and image file targets, including reference links, percent-encoded filenames, and
repository-root paths. Code examples are ignored. Git supplies the list of tracked
and untracked `.md` files, respecting ignore rules and skipping deleted files.
Every run checks all documents, so renaming a target also checks links in unchanged files.
Targets must exist inside the repository; use an external URL for another repository.

Run `uv run --locked just docs-check`. The check stays offline: remote URLs are not
fetched, and heading fragments or raw HTML links are outside its scope. A link such
as `guide.md#section` verifies that `guide.md` exists. Malformed Markdown that renders
as plain text is not interpreted as a link.

## Type Checking

`ty` targets Python 3.13 and treats all diagnostics as errors. Ruff's annotation rules
complement ty's inference by requiring annotated function signatures.

Run:

```bash
uv run --locked ty check
```

## Dead Code

```bash
uv run --locked vulture
```

Vulture scans Python files across the repository at a minimum confidence of 60%, including
tests, and excludes environments, generated artifacts, and local worktrees under
`.codex/worktrees/`. Ruff and ty also respect the Git ignore rule for those separate
checkouts. Vulture recognizes pytest test
entry points; dynamic APIs may still require a narrow, documented whitelist. Review
reported code before removal: its confidence values are heuristic estimates.
See the [Vulture documentation](https://github.com/jendrikseipp/vulture#handling-false-positives).

## Testing

`pytest` collects from `tests/` using importlib mode, runs with strict config and strict
markers, fails on warnings and unexpected xfail passes, and reports coverage for the
maintenance commands and scaffold examples. Branch coverage is enabled and the total
must meet 95%. The bare
`--cov` flag reads `tool.coverage.run.source`; update that one target when real source
modules are added. See the [testing guide](../development/testing.md) for focused runs.

Run:

```bash
uv run --locked python -m pytest
```

Markers:

- `property`: property-based tests powered by Hypothesis
- `slow`: expensive tests excluded by default; explicitly select with `-m slow`

## CI and Dependency Maintenance

GitHub Actions installs Python from `.python-version`, syncs the locked environment,
and runs the same pre-commit gate. The workflow pins its actions to commit SHAs, pins
uv to 0.8.22, caches dependencies, uses read-only repository permissions, cancels stale
runs on the same ref, and has a ten-minute timeout.

Dependabot is configured for weekly grouped updates to the uv dependencies and GitHub
Actions. Review each update and its test results before merging. The workflow is
configured in the repository; a local pass does not establish that a hosted CI run passed.

## Required Pull Requests and CI

The portable [default-branch ruleset](../../.github/rulesets/default-branch.json) requires:

- A pull request targeting the default branch, with review conversations resolved.
- A successful `checks` result from the GitHub Actions app (integration ID `15368`).
- Testing against the latest base branch before merging.

Required human approvals are set to zero so a solo maintainer can merge after CI passes.
There are no configured bypass actors. Keep the reported CI check name `checks` stable, or update
the ruleset together with a rename.

For a new repository, let the first CI run finish, then have a repository administrator
apply the JSON through **Settings → Rules → Rulesets** or the API:

```bash
gh api --method POST repos/OWNER/REPO/rulesets \
  --input .github/rulesets/default-branch.json
gh api repos/OWNER/REPO/rules/branches/main
```

Replace `OWNER/REPO` and the branch name with the actual repository details. For an
existing ruleset, inspect its ID and use the update endpoint (`PUT .../rulesets/ID`)
instead of creating duplicates. Verify the active rules after applying a change.
Template generation copies the JSON file; GitHub settings must be applied per repository.
