# AGENTS.md - research-project-template

You are working in a correctness-first Python research template. Keep changes small,
explicit, typed, and easy to review. The repository currently has tooling and executable
examples, with no research implementation or installable source package.

This file is the AI-agent entry point. It should point to docs that contain durable
project knowledge. If you want to add detail here, usually update the linked doc instead.

## Read these first

- [`README.md`](README.md) - project pitch and quickstart
- [`docs/README.md`](docs/README.md) - documentation map
- [`docs/onboarding/getting-started.md`](docs/onboarding/getting-started.md) - local setup
- [`docs/onboarding/workflows.md`](docs/onboarding/workflows.md) - common development flows
- [`docs/development/correctness.md`](docs/development/correctness.md) - correctness philosophy and tools
- [`docs/development/testing.md`](docs/development/testing.md) - test selection and coverage
- [`docs/reference/architecture.md`](docs/reference/architecture.md) - layout and growth path
- [`docs/reference/configuration.md`](docs/reference/configuration.md) - tool configuration
- [`docs/reference/file-reference.md`](docs/reference/file-reference.md) - file-by-file reference

## Repo layout

```
tests/              pytest suite, including property tests
scripts/            tested repository maintenance commands
docs/               source-of-truth documentation
.github/workflows/  CI checks
justfile           commands shared by agents and humans
```

## Working on a change

1. Inspect `git status` and read the relevant docs and code. Preserve unrelated changes.
2. Define the input/output contract and failure cases before implementing behavior.
3. Keep reusable logic separate from scripts, notebooks, and experiment orchestration.
4. For behavior changes, test the external contract and add regression coverage for bugs.
5. Update the owning documentation and the [file map](docs/reference/file-reference.md).
6. Run the full gate below and report changes, validation, and any remaining limitations.

## Environment and commands

- Use `uv sync --locked` to install and `uv run --locked ...` to invoke project tools.
- Install commit hooks once per clone with `uv run --locked pre-commit install`.
- Use `uv add <package>` or `uv add --dev <package>` to change dependencies. Commit
  `pyproject.toml` and `uv.lock` together; do not edit the lockfile by hand.
- Keep `.python-version`, `requires-python`, Ruff, and ty aligned on Python 3.13.
- Use `uv run --locked just` to list recipes, `just fmt` to fix formatting, and
  `just check` for the full gate when `just` is already on `PATH`.

## Correctness and maintainability

- Prefer making bad state unrepresentable over documenting invalid states after the fact.
- Use `phantom-types` for domain invariants that narrow primitive values.
- Refine untrusted inputs through parsers before passing them to core functions.
  Validate cross-field constraints explicitly; a type annotation alone does not enforce them.
- Use `beartype` at runtime boundaries where invalid values can enter the system.
- Use `jaxtyping` for array shape and dtype contracts.
- Check semantic constraints separately: finiteness, ranges, nonempty inputs, and valid
  combinations. Treat booleans deliberately when accepting numeric input.
- Use Hypothesis for invariants, edge cases, and regression tests that should hold over many inputs.
- Keep imports at the top of each file. Annotate function signatures and use `@override`
  for overridden methods. Prefer precise types to `Any` and unexplained casts.
- Use explicit exceptions for input validation. Reserve `assert` for tests and internal
  invariants, since Python can disable assertions.
- Do not lower coverage, widen exclusions, or add blanket suppressions to pass checks.
  Any necessary suppression should be narrow and explain the tool's limitation.
- Review Vulture findings against actual callers and framework entry points before removing
  code. Record a specific false positive instead of excluding a whole module.
- Keep generated data, checkpoints, credentials, and outputs out of Git; small deterministic
  test fixtures belong under `tests/`. Record seeds and artifact identity for experiments.
- Add source packages and documentation sections when real code needs them. Avoid speculative
  frameworks, unused helpers, and placeholder hierarchies.

## Correctness tools

The scaffold tests demonstrate:

- `Probability`: a phantom type for closed-range probabilities.
- `normalize_weights`: a `jaxtyping` + `beartype` checked NumPy function.
- property tests that use `st.from_type(...)` with phantom types
- finite probability validation, extreme float magnitudes, and dtype/rank/shape rejection.

Copy these patterns for project-specific concepts such as dataset splits, feature IDs,
sample counts, model dimensions, or validated artifact paths.

## Required checks

```bash
uv run --locked pre-commit run --all-files
```

This runs lock validation, Ruff lint and formatting, ty, Vulture, pytest with coverage,
actionlint, local Markdown target checks, and repository hygiene checks. CI runs the same
hooks. The `just check` recipe is a
convenient equivalent. Hygiene hooks may fix files; review their diff and rerun.

`pytest` uses strict configuration and markers, treats warnings as errors, and excludes
`slow` tests by default. Use `uv run --locked python -m pytest --no-cov -k <expression>` while
iterating; focused runs do not replace the full gate. See the [testing guide](docs/development/testing.md).

Coverage requires 95% with branch measurement on repository scripts and scaffold tests.
Add the research package to `tool.coverage.run.source` as soon as one is introduced.
Do not present scaffold coverage as evidence about unimplemented research code.

The [merge policy](.github/rulesets/default-branch.json) requires a pull request, a passing
GitHub Actions `checks` job tested against the latest base, and resolved review threads.
Review approval is optional. Apply and verify this policy separately in every repository;
copying a template or editing the JSON does not configure GitHub automatically. See the
[configuration guide](docs/reference/configuration.md) before changing repository settings.

For new untracked files, also run the relevant hooks with `--files <paths>`; `--all-files`
only enumerates tracked files for file-based hooks. If a check cannot run, state the
exact reason and what remains unverified.
