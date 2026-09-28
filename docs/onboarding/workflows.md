# Workflows

[Documentation index](../README.md) · [Getting started](getting-started.md) · [Testing](../development/testing.md)

## Add a Domain Type

1. Add the phantom type near the code that owns the domain concept.
2. Add a `parse_*` refinement function for untrusted inputs.
3. Use the refined type in public functions and dataclasses.
4. Add `st.from_type(...)` property tests when the type has a Hypothesis strategy.
5. Update `docs/development/correctness.md` if the pattern is new.

Use the [correctness guide](../development/correctness.md) for concrete examples and
the [architecture guide](../reference/architecture.md) when adding the first source package.

## Add an Experiment Helper

1. Put reusable code in the project module or package once one exists.
2. Keep script-only orchestration out of core logic.
3. Validate raw inputs at the boundary.
4. Return typed values, dataclasses, or explicit result objects.
5. Cover invariants with unit tests and property tests.

Record the experiment's inputs, seed, code revision, and artifact paths using the
[experiment lifecycle](../pipelines/experiment-lifecycle.md).

## Change Dependencies

```bash
uv add <runtime-package>
uv add --dev <development-tool>
uv lock --upgrade-package <package-to-update>
uv sync --locked
uv run --locked just check
```

Use the command appropriate to the change and review both `pyproject.toml` and `uv.lock`.
Dependabot proposes weekly Python and GitHub Actions updates; they still need review
and passing checks. Keep GitHub Actions pinned to reviewed commit SHAs.

## Iterate on Code

```bash
uv run --locked just fmt
uv run --locked just test --no-cov -k weighted_mean
uv run --locked just typecheck
uv run --locked just deadcode
```

Focused tests use `--no-cov` so a subset does not fail the full-suite coverage threshold.
Run the complete suite before handoff. Investigate warnings and dead-code findings
instead of suppressing them broadly.

## Before Handoff

Open changes as a pull request and wait for the GitHub Actions `checks` job to pass on
the current base before merging. Resolve review conversations; a human approval is
optional under the default [ruleset](../../.github/rulesets/default-branch.json).

```bash
uv run --locked pre-commit run --all-files
git diff --check
```

Keep the [file reference](../reference/file-reference.md) and relevant docs current.
File-based hooks only enumerate tracked files with `--all-files`; check new untracked
files explicitly with `uv run --locked pre-commit run --files <paths>` as needed.
Report the checks run and explain any remaining failures or checks that could not run.
